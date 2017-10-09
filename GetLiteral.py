import requests
import random
import wikipedia
from openpyxl import Workbook

class Get_Literal(object):
    def __init__(self):
        # wordlist is key word for search test data in wikipedia. There are two kind of test data, one is paragraph, another one is single sentences
        self.wordlistUrl = "http://www-personal.umich.edu/~jlawler/wordlist"
        self.wordlist = ''
        self.wordlistSize = 0

        #for the list of  random number
        self.rand_list=[]

        #to record wether it is need to set new test data
        self.askSetNewTestData = ''

        #number of test need to generate
        self.numberOfTestData = 0;

        #run at begin get wordlist
        self.main()

    def main(self):
        self.askSetNewTestData = input ("Do you want to set new test "Japanese"data? (Y/n) : ")
        if self.askSetNewTestData == 'Y' or self.askSetNewTestData == 'y':
            self.numberOfTestData = input ("How many sentences do you want to generate? ")
            self.setTestData()
        else:
            print("error")
            return;

    def Get_Wordlist(self):
        self.wordlist = requests.get(url = self.wordlistUrl)
        self.wordlist = self.wordlist.text.split()
        self.wordlistSize = len(self.wordlist)
        self.rand_list = random.sample(range(0, self.wordlistSize),self.wordlistSize)

    def Print_Wordlist(self):
        self.Get_Wordlist()
        wordlistFile = open("Wordlist.txt", 'w', encoding='utf-8')
        for i in range(0, self.wordlistSize):
            wordlistFile.writelines(self.wordlist[self.rand_list[i]])
            wordlistFile.writelines("\n")

        wordlistFile.close()

    def setTestData(self):
        self.Print_Wordlist()
        exceptFlag = False
        sentencesFile = open("Sentences.txt", "w", encoding='utf-8')
        sentencesCount = 0
        index = 0

        workbook = Workbook()
        workSheetOne = workbook.active
        workSheetOne.title = "Chinese"

        while sentencesCount < int(self.numberOfTestData):
            try:
                exceptFlag = False
                paragraph = wikipedia.summary(self.wordlist[index])
            except:
                exceptFlag = True
                print("error")
            finally:
                if exceptFlag == False:
                    # Write the sentences into  the txt file
                    sentences = paragraph.split('.')
                    sentencesFile.writelines(sentences[0])
                    sentencesFile.writelines('.')
                    sentencesFile.writelines("\n")
                    sentencesCount += 1
                    workSheetOne['A' + str(sentencesCount)] = sentences[0] + "."
                index += 1
        sentencesFile.close()

        workSheetTwo = workbook.copy_worksheet (workSheetOne)
        workSheetTwo.title = "Swedish"
        workSheetThree = workbook.copy_worksheet (workSheetOne)
        workSheetThree.title = "Japanese"
        workbook.save("csci318.xlsx")
        print ("finah set test data")
