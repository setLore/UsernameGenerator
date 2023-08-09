import random

def random_word(filename,numOfWords):
    randomwordsdict = open(f'{filename}', 'r')
    sortedWords = sorted(randomwordsdict.read().splitlines(), key=len)
    
    return sortedWords[random.randint(0,numOfWords-1)]

