"""
File name : Task1.py
Author's name : Seol Cheon
Student Number : 301113120
File description :  Task 1 of assignment4.

The filenames are nouns.txt, verbs.txt, articles.txt, and prepositions.txt. (Hint: Define a
single new function, getWords. This function should expect a filename as an argument.
The function should open an input file with this name, define a temporary list, read
words from the file, and add them to the list. The function should then convert the list
to a tuple and return this tuple. Call the function with an actual filename to initialize
each of the four variables for the vocabulary.)
"""

"""define new function that has a filename as an argument"""
def getWords(fileName):

    """open a file as a read mode and assign it to wordsFileOPen"""
    wordsFileOpen = open(fileName, "r")

    """make a temporary list"""
    temporaryList = []

    """read strings in wordsFileOpen file and assign it to wordsFileRead"""
    wordsFileRead = wordsFileOpen.read()

    """split the strings by " "(space) and assign them to word""" 
    word = wordsFileRead.split()

    """put the word to the temporary list"""
    temporaryList = [word]

    """change the list to a tuple and assign it to words"""
    words = tuple(temporaryList)   

    """return the tuple"""
    return words


def main():

    """prompt users to input text file names that has words and assign them noun, verb, prepositon and article"""
    noun = input("Enter a file that has nouns with extension: ")
    verb = input("Enter a file that has verbs with extension: ")    
    preposition = input("Enter a file that has prepositions with extension: ")
    article = input("Enter a file that has articles with extension: ")    

    """call the function getWords with argument and assign it to noun, verb, preposition and article """
    noun = getWords(noun)
    verb = getWords(verb)
    preposition = getWords(preposition)
    article = getWords(article)

    """print the tuples returned from getWords function"""
    print(article)
    print(noun)
    print(verb)
    print(preposition)

"""set main function as a main program and implement it"""
if __name__ == "__main__":
    main()

