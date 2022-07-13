import numpy as np
import pandas as pd
import unittest

from monte_carlo import Die
from monte_carlo import Game
from monte_carlo import Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    '''
    This class is used to apply the unittest unit testing framework to 
    each method in each class of the monte_carlo.py file.
    '''
    
    def test_init_Die(self):
        '''
        PURPOSE: ensure Die object is initialized correctly 
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        weights = die.weights
        expected = np.ones(6)
        self.assertTrue((weights == expected)[0])
    
    def test_change_weight_invalid(self):
        '''
        PURPOSE: test whether change_weight method informs the user when 
        attempting to change the weight of an invalid face
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        die_new_weight = die.change_weight(12,5)
        expected = 'This is not a valid face.'
        self.assertEqual(die_new_weight, expected)
        
    def test_change_weight_valid(self):
        '''
        PURPOSE: test whether change_weight method operates correctly 
        and returns None when changing the weight of a valid face
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        die_new_weight = die.change_weight(1,5)
        expected = None
        self.assertEqual(die_new_weight, expected)
        
    def test_roll_die(self):
        '''
        PURPOSE: test whether roll_die method operates correctly 
        and returns a list with length equal to n_rolls
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die(['H', 'T'])
        outcome = die.roll_die(10)
        expected = len(range(10))
        self.assertEqual(len(outcome), expected)
    
    def test_current_faces_and_weights(self):
        '''
        PURPOSE: test whether current_faces_and_weights method 
        operates correctly and returns a pandas DataFrame
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die1 = Die(['H', 'T'])
        die2 = Die([1,2,3,4,5,6])
        die1_faces_and_weights = die1.current_faces_and_weights
        die2_faces_and_weights = die2.current_faces_and_weights
        expected1 = (type(die1_faces_and_weights) == type(die2_faces_and_weights))
        expected2 = (type(die1_faces_and_weights) == pd.core.frame.DataFrame)
        self.assertEqual(True, expected1, expected2)
        
    
    
    def test_init_Game(self):
        '''
        PURPOSE: ensure Game object is initialized correctly 
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die1 = Die([1,2,3,4,5,6])
        die2 = Die(['H', 'T'])
        self.assertRaises(Exception, lambda: Game([die1, die1, die2]))
    
    def test_play(self):
        '''
        PURPOSE: test whether play method operates correctly and 
        returns None
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        game = Game([die, die, die])
        play = game.play(20)
        expected = None
        self.assertEqual(play, expected)
        
    def test_show_invalid(self):
        '''
        PURPOSE: test whether show method raises an exception to the 
        user when incorrectly attempting to specify how the DataFrame
        should be returned (i.e., when inputting something other than 
        "wide"or "narrow")
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        game = Game([die, die, die])
        play = game.play(20)
        self.assertRaises(Exception, lambda: game.show('invalid'))
        
    def test_show_valid(self):
        '''
        PURPOSE: test whether show method operates correctly and returns
        a pandas DataFrame when correctly specifying how the DataFrame
        should be returned (in this case as "narrow)
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        game = Game([die, die, die])
        play = game.play(20)
        df = type(game.show('narrow'))
        expected = pd.core.frame.DataFrame
        self.assertEqual(df, expected)
        
        
        
    def test_init_Analyzer(self):
        '''
        PURPOSE: ensure Analyzer object is initialized correctly 
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        game = Game([die, die, die])
        play = game.play(20)
        analysis = Analyzer(game)
        self.assertTrue(str(type(analysis.__init__(game))) == "<class 'NoneType'>")
    
    def test_jackpot(self):
        '''
        PURPOSE: test whether jackpot method operates correctly and allows the 
        user to access the jackpot_df pandas DataFrame as a public attribute
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        game = Game([die, die, die])
        play = game.play(20)
        analysis = Analyzer(game)
        analysis.jackpot()
        df = type(analysis.jackpot_df)
        expected = pd.core.frame.DataFrame
        self.assertEqual(df, expected)
        
    def test_combo(self):
        '''
        PURPOSE: test whether combo method operates correctly and allows the 
        user to access the combo_df pandas DataFrame as a public attribute
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        game = Game([die, die, die])
        play = game.play(20)
        analysis = Analyzer(game)
        analysis.combo()
        df = type(analysis.combo_df)
        expected = pd.core.frame.DataFrame
        self.assertEqual(df, expected)
        
        
    def test_face_counts(self):
        '''
        PURPOSE: test whether face_counts method operates correctly and allows the 
        user to access the face_counts_df pandas DataFrame as a public attribute
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        die = Die([1,2,3,4,5,6])
        game = Game([die, die, die])
        play = game.play(20)
        analysis = Analyzer(game)
        analysis.face_counts()
        df = type(analysis.face_counts_df)
        expected = pd.core.frame.DataFrame
        self.assertEqual(df, expected)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)