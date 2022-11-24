# David Liddle 11-23-22
# Assignment 6 

import gameBoard
import gamePlay

def main():
    gameOver = False

    gameboardChoice = 0
    humanGameBoard = None
    targetBoard = None
    computerGameBoard = None
    
    numHumanTargets = 0
    numComputerTargets = 0
    
    print("Welcome to Naval Battle!")
    print()
    
    print("By: David Liddle")
    print("[COM S 127 B]")
    print()

    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 

            # assigning board game constants
            gameboardChoice = gameBoard.chooseHumanGameBoard()
            humanGameBoard,numHumanTargets = gameBoard.loadGameBoard(gameboardChoice) 
            humanGameBoard,numHumanTargets = gameBoard.loadGameBoard(gameboardChoice) 
            gameboardChoice  = gameBoard.chooseComputerGameBoard(gameboardChoice)
            computerGameBoard, numComputerTargets = gameBoard.loadGameBoard(gameboardChoice)
            targetBoard = gameBoard.loadTargetBoard()

            # Run the game by passing in the relevant data to the runGame method of the gamePlay module.
            gamePlay.runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets)
        elif choice == "i":
            # TODO: Print out the instructions for the game (1 pt.)
            print("These are the instructions")
        elif choice == "q":
            # TODO: set gameOver to be True and print a 'goodbye' message to the player (1 pt.)
            print("Goodbye")
            gameOver = True
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()