import requests
import random
import wikipedia

class Get_Literal(object):
    def __init__(self):
        self.url="http://www-personal.umich.edu/~jlawler/wordlist"
        self.wordlist=''
        self.word=''
        self.paragraph=''
        self.sentences=''
       # self.rand=''
        #self.count=0

    def Get_Wordlist(self):
        self.wordlist=requests.get(url=self.url)
        self.wordlist=self.wordlist.text.split()
 #       print(self.wordlist[18])

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

