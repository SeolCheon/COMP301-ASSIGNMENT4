import random
def getWords(fileName):

    wordsFileOpen = open(fileName, "r")
    temporaryList = []
    wordsFileRead = wordsFileOpen.read()    
    temporaryList = [wordsFileRead]
    words = tuple(temporaryList)   

    return words
