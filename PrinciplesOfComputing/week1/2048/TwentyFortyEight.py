'''
#- "Clone of 2048 game" by pdk, http://2048game.com/
#- started on 160601@2300; finished on ??????@????
#- For Coursera: Rice U. Principles of Computing pt.1, week1
#--------1---------2---------3---------4---------5---------6---------7-2-------8---------91234567100
'''

#import poc_2048_gui
import Test_Suite_2048
import random

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    '''
    Helper function that merges a single row (or column) in 2048.
    '''
    # slide non-zeroes
    slide_list = [item for item in line if item != 0]
    while len(line) > len(slide_list):
        slide_list.append(0)
    # merge adjacent equals
    merge_list = []
    for number in xrange(len(slide_list[:-1])):
        if slide_list[number] == slide_list[number + 1]:
            merge_list.append(slide_list[number] + slide_list[number + 1])
            slide_list[number + 1] = 0
        else:
            merge_list.append(slide_list[number])
    merge_list.append(slide_list[-1])
    # slide the merged list
    result_list = [item for item in merge_list if item != 0]
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
        self.reset()
        self._initial_tile_cells = {
            UP: [(0, col) for col in xrange(grid_width)],
            DOWN: [(grid_height - 1, col) for col in xrange(grid_width)],
            LEFT: [(row, 0) for row in xrange(grid_height)],
            RIGHT: [(row, grid_width - 1) for row in xrange(grid_height)]
        }

    def reset(self):
        """
        Reset the game so the grid is empty
        except for two initial tiles.
        """
        self._grid = [[0 for dummy_col in xrange(self.get_grid_width())] \
                      for dummy_row in xrange(self.get_grid_height())]
        self.new_tile()
        self.new_tile()
##        return self._grid

    def __str__(self):
        """Return a string representation of the grid"""
        string = str('[' + '\n'.join(map(str, self._grid)) + ']')
        return string
##        return str(self._grid)

    def get_grid_height(self):
        """Get the height of the board; ROWS."""
        return self._grid_height

    def get_grid_width(self):
        """Get the width of the board; COLUMNS."""
        return self._grid_width

##    def move(self, direction):
##        """
##        Move all tiles in the given direction and add
##        a new tile if any tiles moved.
##        """
##        moved = False
##        for_comparison = [list(row) for row in self._grid]
##        if direction == LEFT:
##            new_rows = []
##            for row in self._grid:
##                new_rows.append(merge(row))
##                self._grid = new_rows
##        elif direction == UP:
##            new_rows = []
##            for col in [[self.get_tile(row, col) for row in range(self.get_grid_height())] for col in range(self.get_grid_width())]:
##                new_rows.append(merge(col))
##            col_to_rows = zip(*new_rows)
##            new_grid = map(list, col_to_rows)
##            self._grid = new_grid
##        elif direction == RIGHT:
##            reverse_rows = []
##            for row in self._grid:
##                print '**' + str(self._grid) + '**'
##                reverse_rows.append(row[::-1])
##                print reverse_rows
##            rev_merged_rows = []
##            for row in reverse_rows:
##                rev_merged_rows.append(merge(row))
##            rev_rev_merged_rows = [i[::-1] for i in rev_merged_rows]
##            self._grid = rev_rev_merged_rows
##        elif direction == DOWN:
##            print str(self._grid)
##            new_cols = map(list, zip(*self._grid))
##            print new_cols
##            reverse_cols = []
##            rev_merge_cols = []
##            merge_reverse_cols = []
##            for col in new_cols:
##                reverse_cols.append(col[::-1])
##            print reverse_cols
##            for row in reverse_cols:
##                merge_reverse_cols.append(merge(row))
##            print merge_reverse_cols
##            for col in merge_reverse_cols:
##                rev_merge_cols.append(col[::-1])
##            print rev_merge_cols
##            col_to_rows = map(list, zip(*rev_merge_cols))
##            print col_to_rows
##            self._grid = col_to_rows
##        if for_comparison != self._grid:
##            moved = True
##        if moved:
##            self.new_tile()

    def move(self, direction):
        moved = False
        for_comparison = [list(row) for row in self._grid]
        if direction in [UP, DOWN]:
            distance = self.get_grid_height()
        elif direction in [LEFT, RIGHT]:
            distance = self.get_grid_width()
        for cell in self._initial_tile_cells[direction]:
            tmp_list = self.traverse_grid(cell, OFFSETS[direction], distance)
            merged_list = merge(tmp_list)
            if merged_list != tmp_list:
                changed = True
            self.change_grid(cell, OFFSETS[direction], merged_list)




##        if for_comparison != self._grid:
##            moved = True
        if moved:
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
            if random.random() <= 0.9:
                self._tile = 2
                self.set_tile(row, col, self._tile)
            else:
                self._tile = 4
                self.set_tile(row, col, self._tile)
        else:
            self.new_tile() #This might not be the best method to deal with !=0?

    def set_tile(self, row, col, value):
        """Set the tile at position row, col to have the given value."""
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """Return the value of the tile at position row, col."""
        return self._grid[row][col]


    def get_rows(self):
        '''returns each row'''
        for row in xrange(len(self._grid)):
            print 'row #' + str(row) + ' = ' + str(self._grid[row])

    def get_columns(self):
        '''returns each column'''
        each_column = [[self.get_tile(row, col) for row in xrange(self.get_grid_height())] for col in xrange(self.get_grid_width())]
        for col in xrange(self.get_grid_width()):
            print 'col.#' + str(col) + ' = ' + str(each_column[col])

    def traverse_grid(self, start_cell, direction, num_steps):
        for step in xrange(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
        return self._grid[row][col]

    def change_grid(self, start_cell, direction, new_list):
        """
        Helper function that changes the value of row or colmun to new_list 
        """
        for step in range(len(new_list)):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            self.set_tile(row, col, new_list[step])

#RICE = TwentyFortyEight(4, 4)
#poc_2048_gui.run_gui(RICE)




TEST1 = TwentyFortyEight(4, 6)
print 'TEST1\n', TEST1
TEST1.get_rows()
TEST1.get_columns()
print TEST1._initial_tile_cells
####TEST1.move(LEFT)
####print 'TEST1.move(LEFT)\n', TEST1.move(LEFT)
####print 'TEST1\n', TEST1
####print 'TEST1.move(UP)\n', TEST1.move(UP)
####print 'TEST1\n', TEST1
##print 'TEST1.move(RIGHT)\n', TEST1.move(RIGHT)
##print 'TEST1 after RIGHT\n', TEST1
##print 'TEST1.move(DOWN)\n', TEST1.move(DOWN)
##print 'TEST1 after DOWN\n', TEST1
##print
###poc_2048_gui.run_gui(TEST1)
####Test_Suite_2048.run_suite(TEST1)
####
####
##TEST2 = TwentyFortyEight(3, 3)
####Test_Suite_2048.run_suite(TEST2)
##print 'TEST2\n', TEST2
##print
####
##TEST3 = TwentyFortyEight(2, 2)
##Test_Suite_2048.run_suite(TEST3)
##print 'TEST3\n', TEST3
##print
####
##TEST4 = TwentyFortyEight(2, 1)
##print 'TEST4\n', TEST4
##print
####print type(TEST4.reset())
##
####TEST5 = TwentyFortyEight(1, 1)
####print 'TEST5\n', TEST5
####print
##
##

#MERGE TESTS
##print 'merge([0, 0, 0, 0, 0, 0]) >>', merge([0, 0, 0, 0, 0, 0])
##print 'merge([2,0,2,2]) >>', merge([2,0,2,2])
##TEST1 = [2, 0, 2, 2]
##print "list to be merged:", TEST1
##print 'length of list to be merged', len(TEST1)
##print 'EXECUTING THE FUNCTION:\n', merge(TEST1)
##print
##TEST2 = [4, 0, 2, 0, 0, 4, 2]
##print "list to be merged:", TEST2
##print 'length of list to be merged', len(TEST2)
##print 'EXECUTING THE FUNCTION:\n', merge(TEST2)
##print
##TEST3 = [0, 0, 0, 2, 0, 0, 2, 0, 0, 4, 4, 2]
##print "list to be merged:", TEST3
##print 'length of list to be merged', len(TEST3)
##print 'EXECUTING THE FUNCTION:\n', merge(TEST3)
##print
##TEST4 = [0]
##print "list to be merged:", TEST4
##print 'length of list to be merged', len(TEST4)
##print 'EXECUTING THE FUNCTION:\n', merge(TEST4)
##print
##test5 = [0, 0, 0, 0, 0, 0]
##print merge(test5)
##test6 = [2,2,2,2,2,2]
##print merge(test6)
##print merge(test6)
