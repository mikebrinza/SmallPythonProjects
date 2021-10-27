#Simple Rock, Paper, Scissor's game
#Plays 3 matches  
import random

strOptions = ["rock", "paper", "scissors"]
gameRunning = True
bestOf = 3
matchCount = 0
score = {
    "pl": 0, 
    "ai":0
        }

#define function to print the result for every match
def printResult(condition,userString,aiString):
    print("Your choise: ", userString)
    print("Computer's choise: ", aiString)
    print(" ")
    if (condition == "w"):
        print("Congrats, you won")
    elif (condition == "l"):
        print("You're dead! Try again!")
    elif (condition == "d"):
        print("Equal power! Go Again!")

#function to play a match
def playMatch():
    aiChoice = strOptions[random.randrange(0,3)]
    if getUserString == aiChoice:
        printResult("d", getUserString, aiChoice)
    elif getUserString == "rock" and aiChoice == "scissors":
        printResult("w", getUserString, aiChoice)
        score["pl"] += 1
    elif getUserString == "paper" and aiChoice == "rock":
        printResult("w", getUserString, aiChoice)
        score["pl"] += 1
    elif getUserString == "scissors" and aiChoice == "paper":
        printResult("w", getUserString, aiChoice)
        score["pl"] += 1
    else:
        printResult("l", getUserString, aiChoice)
        score["ai"] += 1

while gameRunning == True:
    #get user input
    getUserString = input("Type Rock, Paper or Scissors: ").lower()

    #check if user input is a valid choice
    if getUserString not in strOptions:
        print("Must be a valid choice('rock', 'paper', or 'scissors'")
        break
    playMatch()
    if score["ai"] + score["pl"] == bestOf:
        gameRunning = False
    matchCount += 1

#print final score
print("Final Score: ")
print("Computer score: ", score["ai"])
print("Your score: ", score["pl"])
print("Number of matches: ", matchCount)


#TO DO 
# implement game on a website

