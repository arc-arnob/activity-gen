import numpy as np
import pygame
from snake_game.snake import Cube, Snake, draw_grid, run, redraw_window, random_snack
from snake_game.snake import Cube, Snake, draw_grid, run, redraw_window, random_snack, message_box
from sudoku_game.coverpage import view_coverpage, view_main_coverpage
from sudoku_game.boards import board_easy, board_hard, board_mid, board_very_hard, board_notnull, board_all_null
from sudoku_game.sudoku import print_board, solver, find_empty
from sudoku_game.sudoku import view_options, tasks, default
from sudoku_game.sudoku import solve_easy, solve_hard, solve_mid, solve_user_board, solve_very_hard
from tictactoe_game.tictactoe import check_xy, check_for_win, block_empty, set_block

from tictactoe_game.tictactoe import check_xy, check_for_win, block_empty, set_block
from connect_four_game.c4 import is_valid_location, winning_move, get_next_open_row, draw_board, drop_piece
import main


# ===========================Test Cases for Snake Game=====================


def test_reset():
    snake = Snake((121, 121, 121), (10, 10))
    assert snake.reset((10, 10)) == 0


def test_move_left():
    cube = Cube((20, 20), color=(213, 234, 123))

    assert cube.move(-1, 0) == 19
    assert cube.pos[1] == 20


def test_move_right():
    cube = Cube((20, 20), color=(213, 234, 123))
    assert cube.move(1, 0) == 21


def test_move_up():
    cube = Cube((20, 20), color=(213, 234, 123))
    assert cube.move(0, -1) == 20
    assert cube.pos[1] == 19


def test_move_down():
    cube = Cube((20, 20), color=(213, 234, 123))
    assert cube.move(0, 1) == 20
    assert cube.pos[1] == 21


def test_draw_grid():
    width = 500
    height = 500
    windows = pygame.display.set_mode((width, height))
    assert draw_grid(500, 20, windows) == 0


def test_cube_draw():
    width = 500
    height = 500
    cube = Cube((20, 20), color=(213, 234, 123))
    cube.rows = 20
    cube.w = 500
    windows = pygame.display.set_mode((width, height))
    assert cube.draw(windows, eyes=False) == 0


def test_add_cube():
    snake = Snake((255, 0, 0), (10, 10))
    assert snake.add_cube() == 0
    assert len(snake.body) == 3


def test_win():  # Boundary based test
    assert run(1) == 0


def test_message_box():
    assert message_box("Test", "test", 1) == 0


def test_loss():
    snake = Snake((255, 0, 0), (10, 10))
    snake.body.append(Cube((20, 20)))
    snake.body[0].pos = (20, 20)
    assert run(1) == 0


def test_snake_draw():
    snake = Snake((255, 0, 0), (10, 10))
    width = 500
    height = 500
    windows = pygame.display.set_mode((width, height))
    assert snake.draw(windows) == 0


def test_reset_window():
    width = 500
    windows = pygame.display.set_mode((width, width))
    assert redraw_window(windows) == 0


def test_random_snack():
    snake = Snake((255, 0, 0), (10, 10))
    r = 20
    assert random_snack(r, snake, 1) == 0


# ===========================Test Cases for Tic Tac Toe Game=====================


def test_block_empty():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    for x in range(3):
        for y in range(3):
            if board[x][y] == '':
                assert block_empty(board) is True
            elif board[x][y] != '':
                assert block_empty(board) is False


def test_check_xy():
    assert check_xy(12) is True
    assert check_xy(-11) is False
    assert check_xy(50) is False
    assert check_xy(501) is False
    assert check_xy('abc') is False


def test_set_block():
    board = [['x', 'x', 'x'], ['', '', ''], ['', '', '']]
    assert set_block(board, '11', 'x') is False
    assert set_block(board, '12', 'o') is False
    assert set_block(board, '11', 'o') is False
    assert set_block(board, '22', 'x') is True


def test_check_for_win_horizontal_1():
    board = [['x', 'x', 'x'], ['', '', ''], ['', '', '']]
    assert check_for_win(board) is True


def test_check_for_win_horizontal_2():
    board = [['', '', ''], ['x', 'x', 'x'], ['', '', '']]
    assert check_for_win(board) is True


def test_check_for_win_horizontal_3():
    board = [['', '', ''], ['', '', ''], ['x', 'x', 'x']]
    assert check_for_win(board) is True


def test_check_for_win_vertical_1():
    board = [['o', '', ''], ['o', '', ''], ['o', '', '']]
    assert check_for_win(board) is True


def test_check_for_win_vertical_2():
    board = [['', 'o', ''], ['', 'o', ''], ['', 'o', '']]
    assert check_for_win(board) is True


def test_check_for_win_vertical_3():
    board = [['', '', 'o'], ['', '', 'o'], ['', '', 'o']]
    assert check_for_win(board) is True


def test_check_for_win_diagonal_1():
    board = [['o', '', ''], ['', 'o', ''], ['', '', 'o']]
    assert check_for_win(board) is True


def test_check_for_win_diagonal_2():
    board = [['', '', 'x'], ['', 'x', ''], ['x', '', '']]
    assert check_for_win(board) is True


def test_check_for_win():
    board = [['x', 'o', 'x'], ['', '', ''], ['', '', '']]
    assert check_for_win(board) is False


# ===========================Test Cases for Sudoku Game=====================


def test_find_empty():  # Requirement based
    assert find_empty(board_notnull) is None  # test case 1
    assert find_empty(board_easy) is not None  # test case 2
    assert find_empty(board_mid) is not None  # test case 3
    assert find_empty(board_hard) is not None  # test case 4
    assert find_empty(board_very_hard) is not None  # test case 5
    assert find_empty(board_all_null) is not None  # test case 6
    print("\n\n")


def test_solver():  # boundary based test cases,
    #   is testing the solver function which solves the Sudoku with different type of inputs
    assert solver(board_notnull) is True  # test case 1
    assert solver(board_easy) is True  # test case 2
    assert solver(board_mid) is True  # test case 3
    assert solver(board_hard) is True  # test case 4
    assert solver(board_very_hard) is True  # test case 5


def test_solver_scenario():  # scenario based
    # It is testing the solver function whether it is able to solve a sudoku if all the inputs are 0
    assert solver(board_all_null) is True  # test case 1


def test_view_cover_page():  # Requirement based
    # It is testing the opening of the cover page    rus using: pytest -s -v test.py
    assert view_coverpage() is None


def test_view_main_cover_page():  # Requirement based
    assert view_main_coverpage() is None


def test_print_board_sudoku_solver():  # Requirement based
    # It is testing if the sudoku board is being printed or not

    assert print_board(board_easy) is None  # test case 1
    print("\n")
    assert print_board(board_all_null) is None  # test case 2
    print("\n")
    assert print_board(board_hard) is None  # test case 3
    print("\n")
    assert print_board(board_mid) is None  # test case 4
    print("\n")
    assert print_board(board_very_hard) is None  # test case 2
    print("\n")


def test_view_options():  # Requirement
    # It is testing if the function is viewing options or not
    assert view_options() is None


# ==========================================End of sudoku test=================================


# Connect 4 Test cases
def test_is_valid_location():
    assert is_valid_location(np.zeros((6, 7)), 0) == True
    assert is_valid_location(np.zeros((6, 7)), 1) == True
    assert is_valid_location(np.zeros((6, 7)), 2) == True
    assert is_valid_location(np.zeros((6, 7)), 3) == True
    assert is_valid_location(np.zeros((6, 7)), 4) == True
    assert is_valid_location(np.zeros((6, 7)), 5) == True
    assert is_valid_location(np.zeros((6, 7)), 6) == True


def test_print_board():
    assert print_board(np.zeros((6, 7))) is None


def test_winning_move():
    assert winning_move(np.zeros((6, 7)), np.zeros((6, 7))[2][3]) == True
    assert winning_move(np.zeros((6, 7)), np.zeros((6, 7))[4][6]) == True
    assert winning_move(np.zeros((6, 7)), np.zeros((6, 7))[5][2]) == True


def test_get_next_open_row():
    assert get_next_open_row(np.zeros((6, 7)), 1) == 0 or 1 or 2 or 3 or 4 or 5 or 6
    assert get_next_open_row(np.zeros((6, 7)), 2) == 0 or 1 or 2 or 3 or 4 or 5 or 6
    assert get_next_open_row(np.zeros((6, 7)), 3) == 0 or 1 or 2 or 3 or 4 or 5 or 6
    assert get_next_open_row(np.zeros((6, 7)), 4) == 0 or 1 or 2 or 3 or 4 or 5 or 6
    assert get_next_open_row(np.zeros((6, 7)), 5) == 0 or 1 or 2 or 3 or 4 or 5 or 6
    assert get_next_open_row(np.zeros((6, 7)), 6) == 0 or 1 or 2 or 3 or 4 or 5 or 6


def test_drop_piece():
    assert drop_piece(np.zeros((6, 7)), 2, 3, np.zeros((6, 7))[4][5]) is None
    assert drop_piece(np.zeros((6, 7)), 2, 3, np.zeros((6, 7))[1][4]) is None
    assert drop_piece(np.zeros((6, 7)), 2, 3, np.zeros((6, 7))[2][6]) is None
    assert drop_piece(np.zeros((6, 7)), 2, 3, np.zeros((6, 7))[3][2]) is None


def test_draw_board():
    width = 7 * 100
    height = (6 + 1) * 100
    size = (width, height)
    screen = pygame.display.set_mode(size)
    assert draw_board(np.zeros((6, 7)), width, height, size, screen) is None

# ==========================================Testing Main Function=================================


def test_first_input():

    assert main.validate_input_first("121343") == False
    assert main.validate_input_first("$%$#$%$") == False
    assert main.validate_input_first("1") == True
    assert main.validate_input_first("0") == True
    assert main.validate_input_first("2") == True


def test_cli_input():
    assert main.validate_input_cli("121343") == False
    assert main.validate_input_cli("$%$#$%$") == False
    assert main.validate_input_cli("1") == True
    assert main.validate_input_cli("0") == True
    assert main.validate_input_cli("2") == True
    assert main.validate_input_cli("3") == True


def test_gui_input():
    assert main.validate_input_gui("121343") == False
    assert main.validate_input_gui("$%$#$%$") == False
    assert main.validate_input_gui("1") == True
    assert main.validate_input_gui("0") == True
    assert main.validate_input_gui("2") == True
    assert main.validate_input_gui("3") == True
    assert main.validate_input_gui("4") == True