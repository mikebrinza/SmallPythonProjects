#Guess the number minigame
#Inspired by djangocentral.com

import random

randNum = random.randrange(1,101)
playerName = input("Type your name: ")
guessCount = 0
noGames = 7
choicesLeft = noGames - guessCount

print("Hey " + playerName + "! Guess what number from 1 to 100 I'm thinking of!")
print("You have " + str((noGames - guessCount)) + " guesses")

while guessCount < noGames:
    guess = int(input())
    guessCount += 1
    if guess == randNum:
        print("You guessed right! Congrats")
        exit(1)
    elif guess < randNum:
        print("Nope, it's higher than that. You have " + str(choicesLeft) + " choices left.")
    elif guess > randNum:
        print("Nope, it's lower than that. You have " + str(choicesLeft) + " choices left.")

print("Oops you are out of tries")
print("The number was ",randNum)
print("Better luck next time, "+ playerName +" !")