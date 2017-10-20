import nltk
import openpyxl
import random
import warnings
from commonTranslator import CommonTranslator
from fileManager import FileManager
from levDist import levenshteinDistance
from nltk.translate.bleu_score import SmoothingFunction

"""
TestCaseManager
"""
class TestCaseManager:
	def __init__(self, results_file = 'testResults.xlsx'):
		self._translator = CommonTranslator()
		self._translation_file = FileManager()
		self._results_file = FileManager(results_file,
                                         [['Service', 'Test Phrase', 'Source Language', 'Intermediate Language', 'Target Language', 'Direct Translation', 'Alternate Translation'],
                                          ['Service', 'Source Language', 'Target Language', 'Lev-Distance', 'BLEU-Score']],
                                         ['Test Phrases', 'Test Results'],
                                         write_header = True)

		# Assumes structure of results file
		self._language_list = self._translation_file.getColumnNames('Google')


	"""
	Verifies a particular translation by performing one additional 'side-translation'
	and comparing the result.
	The results of each test are then stored in a file.

	TODO: Handle incomplete data file.
	"""
	def uniDirectionalTest(self, services, target_language, rows = None, origin_language = 'en'):
		if rows is None:
			rows = range(1, self._translation_file.getNumberRows('Google'))

		for service in services:
			for row in rows:
				remaining_languages = [x for x in self._language_list if x != origin_language and x != target_language]

				# Randomly select a side-language and grab its direct translation.
				random_language = random.choice(remaining_languages)	

				# Grab the original, direct, and side-translations from file.
				original_phrase, direct_translation, intermediate_translation = self._translation_file.readRow(service, row, [origin_language, target_language, random_language])

				# Translate the intermediate sentence into the same language as the direct translation.
				alternate_translation = self._translator.translate(service, intermediate_translation, target_language, random_language)

				# If failed translation, keep trying with different selection
				while len(remaining_languages) > 1 and alternate_translation is None:
					warnings.warn('Failed to translate from', random_language, 'to', target_language, '. Repeated failures may introduce biased results.', RuntimeWarning)
					remaining_languages.remove(random_language)
					random_language = random.choice(remaining_languages)
					alternate_translation = self._translator.translate(service, intermediate_translation, target_language, random_language)

				# Check for complete failure.
				if alternate_translation is None:
					print('Unable to perform side-translation. Recording as N/A..')
					self._results_file.appendEntry('Test Phrases', [service, original_phrase, origin_language, 'N/A', target_language, direct_translation, 'N/A'])
					self._results_file.appendEntry('Test Results', [service, origin_language, target_language, 'N/A'])
				else:
					# Compare the two translations.
					score = self.compare(direct_translation, alternate_translation)

					# Record the results.
					self._results_file.appendEntry('Test Phrases', [service, original_phrase, origin_language, random_language, target_language, direct_translation, alternate_translation])
					self._results_file.appendEntry('Test Results', [service, origin_language, target_language, score['Lev-Distance'], score['BLEU-Score']])

		print('Saving..')
		self._results_file.save()

	"""
	Verifies a particular translation by performing a reverse translation back
	to the origin lannguage.
	NOTE: This is simply a special case of the uniDirectionalTest where the
	target language is also the origin language.
	"""
	def biDirectionalTest(self, services, rows, origin_language = 'en'):
		self.uniDirectionalTest(services, rows, origin_language, origin_language)


	"""
	Compares two strings and returns a score based on their similarity.
	Can optionally specify which metrics to use

	TODO: Incorporate more than one test result.
	"""
	def compare(self, phrase1, phrase2, metrics = None):
		if metrics is None:
			metrics = ['Lev-Distance', 'BLEU-Score']
		
		results = dict()

		if 'Lev-Distance' in metrics:
			results['Lev-Distance'] = levenshteinDistance(phrase1, phrase2)['Ratio']

		if 'BLEU-Score' in metrics:
			results['BLEU-Score'] = nltk.translate.bleu_score.sentence_bleu([phrase1.split()], phrase2.split(), smoothing_function = SmoothingFunction().method2)

		return results

	"""
	Performs a single metric calculation for all rows in an existing test case file.
	Primarily used for re-calculating scores without having to run any additional translations.
	"""
	def recomputeMetricResults(self, metric, rows = None):
		if rows is None:
			rows = range(2, self._results_file.getNumberRows('Test Phrases'))

		for row in rows:
			# Get the sample strings for this observation.
			direct_translation, alternate_translation = self._results_file.readRow('Test Phrases', row, ['Direct Translation', 'Alternate Translation'])

			# Compute a metric for observation
			score = self.compare(direct_translation, alternate_translation, [metric])

			# Write result to file
			self._results_file.writeRow('Test Results', row, [score[metric]], [metric])
		self._results_file.save()
