print("                                         welcome to tic tac toe")
print("This game can be played by 2 players X and O. Both the players will alternatively enter their desired coordinates.")
def start():  #this function is used to initialise an empty board for the game.
    global board
    board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

def print_board():      #this function prints the board with the latest values entered by the players.
    print(' ---------')
    for row in board:
        print(' ',row[0],'|',row[1],'|',row[2])
        print(' ---------')

def block_empty():              #this function checks wether the block in which user is trying to enter is empty or not.
    for row in board:
        for room in row:
            if not room:
                return True
    return False

def set_block(roomxy,state):   #this function sets the block to "X" or "O" according to the input.
    x = int(roomxy[0])-1
    y = int(roomxy[1])-1
    row = board[x]
    room = row[y]
    if not room:
        board[x][y] = state
        return True
    return False

def check_xy(xy): #this function is used to check if the entered coordinates are valid or not.
    xy = str(xy)
    if len(xy) != 2:
        return False
    if int(xy[0]) > 3 or int(xy[0]) < 1 or int(xy[1]) > 3 or int(xy[1]) < 1:
        return False
    return True

def check_for_win():         #Checks for a winner
    if board[0][0] == board[0][1] == board[0][2] != '':
        winner = board[0][0]
        print(f'{winner} won! the game')

    elif board[1][0] == board[1][1] == board[1][2] != '':
        winner = board[1][0]
        print(f'{winner} won! the game')

    elif board[2][0] == board[2][1] == board[2][2] != '':
        winner = board[2][0]
        print(f'{winner} won! the game')

    elif board[0][0] == board[1][0] == board[2][0] != '':
        winner = board[0][0]
        print(f'{winner} won! the game')

    elif board[0][1] == board[1][1] == board[2][1] != '':
        winner = board[0][1]
        print(f'{winner} won! the game')

    elif board[0][2] == board[1][2] == board[2][2] != '':
        winner = board[0][0]
        print(f'{winner} won! the game')
        
    elif board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        print(f'{winner} won! the game')
  
    elif board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        print(f'{winner} won! the game')

    else:
        return False
    
    return True


turn = 'o'
start()

while block_empty():     #This is the funtion which takes user input and calls for printing the board while game is not over
    print_board()
    print('\n')
    if turn == 'o':
        turn = 'x'
    else:
        turn = 'o'
    print(f'{turn}\'s Turn:')
    print('')
    while True:
        xy = int(input("enter the row and column(xy):"))
        if check_xy(xy):
            if set_block(str(xy),turn):
                break
            print('This block is already occupied!')
            continue
        print('Please enter valid coordinates!')
        continue
    if check_for_win():
        break
print_board()
print('Game Over')
input()
