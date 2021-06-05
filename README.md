# GameBoi - SDLC Activity Based Learning



Build | Code Quality | Unit Testing | Git Inspector
|---------|------------|-----------|----------------
| [![Python application](https://github.com/arc-arnob/activity-gen/actions/workflows/python-app.yml/badge.svg)](https://github.com/arc-arnob/activity-gen/actions/workflows/python-app.yml)        |[![Pylint](https://github.com/arc-arnob/activity-gen/actions/workflows/pylint.yml/badge.svg)](https://github.com/arc-arnob/activity-gen/actions/workflows/pylint.yml) [![flake8](https://github.com/arc-arnob/activity-gen/actions/workflows/flake8.yml/badge.svg)](https://github.com/arc-arnob/activity-gen/actions/workflows/flake8.yml)| [![Pytest](https://github.com/arc-arnob/activity-gen/actions/workflows/main.yml/badge.svg)](https://github.com/arc-arnob/activity-gen/actions/workflows/main.yml)         |  [![Contribution Check - Git Inspector](https://github.com/arc-arnob/activity-gen/actions/workflows/gitinspector.yml/badge.svg)](https://github.com/arc-arnob/activity-gen/actions/workflows/gitinspector.yml)



## Folder Structure
Folder             | Description
-------------------| -----------------------------------------
`1_Requirements`   | Documents detailing requirements and research
`2_Design`         | Documents specifying design details
`3_Implementation` | All code and documentation
`4_Test_plan`      | Documents with test plans and procedures

## Contributors List and Summary

PS Id. |  Name   |    Features    | Issues Raised | Issues Resolved | No Test Cases |Test Case Pass
-------|---------|----------------|----------------|---------------|-------------|--------------
`99004349` | Arnob Chowdhury  | Snake GUI, Main Menu, Git Workflow, Code coverage, Code refactor- Tic Tac Toe, Connect Four  |  21    | 16  | 27  | 27     
`99004351` | Debashish Dash  | Sudoku solver, breaking files intomodules, Main menu, Coloring and clear-screen feature in main.py and sudoku.py, Banner and cover page of the project | 8   | 5  | 7  | 7  
`99004350` | Durgapu Venkata Shyam Sudheer  | Tetris GUI,Documentaion,Report |   2   | 5  | 0  | 0  
`99004352` | Anshul Mehta  | <TBD>  | <TBD>     | <TBD>  |<TBD>  | <TBD>
`99004353` | Anmol Tandon  |  | 3 | 4 | 6 | 6
 * **note: some test cases where user inuts are required are tested manually, those are not mentiones here, those test cases are written in the [4_TestPlans
 folder](https://github.com/GENESIS2021Q1/sdlc-team-31/tree/main/4_TestPlan) || Manually tested test cases: L_18, L19, H_09, H_10**
 
 ------
 
| Feature Id | Feature | Status
| -----------|---------|------
|F_01| Snake game GUI  | IMPLEMENTED
|F_02| Tic Tac Toe Game GUI|  IMPLEMENTED
|F_03| Connect Four game GUI| IMPLEMENTED
|F_04| Tetris Game GUI | IMPLEMENTED
|F_05| Sudoku problems solver CLI | IMPLEMENTED
|F_06| High Score registry | FUTURE
|F_07| High Score gets stored to persistence layer after every game | FUTURE
|F_08| High Score is updated after every game | FUTURE


## Challenges Faced and How Was It Overcome
| No. | Challenge | Solution
|-----|-----------|--------
|1. | <TBD>|

## Run on your PC 

### What Will You Build
You will build and run a gaming console which will allow you to play CLI and GUI based game. 

### What you will need

* A favorite text editor or IDE
* Python 3.7+ Interpretor
* Clone of this repository

### To clone and run the project follow the below steps: 
* Download and unzip the source repository for this guide, or clone it using Git: git clone https://github.com/GENESIS2021Q1/sdlc-team-31.git
* cd to 3_Implementation
* run `pip install -r requirement.txt` 
* open `main.py` file and execute the file

### To run Unit test cases follow the below steps
  * Navigate to 3_Implementation
  * on command line execute `pytest -v test.py`. Set `-s` flag to see more details 
  * to view detailed unit test report please follow the link: [Unit Test Report](https://github.com/GENESIS2021Q1/sdlc-team-31/blob/main/3_Implementation/readme.md#unit-test-report)
  
### To run code coverage follow the below steps
  * Navigate to 3_Implementation
  * in command line execute `pytest --cov=. --cov-report term test.py`
  * to view % coverage please follow the link: [Code Coverage Report](https://github.com/GENESIS2021Q1/sdlc-team-31/tree/main/3_Implementation#code-coverage-report)

  
# References

* **[Pytest Youtube video](https://www.youtube.com/watch?v=bbp_849-RZ4&t=560s)**
* **[Git credentials settings youtube video](https://www.youtube.com/watch?v=lLgWWtOk7gk&t=50s)** 
* **[PyGame](https://www.pygame.org/wiki/tutorials)**
* **[python modules](https://www.w3schools.com/python/python_modules.asp)**
