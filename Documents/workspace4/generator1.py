import random
def getWords(fileName):

    wordsFileOpen = open(fileName, "r")
    temporaryList = []
    wordsFileRead = wordsFileOpen.read()    
    temporaryList = [wordsFileRead]
    words = tuple(temporaryList)   

    return words

def main():

    noun = input("Enter a noun file and extension: ")

    verb = input("\nEnter a verbs file and extension: ")
    
    preposition = input("\nEnter a prepositions file and extension: ")

    article = input("\nEnter an artice file and extension: ")    

    article = getWords(article)
    noun = getWords(noun)
    verb = getWords(verb)
    preposition = getWords(preposition)

    print(article)
    print(noun)
    print(verb)
    print(preposition)

if __name__ == "__main__":
    main()

