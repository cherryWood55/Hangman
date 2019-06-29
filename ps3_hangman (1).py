# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for l in secretWord:
        if l in lettersGuessed:
            word = word + l
        else:
            word = word + "_ "
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remain = ""
    for l in string.ascii_lowercase:
        if l not in lettersGuessed:
            remain += l
    return (remain)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    num = 8
    lettersGuessed = []
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word which is "+ str(len(secretWord)) + " letters long.")
    print ("------------")
    while (num > 0):
        print ("You have " + str(num) +" guesses left.")
        print ("Available letters: "+ getAvailableLetters(lettersGuessed))
        print ("Please guess a letter: ", end='')
        guess = input()
        guessInLowerCase = guess.lower()      
        if guessInLowerCase in secretWord and guessInLowerCase not in lettersGuessed:
            lettersGuessed.append(guessInLowerCase)
            print ('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        elif guessInLowerCase in lettersGuessed:
            print ("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guessInLowerCase)
            print ('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            num -= 1
        print ("------------")
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print ('Congratulations! You won!')
            break
        
    if (isWordGuessed(secretWord, lettersGuessed) == False):
        print ('Sorry, you ran out of guesses. The word was '+ secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
