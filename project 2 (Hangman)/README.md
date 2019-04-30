# Hangman

This code was written to create a Hangman game conforming to the following requirements as provided by MIT edX Intro to CS course (https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/courseware/530b7f9a82784d0cb57de334828e3050/bfe9eb02884a4812883ff9e543887968/1?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2017_2%2Btype%40vertical%2Bblock%40c949e378fb2d42f1b30877fc01b3ef5b):


- The computer must select a word at random from the list of available words that was provided in words.txt. The functions for loading the word list and selecting a random word have already been provided for you in ps3_hangman.py.

- The game must be interactive; the flow of the game should go as follows:

- At the start of the game, let the user know how many letters the computer's word contains.

- Ask the user to supply one guess (i.e. letter) per round.

- The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.

- After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.


Some additional rules of the game:

- A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).

- A user loses a guess only when s/he guesses incorrectly.

- If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.

- The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.
