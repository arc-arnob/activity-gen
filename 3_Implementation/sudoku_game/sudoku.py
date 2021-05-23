# importing the dependencies
import os
import sys
from time import sleep
from termcolor import colored
import algorithm as al
import boards as bd

# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


# this function will print the cover page.... which is saved in the form of a text file
def view_coverpage():
    with open('src/cover_page.txt') as f:
        coverpage = f.read()
    print(coverpage)


# board1 board2 board3  are 3 different types of lists that contains lists of the numbers in sudoku....

user_board=[]

def user_input_board():
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


# print board function will print the board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print(colored("-----------------------", 'red'))
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(colored(" | ", 'red'), end="")
            if j == 8:
                print(colored(bo[i][j], 'blue'))
            else:
                print(colored(str(bo[i][j]), 'blue') + " ", end="")
                # End of print_board function


# this function solves the easy board
def solve_easy():
    print_board(bd.board_easy)
    al.solver(bd.board_easy)
    print("\n\n\n")
    print(colored("=============================" + "Solving" + "=============================", 'yellow'))
    print("\n\n")
    print_board(bd.board_easy)
    print("\n")
    print(colored("=============================" + "Solved" + "===============================", 'blue'))
    print("\n\n")
    choice = int(input(colored("Enter 1 to get back to the option: \nEnter 0 to exit: ", 'yellow')))
    sleep(1)
    screen_clear()
    if choice == 1:
        tasks()
    elif choice == 0:
        sys.exit(colored("\n\nThank You for visiting us...\nRegards Debashish Dash (265057) \n", 'yellow', attrs=['bold']))
    else:
        print(colored("Entered choice is invalid...\n\n", 'red'))
    # end of function


# this function solves the medium board
def solve_mid():
    print_board(bd.board_mid)
    al.solver(bd.board_mid)
    print("\n")
    print(colored("=============================" + "Solving" + "=============================", 'yellow'))
    print("\n\n")
    print_board(bd.board_mid)
    print("\n")
    print(colored("=============================" + "Solved" + "===============================", 'blue'))
    print("\n\n")
    choice = int(input(colored("Enter 1 to get back to the option: \nEnter 0 to exit: ", 'yellow')))
    sleep(1)
    screen_clear()
    if choice == 1:
        tasks()
    elif choice == 0:
        sys.exit(colored("\n\nThank You for visiting us...\nRegards Debashish Dash (265057) \n", 'yellow', attrs=['bold']))
    else:
        print(colored("Entered choice is invalid...\n\n", 'red'))
    # end of function


# this function solves the hard board
def solve_hard():
    print_board(bd.board_hard)
    al.solver(bd.board_hard)
    print("\n")
    print(colored("=============================" + "Solving" + "=============================", 'yellow'))
    print("\n\n")
    print_board(bd.board_hard)
    print("\n")
    print(colored("=============================" + "Solved" + "===============================", 'blue'))
    print("\n\n")
    choice = int(input(colored("Enter 1 to get back to the option: \nEnter 0 to exit: ", 'yellow')))
    sleep(1)
    screen_clear()
    if choice == 1:
        tasks()
    elif choice == 0:
        sys.exit(colored("\n\nThank You for visiting us...\nRegards Debashish Dash (265057) \n", 'yellow', attrs=['bold']))
    else:
        print(colored("Entered choice is invalid...\n\n", 'red'))
    # end of function


# this function solves the very hard board
def solve_very_hard():
    print_board(bd.board_very_hard)
    al.solver(bd.board_very_hard)
    print("\n")
    print(colored("=============================" + "Solving" + "=============================", 'yellow'))
    print("\n\n")
    print_board(bd.board_very_hard)
    print("\n")
    print(colored("=============================" + "Solved" + "===============================", 'blue'))
    print("\n\n")
    choice = int(input(colored("Enter 1 to get back to the option: \nEnter 0 to exit: ", 'yellow')))
    sleep(1)
    screen_clear()
    if choice == 1:
        tasks()
    elif choice == 0:
        sys.exit(colored("\n\nThank You for visiting us..\nRegards Debashish Dash (265057). \n", 'yellow', attrs=['bold']))
    else:
        print(colored("Entered choice is invalid...\n\n", 'red'))
    # end of function


def solve_user_board():
    ip=int(input(colored("\n\nPress 1 to get the solution of this problem...\n\nPress 2 to get back to the options...\n\nOr press any key to exit...", 'yellow', attrs=['bold'])))
    
    if ip == 1:
        al.solver(user_board)
        print("\n")
        print(colored("=============================" + "Solving" + "=============================", 'yellow'))
        print("\n\n")
        print_board(user_board)
        print("\n")
        print(colored("=============================" + "Solved" + "===============================", 'blue'))
        print("\n\n")
    elif ip == 2:
        user_choice()
    else:
        sys.exit(colored("\n\nThank You for visiting us..\nRegards Debashish Dash (265057). \n", 'yellow', attrs=['bold']))



def tasks():
    screen_clear()
    view_options()
    choice = int(input(colored("Enter The Difficulty Level: ", 'yellow', attrs=['bold'])))
    sleep(1)
    screen_clear()
    print("\n\n")

    # using switcher to mimic the switch cse statement
    switcher = {
        1: solve_easy,
        2: solve_mid,
        3: solve_hard,
        4: solve_very_hard
    }
    switcher.get(choice, default)()  # calling the function acc to ip given by the user



def default():
    return "Please enter a valid Difficulty level... :("



def user_choice():
    with open('src/user_choice1.txt') as f:
        userchoice = f.read()
    print(userchoice)
    ip = int(input(colored("\nEnter ur choice 1 or 2: ", 'yellow', attrs=['bold'])))
    if ip == 1:
        tasks()
    elif ip == 2:
        user_input_board()
    else:
        print("You have entered a wrong input...\nPlease Enter either 1 or 2")
    #End of Funtion



# this function prints the options which are written in the difficulty_level_choice.txt file inside src folder
def view_options():
    with open('src/difficulty_level_choice.txt') as f:
        options = f.read()
    print(colored(options, 'cyan'))
    # end of function

def main():
        # taking the difficult level choice from the user
    view_coverpage()
    print(colored("""
    Enter 1 to Continue...
    Enter 0 to exit...
    """, 'yellow', attrs=['bold']))

    ip = int(input(colored("enter ur choice(either 0 or 1): ", 'yellow', attrs=['bold'])))
    sleep(1)
    screen_clear()

    if ip == 1:
        user_choice()
    else:
        sys.exit(colored("\n\nThank You for visiting us... \nRegards Team-31", 'yellow', attrs=['bold']))

main()