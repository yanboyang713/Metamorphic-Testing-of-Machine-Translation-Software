import requests
import random
import wikipedia

class Get_Literal(object):
    def __init__(self):
        # wordlist is key word for search test data in wikipedia. There are two kind of test data, one is paragraph, another one is single sentences
        self.wordlistUrl = "http://www-personal.umich.edu/~jlawler/wordlist"
        self.wordlist = ''
        self.wordlistSize = 0
        self.wordlistIndex = 0

        #for paragraph test data
        self.paragraph = []
        self.paragraphSize = 0
        self.paragraphCount = 0

        #for sentences test data
        self.sentence = ''
        self.sentenceSize = 0
        self.sentenceCount= 0

        #for the list of  random number
        self.rand_list=[]

        # To record the index of the validly searched words.
        self.validIndex_List=[]

        #To record wether it is need to print the wordlist
        self.askPrintwordlist=''



        #run at begin get wordlist
        self.main()

        self.Get_Wordlist()

        self.setTestData()

        self.Print_Wordlist()


    def main(self):
        self.askPrintwordlist = input ("Do you want to get wordlist as key word search in wikipedia in Internet? (Y/n) : ")
        print(self.askPrintwordlist)


    def Get_Wordlist(self):
        self.wordlist = requests.get(url = self.wordlistUrl)
        self.wordlist = self.wordlist.text.split()
        self.wordlistSize = len(self.wordlist)
        #self.wordlistSize = 1000
        self.rand_list = random.sample(range(0, self.wordlistSize),self.wordlistSize)
        print (self.rand_list[0])

        '''
        #write the wordlist into the file "wordlist.txt"
        for i in range(0,20):
            f1=open("Wordlist.txt","a+",encoding='utf-8')
            f1.writelines(self.wordlist[self.rand_list[i]])
            f1.writelines("\n")
            f1.close()
        '''

        #print(self.wordlist[18])


    def Print_Wordlist(self):
        while self.askPrintwordlist !='Y'and self.askPrintwordlist !='n':
            self.askPrintwordlist = input("Incorrect input, please enter (Y/n) again: ")

        if self.askPrintwordlist == 'Y':
            for i in range(0,len(self.validIndex_List)):
                #print("valid word: %s" %self.wordlist[self.validIndex_List[i]])
                f2=open("Wordlist.txt","a+",encoding='utf-8')
                f2.writelines(self.wordlist[self.validIndex_List[i]])
                f2.writelines("\n")
                f2.close()
        elif self.askPrintwordlist == 'n':
            return



    def setTestData(self):
        exceptFlag = False
        #count = 0

        while self.sentenceCount < 10:
            print("*******")
            try:
                exceptFlag = False
                paragraph = wikipedia.summary(self.wordlist[self.rand_list[self.wordlistIndex]])
                print ("get")
            except:
                exceptFlag = True
                print("error")
                #continue
            finally:
                    #self.paragraph.extend(paragraph)
                    #self.sentences.extend(self.paragraph[self.paragraphSize].split('.'))
                if exceptFlag == False:
                    # Write the sentences into  the txt file
                    sentences = paragraph.split('.')
                    # print(sentences[0])
                    self.sentenceSize = len(sentences)
                    print(self.sentenceSize)
                    f3 = open("Sentences.txt", "a+", encoding='utf-8')
                    #f3.writelines(str(self.sentenceCount))
                    #f3.writelines(":  ")
                    #f3.writelines(self.wordlist[self.rand_list[self.wordlistIndex]])
                    #f3.writelines("_____:")
                    f3.writelines(sentences[0])
                    #f3.writelines("\n" + " -----------------------------END---------------------------------" + "\n")
                    f3.writelines("\n")
                    f3.close()
                    self.paragraphCount=self.paragraphCount+1
                    self.sentenceCount = self.sentenceCount + 1
                    self.validIndex_List.append(self.rand_list[self.wordlistIndex])
                    #print("valid index: %d" %self.rand_list[self.wordlistIndex])
            self.wordlistIndex = self.wordlistIndex + 1
            #print("self.sentenceCount: ")
            #print(self.sentenceCount)
            #print("self.wordlistIndex: ")
            #print(self.wordlistIndex)







        '''
        for i in range(0, 10):
            try:
                exceptFlag = False
                paragraph = wikipedia.summary(self.wordlist[self.rand_list[i]])
                print ("get")
            except:
                exceptFlag = True
                #continue
            finally:
                    #self.paragraph.extend(paragraph)
                    #self.sentences.extend(self.paragraph[self.paragraphSize].split('.'))
                if exceptFlag == False:
                    
                    #Write the paragraphs into the txt file
                    f2=open("Paragraph.txt","a+",encoding='utf-8')
                    f2.writelines(str(self.paragraphCount))
                    f2.writelines(":  ")
                    f2.writelines(self.wordlist[self.rand_list[i]])
                    f2.writelines("_____:")
                    f2.writelines(paragraph)
                    #f2.writelines("\n"+"PNUM=")
                    #f2.writelines(count)
                    f2.writelines("\n" + " -----------------------------END---------------------------------" + "\n")
                    f2.close()
                    self.paragraphCount=self.paragraphCount+1
                    #count=count+1

                    
                    #Write the sentences into  the txt file
                    sentences = paragraph.split('.')
                    #print(sentences[0])
                    self.sentenceSize = len(sentences)
                    print(self.sentenceSize)
                    for j in range(0, self.sentenceSize):
                        if self.sentenceCount<10:
                            #print("*******")
                            f3 = open("Sentences.txt", "a+", encoding='utf-8')
                            f3.writelines(str(self.sentenceCount))
                            f3.writelines(":  ")
                            f3.writelines(self.wordlist[self.rand_list[i]])
                            f3.writelines("_____:")
                            f3.writelines(sentences[j])
                            f3.writelines("\n" + " -----------------------------END---------------------------------" + "\n")
                            #f3.writelines("\n")
                            f3.close()
                            self.sentenceCount=self.sentenceCount+1
                        else:
                            continue

        '''




        '''
        #self.paragraphSize = len(self.paragraph)
        #self.sentenceSize = len(self.sentences)

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

    
    def Get_Random_List(self,length):
        rand_list=random.sample(range(0,length-1),length-1)
        return rand_list
    
    
    def Get_Random_Num(self):
        return self.rand[self.count]
        self.count=self.count+1
        '''

