import sys
from nltk import Nltk
import sched, time
from youdao import Youdao
from bing import Bing
from GetLiteral import Get_Literal
# each 9 mins get a new token for bing translate
def getToken(scheduler, bing):
    print ("Doing stuff...")

    bing.getToken()
    # do your stuff
    scheduler.enter(60, 1, getToken, (scheduler,bing))

#main function
def main():
    #Test obtain paragraph & sentence
    #l1=Get_Literal()
    #l1.Get_Wordlist()
    #l1.Capture_Word()
    #P1=l1.Get_Paragraph()
    #print(P1)
    #print('*********************************************')
    #S1=l1.Get_Sentence()
    #print(S1)

    #Test translation
    youdao = Youdao()
    #youdao.translate("EN", "zh_CHS", S1)
    print (youdao.translate("EN", "zh_CHS", "this is a test"))
    bing = Bing()
    fromLanguage = "en"
    toLanguage = "fr"
    translateText = "this is a test, hope well word"
    bing.getToken()
    print (bing.translate(translateText, fromLanguage, toLanguage))

    # nltk
    ownnltk = Nltk()
    #ownnltk.checkScore()
    # this is for get a new bing token every 9 mins because one token only vaild 10 mins
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(60, 1, getToken, (scheduler, bing))
    scheduler.run()


if __name__ == "__main__":
  main()
