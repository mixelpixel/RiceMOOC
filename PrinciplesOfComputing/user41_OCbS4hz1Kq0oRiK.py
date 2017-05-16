"""
#- "Zombie Apocalypse" by pdk
#- For Coursera: Rice U. Principles of Computing pt.2
#---#----1----#----2----#----3----#----4----#----5----#----6----#----7-2--#----8----#----91234567100
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui


EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    zombie pursuit of human on grid with obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Simulation of given size with given obstacles, humans, and zombies
        """

        self._grid_width = grid_width
        self._grid_height = grid_height
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """

        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """

        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        max_dist = self._grid_width * self._grid_height
        distance_field = [[max_dist for dummy_item in row] for row in self._cells]

        boundary = poc_queue.Queue()

        if entity_type is ZOMBIE:
            for item in self._zombie_list:
                boundary.enqueue(item)
        elif entity_type is HUMAN:
            for item in self._human_list:
                boundary.enqueue(item)
        else:
            return

        for item in boundary:
            visited.set_full(item[0], item[1])
            distance_field[item[0]][item[1]] = 0

        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            neighbour_cells = self.four_neighbors(current_cell[0], current_cell[1])
            for neighbour_cell in neighbour_cells:
                # check whether the cell has not been visited and is passable
                if visited.is_empty(neighbour_cell[0], neighbour_cell[1]) and self.cell_is_passible(neighbour_cell):
                    visited.set_full(neighbour_cell[0], neighbour_cell[1])
                    boundary.enqueue(neighbour_cell)
                    distance_field[neighbour_cell[0]][neighbour_cell[1]] = distance_field[current_cell[0]][current_cell[1]] + 1

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """

        idx = 0
        for human in self.humans():
            neighbouring_cells = self.eight_neighbors(human[0], human[1])
            starting_distance = zombie_distance_field[human[0]][human[1]]
            best_distance = 0
            best_cells = []

            for row, distances in enumerate(zombie_distance_field):
                for col, distance in enumerate(distances):
                    cell = (row, col)
                    if self.cell_is_passible(cell) and cell in neighbouring_cells and distance > best_distance:
                        best_distance = distance

            if best_distance is starting_distance:
                continue

            for cell in neighbouring_cells:
                if zombie_distance_field[cell[0]][cell[1]] is 0 or self.cell_is_passible(cell) is not True:
                    continue
                if zombie_distance_field[cell[0]][cell[1]] is best_distance:
                    best_cells.append(cell)

            if len(best_cells) > 0:
                self._human_list[idx] = random.choice(best_cells)
            idx += 1

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """

        idx = 0
        for zombie in self.zombies():
            neighbouring_cells = self.four_neighbors(zombie[0], zombie[1])
            starting_distance = human_distance_field[zombie[0]][zombie[1]]
            best_distance = starting_distance
            best_cells = []

            for row, values in enumerate(human_distance_field):
                for col, distance in enumerate(values):
                    cell = (row, col)
                    if self.cell_is_passible(cell) and cell in neighbouring_cells and distance < best_distance:
                        best_distance = distance

            if best_distance is starting_distance:
                continue

            for cell in neighbouring_cells:
                if self.cell_is_passible(cell) is not True:
                    continue
                if human_distance_field[cell[0]][cell[1]] is best_distance:
                    best_cells.append(cell)

            if len(best_cells) > 0:
                self._zombie_list[idx] = random.choice(best_cells)
            idx += 1

    def cell_is_passible(self, cell):
        """
        Whether or not a cell is passible.
        """

        return self._cells[cell[0]][cell[1]] is EMPTY


poc_zombie_gui.run_gui(Apocalypse(30, 60))

#import user41_l4xt1oBRqy_5 as tests
#tests.run_suite(Apocalypse)