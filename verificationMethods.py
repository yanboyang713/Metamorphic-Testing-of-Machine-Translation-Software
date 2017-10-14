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
	results_file = createResultsFile()

	# Get a language reference for the file being read.
	language_list = translation_file.getLanguages()

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
			recordPhrases(results_file, [service, original_phrase, origin_language, target_language, direct_translation, alternate_translation])
			recordScores(results_file, [service, origin_language, target_language, score])
	print('Saving..')
	results_file.save('testResults.xlsx')


"""
Compares two strings and returns a score based on their similarity.
TODO: Incorporate more than one test result.
"""
def compare(phrase1, phrase2):
	return levenshteinDistance(phrase1, phrase2)['Ratio']


"""
Function which prepares a spread sheet to store results of one-way comparison procedure.
Had to do this instead of using a FileManager() class as that was coupled to the structure
of the data sheet. Could've generalised it further to avoid this but meh..
"""
def createResultsFile(fname = 'testResults.xlsx'):
	try:
		workbook = openpyxl.load_workbook(fname)
	except:
		print('\'%s\' does not exist. constructing file..' % (fname))
		workbook = openpyxl.Workbook()

		workbook.create_sheet('Test Phrases')
		for index, head in enumerate(['Service', 'Test Phrase', 'Source Language', 'Target Language', 'Direct Translation', 'Alternate Translation']):
			workbook['Test Phrases'].cell(row = 1, column = index + 1).value = head

		workbook.create_sheet('Test Results')
		for index, head in enumerate(['Service', 'Source Language', 'Target Language', 'Score']):
			workbook['Test Results'].cell(row = 1, column = index + 1).value = head

	return workbook


"""
Method for recording the strings from the uniDirectionalTest.
Assumes correct order of arguments:
  - Service
  - Test Phrase
  - Source Language
  - Target Language
  - Direct Translation
  - Alternate Translation
"""
def recordPhrases(workbook, record):
	new_row = workbook['Test Phrases'].max_row + 1  # Position of next empty row.
	for index, value in enumerate(record):
		workbook['Test Phrases'].cell(row = new_row, column = index+1).value = value


"""
Method for recording the scores from the uniDirectionalTest.
Assumes correct order of arguments:
  - Service
  - Source Language
  - Target Language
  - Score     (currently just L-Distance, can add more columns for more methods).

This should be performed along with the 'recordPhrases' method to ensure consistency
between row numbers.
"""
def recordScores(workbook, record):
	new_row = workbook['Test Results'].max_row + 1  # Position of next empty row.
	for index, value in enumerate(record):
		workbook['Test Results'].cell(row = new_row, column = index+1).value = value


uniDirectionalTest(["Youdao"], [2, 17, 50], "ja")
uniDirectionalTest(["Youdao"], [2, 17, 50], "sv")
