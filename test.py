from random import *
interval = 10
startIndex = 0
for i in range(0, 5):
    x = randint(startIndex, startIndex + interval - 1)    # Pick a random number between 1 and 100.
    startIndex += interval
    print (x)
