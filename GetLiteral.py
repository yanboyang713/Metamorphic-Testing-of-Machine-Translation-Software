import requests
from random import *
import random
import wikipedia
from openpyxl import Workbook

'''
Class for  generate a list of sentences as test data. The result will be written into an Excel file called "csci318.xlsx"

Example Usage:
    TestData=Get_Literal()
    TestData.setTestData(samplesize=20)

There will be some exception-thrown warning which won't affect the final result.

'''

class Get_Literal(object):
    def __init__(self):
        # wordlist is key word for search test data in wikipedia. There are two kind of test data, one is paragraph, another one is single sentences
        self.wordlistUrl = "http://www-personal.umich.edu/~jlawler/wordlist"
        self.wordlist = ''
        self.wordlistSize = 0

        #number of test need to generate
        self.numberOfTestData = 0;

    #run at begin get wordlist
    def Get_Wordlist(self):
        self.wordlist = requests.get(url = self.wordlistUrl)
        self.wordlist = self.wordlist.text.split()
        self.wordlistSize = len(self.wordlist)

    #parameter "sample "to tell how many sentences do you want to generate
    def setTestData(self,samplesize):
        self.Get_Wordlist()
        exceptFlag = False
        self.numberOfTestData=samplesize
        #sentencesFile = open("Sentences.txt", "w", encoding='utf-8')
        #wordlistFile = open("Wordlist.txt", 'w', encoding='utf-8')
        sentencesCount = 0


        interval = int((self.wordlistSize / self.numberOfTestData) / 2)
        startIndex = 0

        workbook = Workbook()
        workSheetOne = workbook.active
        workSheetOne.title = "English"

        while sentencesCount < self.numberOfTestData:
            try:
                exceptFlag = False
                randomNum = randint(startIndex, startIndex + interval - 1)    # Pick a random number between 1 and 100.
                startIndex += interval
                sentences = wikipedia.summary(self.wordlist[randomNum], sentences = 1)
            except:
                exceptFlag = True
            finally:
                if exceptFlag == False:
                    if sentences:
                        # Write the sentences into  the txt file
                        #sentencesFile.writelines(sentences)
                        #sentencesFile.writelines("\n")
                        # write send to wordlist
                        #wordlistFile.writelines(self.wordlist[randomNum])
                        #wordlistFile.writelines("\n")
                        sentencesCount += 1
                        workSheetOne['A' + str(sentencesCount)] = sentences
        #sentencesFile.close()
        #wordlistFile.close()
        '''
        workSheetTwo = workbook.copy_worksheet (workSheetOne)
        workSheetTwo.title = "Swedish"
        workSheetThree = workbook.copy_worksheet (workSheetOne)
        workSheetThree.title = "Japanese"

        '''
        workbook.save("csci318.xlsx")
        print ("finah set test data")
