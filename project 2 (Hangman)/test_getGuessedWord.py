# -*- coding: utf-8 -*-
"""
Created on Wed Jan 4 18:13 2019
 
@author: D. Plyler
"""
#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

secretWord = 'grapefruit' 
lettersGuessed = ['g', 'r', 'a', 'p', 'e', 'f', 'r']

#secretWord = 'banana'
#lettersGuessed = ['y', 'm', 's', 'a', 'c', 'g', 'e', 'o', 'q', 'p']
#
#secretWord = 'lettuce'
#lettersGuessed = ['k', 'v', 'u', 't', 'x', 'h', 'z', 'g', 'w', 'j']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      
    EXAMPLE:  secretWord = 'apple' 
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(getGuessedWord(secretWord, lettersGuessed))
    returns  '_ pp_ e'
    '''
    answer = []
    i =   len(secretWord)  # limit the iterations
    index = 0  # track the spot
    wordList = list(secretWord)  # track unique letters

    while i > 0:               
        for letter in secretWord:  # one iteration for each letter
#            print(index)
#            print(wordList)
#            print(letter)
            
            if letter in lettersGuessed:  # if guessed letter is correct
#                print(letter)
                answer.insert(index, letter)  # insert letter into answer
            else: 
                answer.insert(index, '_ ')  # insert blank if not correct
            wordList.pop(0)  # remove each letter from list 
            i -= 1
            index += 1
    answer = ''.join(answer)  # convert to string
#    print(answer)
    return answer
    
print(getGuessedWord(secretWord, lettersGuessed))





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
