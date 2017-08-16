import sys
from youdao import Youdao
from GetLiteral import Get_Literal
#main function
def main():
    #Test obtain paragraph & sentence
    l1=Get_Literal()
    l1.Get_Wordlist()
    l1.Capture_Word()
    P1=l1.Get_Paragraph()
    #print(P1)
    #print('*********************************************')
    S1=l1.Get_Sentence()
    #print(S1)

    #Test translation
    youdao = Youdao()
    youdao.translate("EN", "zh_CHS", S1)
if __name__ == "__main__":
  main()