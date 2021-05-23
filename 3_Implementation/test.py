from snake_game.snake import *
from sudoku_game.algorithm import *
from sudoku_game.boards import board_easy,board_hard,board_mid,board_very_hard,board_notnull
import pytest


def test_reset():
    cube = Cube(20, 20, color=(213, 234, 123))
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
    r = 20
    width = 500
    height = 500
    windows = pygame.display.set_mode((width, height))
    assert draw_grid(500, 20, windows) == 0


def test_find_empty():
    assert find_empty(board_notnull) is None  # test case 1
    assert find_empty(board_easy) is not None  # test case 2
    assert find_empty(board_mid) is not None  # test case 3
    assert find_empty(board_hard) is not None  # test case 4
    assert find_empty(board_very_hard) is not None  # test case 5

def test_solver():
    assert solver(board_notnull) is True  # test case 1


def test_cube_draw():
    r = 20
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


def test_win():     # Boundary based test
    snake = Snake((255, 0, 0), (10, 10))
    for _ in range(400):
        snake.body.append(Cube((20, 20)))
    assert run(1) == 0


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
    r = 20
    width = 500
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube((20, 20))
    windows = pygame.display.set_mode((width, width))
    assert redraw_window(windows) == 0


def test_random_snack():
    snake = Snake((255, 0, 0), (10, 10))
    r = 20
    assert random_snack(r, snake, 1) == 0
