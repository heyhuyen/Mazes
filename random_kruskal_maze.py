"""
Randomized Kruskal's Minimum Spanning Tree Algorithm for Maze Generation.
"""

import sys
from random import shuffle

class Maze:
    def __init__(self, (num_rows, num_cols)):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cells = range(num_rows * num_cols)
        self.sets = []
        self.walls = []
        self.setup_sets_and_walls()
        assert len(self.walls) == (self.num_rows - 1) * self.num_cols + (self.num_cols - 1) * self.num_rows

    def setup_sets_and_walls(self):
        for cell in self.cells:
            self.sets.append(set([cell]))
            if not self.in_last_row(cell):
                self.add_south_wall(cell)
            if not self.in_last_col(cell):
                self.add_east_wall(cell)

    def in_last_row(self, cell):
        return  cell / (self.num_cols * (self.num_rows - 1)) == 1

    def in_last_col(self, cell):
        return cell % self.num_cols == self.num_cols - 1

    def add_south_wall(self, cell):
        self.walls.append(Wall(self.cells[cell], self.cells[cell + self.num_cols]))

    def add_east_wall(self, cell):
        self.walls.append(Wall(self.cells[cell], self.cells[cell + 1]))

    def build(self):
        wall_indices = range(len(self.walls))
        shuffle(wall_indices)
        for index in wall_indices:
            wall = self.walls[index]
            for s in self.sets:
                if wall.a in s:
                    a_set = s
                if wall.b in s:
                    b_set = s
            if a_set.isdisjoint(b_set):
                self.sets.append(a_set.union(b_set))
                self.sets.remove(a_set)
                self.sets.remove(b_set)
                wall.removed = True

    def __repr__(self):
        result = ""
        result += " _" * self.num_cols + "\n|" # top border + next row's left border
        last_row = range((self.num_rows - 1) * self.num_cols, self.num_rows * self.num_cols)
        for wall in self.walls:
            if self.in_last_row(wall.a):
                result += "_" # bottom border
            if wall.removed:
                result += " " # removed wall
            elif wall.is_horizontal:
                result += "_" # horizontal wall
            else:
                result += "|" # vertical wall
            if self.in_last_col(wall.a):
                result += "|\n|" # row's right border + next row's left border
        result += "_|" # SE corner
        return result

class Wall:
    def __init__(self, a, b):
        self.removed = False
        self.a = a
        self.b = b
        self.is_horizontal = True if self.b - self.a > 1 else False

    def __repr__(self):
        return repr((self.removed, self.a, self.b))

DEFAULT_ROWS = 2
DEFAULT_COLS = 3

if __name__ == "__main__":
    if len(sys.argv) == 1:
        maze = Maze((DEFAULT_ROWS, DEFAULT_COLS))
    elif len(sys.argv) == 3:
        num_rows, num_cols = [int(x) for x in sys.argv[1:]]
        if num_rows < 2 or num_cols < 2:
            print "Maze must be at least 2 x 2."
            sys.exit()
        maze = Maze((num_rows, num_cols))
    else:
        print "Usage: random_kruskal_maze.py num_rows num_cols"
        sys.exit()

    maze.build()
    print maze
