#create list of words, pick a random word and have the user guess
#input, random, time (to delay)

import random
import time

#ask user for name
name = input("What is your name > ")
print("Welcome to the Xhorhouse", name)

wordList = ["Vex", "Percy", "Grog", "Vax", "Scanlan", "Pike", "Keyleth", "Gilmore", "Allura", "Kima", "Tary", "Doty"]

game = input("You wanna play > ")
while game == "yes":
    word = random.choice(wordList)
    guess = ""
    turns = 5
    print(name, "You have", turns, "turns to guess the word")
    while turns > 0:
        for char in word:
            if char in guess:
                print(char, end=" ")
            else:
                print("_", end=" ")
        print()
        guess = input("What is your guess > ")
        turns = turns - 1
        if guess == word:
            print("You won with", turns, "turns left")
            break
    game = input("Do you want to play again > ")