'''
#- "Clone of 2048 game" by pdk, http://2048game.com/
#- started on 160601@2300; finished on ??????@????
#- For Coursera: Rice U. Principles of Computing pt.1, week1
#--------1---------2---------3---------4---------5---------6---------7-2-------8---------91234567100
'''

import poc_2048_gui
#import Test_Suite_2048
import random

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
    Helper function that merges a single row (or column) in 2048.
    '''
    #CURRENTLY ONLY SLIDES A LIST IN DIRECTION
    # ADD FUNCTIONALITY TO SLIDE COLUMNS UP OR DOWN
    # AND ROWS LEFT OR RIGHT???????????????????????

##    print line, 'merge() function argument parameter'

    # slide non-zeroes
    slide_list = []
    poop = [slide_list.append(item) for item in line if item != 0]
    del(poop)
    while len(line) > len(slide_list):
        slide_list.append(0)
##    print slide_list, 'slide to the left over zeros'

    # merge adjacent equals
    merge_list = []
    for number in range(len(slide_list[:-1])):
        if slide_list[number] == slide_list[number + 1]:
            merge_list.append(slide_list[number] + slide_list[number + 1])
            slide_list[number + 1] = 0
        else:
            merge_list.append(slide_list[number])
    merge_list.append(slide_list[-1])
##    print merge_list, 'if any adjacent duplicates, merged leaving a zero'


    # slide the merged list
    result_list = []
    poop = [result_list.append(item) for item in merge_list if item != 0]
    del(poop)
    while len(line) > len(result_list):
        result_list.append(0)
##    print result_list, 'merged list, slid over zeros with padding'

    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty
        except for two initial tiles.
        """
        self._grid = [[0 for dummy_col in xrange(self.get_grid_width())] \
                      for dummy_row in xrange(self.get_grid_height())]
        print '**inside reset():\n', self, '**'
        self.new_tile()
        self.new_tile()
        print '**inside reset():\n', self, '**'
        return self._grid

    def __str__(self):
        """Return a string representation of the grid"""
        string = str('[' + '\n'.join(map(str, self._grid)) + ']')
        return string

    def get_grid_height(self):
        """Get the height of the board; ROWS."""
        return self._grid_height

    def get_grid_width(self):
        """Get the width of the board; COLUMNS."""
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        change = False
        new_rows = []
        if direction == LEFT:
            for row in self._grid:
                new_rows.append(merge(row))
                self._grid = new_rows
        elif direction == UP:
            for col in [[self.get_tile(row, col) for row in range(self.get_grid_height())] for col in range(self.get_grid_width())]:
                new_rows.append(merge(col))
##                print new_rows
            col_to_rows = zip(*new_rows)
            new_poop = map(list, col_to_rows)
##            print new_poop
            self._grid = new_poop
        elif direction == RIGHT:
            reverse_rows = []
            for row in self._grid:
                row.reverse()
                reverse_rows.append(row)
##                print reverse_rows
            snoopy = []
            for row in reverse_rows:
                snoopy.append(merge(row))
##                print snoopy
            for snoop in snoopy:
                snoop.reverse()
##                print snoopy
            self._grid = snoopy
##            print self._grid
        elif direction == DOWN:
            for col in [[self.get_tile(row, col) for row in range(self.get_grid_height())] for col in range(self.get_grid_width())]:
                new_rows.append(merge(col))
##                print new_rows
            reverse_rows = []
            for row in new_rows:
                row.reverse()
                reverse_rows.append(row)
            col_to_rows = zip(*reverse_rows)
            new_poop = map(list, col_to_rows)
            self._grid = new_poop
        if change:
            self.new_tile()



    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = random.randrange(0, self.get_grid_height())
        col = random.randrange(0, self.get_grid_width())
        # if there's no zero anywhere on the grid AND
        # no adjacent equal tiles:
            #then game over...
        if self.get_tile(row, col) == 0:
            print 'randomly selected: row', str(row), 'col', str(col), 'value =', self.get_tile(row, col)
            if random.random() <= 0.9:
                self._tile = 2
                print 'now value = 2 @row' + str(row) + ', col' + str(col)
                self.set_tile(row, col, self._tile)
            else:
                self._tile = 4
                print 'now value = 4 @row' + str(row) + ', col' + str(col)
                self.set_tile(row, col, self._tile)
        else:
            print 'new_tile(): self.get_tile()=', self.get_tile(row, col), '& !=0 @row:', str(row), '&col:', str(col), '>>>else: recursion'
            self.new_tile() #This might not be the best method to deal with !=0?

    def set_tile(self, row, col, value):
        """Set the tile at position row, col to have the given value."""
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """Return the value of the tile at position row, col."""
        return self._grid[row][col]

    def get_rows(self):
        '''returns each row'''
        for row in range(len(self._grid)):
            print 'row #' + str(row) + ' = ' + str(self._grid[row])

    def get_columns(self):
        '''returns each column'''
        each_column = [[self.get_tile(row, col) for row in range(self.get_grid_height())] for col in range(self.get_grid_width())]
        for col in range(self.get_grid_width()):
            print 'col.#' + str(col) + ' = ' + str(each_column[col])



RICE = TwentyFortyEight(4, 4)
poc_2048_gui.run_gui(RICE)