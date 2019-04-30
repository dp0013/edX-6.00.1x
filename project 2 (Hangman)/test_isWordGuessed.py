# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:50:52 2019
 
@author: D. Plyler
"""
secretWord = 'grapefruit' 
lettersGuessed = ['h', 'z', 'r', 'a', 'p', 'e', 'f', 'r', 'u', 'i', 't']

def isWordGuessed(secretWord, lettersGuessed):
    maxG = 8 + len(secretWord)  # max Guesses
    answer = []
    while maxG > 0:
        for letter in lettersGuessed:
            if letter in sorted(set(secretWord)):
                answer.append(letter)
                print("TEST -- sorted(set(answer)) is", sorted(set(answer)))
                print("TEST -- sorted(set(secretWord)) is", sorted(set(secretWord)))

        if (sorted(set(answer))) == (sorted(set(secretWord))):
            return True
        else:
            return False
        maxG -= 1
            
print(isWordGuessed(secretWord, lettersGuessed))
