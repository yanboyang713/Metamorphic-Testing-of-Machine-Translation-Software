import sys
#from nltk import Nltk
from commonTranslator import CommonTranslator
#from GetLiteral import Get_Literal
import time

#main function
def main():
    translator = CommonTranslator()
    # Chinese, Japanese, Korean, French, Russian, Portuguese, Spanish and Swedish
    desired_languages = ['zh-CHS', 'ja', 'ko', 'fr', 'ru', 'pt', 'es', 'sv']

    #Test obtain paragraph & sentence
    #setTestData = Get_Literal()
    #l1=Get_Literal()
    #l1.setTestData()
    #print ("finish set up data")
    #l1.print()
    #l1.Capture_Word()
    #P1=l1.Get_Paragraph()
    #print(P1)
    #print('*********************************************')
    #S1=l1.Get_Sentence()
    #print(S1)

    translator = CommonTranslator()

    print( translator.translate('Bing', 'Hello, World!', 'fr', 'EN') )
    # Perform translations with a common iunterface

    # For each sentence convert to all desired languages and write to the excel file.
    # Languages codes that we will be examining in our test are:
    sentence = 'Hello World.'
    for language in desired_languages:
        translations = translator.translate('All', sentence, language, 'EN')
        print (translations)
    print('Complete')


    # nltk
    #ownnltk = Nltk()
    #ownnltk.checkScore()

if __name__ == "__main__":
  main()
