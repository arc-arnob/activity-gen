import sys
from termcolor import colored
from snake_game.snake import run
from sudoku_game.sudoku import run_sudoku, screen_clear
from sudoku_game.coverpage import view_coverpage, view_main_coverpage
from tictactoe_game.tictactoe import run_tic_tac_toe
from tetris_game.tertis import run_tetris
from connect_four_game.c4 import run_connect


def validate_input_first(user_input):

    """
    This Function validates input for very first menu
    :param user_input: User input
    :return: Bool
    """

    if user_input in ('0', '1', '2'):
        return True

    return False


def validate_input_cli(user_input):

    """
    This function validates the input of the user during 2nd menu
    :param user_input:
    :return: bool
    """

    if user_input in ('0', '1', '2', '3'):
        return True

    return False


def validate_input_gui(user_input):

    """
    This function validates the input of the user during 2nd menu
    :param user_input:
    :return: bool

    """

    if user_input in ('0', '1', '2', '3', '4'):
        return True

    return False


def main_menu():
    """
    This function is used to execute the program
    :param : None
    :return: None
    """
    while True:
        view_main_coverpage()
        print("Press 1 to play CLI games\n")
        print("Press 2 to play GUI games\n")
        print("Press 0 to to exit\n")
        graphic_choice = input()
        if not validate_input_first(graphic_choice):
            print("Invalid Choice, enter again")
            continue
        screen_clear()
        if graphic_choice == '0':
            sys.exit(colored("\n\nThank You for visiting us... \nRegards Team-31",
                             'yellow', attrs=['bold']))
        choice = ''
        while choice != '0':
            if graphic_choice == '1':
                print("Press 1 to play tic tac toe")
                print("Press 2 to Solve a sudoku problem")
                print("Press 3 to go to previous menu")
                print("Enter 0 if you want to exit")
                choice = input()
                if not validate_input_cli(choice):
                    print("Invalid input, try again")
                    continue
                screen_clear()
                if choice == '1':
                    print("   Welcome to tic tic tac toe")
                    run_tic_tac_toe()
                elif choice == '2':
                    view_coverpage()
                    run_sudoku()
                elif choice == '3':
                    break
                elif choice == '0':
                    sys.exit(colored("\n\nThank You for visiting us... \nRegards Team-31",
                                     'yellow', attrs=['bold']))
                else:
                    print(colored("OOPs YOU have Entered a Wrong Option.."
                                  "\nPlease enter a valid option",
                                  'red', attrs=['bold']))
            elif graphic_choice == '2':
                screen_clear()
                print("Press 1 to play Snake game")
                print("Press 2 to play Tetris")
                print("Press 3 to play connect four")
                print("Press 4 to go to previous menu")
                print("Enter 0 if you want to exit")
                choice = input()
                if not validate_input_gui(choice):
                    print("Invalid input, try again")
                    continue
                if choice == '1':
                    run(0)

                elif choice == '2':
                    run_tetris()
                elif choice == '3':
                    run_connect()
                elif choice == '0':
                    sys.exit(colored("\n\nThank You for visiting us... "
                                     "\nRegards Team-31",
                                     'yellow', attrs=['bold']))
                elif choice == '4':
                    break
                else:
                    print(colored("OOPs YOU have Entered a Wrong Option.."
                                  "\nPlease enter a valid option",
                                  'red', attrs=['bold']))
            else:
                print(colored("OOPs YOU have Entered a Wrong Option.."
                              "\nPlease enter a valid option",
                              'red', attrs=['bold']))


if __name__ == '__main__':
    main_menu()
