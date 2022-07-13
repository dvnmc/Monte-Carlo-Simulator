import numpy as np
import pandas as pd
from collections import Counter

class Die():
    '''
    This class is used to create a die that has N sides, or “faces”, and W weights. 
    Additionally, the weights can be changed, and the die can be rolled to select a face.
    '''
    
    def __init__(self, faces):
        '''
        PURPOSE: initialize a Die object
    
        INPUTS
        faces    array of ints, floats, or strings
    
        OUTPUT
        None
        '''
        self.faces = faces
        self.weights = np.ones(len(self.faces))
        self.__privatedf = pd.DataFrame({'faces': self.faces, 
                                         'weights': self.weights})
        
    def change_weight(self, face_val, new_weight):
        '''
        PURPOSE: change the weight of a single side of a die object
    
        INPUTS
        face_val     int, float, or string      
        new_weight   int or float 
    
        OUTPUT
        None 
        '''
        self.face_val = face_val
        try:
            self.new_weight = float(new_weight)
        except ValueError:
            print('Please input a number of type int, float, or str.')
        if self.face_val not in self.faces:
            return 'This is not a valid face.'
        else:
            index = self.faces.index(self.face_val)
            self.weights[index] = new_weight
            self.__privatedf = pd.DataFrame({'faces': self.faces, 
                                             'weights': self.weights})
            
    def roll_die(self, n_rolls = 1):
        '''
        PURPOSE: roll the die one or more times
    
        INPUTS
        n_rolls      int  
    
        OUTPUT
        *not stored* list of ints
        '''
        self.n_rolls = n_rolls
        outcome = self.__privatedf.sample(weights = self.weights).values[0][0]
        if type(outcome) == np.float64:
            return [int(self.__privatedf.sample(weights = self.weights).\
                values[0][0]) for i in range(self.n_rolls)]
        else:
            return [self.__privatedf.sample(weights = self.weights).\
                values[0][0]for i in range(self.n_rolls)]
    
    def current_faces_and_weights(self):
        '''
        PURPOSE: show the die’s current set of faces and weights
    
        INPUTS
        None
    
        OUTPUT
        *private*  pd.DataFrame
        '''
        return self.__privatedf
    
    
class Game():
    '''
    This class is used to create a game that consists of rolling of one or more dice 
    of the same kind. The dice can be rolled one or more times. 
    '''
    
    def __init__(self, dice):
        '''
        PURPOSE: initialize a Game object 
    
        INPUTS
        dice     list of already instantiated similar Die objects
    
        OUTPUT
        None
        '''
        self.dice = dice
        for i in range(len(self.dice)):
            first = sorted(self.dice[0].current_faces_and_weights()['faces'].to_numpy())
            rest = sorted(self.dice[i].current_faces_and_weights()['faces'].to_numpy())
            if rest == first:
                self.dice = dice
            else:
                raise Exception('Please input dice with equivalent faces.')
                self.dice = []
        
    def play(self, n_rolls):
        '''
        PURPOSE: roll the dice a specified number of times
    
        INPUTS
        n_rolls  int
    
        OUTPUT
        None
        '''
        self.n_rolls = n_rolls
        outcomes = np.array([die.roll_die(n_rolls) for die in self.dice])
        index_labels = ['roll ' + str(x + 1) for x in range(n_rolls)]
        self.__privatedf = pd.DataFrame(index = index_labels)
        for i in range(len(self.dice)):
            self.__privatedf['die ' + str(i + 1)] = outcomes[i]
                  
    def show(self, wide_or_narrow = 'wide'):
        '''
        PURPOSE: show the user the results of the most recent play
        
        INPUTS
        wide_or_narrow   str (either "wide" or "narrow")
    
        OUTPUT           
        *private*        pd.DataFrame (either stacked or unstacked)        
        '''
        self.wide_or_narrow = wide_or_narrow
        if self.wide_or_narrow == 'wide':
            return self.__privatedf
        elif self.wide_or_narrow == 'narrow':
            return self.__privatedf.stack().to_frame('face')
        else:
            raise Exception('Enter either "wide" or "narrow" (defaults to "wide")')
            

class Analyzer():
    '''
    This class takes the results of a single game and computes various descriptive statistical properties.
    '''
    
    def __init__(self, game):
        '''
        PURPOSE: initialize an Analyzer object

        INPUTS
        game     already instantiated Game object

        OUTPUT
        None
        '''
        self.game = game
    
    def jackpot(self):
        '''
        PURPOSE: compute how many times the game resulted in all identical faces
    
        INPUTS
        None
    
        OUTPUT
        total_jackpots   int
        '''
        jackpots = []
        rows = []
        for i in range(len(self.game.show())):
            row = list(self.game.show().iloc[i])
            rows.append(row)
            if len(set(rows[i])) == 1:
                jackpots.append(1)
            else:
                jackpots.append(0)
        index_labels = ['roll ' + str(x + 1) for x in range(self.game.n_rolls)]
        self.jackpot_df = pd.DataFrame(index = index_labels)
        self.jackpot_df['jackpot'] = jackpots
        self.total_jackpots = len([x for x in jackpots if x == 1])
        return self.total_jackpots
        
    def combo(self):
        '''
        PURPOSE: compute the distinct combinations of faces rolled, along with their counts
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        rows = sorted([tuple(self.game.show().iloc[x]) for x in range(self.game.n_rolls)])
        combo_keys = Counter(rows).keys()
        count_vals = Counter(rows).values()
        self.combo_df = pd.DataFrame({
            'faces': combo_keys, 
            'count': count_vals})
        index_labels = ['combo ' + str(x + 1) for x in range(len(combo_keys))]
        self.combo_df.index = index_labels
    
    def face_counts(self):
        '''
        PURPOSE: compute how many times a given face is rolled in each event
    
        INPUTS
        None
    
        OUTPUT
        None
        '''
        rows = [list(self.game.show().iloc[x]) for x in range(self.game.n_rolls)]
        index_labels = ['roll ' + str(x + 1) for x in range(self.game.n_rolls)]
        count = [Counter(x) for x in rows]
        self.face_counts_df = pd.DataFrame.from_dict(count)
        self.face_counts_df.index = index_labels
        self.face_counts_df = self.face_counts_df.fillna(0)
        columns_sorted = sorted(self.face_counts_df.columns)
        self.face_counts_df = self.face_counts_df.reindex(columns=columns_sorted)
        for i in range(len(columns_sorted)):
            self.face_counts_df[i+1] = self.face_counts_df[i+1].apply(np.int64)
        faces = ['faces']
        self.face_counts_df.columns = pd.MultiIndex.from_tuples(
            list(zip(faces*len(columns_sorted), columns_sorted)))