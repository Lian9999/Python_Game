# Hangman Game
# -----------------------------------
# Helps user play the game Hangman
# -----------------------------------
import random 
 
def get_word(): 
	words = ['pizza', 'cheese', 'apples', 'bread'] 
	return random.choice(words) 

 # Function to check if the letter entered by the user exists in the word 
def check(word, letter, guesses): 

	status = '' 
	matches = 0

	for char in word: 

		if char in guesses: 

			status += char  

		else:  

		    status += '*'  

        # If user has guessed all the letters 

            if status == word:  

                print('You won!')  

                break  

        # print current status of word  

        print(status)  

        # If user has used all of his chances  

        if len(letter) == 0:  

            print('You lost! The word was {}'.format(word))