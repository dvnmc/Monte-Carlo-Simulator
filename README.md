# Monte-Carlo-Simulator
**Final Project for DS51000**


## Metadata
Package: Monte Carlo Simulator

Creator: Devin McDonald

Net ID: djm6cz


## Synopsis

### Installing:

First clone the Monte-Carlo-Simulator GitHub repository to Desktop or any other desired directory

From the command line: 

`cd <Directory>`

`git clone https://github.com/dvnmc/Monte-Carlo-Simulator.git`

After successfully cloning the repository, run the following to install the Monte-Carlo-Simulator package

From the command line: 

`cd Monte-Carlo-Simulator/src; pip install ..`

or

In Jupyter Notebook: 

`!cd Monte-Carlo-Simulator/src; pip install ..`


### Importing:

Import the three classes Die, Game, and Analyzer as modules from the monte_carlo.py file

`from monte_carlo import Die`

`from monte_carlo import Game`

`from monte_carlo import Class`


### Creating Dice:

The user can create a die object by passing a list of numbers or strings to the Die class

`die_1 = Die([1,2,3,4,5,6])`

`die_2 = Die(['H', 'T'])`

Additionally, the user can change the weights of a die's faces as such

`example_die_1.change_weight(face_val, new_weight)`

face_val represents the face value that the user would like to assign a new weight (new_weight) to


### Playing Games:

The user can create a game object by passing a list of already instantiated similar Die objects to the Game class

`game_1 = Game([die_1, die_1, die_1])`

Once a game object is instantiated, the user can use the following lines of code to play a game by rolling the dice N times

`game_1.play(10)`

The user can see the results of the rolls by using the show method

`game_1.show()`






