import requests
import random
import wikipedia

class Get_Literal(object):
    def __init__(self):
        self.url="http://www-personal.umich.edu/~jlawler/wordlist"
        self.wordlist=''
        self.word=''
        self.paragraph=''
        self.sentence=''

    def Get_Wordlist(self):
        self.wordlist=requests.get(url=self.url)
        self.wordlist=self.wordlist.text.split()
 #       print(self.wordlist[18])

    def Capture_Word(self):
        rand1=random.randint(0,len(self.wordlist)-1)
        self.word=self.wordlist[rand1]
 #       print(self.word)

    def Get_Paragraph(self):
            self.paragraph = wikipedia.summary(self.word)
            return self.paragraph

    def Get_Sentence(self):
        self.paragraph=wikipedia.summary(self.word)
        self.sentence=self.paragraph.split('.')
        rand2 = random.randint(0, len(self.sentence) - 1)
        return self.sentence[rand2]
#      print(self.paragraph[0])

