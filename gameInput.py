# Matthew Holman             8-11-2022
# Assignment #6 Naval Battle

import random
import gameBoard

def getHumanInput():
    """This function takes in input from the human for wich row and column they want to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the human to attack.
    """
    # TODO: Complete the logic below so that the human can take input the row and column they want to attack. (1 pt.)

    # Input an integer value for the row to attack and assign it to the variable 'row'. 
    # If the number the user enteres is < 0 or > gameBoard.GAME_BOARD_HEIGHT-1
    # print an 'invalid input' message and have the user enter another number.
    # Apply input validation to ensure that the type the user enters is a valid int, not a string like 'asdf'.
    # If the user enters an invalid (non int) string, print an error message and have the user try again.
    # HINT: One of the slide decks contains code that effectively does this. 
    # HINT: Consider how try/ except statements work.
    # HINT: Consider how while loops work.
    pass
    
    # Input an integer value for the column to attack and assign it to the variable 'col'. 
    # If the number the user enteres is < 0 or > gameBoard.GAME_BOARD_HEIGHT-1
    # print an 'invalid input' message and have the user enter another number.
    # Apply input validation to ensure that the type the user enters is a valid int, not a string like 'asdf'.
    # If the user enters an invalid (non int) string, print an error message and have the user try again.
    # HINT: One of the slide decks contains code that effectively does this. 
    # HINT: Consider how try/ except statements work.
    # HINT: Consider how while loops work.
    pass
    
    return row, col

def getComputerInput():
    """This function randomly generates input from the computer for which row and column it wants to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the computer to attack.
    """
    # TODO: Complete the logic below so that the computer can produce input the row and column they want to attack. (1 pt.)

    # Use the random module to generate a random integer between 0 and gameBoard.GAME_BOARD_WIDTH - 1.
    # Assign this value to the variable 'row'.
    pass

    # Use the random module to generate a random integer between 0 and gameBoard.GAME_BOARD_WIDTH - 1.
    # Assign this value to the variable 'col'.
    pass

    return row, col