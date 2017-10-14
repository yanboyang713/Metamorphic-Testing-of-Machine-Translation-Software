import openpyxl

"""
A standardised class for accessing the translation data.
This class is designed to standardise the reading/writing of translations to the
translation file.
"""
class FileManager:
	# A reference for the fixed language translations. 
	# The order mirrors the column entries of the file. 
	_languages = ['en',       # English
                  'zh-CHS',   # Chinese
                  'ja',       # Japanese
                  'ko',       # Korean
                  'fr',       # French
                  'ru',       # Russian
                  'pt',       # Portuguese
                  'es',       # Spanish
                  'sv'        # Swedish
                 ]

	def __init__(self, fname = 'translations.xlsx'):
		self._fname = fname

		try:
			self._dataFile = openpyxl.load_workbook(fname)
		except:
			print('\'%s\' does not exist. constructing file..' % (fname))
			self._dataFile = openpyxl.Workbook()
			self._dataFile.create_sheet('Google')
			self._dataFile.create_sheet('Bing')
			self._dataFile.create_sheet('Youdao')

	def getLanguages(self):
		return self._languages

	# Returns selected language entries from a given Row, or the entire row.
	def readRow(self, service, row_number, languages = _languages):
		return [self._dataFile[service].cell(row = row_number, column = self._languages.index(l)+1).value for l in languages]

	
	def readCell(self, service, row_number, language):
		return self.readRow(service, row_number, [language])[0]


	# Writes a set of translations to the form for a given row. Can be the entire row of translations, or a subset.
	# Example Usage:
	# 	testFile = FileManager('test_file.xlsx')
	#	testFile.writeRow('Google', 1, ["This little piggy..", "went \'wee wee wee\'.."], ['en', 'sv'])
	#	testFile.save()
	def writeRow(self, service, row_number, values, languages = _languages):
		if len(values) == len(languages):
			for index, v in enumerate(values):
				self._dataFile[service].cell(row = row_number, column = self._languages.index(languages[index])+1).value = v
		else:
			raise ValueError('the lists \'values\' and \'languages\' are not of same length.')
				

	def writeCell(self, service, row_number, language, value):
		self.writeRow(row_number, value, language)


	def save(self):
		self._dataFile.save(self._fname)
