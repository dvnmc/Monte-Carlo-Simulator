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

`die = Die([1,2,3,4,5,6])`

or

`die = Die(['H', 'T'])`

Additionally, the user can change the weights of a die's faces as such

`die.change_weight(1, 5)`

In this case, 1 represents the face (or side) marked 1 on a six sided die and 5 is the new weight assigned to that face (all faces initially default to a weight of 1)


### Playing Games:

The user can create a game object by passing a list of already instantiated similar Die objects to the Game class

`game = Game([die, die, die])`

Once a game object is instantiated, the user can use the following lines of code to play a game by rolling the dice N times -- in this example N = 10

`game.play(10)`

The user can see the results of the rolls by using the show method

`game.show()`


### Analyzing Games:

The user can create an analysis object by passing a game object to the Analyzer class

`analysis = Analyzer(game)`

There are several ways in which games can be analyzed including through jackpot count (all identical faces), combination count (distinct combinations of faces), and face count (how many times a given face is rolled in each event)

`analysis.jackpot()`

`analysis.combo()`

`analysis.face_counts()`

Each analysis method also returns a unique DataFrame

`analysis.jackpot_df`

`analysis.combo_df`

`analysis.face_counts_df`


## API description

### All Classes and Methods

**Class**

`Die()`

'''

This class is used to create a die that has N sides, or “faces”, and W weights. 
Additionally, the weights can be changed, and the die can be rolled to select a face.

'''
    
**Methods**
    
`__init__(self, faces)`

'''

PURPOSE: initialize a Die object

INPUTS

faces (array of ints, floats, or strings)

OUTPUT

None

'''

`change_weight(self, face_val, new_weight)`

'''

PURPOSE: change the weight of a single side of a die object

INPUTS

face_val (int, float, or string)     
new_weight (int or float) 

OUTPUT

None 

'''

`roll_die(self, n_rolls = 1)`

'''

PURPOSE: roll the die one or more times

INPUTS

n_rolls (int)

OUTPUT

*not stored* (list of ints)

'''

`current_faces_and_weights(self)`

'''

PURPOSE: show the die’s current set of faces and weights

INPUTS

None

OUTPUT

N/A (private pd.DataFrame)

'''


**Class**

`Game()`

'''

This class is used to create a game that consists of rolling of one or more dice 
of the same kind. The dice can be rolled one or more times. 

'''

**Methods**

`__init__(self, dice)`

'''

PURPOSE: initialize a Game object 

INPUTS

dice (list of already instantiated similar Die objects)

OUTPUT

None

'''

`play(self, n_rolls)`

'''

PURPOSE: roll the dice a specified number of times

INPUTS

n_rolls (int)

OUTPUT

None

'''

`show(self, wide_or_narrow = 'wide')`

'''

PURPOSE: show the user the results of the most recent play

INPUTS

wide_or_narrow (str, either "wide" or "narrow")

OUTPUT   

N/A (private pd.DataFrame either stacked or unstacked)  


'''


**Class** 

`Analyzer()`

'''

This class takes the results of a single game and computes various descriptive statistical properties.

'''

**Methods**

`__init__(self, game)`

'''

PURPOSE: initialize an Analyzer object

INPUTS

game (already instantiated Game object)

OUTPUT

None

'''

`jackpot(self)`

'''

PURPOSE: compute how many times the game resulted in all identical faces

INPUTS

None

OUTPUT

total_jackpots (int)

'''

`combo(self)`

'''

PURPOSE: compute the distinct combinations of faces rolled, along with their counts

INPUTS

None

OUTPUT

None

'''

`face_counts(self)`:

'''

PURPOSE: compute how many times a given face is rolled in each event

INPUTS

None

OUTPUT

None

'''


## Manifest
### Files

- LICENSE
- README.md
- scenarios.ipynb
- setup.py
- test_results.txt
- src
    - \_\_init_\_\.py
    - monte_carlo.py
    - unit_tests.py
