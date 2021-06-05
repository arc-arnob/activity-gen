# TEST PLAN:

## Table no: High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Status** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  H_01       | Check for System Compatabilty|Requirement.txt file |Environment Setup| PASS |Scenario|
|  H_02       | Check if Snake game GUI executes properly|Key press in accordance to Menu option |GUI should open|PASS|Technical|
|  H_03       | Check if Grids are properly displayed| Key press in accordance to Menu option |A grid should be visible on a new frame|PASS| Technical |
|  H_04       | Check if Snake Moves in accordance to arrow keys|Key press for movement of snake |Snake should turn in desired direction|PASS|Technical|
|  H_05       | Check if Snake gets longer each time it's head overlaps with cube | Key press |Snake's length should increase by 1|PASS|Technical|
|  H_06       | Check if game gets over if when snake head hits itself|Key presses |Pop up message showing "Game over" with point scored|PASS|Technical|
|  H_07       | Check if Snake game gets over if the snake head hits the wall|Key press |Pop up message showing "Game over" with point scored|MODIFIED-PASS|Technical|
|  H_08       | Check if player wins if all the cubes except one are filled with snake body| Key press |Pop up message showing "You win"|PASS|Technical|
|  H_09       | Check if the user is able to opt to his desired difficulty level. |Enter the suggested option|Solution of the selected difficulty option| TBD | Technical |
|  H_10       | Check if the user is able to submit his own problem board in to the solver. |Enter own sudoku problem board|Solution of the entered problem| TBD | Technical |
|  H_11       | Check if the user is able to get back to the cover page after getting the solution of his code. |Enter the suggested choice|Coverpage will be printed| TBD | Technical |
|  H_12       | Check if the user is able to able to submit another problem after solving one proble |Enter the suggested choice|difficulty level options| TBD | Technical |
|  H_13       | Check if the sudoku solver is checking the available blank spaces or not |Enter the difficulty level|fill the blank spaces with correct number| TBD | Technical |
|  H_14       | Check if the game board is displayed correctly |key press according to menu options|An empty 3x3 square grid will be displayed| TBD | Technical |
|  H_15       | Check if player 1 is prompted to enter desired coordinates|key press according to menu options|Player will be prompted to enter coordinates of the desired cell in th game board.| TBD | Technical |
|  H_16       | Check if the player input is valid and postion is not already occupied |Entering desired coordinates|If valid, Player 2 will be prompted for input otherwise error will be displayed and player will be prompted for input again.| TBD | Technical |
|  H_17       | Check the validity of input again for Player 2|User input |If valid Proceed to next step otherwise error will be displayed| TBD | Technical |
|  H_18       | Check for a winner . |key press according game requirement|If a winner is found , game is over otherwise the game shall continue untill a winner is found.| TBD | Technical |
|  H_19       | Check if player is able to put dot at right place | Mouse Click |Board should be visible with dot at desired place|TBD|Scenario|
|  H_20       | Check if board is getting updated after every player's move| Mouse Click in accordance to player's choice | Board should get update|TBD|Technical|
|  H_21       | Check winner is declared once straight line with 4 consecutive dots are made | Mouse Click |Message is displaying who is the winner|TBD| Technical |
|  H_22       | Check if there is tie when none of the player is able win the game | Mouse Click |Message is displaying that its a tie|TBD|Technical|
|  H_23       | Check if game is able to calculate time at the end of game  | Mouse Click  |Time is shown at terminal |TBD|Technical|
|  H_24       | Check if game is able sees GUI is properly excutes  | key pressing |GUI should be opened | pass |Technical|
|  H_25       | Check if game is able to checks the blocks are moving in particular direction according pressing the key |key press   |checks length of grid |pass |Technical|
|  H_26       | Check if game is able to checks the row blocks are filled   | key press |increase the score | pass |Technical|
|  H_27       | Check if game is able to checks the coloumn blocks are filled  | key press  |it time to exit game and visibility of scores | pass |Technical|
|  H_28       | Check if game checks the if player gets high score it will update the high score module  | Mouse click   |score will be updated | pass |Technical|

## Table no: Low level test plan

| **Test ID** | **HLT ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Status** |**Type**  |   **Feature Name**   |
|-------------|-----|--------------------------------------------------------------|------------|-------------|----------------|------------------|-----------------|
|  L_01       |H_01|requirement.txt|System Setup Successful|System Setup Successful| SUCCESS | Scenario Based | Snake |
|  L_02       |H_02|Application should start w/o any error|Application executed|dependencies| SUCCESS | Scenario Based | Snake |
|  L_03       |H_03|grid of 500 px X 500 px should be developed|width and height of the grid in px|grid of 500 px X 500 px created| SUCCESS | Requirement Based | Snake |
|  L_04       |H_03|Grid should contain 20 rows and 20 columns|row number| 20 x 20 grid was created | SUCCESS | Requirement Based | Snake |
|  L_05       |H_04|Snake head X-Coordinate should decrement by 1 if ⬅️ is pressed |:arrow_up: key press| Snake should move left | SUCCESS | Requirement Based | Snake |
|  L_06       |H_04|Snake head X-Coordinate should increment by 1 if ➡️ is pressed |➡️ key press| Snake should move right | SUCCESS | Requirement Based | Snake |
|  L_07       |H_04|Snake head Y-Coordinate should decrement by 1 if ⬆️ is pressed |:arrow_up: key press| Snake should move up | SUCCESS | Requirement Based | Snake |
|  L_08       |H_04|Snake head Y-Coordinate should increment by 1 if ⬇️ is pressed |:arrow_down: key press| Snake should move down | SUCCESS | Requirement Based | Snake |
|  L_09       |H_05|A new Cube object is created each time snake head position is equal to random snack position |Snake Object, Cube object| A new Cube object added at the end of the snake | SUCCESS | Requirement Based | Snake |
|  L_10       |H_06|The Snake Object Deletes all Cube objects except one when game restarts|Snake Object, Overlapping first snake cube object with snake body object| Window pop stating score and play again button | SUCCESS | Requirement Based | Snake |
|  L_11       |H_08|The player wins if 499 grids are filled with snake body|Snake Object| window pop up stating "You win" and score  | SUCCESS | Boundary Based | Snake |
|  L_12       | - |The Snake body first obejct should be created at (10,10) cell of the grid moving right |Snake Object| A red cube moving right  | SUCCESS | Requirement Based | Snake |
|  L_13       | H_04 |The snake objects should be repostioned to (0, grid[1]) if hits the right boundary  | Snake Object, Snake postion| Snake object should be repostioned | SUCCESS | Requirement Based | Snake |
|  L_14       | H_04 |The snake objects should be repostioned to (rows-1, grid[1]) if hits the left boundary  | Snake Object, Snake postion| Snake object should be repostioned | SUCCESS | Requirement Based | Snake |
|  L_15       | H_04 |The snake objects should be repostioned to (grid[0], 0) if hits the lower boundary  | Snake Object, Snake postion| Snake object should be repostioned | SUCCESS | Requirement Based | Snake |
|  L_16       | H_04 |The snake objects should be repostioned to (grid[0], rows-1) if hits the upper boundary  | Snake Object, Snake postion| Snake object should be repostioned | SUCCESS | Requirement Based | Snake |
|  L_17       | H_05 |The snake objects should never overlap with the snake obejct when getting recreated | Snake Object, Snake postion, Cube Object, Cube Position| Random Snack generation without overlapping snake cube objects | SUCCESS | Requirement Based | Snake |
|  L_18       | H_09 |In sudoku if user is pressing 1 then difficulty levels options will get printed| 1 | difficlty levels option | SUCCESS | Requirement based | Sudoku solver | 
|  L_19       | H_09 |In sudoku if user is pressing 2 then user will be prmpted to enter his desired i/p | 2 | user i/p printed in the board | SUCCESS | Requirement based | Sudoku solver | 
|  L_20       | H_09 |In sudoku if the user pressing 1 after the printing board | 1 | solution of user's sudoku problem | SUCCESS | Requirement based | Sudoku solver | 
|  L_21       | H_10 | After entering the user board, find empty function's job | user I/P | checks the empty places or 0s | SUCCESS | Requirement based | Sudoku solver | 
|  L_22       | H_11 |  After getting solution if user presses 1 | user i/p | menue | SUCCESS | Requirement based | Sudoku solver | Connect 4 |   
|  L_23       |H_19| Piece should be placed at right place | Mouse click at one of column | Dependencies | SUCCESS | Requirement Based | Connect 4 |  
|  L_24       |H_20| Rows should get flip i.e upside down | Application executed | System setup successful | SUCCESS | Scenario Based | Connect 4 | 
|  L_25       |H_21| Right winner should be declared| Mouse click at one of 7 column | Winner declared | SUCCESS | Scenario Based | Connect 4 | 
|  L_26       |H_20| To check which rows are available for next move | System setup successful | Updated board should be visible | SUCCESS | Requirement Based | Connect 4 | 
|  L_27       |H_22| To avoid overlapping of making same turn | Mouse click at one of 7 column | Piece should be placed at right place | SUCCESS | Scenario Based | Connect 4 | 
|  L_28       |H_23| Graphics should be well used to display game board | Application executed | Updated board should be visible | SUCCESS | Scenario Based | Connect 4 |
|  L_29       |H_04| Snake X coordinate keeps decreasing if ⬅️ is pressed with any ⬆️ ➡️ ⬇️ |:arrow_left: + ⬆️ / ➡️ / ⬇️ key press| Snake should keep moving left | SUCCESS | Scenario Based | Snake |
|  L_30       |H_04| Snake X coordinate keeps increasing if ➡️ is pressed with any ⬆️  ⬇️ |➡️: + ⬆️ / ⬇️ key press| Snake should keep moving right | SUCCESS | Scenario Based | Snake |
|  L_31       |H_04| Snake Y coordinate keeps decreasing if ⬆️ is pressed with any ⬇️ |⬆️: + ⬇️ key press| Snake should keep moving UP | SUCCESS | Scenario Based | Snake |
|  L_32       |H_14| Tictactoe Game should execute successfully | Application executed Successfully | Dependencies | SUCCESS | Scenario Based | TicTacToe |
|  L_33       |H_14| 3x3 Square Game Board should be initailised correctly | Execute tictactoe.py file | An Empty game board should be visible | SUCCESS | Requirement Based | TicTacToe |
|  L_34       |H_15| Player should enter the column and row(xy) | User input  | Checks if the coordinates are valid | SUCCESS | Requirement Based | TicTacToe |
|  L_35       |H_16| User Input shall be tested for validity | User input  | Error will be shown if  coordinates are not valid | SUCCESS | Requirement Based | TicTacToe |
|  L_36       |H_16| If a player enters a non-number , he should be prompted to enter again| User input  |Error is displayed and player is asked to enter again | SUCCESS | Requirement Based | TicTacToe |
|  L_37       |H_17|User input should be invalid if it is not between 1 and 3| User input  | Error is displayed and player is asked to enter again | SUCCESS | Boundary Based | TicTacToe |
|  L_38       |H_17|User input should be only double digit number in (row column) format| User input  | Error is displayed and player is asked to enter again | SUCCESS | Boundary Based | TicTacToe |
|  L_39       |H_17| If a player enters a non-number , he should be prompted to enter again| User input  |Error is displayed and player is asked to enter again | SUCCESS | requirement based | TicTacToe | 
|  L_40       |H_18| If a player wins game should end | Players's moves |When a Player wins, winner is displayed and the game ends | SUCCESS | Requirement Based | TicTacToe |
|  L_41       |H_18| If no player wins and the board is filled, game should be a Draw | Players's moves |DRAW is displayed and the game ends | SUCCESS | Requirement Based | TicTacToe |
|  L_42       | H_10 | In sudoku, solution of easy easy problem | easy sudoku | solution for easy sudoku | SUCCESS | Boundary Based | Sudoku Solver |
|  L_43       | H_10 | In sudoku, solution of mid problem | mid problem sudoku | solution for mid sudoku | SUCCESS | Boundary Based | Sudoku Solver |
|  L_44       | H_10 | In sudoku, solution of easy Hard problem | Hard sudoku | solution for hard sudoku | SUCCESS | Boundary Based | Sudoku Solver |
|  L_45       | H_10 | In sudoku, solution of easy very hard problem | Very Hard sudoku | solution for very hard sudoku | SUCCESS | Boundary Based | Sudoku Solver |
|  L_46       | H_11 | On running the cover page | user i/p | coverpage | SUCCESS | Requirement based | Sudoku solver |
|  L_47       | H_24 | GUI should will appear | appplication executed | GUI setup | SUCCESS | Scenario | Tetris |
|  L_48       | H_25 | blocks are moving when left arrow is pressed  | key press |the block will moves left side  | SUCCESS | Requirement based | Tetris |
|  L_49       | H_25 | blocks are moving when right arrow is pressed  | key press | the block will moves right side | SUCCESS | Requirement based| Tetris |
|  L_50       | H_25 | blocks are moving when up arrow is pressed  | key press | the block will rotate 90 degree with respective direction | SUCCESS | Scenario | Tetris |
|  L_51       | H_25 | blocks are moving when down arrow is pressed  | key press | the block will moves down the grid  | SUCCESS | requirement based | Tetris |
|  L_52       | H_27 | when 1 bock is intersected the grid   | tetris object | A new block is created  | SUCCESS | requirement based | Tetris |
|  L_53       | H_28 | when 1 row is fully filled without any gap  | updated score | the score will increased by 1 point  | SUCCESS | Scenario | Tetris |
|  L_54       | H_29 | when 1 column is fully filled without any gap  | score decalaration | the game will end | SUCCESS | Scenario | Tetris |
|  L_55       | H_29 | after completion of the game  press esc button | key press | it will enters into the new game again | SUCCESS | Scenario | Tetris |
|  L_56       | - | When first menu is displayed, only 0️⃣ 1️⃣ and 2️⃣ keys should be validated |  Any input | Only 0️⃣/1️⃣/2️⃣ should be validated | SUCCESS | Scenario | Main Menu |
|  L_57       | - | When CLI games menu is displayed, only 0️⃣ 1️⃣ 2️⃣ and 3️⃣ keys should be validated |  Any input | Only 0️⃣/1️⃣/2️⃣/3️⃣  should be validated | SUCCESS | Scenario | Main Menu |
|  L_58       | - | When GUI games menu is displayed, only 0️⃣ 1️⃣ 2️⃣ 3️⃣ and 4️⃣ keys should be validated |  Any input | Only 0️⃣/1️⃣/2️⃣/3️⃣/:four:  should be validated | SUCCESS | Scenario | Main Menu |


# Code Coverage Report
**============================= Test session starts =============================**

**platform win32 -- Python 3.7.3, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
plugins: cov-2.12.0
collected 42 items**

test.py ..........................................                       [100%]

**----------- coverage: platform win32, python 3.7.3-final-0 -----------**

| Name | Stmts | Miss| Cover | developer PS number
|------------|-------|------|-------------|---------
connect_four_game\__init__.py  |     0  |    0 |  100%  | 
connect_four_game\c4.py     |      118  |   78 |   34%  |
main.py                    |        81  |   59 |   27%  | 99004349
snake_game\__init__.py     |         0  |    0 |  100%  | 99004349
snake_game\snake.py       |        184  |   46 |   75%  | 99004349
sudoku_game\__init__.py   |          0  |   0 |  100%   | 99004351
sudoku_game\boards.py     |          6  |   0 |  100%   | 99004351
sudoku_game\coverpage.py  |          7  |   0 |  100%   | 99004351
sudoku_game\sudoku.py     |        202  |  135 |   33%  | 99004351
test.py                   |        204  |   2  |  99%   | 99004349
tetris_game\__init__.py   |          0  |      0  |   100%  |
tetris_game\tertis.py      |       157  |    126  |  20%  |
tictactoe_game\__init__.py  |        0  |    0  | 100%  |
tictactoe_game\tictactoe.py  |      93  |     32  |    66%  |
TOTAL                     |       1052  |  478 |   55%


**============================= 42 passed in 2.49s ==============================**

* **Note: In sudoku.py file most of the functions are user defined so those are tested manually, hence the code overage is low, but in the other files of the same sudoku modules code coverage is high as those are tested in test.py**







