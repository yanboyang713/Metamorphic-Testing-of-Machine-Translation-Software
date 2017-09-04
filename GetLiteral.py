import requests
import random
import wikipedia

class Get_Literal(object):
    def __init__(self):
        # wordlist is key word for search test data in wikipedia. There are two kind of test data, one is paragraph, another one is single sentences
        self.wordlistUrl = "http://www-personal.umich.edu/~jlawler/wordlist"
        self.wordlist = ''
        self.wordlistSize = 0

        #for paragraph test data
        self.paragraph = []
        self.paragraphSize = 0

        #for sentences test data
        self.sentences = ''
        self.sentenceSize = 0

        self.main()

        #run at begin get wordlist
        self.Get_Wordlist()


    def main(self):
        askGetwordlist = input ("Do you want to get wordlist as key word search in wikipedia in Internet? (Y/n) : ")
    def Get_Wordlist(self):
        self.wordlist = requests.get(url = self.wordlistUrl)
        self.wordlist = self.wordlist.text.split()
        self.wordlistSize = len(self.wordlist)
        print (self.wordlistSize)
        #print(self.wordlist[18])

    def setTestData(self):
        for i in range(0, self.wordlistSize):
            try:
                temp = wikipedia.summary(self.wordlist[i])
                print ("get")
            except:
                continue
            finally:
                    self.paragraph.extend(temp)
                    self.sentences.extend(self.paragraph[self.paragraphSize].split('.'))

        self.paragraphSize = len(self.paragraph)
        self.sentenceSize = len(self.sentences)

    def print(self):
        print("print all of paragraph : )")
        for i in range(0, self.paragraphSize):
            print(self.paragraph[i])

        print("print all of sentences : )")
        for i in range(0, self.sentenceSize):
            print(self.sentences[i])

    def Capture_Word(self,num):
       # rand1=random.randint(0,len(self.wordlist)-1)
        self.word=self.wordlist[num]
        print(self.word)

    def Get_Paragraph(self):
            self.paragraph = wikipedia.summary(self.word)
            self.sentences = self.paragraph.split('.')
            return self.paragraph

    def Get_Sentence(self,num):
        #self.paragraph=wikipedia.summary(self.word)
        #self.sentences=self.paragraph.split('.')
        #rand2 = random.randint(0, len(self.sentences) - 1)
        return self.sentences[num]
#      print(self.paragraph[0])

    def Get_Wordlist_Length(self):
        return len(self.wordlist)

    def Get_Sentences_Length(self):
        return len(self.sentences)

    '''
    def Get_Random_List(self,length):
        rand_list=random.sample(range(0,length-1),length-1)
        return rand_list
    '''
    '''
    def Get_Random_Num(self):
        return self.rand[self.count]
        self.count=self.count+1
    '''

