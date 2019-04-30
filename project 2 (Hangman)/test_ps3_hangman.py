# -*- coding: utf-8 -*-
"""
Created on Wed Jan 4 18:13 2019
 
@author: D. Plyler

Hangman game
----------------------------------
"""
import random
import string

WORDLIST_FILENAME = "words.txt"
#answer = []  # empty answer container

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

def chooseWord(wordlist):  # chooses random word from 'words.txt'
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
lettersGuessed = []
answer = []

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if sorted(set(answer)) == sorted(set(secretWord)):
        return True
    else:
        return False
                

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    progress = []
    i =   len(secretWord)  # limit the iterations
    index = 0  # track the spot
    wordList = list(secretWord)  # track unique letters

    while i > 0:               
        for letter in secretWord:  # one iteration for each letter
            if letter in lettersGuessed:  # if guessed letter is correct
                progress.insert(index, letter)  # insert letter into answer
            else: 
                progress.insert(index, '_ ')  # insert blank if not correct
            wordList.pop(0)  # remove each letter from list 
            i -= 1
            index += 1
    progress = ''.join(progress)  # convert to string
    return progress


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # return a string of all unused letters after subtracting the ones in lettersGuessed from the string of all lowercase ascii letters  
    return ''.join(sorted(set(string.ascii_lowercase).difference(set(lettersGuessed))))
    

def hangman(secretWord):
    # FILL IN YOUR CODE HERE...
    maxGuesses = 9
    lettersGuessed = []
    answer = []

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    print("-------------")
    
    while maxGuesses > 0:  # while guesses remaining
        
        if sorted(set(answer)) == sorted(set(secretWord)):
            print("Congratulations, you won!")
            break
        
        elif maxGuesses == 1:
            print("Sorry, you ran out of guesses. The word was", secretWord + '.')
            break
        
        else:
            print("You have", maxGuesses-1, "guesses left")
            print("Available letters:", getAvailableLetters(lettersGuessed))
            guess = input("Please guess a letter: ")
            guess = guess.lower()
                     
            if guess in sorted(set(secretWord)):
                answer.append(guess)
    
            if guess in lettersGuessed:  # guess is redundant
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                
            elif guess not in secretWord:  # bad guess
                lettersGuessed.append(guess)
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)) 
                print("-----------")
                maxGuesses -= 1
                    
            elif guess in secretWord:  # good guess
                lettersGuessed.append(guess)
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
             
            print("TEST -- sorted(set(answer)) is", sorted(set(answer)))
#            print("TEST -- These are the letters guessed so far:", lettersGuessed)
            print("TEST -- The sorted(set(secretWord)):", (sorted(set(secretWord))))



#secretWord = 'c'
secretWord = chooseWord(wordlist).lower()
#print("secret word is ", secretWord, '\n')
hangman(secretWord)
