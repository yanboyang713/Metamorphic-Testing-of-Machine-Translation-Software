import openpyxl
import sys
import time
from verificationMethods import TestCaseManager
import GetLiteral




#main function
def main():
	print('Would you like to generate new test data? y/n: ')
	new_data = input()
	if new_data == 'y' or new_data == 'Y':
		testData = GetLiteral
		print ('How many lines of data do you wish to generate?: ')
		num_lines = input()
		testData.setTestData(num_lines)

	testCaseManager = TestCaseManager('local_test_results.xlsx')
	languages = ['en', 'zh-CHS', 'ja', 'ko', 'fr', 'ru', 'pt', 'es', 'sv']

	print ('Please enter the starting row number: ')
	start_row = int(input())
	print ('Please enter the final row number: ')
	last_row = int(input())

	row_entries = range(start_row, last_row+1)

	print('***BEGINNING TESTS***')
	for index, language in enumerate(languages):
		print('Beginning performance tests, targeting:', language, '( PHASE ', index+1, 'of', len(languages),')')
		testCaseManager.uniDirectionalTest(['Google', 'Bing', 'Youdao'], language, row_entries)

	print('***TESTING COMPLETE***')

if __name__ == "__main__":
	main()
