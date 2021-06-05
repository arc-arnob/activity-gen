def print_board(board):
    print(' ---------')
    for row in board:
        print(' ', row[0], '|', row[1], '|', row[2])
        print(' ---------')
    return board


def block_empty(board):
    for row in board:
        for room in row:
            if not room:
                return True
    return False


def set_block(board, room_xy, state):  # this function sets the block to "X" or "O" according to the input.
    print(room_xy[0])
    x = int(room_xy[0]) - 1
    y = int(room_xy[1]) - 1
    row = board[x]
    room = row[y]
    if not room:
        board[x][y] = state
        return True
    return False


def check_xy(xy):  # this function is used to check if the entered coordinates are valid or not.
    xy = str(xy)

    if len(xy) != 2:
        return False
    elif ord(xy[0]) < 48 or ord(xy[1]) > 57 or ord(xy[0]) < 48 and ord(xy[1]) > 57:
        return False
    elif int(xy[0]) > 3 or int(xy[0]) < 1 or int(xy[1]) > 3 or int(xy[1]) < 1:
        return False
    return True


def check_for_win(board):  # Checks for a winner
    if board[0][0] == board[0][1] == board[0][2] != '':
        winner = board[0][0]
        print(' ')
        print(f'{winner} won! the game')

    elif board[1][0] == board[1][1] == board[1][2] != '':
        winner = board[1][0]
        print(' ')
        print(f'{winner} won! the game')

    elif board[2][0] == board[2][1] == board[2][2] != '':
        winner = board[2][0]
        print(' ')
        print(f'{winner} won! the game')

    elif board[0][0] == board[1][0] == board[2][0] != '':
        winner = board[0][0]
        print(' ')
        print(f'{winner} won! the game')

    elif board[0][1] == board[1][1] == board[2][1] != '':
        winner = board[0][1]
        print(' ')
        print(f'{winner} won! the game')

    elif board[0][2] == board[1][2] == board[2][2] != '':
        winner = board[0][0]
        print(' ')
        print(f'{winner} won! the game')

    elif board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        print(' ')
        print(f'{winner} won! the game')

    elif board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        print(' ')
        print(f'{winner} won! the game')

    else:
        return False

    return True


def run_tic_tac_toe():
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    turn = 'o'
    # start()

    while block_empty(board):
        print_board(board)
        print('\n')
        if turn == 'o':
            turn = 'x'
        else:
            turn = 'o'
        print(f'{turn}\'s Turn:')
        print('')
        while True:
            xy = input("enter the row and column(xy):")
            if check_xy(xy):
                if set_block(board, str(xy), turn):
                    break
                print('This block is already occupied!')
                continue
            print('Please enter valid coordinates!')
            continue
        if check_for_win(board):
            print_board(board)

            return

    print("Match Draw")
    return


if __name__ == "__main__":
    run_tic_tac_toe()
