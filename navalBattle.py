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
            print("1. Enter the letter [p] for 'play'")
            print("2. The computer will prompt you for what board to choose")
            print("3. The target board will print to the screen.")
            print("4. The computer will prompt you to enter a target coordinate for the row you want to attack.")
            print("5. The computer will prompt you to enter a target coordinate for the column you want to attack.")
            print("6. Then the computer will take a turn")
            print("7. You and the computer will take turns until either your or the enemy ships are destroyed")
            print()
        elif choice == "q":
            print("Goodbye")
            gameOver = True
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()