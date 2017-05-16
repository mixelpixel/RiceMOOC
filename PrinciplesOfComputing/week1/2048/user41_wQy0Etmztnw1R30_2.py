'''
#- "Clone of 2048 game" by pdk
#- http://2048game.com/
#- started on 160601@2300; finished on ??????@????
#- For Coursera: Rice U. Principles of Computing pt.1, week1
#--------1---------2---------3---------4---------5---------6---------7-2-------8---------91234567100
'''

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    '''
    Helper function that merges a single row or column in 2048.
    '''

    #This function slides nonzeros to the left. Then any adjacent and
    #equal integers are summed to the left index of the two while also
    #replacing the second integer (index + 1) of the two integers with
    #a zero (aka, 'merged'). Then nonzeros are again slid to the left
    #while returning a list of the same length as the original by'
    #padding zeros on the right.

    # - slide non-zeroes
    slide_list = []
    [slide_list.append(item) for item in line if item != 0]

    # - merge adjacent equals
    merge_list = []
    for number in range(len(slide_list[:-1])):
        if slide_list[number] == slide_list[number + 1]:
            merge_list.append(slide_list[number] + slide_list[number + 1])
            slide_list[number + 1] = 0
        else:
            merge_list.append(slide_list[number])
    merge_list.append(slide_list[-1])

    # - slide the merged list
    result_list = []
    [result_list.append(item) for item in merge_list if item != 0]
    while len(line) > len(result_list):
        result_list.append(0)

    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_list = [[] for row in xrange(self._grid_height)]
        for row in xrange(self._grid_height):
#            grid_list.append(list())
            for col in xrange(self._grid_width):
                grid_list[row].append([row, col])
        return str('GRID COORDINATES:\n' + '\n'.join(map(str, grid_list))\
                   + '\nGAME BOARD VALUES:\nTBD')

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0

#RICE = TwentyFortyEight(4, 4)
#poc_2048_gui.run_gui(RICE)

TEST1 = TwentyFortyEight(4, 6)
print TEST1
poc_2048_gui.run_gui(TEST1)
