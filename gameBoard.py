# David Liddle  11-23-22
# Assignment 6 

# gameBoard module defines the game boards for either the player of computer and returns list of lists of each

import random

# board constants
GAME_BOARD_WIDTH = 10
GAME_BOARD_HEIGHT = 10

BOARD_SELECTION_LOW = 1
BOARD_SELECTION_HIGH = 2

# function that takes user input and returns an integer to select a game board
def chooseHumanGameBoard(): 
    while True:
        try:
            gameboardChoice = int(input("Which gameboard to use for the player (" + str(BOARD_SELECTION_LOW) + " - " + str(BOARD_SELECTION_HIGH) + ")?: "))
            while gameboardChoice < BOARD_SELECTION_LOW or gameboardChoice > BOARD_SELECTION_HIGH:
                print("Invalid input...")
                gameboardChoice = int(input("Which gameboard to use for the player (" + str(BOARD_SELECTION_LOW) + " - " + str(BOARD_SELECTION_HIGH) + ")?: "))
            break
        except Exception as e:
            print("ERROR: chooseGameBoard - please enter an integer:", e)
            continue

    return gameboardChoice

# function that determines the computers game board with randomization 
def chooseComputerGameBoard(playerChoice):
    if (playerChoice == 1): 
       computerChoice  = 2
    else:
        computerChoice = 1
    return computerChoice

# function that iterates through the lines of a text file and returns a list of lists data structure making it a mutable game board
def loadGameBoard(gameboardChoice):

    # load gameboard from file
    with open("board" + str(gameboardChoice) + ".txt", "r") as f:
        contents = f.readlines()
    
    # set up gameboard into a list of lists of characters (except the final \n character)
    gameBoard = []
    for line in contents:
        line = list(line)
        gameBoard.append(line[:len(line)-1])
    
    numTargets = 0
    for row in gameBoard:
        for character in row:
            if character == "@":
                numTargets += 1
    
    return gameBoard, numTargets

# same as the loadGameBoard but written for the specific targetBoard file
def loadTargetBoard():
    
    # load targetboard from file
    with open("targetBoard.txt", "r") as f:
        contents = f.readlines()
    
    targetBoard = []
    for line in contents:
        line = list(line)
        targetBoard.append(line[:len(line)-1])
    
    return targetBoard

# function that iterates through a specified game board and returns an ordered matrix/game board
def printBoard(board, boardWidth, boardHeight):

    colCoordinates = " "

    for i in range(0, boardWidth):
        colCoordinates += str(i)
    print('\n')
    print('  ' + colCoordinates + '\n')
    for i in range(0, boardHeight):
        row = str(i) + '  '
        for j in range(0, boardWidth):
            row += board[i][j]
        print(row)
    print('\n')

    return