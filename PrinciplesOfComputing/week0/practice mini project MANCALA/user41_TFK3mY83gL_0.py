'''
"SOLITAIRE MANCALA" by pdk
started on 160531@1600start; finished on 100631@2300
For Coursera: Rice U. Principles of Computing pt.1
#---#----1----#----2----#----3----#----4----#----5----#----6----#----7-2--#----8----#----91234567100
Solitaire Mancala: Tchoukaillon - based on Mancala, Kallah, etc.
e.g. http://play-mancala.com/
6 houses, 1 store, variable number of seeds per house at start.
Legal moves: only those where the last seed ends up in the Store.
Suggestion for play: "Given the choice of two legal moves, the player
should always choose the move whose house is closer to the store"
per:
https://www.coursera.org/learn/principles-of-computing-1/supplement/HwJPF/practice-mini-project-solitaire-mancala
'''
"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._game = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        for config in configuration:
            self._game.append(config)
        self._game = list(configuration)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return self._game
##        return reverse(list(self._game))
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._game[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        if sum(self._game[1:]) == 0:
            return True
        else:
            return False
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num != 0 and self._game[house_num] == house_num:
            return True
        else:
            return False

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            self._game[house_num] = 0
            for seed in range(house_num):
                self._game[seed] +=1
#            return 'a legal move!'
#        else:
#            return 'not a legal move!'

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        shorty = False
        check_house = 1
        while shorty != True and check_house < len(self._game):
            if self.is_legal_move(check_house):
                shorty = True
            else:
                check_house +=1
        if shorty:
            return check_house
        else:
            return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        list_of_moves = []
        check_moves = SolitaireMancala()
        check_moves.set_board(self._game)
#        print 'duplicate', check_moves.__str__()
        move = check_moves.choose_move()
#        print 'move this house', move
        while move != 0:
            check_moves.apply_move(move)
            list_of_moves.append(move)
            move = check_moves.choose_move()
#            print 'move each house in this order', list_of_moves
        return list_of_moves


# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    # add more tests here
    
test_mancala()


# Import GUI code once you feel your code is correct
import poc_mancala_gui
poc_mancala_gui.run_gui(SolitaireMancala())
