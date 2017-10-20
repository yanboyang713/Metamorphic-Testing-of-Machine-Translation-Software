import math, re
from collections import Counter


def calculateCosineSimilarity(sentence1, sentence2):
    regex = re.compile(r'\w+')

    wordMatches = regex.findall(sentence1)
    wordFrequencyVec1 = Counter(wordMatches)

    wordMatches = regex.findall(sentence2)
    wordFrequencyVec2 = Counter(wordMatches)

    intersection = set(wordFrequencyVec1.keys()) & set(wordFrequencyVec2.keys())

    vecSum1 = sum([wordFrequencyVec1[x]**2 for x in wordFrequencyVec1.keys()])
    vecSum2 = sum([wordFrequencyVec2[x]**2 for x in wordFrequencyVec2.keys()])

    vecSum1Sqrt = math.sqrt(vecSum1)
    vecSum2Sqrt = math.sqrt(vecSum2)

    denom = vecSum1Sqrt * vecSum2Sqrt

    dotProduct = sum([wordFrequencyVec1[x] * wordFrequencyVec2[x] for x in intersection])

    if not denom:
        return 0.0
    else:
        cosine = dotProduct / denom
        return cosine


print (calculateCosineSimilarity('I love apples', 'I like apples'))

print (calculateCosineSimilarity('This string is to test the program', 'The string is being used for testing'))

print (calculateCosineSimilarity('This is a test', 'This is a test'))

print (calculateCosineSimilarity('One Two Three', 'Four Five Six'))