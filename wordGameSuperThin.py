import random
game = input("You wanna play > ")
while game == "h" or game == "m" or game == "e" or game == "yes":
    game = input ("Do you want hard (h), medium (m), or easy (e) > ")
    wordFile = ""
    if (game == 'h'):
        wordFile = open("hard.txt", "r")
    elif (game == 'm'):
        wordFile = open("medium.txt", "r")
    elif (game == 'e'):
        wordFile = open("easy.txt", "r")
    else:
        wordFile = open("stupidEasy.txt", "r")
    wordList = wordFile.read().split("\n")
    word = random.choice(wordList)
    guess = []
    turns = 7
    while turns > 0:
        allRight = True
        for char in word:
            if char in guess:
                print(char, end=" ")
            else:
                allRight = False
                print("_", end=" ")
        if allRight:
            break
        userGuess = input("\nWhat is your guess > ")
        if userGuess in word:
            guess.append(userGuess)
        else:
            turns = turns - 1