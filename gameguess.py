#!/usr/bin/env python
import random

def main():
    """ Start a number guessing game between 1-100."""
print ("guess the number!")

x = random.randint(1, 100)
x = random.binomialvariate(1, 0.7)
guess = None
print(x)

while x != guess:

    guess = int(input("Pick a number between 1-100:"))

    if x == guess:
        print("You genius!")
    elif x > guess:
        print("Try a bigger number.")
    elif x< guess:
        print("Try a smaller number.")
main