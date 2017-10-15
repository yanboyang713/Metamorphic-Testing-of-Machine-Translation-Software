import openpyxl
import random
from commonTranslator import CommonTranslator
from fileManager import FileManager
from levDist import levenshteinDistance

"""
Verifies a particular translation by performing one additional 'side-translation'
and comparing the result.
The results of each test are then stored in a file.

TODO: Handle 'None' cases
"""
def uniDirectionalTest(services, rows, target_language, origin_language = 'en'):
	translator = CommonTranslator()
	translation_file = FileManager()
	results_file = FileManager('testResults.xlsx', [['Service', 'Test Phrase', 'Source Language', 'Intermediate Language', 'Target Language', 'Direct Translation', 'Alternate Translation'], ['Service', 'Source Language', 'Target Language', 'Score']], ['Test Phrases', 'Test Results'], write_header = True)

	# Get a language reference for the file being read.
	language_list = translation_file.getColumnNames('Google')

	for service in services:
		for row in rows:
			# Grab the direct translation from file.
			direct_translation = translation_file.readCell(service, row, target_language)

			# Randomly select a side-language and grab its direct translation.
			random_language = random.choice([x for x in language_list if x != origin_language and x != target_language])	
			intermediate_translation = translation_file.readCell(service, row, random_language)

			# Translate this intermediate sentence into the same language as the direct translation.
			alternate_translation = translator.translate(service, intermediate_translation, target_language, random_language)

			# Compare the two translations.
			score = compare(direct_translation, alternate_translation)

			# Record the results.
			original_phrase = translation_file.readCell(service, row, origin_language)  # Grab original phrase for records.
			results_file.appendEntry('Test Phrases', [service, original_phrase, origin_language, random_language, target_language, direct_translation, alternate_translation])
			results_file.appendEntry('Test Results', [service, origin_language, target_language, score])
	print('Saving..')
	results_file.save()


"""
Compares two strings and returns a score based on their similarity.

TODO: Incorporate more than one test result.
"""
def compare(phrase1, phrase2):
	return levenshteinDistance(phrase1, phrase2)['Ratio']
