import sys
from nltk import Nltk
from commonTranslator import CommonTranslator
from GetLiteral import Get_Literal
import time

#main function
def main():
    #Test obtain paragraph & sentence
<<<<<<< HEAD
    testData=Get_Literal()
    testData.Get_Wordlist()
=======
    l1=Get_Literal()
    l1.setTestData()
    print ("finish set up data")
    l1.print()
>>>>>>> origin/master
    #l1.Capture_Word()
    #P1=l1.Get_Paragraph()
    #print(P1)
    #print('*********************************************')
    #S1=l1.Get_Sentence()
    #print(S1)

    # Perform translations with a common iunterface
<<<<<<< HEAD
    #translator = CommonTranslator()
    #print( translator.translate('Google', 'Hello, World!', 'fr', 'EN') )
    #print( translator.translate('Bing', 'Hello, World!', 'fr', 'EN') )
    #print( translator.translate('Youdao', 'Hello, World!', 'fr', 'EN') )
    #print( translator.translate('All', 'Hello, World!', 'es', 'EN') )
    #print('Complete')

=======
    '''
    translator = CommonTranslator()
    print( translator.translate('Google', 'Hello, World!', 'fr', 'EN') )
    print( translator.translate('Bing', 'Hello, World!', 'fr', 'EN') )
    print( translator.translate('Youdao', 'Hello, World!', 'fr', 'EN') )
    print( translator.translate('All', 'Hello, World!', 'es', 'EN') )
    print('Complete')
'''
>>>>>>> origin/master
    # nltk
    #ownnltk = Nltk()
    #ownnltk.checkScore()

if __name__ == "__main__":
  main()
