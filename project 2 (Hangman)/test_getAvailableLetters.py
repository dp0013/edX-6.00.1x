# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 21:06:38 2019
 
@author: dp

EXAMPLE USAGE:lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
"""
import string

lettersGuessed = ['a', 'z']


#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

#lettersGuessed = ['g', 'r', 'a', 'p', 'e', 'f', 'r']

#lettersGuessed = ['y', 'm', 's', 'a', 'c', 'g', 'e', 'o', 'q', 'p']

#lettersGuessed = ['k', 'v', 'u', 't', 'x', 'h', 'z', 'g', 'w', 'j']



def getAvailableLetters(lettersGuessed):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # return a string of all unused letters after subtracting the ones in lettersGuessed from the string of all lowercase ascii letters  
    return ''.join(sorted(set(string.ascii_lowercase).difference(set(lettersGuessed))))

# end of helper code
# -----------------------------------
   
print(getAvailableLetters(lettersGuessed))
