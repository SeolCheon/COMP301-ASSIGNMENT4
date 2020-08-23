"""
File name : Task2.py
Author's name : Seol Cheon
Student Number : 301113120
File description :  Task 2 of assignment4.

Make the following modifications to the original sentence-generator program
a. The prepositional phrase is optional. (It can appear with a certain probability.)
b. A conjunction and a second independent clause are optional: The boy took a drink and
   the girl played baseball.
c. An adjective is optional: The girl kicked the red ball with a sore foot.
d. You should add new variables for the sets of adjectives and conjunctions
"""

import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL",)
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
conjunctions = ("FOR", "AND", "BUT", "NOR", "OR")
adjectives = ("CUTE", "FAST", "SMALL", "NICE")
    """variables for the sets of words"""

def sentence():
    """Builds and returns a sentence with optional conjuction and a second independent clause"""
    
    optIndClause = ""
    indepClauseChance = random.randrange(100) +1
    if(indepClauseChance >50) :
        optIndClause = random.choice(conjunctions)+ " "+ nounPhrase() + " " + verbPhrase()
            """put conjuctions and second independent clause with 50% of probability after a independent sentece"""
    return nounPhrase() + " " + verbPhrase() + " " + optIndClause
            

def nounPhrase():
    """Builds and returns a noun phrase with optional an adjective"""
    optAdjective = ""
    adjectiveChance = random.randrange(100) +1
    if(adjectiveChance > 50):
        optAdjective = random.choice(adjectives)
        """put adjective with 50 % of  probability before a noun"""

    return random.choice(articles) + " " + optAdjective +" " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    optPrepPhrase = ""
    prepPhraseChance = random.randrange(100) + 1
    if(prepPhraseChance > 50):
        optPrepPhrase =prepositionalPhrase()
        """put prepositional Phrase with 50% probability after verbPhrase"""
    return random.choice(verbs) + " " + nounPhrase() + " " + optPrepPhrase

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        """print the sentences"""
        
main()