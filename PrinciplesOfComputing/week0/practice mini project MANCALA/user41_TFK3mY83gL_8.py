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

Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
'''

#import poc_mancala_gui

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._game = [0]
#        self._game = []
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
#        for config in configuration:
#            self._game.append(config)
        self._game = list(configuration)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        left_to_right = list(self._game)
        left_to_right.reverse()
        return str(left_to_right)
    
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
            return 'a legal move!'
        else:
            return 'not a legal move!'

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
        print '#duplicate', check_moves.__str__()
        move = check_moves.choose_move()
        print '#move this house', move
        while move != 0:
            check_moves.apply_move(move)
            list_of_moves.append(move)
            move = check_moves.choose_move()
            print '#move each house in this order', list_of_moves
            print '#then move this house', move
        return list_of_moves


# Create tests to check the correctness of your code
config = [0, 1, 1, 3, 0, 0, 0]
x = SolitaireMancala()
print 'initialize board', x.__str__()
x.set_board(config)
print 'set board', x.__str__()
print 'seeds in house 1 =', x.get_num_seeds(1)
print 'seeds in house 2 =', x.get_num_seeds(2)
print 'seeds in house 3 =', x.get_num_seeds(3)
print 'seeds in house 4 =', x.get_num_seeds(4)
print 'seeds in house 5 =', x.get_num_seeds(5)
print 'seeds in house 6 =', x.get_num_seeds(6)
print
print 'is game won: ' + str(x.is_game_won())
print
print 'legal to move house 1?', x.is_legal_move(1)
print 'legal to move house 2?', x.is_legal_move(2)
print 'legal to move house 3?', x.is_legal_move(3)
print 'legal to move house 4?', x.is_legal_move(4)
print 'legal to move house 5?', x.is_legal_move(5)
print 'legal to move house 6?', x.is_legal_move(6)
print
print 'apply move to house 6?', x.apply_move(6)
print 'apply move to house 1?', x.apply_move(1)
print x.__str__()
print 'apply move to house 3?', x.apply_move(3)
print x.__str__()
print 'apply move to house 1?', x.apply_move(1)
print x.__str__()
print 'apply move to house 2?', x.apply_move(2)
print x.__str__()
print 'apply move to house 1?', x.apply_move(1)
print x.__str__()
print
print 'is game won:', x.is_game_won()
print
config = [0, 1, 1, 3, 0, 0, 0]
x = SolitaireMancala()
print 'initialize board', x.__str__()
x.set_board(config)
print 'set board', x.__str__()
print 'choose house to move:', x.choose_move()
print 'apply move to house 1?', x.apply_move(x.choose_move())
print x.__str__()
print 'is game won:', x.is_game_won()
print 'choose house to move:', x.choose_move()
print 'apply move to house 3?', x.apply_move(x.choose_move())
print x.__str__()
print 'is game won:', x.is_game_won()
print 'choose house to move:', x.choose_move()
print 'apply move to house 1?', x.apply_move(x.choose_move())
print x.__str__()
print 'is game won:', x.is_game_won()
print 'choose house to move:', x.choose_move()
print 'apply move to house 2?', x.apply_move(x.choose_move())
print x.__str__()
print 'is game won:', x.is_game_won()
print 'choose house to move:', x.choose_move()
print 'apply move to house 1?', x.apply_move(x.choose_move())
print x.__str__()
print 'is game won:', x.is_game_won()
print 'choose house to move:', x.choose_move()
print
config = [0, 1, 1, 3, 0, 0, 0]
x = SolitaireMancala()
print 'initialize board', x.__str__()
x.set_board(config)
print 'set board', x.__str__()
print
print x.plan_moves()
print 'done with my tests'
print


#poc_mancala_gui.run_gui(SolitaireMancala())


#"""
#GUI component of Mancala Solitaire
#"""
#
#import random
#import simplegui
#
## Game and canvas constants
## Focus on boards with six houses and one store
#
#BOARD_SIZE = 7
#HOUSE_NUM = 120
#TEXT_OFFSET = [0.3 * HOUSE_NUM, 0.7 * HOUSE_NUM]
#CANVAS_SIZE = [BOARD_SIZE * HOUSE_NUM, HOUSE_NUM]
#
## all winnable games for six houses
#WINNABLE_BOARDS = [[0, 0, 0, 0, 2, 4, 6], 
#                    [0, 0, 0, 2, 4, 0, 0], 
#                    [0, 0, 1, 1, 3, 5, 0], 
#                    [0, 0, 1, 3, 0, 0, 0], 
#                    [0, 0, 1, 3, 2, 4, 6], 
#                    [0, 0, 2, 0, 0, 0, 0], 
#                    [0, 0, 2, 0, 2, 4, 6], 
#                    [0, 0, 2, 2, 4, 0, 0], 
#                    [0, 1, 0, 0, 0, 0, 0], 
#                    [0, 1, 0, 0, 2, 4, 6], 
#                    [0, 1, 0, 2, 4, 0, 0], 
#                    [0, 1, 1, 1, 3, 5, 0], 
#                    [0, 1, 1, 3, 0, 0, 0], 
#                    [0, 1, 1, 3, 2, 4, 6], 
#                    [0, 1, 2, 0, 0, 0, 0], 
#                    [0, 1, 2, 0, 2, 4, 6], 
#                    [0, 1, 2, 2, 4, 0, 0]]
#
#
#class MancalaGUI:
#    """
#    Container for interactive content
#    """    
#
#    def __init__(self, game):
#        """ 
#        Initializer to create frame, sets handlers and initialize game
#        """
#        self._frame = simplegui.create_frame("Mancala Solitaire", 
#                                            CANVAS_SIZE[0], CANVAS_SIZE[1])
#        self._frame.set_canvas_background("White")
#        self._frame.set_draw_handler(self.draw)
#        self._frame.add_button("New board", self.new_board, 200)
#        self._frame.add_button("Restart board", self.restart_board, 200)
#        self._frame.add_button("Make move", self.make_move, 200)
#        self._frame.set_mouseclick_handler(self.click_move)
#        
#        # fire up game and frame
#        self._game = game
#        self.new_board()
#        
#    def start(self):
#        """
#        Start the GUI
#        """
#        self._frame.start()
#        
#    def restart_board(self):
#        """
#        Restart the game with the current configuration
#        """
#        self._game.set_board(self.start_board)
#                   
#    def new_board(self):
#        """
#        Restart the game with a new winnable baord
#        """
#        self.start_board = random.choice(WINNABLE_BOARDS)
#        self.restart_board()
#    
#    def make_move(self):
#        """
#        Compute and apply next move for solver
#        """
#        self._game.apply_move(self._game.choose_move())    
#        
#    def click_move(self, pos):
#        """
#        Update game based on mouse click
#        """
#        move = (BOARD_SIZE - 1) - pos[0] // HOUSE_NUM
#        self._game.apply_move(move)    
#        
#    def draw(self, canvas):
#        """
#        Handler for draw events, draw board
#        """
#        configuration = [self._game.get_num_seeds(house_num) for house_num in range(BOARD_SIZE)]
#        current_text_pos = [(BOARD_SIZE - 1) * HOUSE_NUM + TEXT_OFFSET[0], TEXT_OFFSET[1]]
#        current_line_pos = [(BOARD_SIZE - 1) * HOUSE_NUM, 0]
#        
#        if self._game.is_game_won():
#            store_color = "LightGreen"
#        else:
#            store_color = "Pink"
#        
#        canvas.draw_polygon([current_line_pos, 
#                             [current_line_pos[0] + HOUSE_NUM, current_line_pos[1]],
#                             [current_line_pos[0] + HOUSE_NUM, current_line_pos[1] + HOUSE_NUM],
#                             [current_line_pos[0], current_line_pos[1] + HOUSE_NUM]], 
#                            3, "Black", store_color)
#        
#        for num_seeds in configuration:
#            canvas.draw_text(str(num_seeds), current_text_pos, 0.5 * HOUSE_NUM, "Black")
#            canvas.draw_line(current_line_pos, [current_line_pos[0], 
#                                                current_line_pos[1] + HOUSE_NUM], 2, "Black")
#            current_text_pos[0] -= HOUSE_NUM
#            current_line_pos[0] -= HOUSE_NUM
#
#def run_gui(game):
#    """
#    Run GUI with given game
#    """
#    gui = MancalaGUI(game)
#    gui.start()








#def test_mancala():
#    """
#    Test code for Solitaire Mancala
#    """
#    
#    my_game = SolitaireMancala()
#    print "Testing init - Computed:", my_game, "Expected: [0]"
#    
#    config1 = [0, 0, 1, 1, 3, 5, 0]    
#    my_game.set_board(config1)   
#    
#    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
#    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
#    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
#    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
#
#    # add more tests here
#    
#test_mancala()
#
#
## Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())
