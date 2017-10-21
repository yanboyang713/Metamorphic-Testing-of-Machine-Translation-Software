import openpyxl
import sys
import time
from verificationMethods import TestCaseManager




#main function
def main():
	testCaseManager = TestCaseManager('local_test_results.xlsx')
	languages = ['en', 'zh-CHS', 'ja', 'ko', 'fr', 'ru', 'pt', 'es', 'sv']

	start_row = 11
	last_row = 12

	row_entries = range(start_row, last_row+1)

	print('***BEGINNING TESTS***')
	for index, language in enumerate(languages):
		print('Beginning performance tests, targeting:', language, '( PHASE ', index+1, 'of', len(languages),')')
		testCaseManager.uniDirectionalTest(['Bing', 'Youdao'], language, row_entries)

	print('***TESTING COMPLETE***')

if __name__ == "__main__":
	main()
