# David Liddle  11-23-22
# Assignment #6 

import random

GAME_BOARD_WIDTH = 10
GAME_BOARD_HEIGHT = 10

BOARD_SELECTION_LOW = 1
BOARD_SELECTION_HIGH = 2

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

def chooseComputerGameBoard():
    gameboardChoice = random.randint(BOARD_SELECTION_LOW, BOARD_SELECTION_HIGH)
    
    return gameboardChoice

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

def loadTargetBoard():
    
    # load targetboard from file
    with open("targetBoard.txt", "r") as f:
        contents = f.readlines()
    
    targetBoard = []
    for line in contents:
        line = list(line)
        targetBoard.append(line[:len(line)-1])
    
    return targetBoard

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


targetBoard = loadTargetBoard()
print(targetBoard)
printBoard(targetBoard, 10, 10)