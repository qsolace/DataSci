#create list of words, pick a random word and have the user guess
#input, random, time (to delay)
import math
import random
import time

#ask user for name
name = input("What is your name > ")
print("Welcome to the Xhorhouse", name)


game = input("You wanna play > ")



while game == "yes" or game == "y":
    difficulty = input ("Do you want hard (h), medium (m), or easy (e) > ")
    wordFile = ""
    if (difficulty == 'h'):
        wordFile = open("hard.txt", "r")
    elif (difficulty == 'm'):
        wordFile = open("medium.txt", "r")
    elif (difficulty == 'e'):
        wordFile = open("easy.txt", "r")
    else:
        print ("You did not select a diffuculty. You failed that simple task, so we're giving you the really easy one. It's **just** the letter a")
        wordFile = open("stupidEasy.txt", "r")
    
    wordList = wordFile.read().split("\n")

    word = random.choice(wordList)
    guess = []
    turns = 7


    print(name, "You have", turns, "turns to guess the word")
    while turns > 0:
        allRight = True
        for char in word:
            if char in guess:
                print(char, end=" ")
            else:
                allRight = False
                print("_", end=" ")

        print()
        if allRight:
            print("You guessed the word with", turns, "turns left!")
            break
        userGuess = input("What is your guess > ")
        if userGuess in word:
            guess.append(userGuess)
        else:
            turns = turns - 1
    if turns == 0:
        print ("You FAILED!!!!")
        print ("=(")
        print()
    game = input("Do you want to play again > ")