#!/usr/bin/env python

import random

def main():
    """Start a Popular PC Game guessing game."""
    print("Guess the popular PC game in the world?")
    
    games = [
        "minecraft",
        "counter-strike",
        "mobile legends",
        "roblox",
        "pac man",
        "scrabble",
        "pubg"
    ]

    x = random.choice(games)
    max_trials = 4
    trial = 0
    guess = None
    
    while trial < max_trials:
        guess = input("What popular PC game are we thinking of? ")
        
        if x == guess.lower():
            print(f"Congratulations! You guessed it right. The game is {x.capitalize()}.")
            break
        else:
            print(f"Unfortunately, that's not correct. Clue: {', '.join(games)}.")
            print(f"You have {max_trials - trial - 1} chances remaining.")
            trial += 1
    else:
        print(f"Out of attempts. The correct answer was {x.capitalize()}.")
 

if __name__ == "__main__":
    main()
