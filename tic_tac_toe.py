# Author: Jonathan Woster CSE210
# Week 2, Tic Tac Toe

# Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal 
# with either three x's or three o's drawn in the spaces of a grid of nine squares.
# Tic-Tac-Toe is played according to the following rules.
# The game is played on a grid that is three squares by three squares.
# Player one uses x's. Player two uses o's.
# Players take turns putting their marks in empty squares.
# The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
# If all nine squares are full and neither player has three in a row, the game ends in a draw.

# import modules needed for the program
import os

# Set up list with values of the squares
square_values = [0,1,2,3,4,5,6,7,8,9]


def main():
    # clear the terminal for the user
    clear_terminal()

    # Player x starts the game
    player = "x"
    # Initialize the game status
    game_status = "active"
    # intialize the number of moves that have ocurred
    move_count = 0

    # Welcome the user and print out the board
    print("Welcome to Tic-Tac-Toe!\n")
    print_board(square_values)

    # As long as the game isn't done, keep going
    while game_status == "active":
        # print(f"Main game status top of function is {game_status}")
        # Find out what moves the player wants and update the values of the squares
        get_user_choice(player, square_values)
        # Print out the board
        print_board(square_values)
        # increment move_count to reflect how many moves or turns have ocurred
        move_count += 1
        # Switch back and forth between x and o turns
        if player == "x":
            player = "o"
        else:  # must be an o therefore make it an x
            player = "x"
        # check game status to see if the game is done
        game_status = check_game_status(move_count)
        # print(f"Main game status bottom of function is {game_status}")


def clear_terminal():
    # This just clears the terminal window
    # no parameters should be passed into this function
    # Returns nothing
    # Uses os module
    command = 'clear' # default command that works for Linux, Apple
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command) # execute it to clear the terminal window
    return

def print_board(square_values):
    # This prints the game board using values passed into this function on the square_values list
    # Returns nothing
    print(f"{square_values[1]}|{square_values[2]}|{square_values[3]}")
    print("-+-+-")
    print(f"{square_values[4]}|{square_values[5]}|{square_values[6]}")
    print("-+-+-")
    print(f"{square_values[7]}|{square_values[8]}|{square_values[9]}")
    return

def check_game_status(move_count):
    # This function checks for winning conditions and end of game (max number of moves)
    # If someone won or we have done 9 turns, it declares the game done
    # It gets move_count passed in from the calling function
    # It returns the game_status to the calling function

    # If they got either of the diagonals, declare winner and be done
    if square_values[1] == "x" and square_values[5] == "x" and square_values[9] == "x":
        print("\nPlayer x won!\n")
        game_status = "done"
    elif square_values[1] =="o" and square_values[5] == "o" and square_values[9] == "o":
        print("\nPlayer o won!\n")
        game_status = "done"
    elif square_values[3] =="x" and square_values[5] == "x" and square_values[7] == "x":
        print("\nPlayer x won!\n")
        game_status = "done" 
    elif square_values[3] =="o" and square_values[5] == "o" and square_values[7] == "o":
        print("\nPlayer o won!\n")
        game_status = "done"
    
    # if they got any of the horizontal rows, declare a winner and end game
    elif square_values[1] =="x" and square_values[2] == "x" and square_values[3] == "x":
        print("\nPlayer x won!\n")
        game_status = "done" 
    elif square_values[1] =="o" and square_values[2] == "o" and square_values[3] == "o":
        print("\nPlayer o won!\n")
        game_status = "done"
    elif square_values[4] =="x" and square_values[5] == "x" and square_values[6] == "x":
        print("\nPlayer x won!\n")
        game_status = "done" 
    elif square_values[4] =="o" and square_values[5] == "o" and square_values[6] == "o":
        print("\nPlayer o won!\n")
        game_status = "done"
    elif square_values[7] =="x" and square_values[8] == "x" and square_values[9] == "x":
        print("\nPlayer x won!\n")
        game_status = "done" 
    elif square_values[7] =="o" and square_values[8] == "o" and square_values[9] == "o":
        print("\nPlayer o won!\n")
        game_status = "done"

    # if they got any of the vertical rows, declare winner and end game
    elif square_values[1] =="x" and square_values[4] == "x" and square_values[7] == "x":
        print("\nPlayer x won!\n")
        game_status = "done" 
    elif square_values[1] =="o" and square_values[4] == "o" and square_values[7] == "o":
        print("\nPlayer o won!\n")
        game_status = "done"
    elif square_values[2] =="x" and square_values[5] == "x" and square_values[8] == "x":
        print("\nPlayer x won!\n")
        game_status = "done" 
    elif square_values[2] =="o" and square_values[5] == "o" and square_values[8] == "o":
        print("\nPlayer o won!\n")
        game_status = "done"
    elif square_values[3] =="x" and square_values[6] == "x" and square_values[9] == "x":
        print("\nPlayer x won!\n")
        game_status = "done" 
    elif square_values[3] =="o" and square_values[6] == "o" and square_values[9] == "o":
        print("\nPlayer o won!\n")
        game_status = "done"
    
    # if we hit 9 moves, be done
    elif move_count == 9:
        print("\nIt's a draw! Good game. Thanks for playing.\n")
        game_status = "done"
    # if nobody has won and we haven't hit 9 moves yet, keep going
    else:
        game_status = "active"

    return game_status

def get_user_choice(player, square_values):
    # This gets the choice of squares from the user
    # In other words, which square do we want to put the 
    # X or O into?
    # It receives the player whose turn it is as a parameter
    # Returns the updated list of square values
    print()
    user_choice = int(input(f"It is {player}'s turn to choose a square (1-9): "))
    print()
    square_values[user_choice] = player
    return square_values

# If this file is executed like this:
# > python tic_tac_toe.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
