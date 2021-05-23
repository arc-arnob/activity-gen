# Detailed requirements

 # Identifying the Requirements:


 ## Non Functional Requirements:
 * We just require Windows or a Linux Operating System Along with some libraries related to the project.
* the gameboy shall be portable .



 ## Functional Requirements:
* The gameboy shall provide user with option to choose from multiple games available.
* Data of players and high scores in different games shall be kept.
* Users will be able to switch between different games easily.
* Everytime users quit a particular game, they will return to the main menu.
## High Level Requirements: 
| ID | Description | Category | Status | 
| ----- | ----- | ------- | ---------|
|HL_01| User shall be able to play GUI Snake game  | Technical | TBD
|HL_02| User shall be able to play Tictactoe game| Technical | TBD
|HL_03| User shall be able to play Connect Four game | Technical | TBD
|HL_04| User shall be able to play Tetris | Technical | TBD
|HL_05| User shall be able to find solution Sudoku problems | Technical | TBD
|HL_06| User shall be able to view High Score per games | Technical | TBD
|HL_07| New scores shall get saved everytime user finishes playing a game | Technical | TBD
|HL_08| High scores shall be updated everytime a user ends a game | Technical | TBD
|HL_09| New scores shall be saved to database for later use | Technical | TBD

## Low Level Requirements
| ID | Description | HLR ID | Status (Implemented/Future) |
| ------ | --------- | ------ | ----- |
| LR01 | There shall be 2 types of color in grids (1). Green for Cubes (2). Red for Snake  | HL_01 |  TBD  |
| LR02 | The game shall generate a grid system | HL_01 |  TBD  |
| LR03 |  The game shall be able to color random cell green| HL_01 |  TBD  |
| LR04 | The snake shall be able to move based on the arrow keys pressed by the player| HL_01 |  TBD  |
| LR04_1 | The :arrow_up: key shall decrement y coordinate keeping the x coordinate same of snake head | HL_01 |  TBD  |
| LR04_2 | The :arrow_down: key shall increment y coordinate keeping the x coordinate same of snake head | HL_01 |  TBD  ||
| LR04_3 | The :arrow_left: key shall decrement x coordinate keeping the y coordinate same of snake head | HL_01 |  TBD  |
| LR04_4 | The :arrow_right: key shall increment x coordinate keeping the y coordinate same of snake head| HL_01 |  TBD  |
| LR05 | Game shall end if the cells occupied by snake overlaps | HL_01 |  TBD  |
| LR06 | Game shall show the points earned once the snake cells overlap | HL_01 |  TBD  |
| LR07 | Game shall be able to update the cells comprising of snake to emulate moving snake| HL_01 |  TBD  |
| LR07_1 | If the snake is moving left then only x coordinate shall be decreased continuously keeping y coordinate same| HL_01 |  TBD  |
| LR07_2 |If the snake is moving right then only x coordinate shall be incremented continuously keeping y coordinate sam| HL_01 |  TBD  |
| LR07_3 |If the snake is moving up then only y coordinate shall be decremented continuously keeping x coordinate sam| HL_01 |  TBD  |
| LR07_4 |If the snake is moving down then only y coordinate shall be incremented continuously keeping x coordinate sam| HL_01 |  TBD  |
| LR08 | The Game shall also end if the snake head goes out of the grid x or y coordinate| HL_01 |  TBD  |
| LR09 | There shall be 6 types of colors in  blocks in tetris game | HL_04 | TBD |
| LR10 | There shall be 6 types of shapes  in blocks they are S,Z,I,O,J,L,T | HL_04 | TBD |
| LR11 | The grid will move on based on the arrow keys are pressed by the player | HL_04 | TBD |
| LR11_1 | The :arrow_up:key shall rotate the block in the 90 deg to beside co-ordinate axis | HL_04 | TBD |
| LR11_2 | The :arrow_down:key shall downs the block in the  to straight co-ordinate axis | HL_04 | TBD |
| LR11_3 | The :arrow_left:key shall change the position of the blocks in the x-axis in left side grid | HL_04 | TBD |
| LR11_4 | The :arrow_right:key shall change the position of the blocks in the x-axis in right side grid| HL_04 | TBD |
| LR12 | Game shall end if the blocks are filled in the y axis grid | HL_04 | TBD |
| LR13 | Game shall produce one after one block in the y co-ordinate upto end game | HL_04 | TBD |
| LR14 | Game shall show the points earned when one full x axis grid is filled  | HL_04 | TBD |
| LR15 | There shall be a 3x3 square grid board for tic tac toe game.| HL_02 |  TBD  |
| LR16 | There shall be two players who wil be able to play the game.| HL_02 |  TBD  |
| LR17 | The First player shall be called as 'X' and the second player will be called 'O'| HL_02 |  TBD  |
| LR18 | Both the players shall play alternatively by entering the coordinates for desired position in the game board.| HL_02 |  TBD  |
| LR19 | Players will be prompted to enter their desired coordinates one by one untill someone wins.| HL_02 |  TBD  |
| LR20 | After every move made, an updated version of the game board will be printed.| HL_02 |  TBD  |
| LR21 | If a player chooses a postion which is already occupied, he will be propmted to enter again.| HL_02 |  TBD  |
| LR22 | When the game ends the final board will be printed along with the winners name.| HL_02 |  TBD  |
| LR23 | There shall be few predefined sudoku problems available | HL_05 | TBD |
| LR24 | User shall be able to choose the difficulty level | HL_05 | TBD |
| LR25 | User shall be able to enter his/her own sudoku problem to get its solution | HL_05| TBD |
| LR26 | User shall be able to exit from the program by his own | HL_05 | TBD |
| LR27 | User shall be able to go back to the options after getting the solution of a problem | HL_05 | TBD |
| LR28 | There shall be a board of 6x7 matrix for Connect 4 game. | HL_03 | TBD |
| LR29 | 2 Players shall be there to play the game. | HL_03 | TBD |
| LR30 | Player 1 and Player 2 shall put their entries with Red and Yellow color respectively. | HL_03| TBD |
| LR31 | Both the players will put their entries until line with 4 colored dots is made. | HL_03 | TBD |
| LR32 | At the end winner with final board shall be visible. | HL_03 | TBD |







# State Of Art

## Features with Time 

| Time | Feature |
| ----- | ----- |
| Past |  Few years back games like tic tac toe, sudoko etc were supposed to play on boards or paper that is in offline mode with family and friends. |
| Present | Nowdays most of the games can be played online with computer or friends and likewise we have made 5 games  and based on user's choice it can be played with computer or friends . |
| Future | Near future all these games shall be modified with more advanced graphics and thus can give us a realistic experience like playing them offline on board or paper. |


## Cost with Time 

| Time | Cost |
| ----- | ----- |
| Past | Earlier playing games use to cost less than 1000 where we just need to buy game in physical form for 1 time.  |
| Present | These days playing games costs 0-10000 where we need to pay for internet usage, to buy servers and need to pay some amount for paid games and so on. |
| Future | Coming years cost shall be increased to 0-100000 where we will be able to play games with high graphics on low system configuration through cloud and cost of paid games will also increase as they shall be giving you more realistic experience.  |


## SWOT ANALYSIS
![SWOT Analysis](https://github.com/GENESIS2021Q1/sdlc-team-31/blob/main/1_Requirements/Screenshot%20(305).png)

# 4W&#39;s and 1&#39;H

## WHO:

* All the Puzzle lovers of all ages
* People who want to get answer of a sudoku puzzle.
* GUI games for kids.

## WHAT:

* House of simple fun games(both console and GUI)
* User will get a choice to choose what type and which game he wants to play.

## WHEN:

* During the genesis program first assignment on SDLC, may 2021

## WHERE:

* This gaming application can be used all over the globe, by any one who love playing puzzle games.
* All age group people can use this gaming application.

## HOW:

* User can use this gaming app to entertain themself in the vacant time.
* Playing puzzles helps exercising brain, so this ap will be effective for kids.
 
