# TEST PLAN:

## Table no: High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  H_01       | Check for System Compatabilty|Requirement.txt file |Environment Setup|TBD|Scenario|
|  H_02       | Check if Snake game GUI executes properly|Key press in accordance to Menu option |GUI should open|TBD|Technical|
|  H_03       | Check if Grids are properly displayed| Key press in accordance to Menu option |A grid should be visible on a new frame|TBD| Technical |
|  H_04       | Check if Snake Moves in accordance to arrow keys|Key press for movement of snake |Snake should turn in desired direction|TBD|Technical|
|  H_05       | Check if Snake gets longer each time it's head overlaps with cube | Key press |Snake's length should increase by 1|TBD|Technical|
|  H_06       | Check if game gets over if when snake head hits itself|Key presses |Pop up message showing "Game over" with point scored|TBD|Technical|
|  H_07       | Check if Snake game gets over if the snake head hits the wall|Key press |Pop up message showing "Game over" with point scored|TBD|Technical|
|  H_08       | Check if player wins if all the cubes except one are filled with snake body| Key press |Pop up message showing "You win"|TBD|Technical|
|  H_09       | Check if the user is able to opt to his desired difficulty level. |Enter the suggested option|Solution of the selected difficulty option| TBD | Technical |
|  H_10       | Check if the user is able to submit his own problem board in to the solver. |Enter own sudoku problem board|Solution of the entered problem| TBD | Technical |
|  H_11       | Check if the user is able to get back to the cover page sfter getting the solution of his code. |Enter the suggested choice|Coverpage will be printed| TBD | Technical |
|  H_12       | Check if the user is able to able to submit another problem after solving one proble |Enter the suggested choice|difficulty level options| TBD | Technical |
|  H_13       | Check if the sudoku solver is checking the available blank spaces or not |Enter the difficulty level|fill the blank spaces with correct number| TBD | Technical |
|  H_14       | Check if the game board is displayed correctly |key press according to menu options|An empty 3x3 square grid will be displayed| TBD | Technical |
|  H_15       | Check if player 1 is prompted to enter desired coordinates|key press according to menu options|Player will be prompted to enter coordinates of the desired cell in th game board.| TBD | Technical |
|  H_16       | Check if the player input is valid and postion is not already occupied |Entering desired coordinates|If valid, Player 2 will be prompted for input otherwise error will be displayed and player will be prompted for input again.| TBD | Technical |
|  H_17       | Check the validity of input again for Player 2|User input |If valid Proceed to next step otherwise error will be displayed| TBD | Technical |
|  H_18       | Check for a winner . |key press according game requirement|If a winner is found , game is over otherwise the game shall continue untill a winner is found.| TBD | Technical |
|  H_19       | Check if player is able to put dot at right place | Mouse Click |Board should be visible with dot at desired place|TBD|Scenario|
|  H_20       | Check if board is getting updated after every player's move| Mouse Click in accordance to player's choice | Board should get update|TBD|Technical|
|  H_21       |  Check winner is declared once straight line with 4 consecutive dots are made | Mouse Click |Message is displaying who is the winner|TBD| Technical |
|  H_22       |Check if there is tie when none of the player is able win the game | Mouse Click |Message is displaying that its a tie|TBD|Technical|
|  H_23       | Check if game is able to calculate time at the end of game  | Mouse Click  |Time is shown at terminal |TBD|Technical|
|  H_24       | Check if game is able sees GUI is properly excutes  | key pressing |GUI should be opened |TBD|Technical|
|  H_25       | Check if game is able to checks the blocks are moving in particular direction according pressing the key |key press   |checks length of grid |TBD|Technical|
|  H_26       | Check if game is able to checks the row blocks are filled   | key press |increase the score |TBD|Technical|
|  H_27       | Check if game is able to checks the coloumn blocks are filled  | key press  |it time to exit game and visibility of scores |TBD|Technical|
|  H_28       | Check if game checks the if player gets high score it will update the high score module  | Mouse click   |score will be updated |TBD|Technical|

## Table no: Low level test plan

| **Test ID** | **HLT ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|-----|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  L_01       |H_02|<TBD>|<TBD>|<TBD>| SUCCESS/FAIL |Requirement based/Scenario Based |

