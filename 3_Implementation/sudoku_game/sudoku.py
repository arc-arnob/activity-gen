# importing the dependencies
import os
import sys
from time import sleep
from termcolor import colored



# The screen clear function
def screen_clear():
    """
    clears the screen, worrks in both the os
    """
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
"""
board1 board2 board3  are 3 different types of 
lists that contains lists of the numbers in sudoku....
"""
user_board=[]

def user_input_board():
    """
    [Takes input from the user]
    """
    for i in range(0,9):
        user_board.append([])
    for i in range(0,9):
        for j in range(0,9):
            user_board[i].append(j)
            user_board[i][j]=0
    for i in range(0,9):
        for j in range(0,9):
            print("Entery in row: ",i+1,"Column: ",j+1)
            user_board[i][j]=int(input())
    screen_clear()
    print(colored("Your entered board is: \n\n",'yellow', attrs=['bold']))
    print_board(user_board)

    solve_user_board()
# End Of Function

def view_options():
    """
    [prints the difficulty level for the user]
    """
    options= """
    



                                                            press 1 to solve the easy difficulty level question.

                                                            press 2 to solve the medium difficulty level question.

                                                            press 3 to solve the hard difficulty level question.

                                                            press 4 to solve the very hard difficulty level question.

                                                            press 5 to go to sudoku options.

                                                            press Any key to go to main menu.
    """
    print(colored(options, 'cyan'))
    # end of function




board_easy = [  # easy level sudoku
    [0, 2, 0, 1, 5, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 7, 0],
    [9, 8, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 3, 0, 4, 8, 0, 0],
    [8, 3, 6, 9, 2, 0, 7, 4, 1],
    [0, 4, 0, 0, 0, 7, 3, 6, 9],
    [0, 0, 0, 0, 0, 0, 2, 0, 6],
    [0, 0, 0, 4, 9, 8, 0, 0, 0],
    [5, 0, 1, 0, 0, 0, 0, 0, 4]
]

board_mid = [  # mid level sudoku
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

board_hard = [  # Hard level sudoku
    [0, 0, 0, 8, 0, 0, 6, 9, 3],
    [0, 8, 1, 3, 0, 0, 0, 0, 5],
    [0, 0, 0, 6, 0, 5, 4, 0, 0],
    [9, 0, 0, 0, 0, 0, 8, 5, 6],
    [8, 0, 0, 1, 0, 0, 0, 4, 0],
    [4, 0, 0, 5, 9, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 8, 0],
    [0, 5, 0, 0, 0, 0, 3, 6, 9],
    [0, 0, 0, 9, 2, 0, 0, 7, 0]
]

board_very_hard = [  # very hard level sudoku
    [0, 0, 7, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 1, 0, 4, 7, 2],
    [0, 0, 4, 0, 8, 0, 0, 0, 0],
    [0, 6, 0, 9, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 9, 0, 6, 0, 3, 0, 0, 0],
    [1, 0, 0, 7, 0, 8, 0, 0, 0],
    [7, 0, 0, 0, 0, 6, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 8, 5]
]
"""
board not null doesnot contains 0
"""
board_notnull = [  
    [3, 2, 4, 1, 5, 7, 6, 8, 9],
    [1, 5, 6, 2, 8, 9, 4, 7, 3],
    [9, 8, 7, 3, 4, 6, 1, 5, 2],
    [1, 7, 9, 3, 6, 4, 8, 2, 5],
    [8, 3, 6, 9, 2, 5, 7, 4, 1],
    [2, 4, 5, 1, 8, 7, 3, 6, 9],
    [3, 4, 8, 1, 5, 7, 2, 9, 6],
    [2, 6, 7, 4, 9, 8, 1, 3, 5],
    [5, 9, 1, 2, 3, 6, 7, 8, 4]
]


# print board function will print the board
def print_board(input_board):
    """[Prints the board]

    Args:
        input_board ([type: list]): [enter a 9 by 9 2-D list]
    """
    for i in range(len(input_board)):
        if i % 3 == 0 and i != 0:
            print(colored("-----------------------", 'red'))
        for j in range(len(input_board[0])):
            if j % 3 == 0 and j != 0:
                print(colored(" | ", 'red'), end="")
            if j == 8:
                print(colored(input_board[i][j], 'blue'))
            else:
                print(colored(str(input_board[i][j]), 'blue') + " ", end="")
                # End of print_board function



# find_empty function will find the empty place(s)
def find_empty(input_board):
    """[Finds the 0 values present in the input list]

    Args:
        input_board ([type: List]): [9 by 9 2D list]

    Returns:
        [type: None]: [returns the co ordinate if 0 present else retunrs Nonr]
    """
    for i in range(len(input_board)):
        for j in range(len(input_board[0])):
            if input_board[i][j] == 0:
                return (i, j)
    return None
    # End of find_empty function


# this function checks the validity
def is_valid(input_board, num, pos):
    """[checks if the sudoku board is valid]

    Args:
        input_board ([type: List]): [9 by 9 2-D board]
        num ([type: int]): [number]
        pos ([type: int]): [Position]

    Returns:
        [type]: [description]
    """
    for i in range(len(input_board[0])):  # checking row
        if input_board[pos[0]][i] == num and pos[1] != i:
            return False
    for j in range(len(input_board)):  # checking column
        if input_board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if input_board[i][j] == num and (i, j) != pos:
                return False
    return True
    # End of valid funtion


# this is the function which solves the sudoku puzzle
def solver(input_board):
    """[solves the sudoku]

    Args:
        input_board ([type: List]): [9 by 9 matrix]

    Returns:
        [type: boolean]: [True if doesnt find empty or 0 values in the sudoku board else returns false]
    """
    find = find_empty(input_board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if is_valid(input_board, i, (row, col)):
            input_board[row][col] = i
            if solver(input_board):  # using recursion
                return True
            input_board[row][col] = 0
    return False
    # end of solver function




# this function solves the easy board
def solve_easy():
    """[solves the easy board]
    """
    print_board(board_easy)
    solver(board_easy)
    print("\n\n\n")
    print(colored("=============================" + "Solving" + "=============================", 'yellow'))
    print("\n\n")
    print_board(board_easy)
    print("\n")
    print(colored("=============================" + "Solved" + "===============================", 'blue'))
    print("\n\n")
    print(colored("Enter 1 to get back to sudoku ptions: ", 'yellow'))
    print(colored("Enter 2 to get back to difficulty options", 'yellow'))
    print(colored("Enter 0 to exit: \nEnter any key to go back to main menu..."))
    choice = input()
    sleep(1)
    screen_clear()
    if choice == '1':
        user_choice()
    elif choice == '2':
        tasks()
    elif choice == '0':
        sys.exit(colored("\n\nThank You for visiting us...\nRegards Team 31 \n", 'yellow', attrs=['bold']))
    else:
        return
    # end of function


# this function solves the medium board
def solve_mid():
    """
    Solves midium level board
    """
    print_board(board_mid)
    solver(board_mid)
    print("\n")
    print(colored("=============================" + "Solving" + "=============================", 'yellow'))
    print("\n\n")
    print_board(board_mid)
    print("\n")
    print(colored("=============================" + "Solved" + "===============================", 'blue'))
    print("\n\n")
    print(colored("Enter 1 to get back to sudoku ptions: ", 'yellow'))
    print(colored("Enter 2 to get back to difficulty options", 'yellow'))
    print(colored("Enter 0 to exit: \nEnter any key to go back to main menu..."))
    choice = input()
    sleep(1)
    screen_clear()
    if choice == '1':
        user_choice()
    elif choice == '2':
        tasks()
    elif choice == '0':
        sys.exit(colored("\n\nThank You for visiting us...\nRegards Team 31 \n", 'yellow', attrs=['bold']))
    else:
        return
    # end of function


# this function solves the hard board
def solve_hard():
    """
    solves hard level board
    """
    print_board(board_hard)
    solver(board_hard)
    print("\n")
    print(colored("=============================" + "Solving" + "=============================", 'yellow'))
    print("\n\n")
    print_board(board_hard)
    print("\n")
    print(colored("=============================" + "Solved" + "===============================", 'blue'))
    print("\n\n")
    print(colored("Enter 1 to get back to sudoku ptions: ", 'yellow'))
    print(colored("Enter 2 to get back to difficulty options", 'yellow'))
    print(colored("Enter 0 to exit: \nEnter any key to go back to main menu..."))
    choice = input()
    sleep(1)
    screen_clear()
    if choice == '1':
        user_choice()
    elif choice == '2':
        tasks()
    elif choice == '0':
        sys.exit(colored("\n\nThank You for visiting us...\nRegards Team 31 \n", 'yellow', attrs=['bold']))
    else:
        return
    # end of function


# this function solves the very hard board
def solve_very_hard():
    """
    solves very hard level code
    """
    print_board(board_very_hard)
    solver(board_very_hard)
    print("\n")
    print(colored("=============================" + "Solving" + "=============================", 'yellow'))
    print("\n\n")
    print_board(board_very_hard)
    print("\n")
    print(colored("=============================" + "Solved" + "===============================", 'blue'))
    print("\n\n")
    print(colored("Enter 1 to get back to sudoku ptions: ", 'yellow'))
    print(colored("Enter 2 to get back to difficulty options", 'yellow'))
    print(colored("Enter 0 to exit: \nEnter any key to go back to main menu..."))
    choice = input()
    sleep(1)
    screen_clear()
    if choice == '1':
        user_choice()
    elif choice == '2':
        tasks()
    elif choice == '0':
        sys.exit(colored("\n\nThank You for visiting us...\nRegards Team 31 \n", 'yellow', attrs=['bold']))
    else:
        return
    # end of function


def solve_user_board():
    """[solves the sudoku board entered by user]

    Returns:
        [type: None]: [returns to the loop if user inputsany invalid input.]
    """
    i_p=input(colored("\n\nPress 1 to get the solution of this problem...\n\nPress 2 to get back to the options...\n\nPress 0 to exit...\n\n Or press any key to return main menu", 'yellow', attrs=['bold']))
    if i_p == '1':
        solver(user_board)
        print("\n")
        print(colored("=============================" + "Solving" + "=============================", 'yellow'))
        print("\n\n")
        print_board(user_board)
        print("\n")
        print(colored("=============================" + "Solved" + "===============================", 'blue'))
        print("\n\n")
    elif i_p == '2':
        user_choice()
    elif i_p == 0:
        sys.exit(colored("\n\nThank You for visiting us..\nRegards Team 31 \n", 'yellow', attrs=['bold']))
    else:
        return


def tasks():
    screen_clear()   #clears the screen
    view_options()   #displays the options
    choice = input(colored("Enter The Difficulty Level: ", 'yellow', attrs=['bold']))
    sleep(1)
    screen_clear()
    print("\n\n")

    # using switcher to mimic the switch cse statement
    switcher = {
        '1': solve_easy,
        '2': solve_mid,
        '3': solve_hard,
        '4': solve_very_hard,
        '5': user_choice
    }
    switcher.get(choice, default)()  # calling the function acc to ip given by the user



def default():
    return colored("Please enter a valid Difficulty level... :(", 'red', attrs=['bold'])
    #tasks()



def user_choice():
    """
    takes input from the user and performs the tasks accordingly
    """

    userchoice = """
                                        
                                    Enter 1 for solving available problems.

                                    Enter 2 for giving your own sudoku problem.

                                    Enter any key to go back to main menue.
    """
    print(userchoice)
    i_p = input(colored("\nEnter ur choice 1 or 2: ", 'yellow', attrs=['bold']))
    if i_p == '1':
        tasks()
    elif i_p == '2':
        user_input_board()
    else:
        return
        #End of Funtion




# # this function prints the options which are written in the difficulty_level_choice.txt file inside src folder
# def view_options():
#     with open('src/difficulty_level_choice.txt') as f:
#         options = f.read()
#     print(colored(options, 'cyan'))
#     # end of function



def run_sudoku():

    print(colored("""
    Enter 1 to Continue...
    Enter 0 to exit...
    Enter Any key to go to main menue...
    """, 'yellow', attrs=['bold']))

    i_p = input(colored("enter ur choice: ", 'yellow', attrs=['bold']))
    sleep(1)
    screen_clear()

    if i_p == '1':
        user_choice()
    elif i_p == '0':
        sys.exit(colored("\n\nThank You for visiting us... \nRegards Team-31", 'yellow', attrs=['bold']))
    else:
        return

if __name__ =="__main__":
    run_sudoku()