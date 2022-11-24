# David Liddle
# Assignment #6 

import gameBoard
import gameInput

# function that defines the players turn
def _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets):

        print("Iti's the human's turn.") # Alert the user of his turn
    gameBoard.printBoard(targetBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT) # print the current game board 
    print() 
    while True: # loop that takes user input and determines a 'HIT' or 'MISS'
        playerTargetRow, playerTargetColumn  = gameInput.getHumanInput()
        print(f"Your target coordinate is ({playerTargetRow},{playerTargetColumn})")
        if targetBoard[playerTargetRow][playerTargetColumn] != "#":
            print("This coordinate has already been fired. Choose a coordinate")
            continue
        else:
            if (computerGameBoard[playerTargetRow][playerTargetColumn] == '.'):
                targetBoard[playerTargetRow][playerTargetColumn] = 'O'
                computerGameBoard[playerTargetRow][playerTargetColumn] = 'O'
                gameBoard.printBoard(targetBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
                print("Your shot was a miss.")
            else:
                targetBoard[playerTargetRow][playerTargetColumn] = 'X'
                computerGameBoard[playerTargetRow][playerTargetColumn] = 'X'
                print("Your shot was a hit.")
                numComputerTargets -= 1
                gameBoard.printBoard(targetBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
            return humanGameBoard, targetBoard, computerGameBoard, numComputerTargets

# function that defines the computer's turn
def _computerTurn(humanGameBoard, numHumanTargets):

    print("It's the computer's turn") # Alert the player whose turn it is
    while True: # loop that determines the computer's shot
        computerTargetRow, computerTargetColumn = gameInput.getComputerInput()
        print(computerTargetRow, computerTargetColumn)
        gameBoard.printBoard(humanGameBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
       # print(humanGameBoard[computerTargetRow][computerTargetColumn])
        if (humanGameBoard[computerTargetRow][computerTargetColumn] == 'O' or humanGameBoard[computerTargetRow][computerTargetColumn] == 'O'):
            print("Run Again")
            continue
        else:
            print(f"The PCs target coordinate is ({computerTargetRow},{computerTargetColumn})")
            if (humanGameBoard[computerTargetRow][computerTargetColumn] == '.'):
                humanGameBoard[computerTargetRow][computerTargetColumn] = 'O'
                gameBoard.printBoard(humanGameBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
                print("The PCs shot was a miss.")
            else:
                humanGameBoard[computerTargetRow][computerTargetColumn] = 'X'
                print("The PCs shot was a hit.")
                numHumanTargets -= 1
                gameBoard.printBoard(humanGameBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
            return humanGameBoard, numHumanTargets

# this function outputs the winner of the battleship game to the terminal
def _printWinner(numComputerTargets, computerGameBoard):
    
    if numComputerTargets == 0:
        print("You are the WINNER!")
        print()
        gameBoard.printBoard(computerGameBoard,gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
    else:
        print("The computer is the WINNER!")
        print()
        gameBoard.printBoard(computerGameBoard,gameBoard.GAME_BOARD_WIDTH,gameBoard.GAME_BOARD_HEIGHT)

    return

# function that takes the other functions outputs as parameters and creates a conditional game loop
def runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets):
    currentTurn = 0 # 0 = human, 1 = computer

    # play the game (HUMAN goes first)
    while numHumanTargets > 0 and numComputerTargets > 0:
        if currentTurn == 0:
            humanGameBoard, targetBoard, computerGameBoard, numComputerTargets = _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets)
        else:
            humanGameBoard, numHumanTargets = _computerTurn(humanGameBoard, numHumanTargets)

        # switch whose turn it is
        currentTurn += 1
        currentTurn %= 2
    
    # print the winner once the game is over
    _printWinner(numComputerTargets, computerGameBoard)

    return

# see if you can incorporate sound and design an acutal sprite sheet
# In terms of this assignment write a module that outputs a random arrangement of ships
#   create a blank game board
#   create several matrices each with a number on the end to be randomly drawn and the merge if there are no conflicts 
# then expand that to choose what type of game board there is


    # Desing a sensor that sends voip or sms when it is opened along with turning on the camera