import sys
import requests
import nltk
class Nltk(object):
    def __init__(self):
        weights = [0.25, 0.25, 0.25, 0.25]
        candidate1 = ['It', 'is', 'a', 'guide', 'to', 'action', 'which',
                      'ensures', 'that', 'the', 'military', 'always',
                      'obeys', 'the', 'commands', 'of', 'the', 'party']

        candidate2 = ['It', 'is', 'to', 'insure', 'the', 'troops',
                     'forever', 'hearing', 'the', 'activity', 'guidebook',
                      'that', 'party', 'direct']

        reference1 = ['It', 'is', 'a', 'guide', 'to', 'action', 'that',
                      'ensures', 'that', 'the', 'military', 'will', 'forever',
                      'heed', 'Party', 'commands']

        reference2 = ['It', 'is', 'the', 'guiding', 'principle', 'which',
                      'guarantees', 'the', 'military', 'forces', 'always',
                      'being', 'under', 'the', 'command', 'of', 'the',
                      'Party']

        reference3 = ['It', 'is', 'the', 'practical', 'guide', 'for', 'the',
                      'army', 'always', 'to', 'heed', 'the', 'directions',
                      'of', 'the', 'party']


    def checkScore(self):
        #there may be several reference
        nltk.align.bleu_score.bleu(candidate2, [reference1, reference2, reference3], weights)
