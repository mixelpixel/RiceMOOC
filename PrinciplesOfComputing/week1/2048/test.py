h = 4 # = to number of ROWS
w = 6 # = to number of COLUMNS

##grid_list = []
##for row in xrange(h):
##    grid_list.append(list())
##for row in xrange(h):
##    for col in xrange(w):
##        grid_list[row].append(0)
##print grid_list
##print
##
##grid_list = []
##for row in xrange(h):
##    grid_list.append(list())
##    for col in xrange(w):
##        grid_list[row].append(0)
##print grid_list
##print

##grid = [[] for row in xrange(h)]
##print grid
##for row in xrange(h):
##    for col in xrange(w):
##        grid[row].append(0)
##print grid
##
##grid = [[] for row in xrange(h)]
##grid[0].append(0)
##grid[0].append(0)
##grid[0].append(0)
##grid[0].append(0)
##grid[0].append(0)
##grid[0].append(0)
##print grid
##
##grid = [[] for row in xrange(h)]
##grid = [[0 for col in xrange(w)]\
##        for row_list in grid]
##print grid
##

##grid = [[0 for col in xrange(w)] for row in xrange(h)]
##grid = [[0 for col in xrange(w)] for row in xrange(h)]

grid = [[0] * w for _ in range(h)]
print grid
print id(grid[0])
print id(grid[1])
print id(grid[2])
print id(grid[3])
