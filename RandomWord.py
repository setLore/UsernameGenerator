import random

def random_word(filename,numOfWords):
    randomwordsdict = open(f'{filename}', 'r')
    sortedWords = randomwordsdict.read().splitlines()
    
    return sortedWords[random.randint(0,numOfWords-1)]

