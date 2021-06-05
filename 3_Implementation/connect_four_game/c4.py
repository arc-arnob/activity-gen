import math
import time
import numpy as np
import pygame


BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():

    """
    Creates a 6 by 7 matrix of zeros
    :return: None
    """

    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):

    """
    This function allows to place a piece on desired block
    :param board: 6x7 matrix
    :param row: int
    :param col: int
    :param piece: GUI element
    :return:  None
    """
    board[row][col] = piece


def is_valid_location(board, col):
    """
    This function checks if the location selected is valid or not
    :param board: 6x7 matrix
    :param col: int
    :return: int

    """
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):      # Tested

    """
    This function returns the next open row in
    which the new gui piece can be places
    :param board: 6x7 matrix
    :param col: int
    :return: int
    """

    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row


def print_board(board):
    """
    This function prints out 6x7 matrix
    :param board: 6x7 matrix
    :return: None
    """
    print(np.flip(board, 0))


def winning_move(board, piece):
    """
    This functions checks if a winning move is made or not,
    checks if 4 same color are in same line

    :param board: 6x7 matrix
    :param piece: GUI element
    :return: bool
    """
    for column in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][column] == piece \
                    and board[row][column + 1] == piece \
                    and board[row][column + 2] == piece \
                    and board[row][column + 3] == piece:
                return True

    # Check vertical locations for win
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][column] == piece\
                    and board[row + 1][column] == piece\
                    and board[row + 2][column] == piece \
                    and board[row + 3][column] == piece:
                return True

    for column in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][column] == piece \
                    and board[row + 1][column + 1] == piece \
                    and board[row + 2][column + 2] == piece \
                    and board[row + 3][column + 3] == piece:
                return True

    for column in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][column] == piece \
                    and board[row - 1][column + 1] == piece \
                    and board[row - 2][column + 2] == piece \
                    and board[row - 3][column + 3] == piece:
                return True


def draw_board(board, width, height, size, screen):
    """
    This function draws a GUI board
    :param board: 6x7 matrix
    :param width: int
    :param height: int
    :param size: int
    :param screen: GUI element
    :return:
    """
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen,
                             BLUE,
                             (column * SQUARE_SIZE,
                              row * SQUARE_SIZE + SQUARE_SIZE,
                              SQUARE_SIZE,
                              SQUARE_SIZE))
            pygame.draw.circle(screen,
                               BLACK,
                               (int(column * SQUARE_SIZE + SQUARE_SIZE / 2),
                                int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)),
                               RADIUS)

    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][column] == 1:
                pygame.draw.circle(screen, RED, (
                    int(column * SQUARE_SIZE + SQUARE_SIZE / 2),
                    height - int(row * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   RADIUS)
            elif board[row][column] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(column * SQUARE_SIZE + SQUARE_SIZE / 2),
                    height - int(row * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   RADIUS)
    pygame.display.update()


def reset_window(board):
    """
    This function resets the game gui state
    :param board: 6x7 matrix
    :return: None
    """
    width = COLUMN_COUNT * SQUARE_SIZE
    height = (ROW_COUNT + 1) * SQUARE_SIZE
    size = (width, height)
    screen = pygame.display.set_mode(size)
    draw_board(board, width, height, size, screen)
    pygame.display.update()


SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)


def run_connect():
    """
    This function is reponsible for execution of the connect four feature
    :return: None
    """
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    pygame.init()
    width = COLUMN_COUNT * SQUARE_SIZE
    height = (ROW_COUNT + 1) * SQUARE_SIZE
    size = (width, height)
    screen = pygame.display.set_mode(size)
    draw_board(board, width, height, size, screen)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                # print(event.pos)
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARE_SIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", True, RED)
                            screen.blit(label, (40, 10))
                            game_over = True
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARE_SIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", True, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                print_board(board)
                draw_board(board, width, height, size, screen)

                turn += 1
                turn = turn % 2

                if game_over:
                    game_over = False
                    time.sleep(3)
                    board = create_board()
                    reset_window(board)
