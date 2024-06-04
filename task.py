#!/usr/bin/env python

import random

def main():
    """Start a Popular PC Game guessing game."""
    print("Guess the Porpular PC Game in the world?")
    
    games = [
        "minecraft",
        "counter-strike",
        "mobile legends",
        "roblox",
        "pac man",
        "scrabble",
        "pubg"
        ]

    x =random.choice(games)
    max_trials= 4
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("What the popular pc game are we thinking of? "))
        
        if x == guess:
            print(f"You guessed.Congratulations you got it right!".format(guess))
            break
        else:
            print(f"Unfortunately you got the wrong answer.".format(guess))
            
            print(f"You have {max_trials} chances remaining.")
            max_trials -= 1
        if max_trials == 0:
            print(f"out of attempts. The genre is actually {x}.".format(guess))
        
main()