# David Liddle  11-23-22
# Assignment 6 

import random
import gameBoard

def getHumanInput():
    # user input for target coordinate row
    while True:
        try:
            row = int(input("Enter the ROW that you are going to attack: "))
            if 0 > row or row > gameBoard.GAME_BOARD_HEIGHT:
                print(f"ERROR: Invalid Input. Enter a number between 0 - {gameBoard.GAME_BOARD_HEIGHT}")
            else:
                break
        except ValueError:
            print("ERROR: Invalid Input. Please enter an integer!")


    # user input for target coordinate column 
    while True:
        try:
            column = int(input("Enter the COLUMN that you are going to attack: "))
            if 0 > column or column > gameBoard.GAME_BOARD_WIDTH:
                print(f"ERROR: Invalid Input. Enter a number between 0 - {gameBoard.GAME_BOARD_WIDTH}")
            else:
                break
        except ValueError:
            print("ERROR: Invalid Input. Please enter an integer!")

    return row, column

def getComputerInput():
    # randomized computer input for attack coordinates    
    row = random.randint(0,gameBoard.GAME_BOARD_HEIGHT-1)
    column = random.randint(0,gameBoard.GAME_BOARD_WIDTH-1)

    return row, column