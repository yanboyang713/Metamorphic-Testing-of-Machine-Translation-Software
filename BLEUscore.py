import nltk

'''
Class to generate the BLEU score based on two passing sentences

Example Usage:
    Sentence1="an orangle"
    Sentence2="This an orangle"
    B1=GetBLEUscore(Sentence1,Sentence2)
    print(B1)
'''
def GetBLEUscore(string1, string2):
    hyp=string1.split()
    ref=string2.split()

    len_max = max(len(hyp), len(ref))
    len_min = min(len(hyp), len(ref))

    print(len_max)
    print(len_min)
    if len_max < 4:
        weight = (1 / len_min,) * len_min

    BLEU_score = nltk.translate.bleu_score.sentence_bleu([ref], hyp,weights=weight)
    #print(BLEU_score)

    return BLEU_score