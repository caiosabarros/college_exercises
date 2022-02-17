"""
File: 075guessnumber.py
Author: Caio Sa

Purpose: Computer guess random number itself
"""

import random

def guess_Game():

    number = random.randint(1,10)
    number_was_guessed = False
    trials = 0

    while number_was_guessed == False:
        guess = random.randint(1,10)
        trials += 1
        if guess == number:
            print(f"The computer guessed it right in the {trials} trial!")
            number_was_guessed = True
        elif guess > number:
            print("Lower")
        else:
            print("Higher")
    
play = True
while play:
    guess_Game()
    play_again = input("Do you want to play again? ")
    if play_again == "no":
        play = False
        print("Thanks for playing")