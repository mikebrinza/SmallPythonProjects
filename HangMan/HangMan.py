#A hangman game where the user must guess the computer's word before being hanged
#inspired by "selftaught.blog" tutorial for hangman

import random

wordCollection = []
#import words from the wordCollection.txt file
with open("wordCollection.txt", "r") as file:
    for word in file:
        stripWords = word.strip().replace("'","").strip(",")
        wordCollection.append(stripWords)
randomWord = wordCollection[random.randrange(0,len(wordCollection))]

def main():
    hangMan(randomWord)

#code to return a letter guessed by the user
def userGuessLetter():
    while True:
        userInput = str(input("Guess a letter: "))
        if len(userInput) != 1:
            print("Must be a letter only")
        else:
            return userInput

#function if the game is won
def gameWon(word):
    print("Congratulations! You guessed the word!")
    print("The word to guess was: ", word)
    exit()

#function if the game is lost
def gameOver(word):
    print("Game Over!")
    print("You ran out of guesses :(")
    print("The word to guess was: ", word)
    print("May you swing in peace!")
    exit()

#main game
def hangMan(word :str):
    wrongGuesses = 0
    lettersUsed = []
    stages = ["_______ ", "|   | ", "|   0 ", "|  /|\ ", "|  / \ ", "| ", "|[^^^^^^^]"]
    board = ["_"] * len(word)
    wordList = list(word)
    print("\n")
    print("Let's play Hangman!")

    #loop of the game
    while wrongGuesses < len(stages):
        #check to see if game is over
        if "_" not in board:
            gameWon(word)

        print("\n")
        #print the board (hidden word to guess)
        print("The word to guess is: ")
        for boardSpace in board:
            print(boardSpace, end="")
        print("\n")
        userLetter = userGuessLetter()
        #check if letter is already guessed
        if userLetter not in lettersUsed:
            lettersUsed.append(userLetter)

            #if player guessed a letter correctly
            if (userLetter in wordList):
                print("You guessed it!")
                occurances = [index for index, element in enumerate(word) if element == userLetter]
                for index in occurances:
                    board[index] = userLetter
            
                

            else:
                print("You guessed wrong")
                for stage in stages[0:wrongGuesses + 1]:
                    print(stage)
                wrongGuesses += 1
        
        #if user already guessed the same letter
        else:
            print("You already guessed that letter")
            print("Letters already guessed: ", lettersUsed)
        
    
    #logic if game lost
    gameOver(word)

    

if __name__ == "__main__":
    main()
