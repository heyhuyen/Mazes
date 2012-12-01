import time
import sys
from random import choice

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N E S W
OPPOSITE= { NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}

class Maze:
    def __init__(self, rows, cols):
        self.nrows = rows
        self.ncols = cols
        self.cells = []
        self.unvisited = []
        self.setup_cells()
        self.start = (0,0)

    def setup_cells(self):
        for row in range(self.nrows):
            new_row = []
            for col in range(self.ncols):
                new_row.append([1]*4 + [0]) # [ N E S W]
                self.unvisited.append((row, col))
            self.cells.append(new_row)

    def build(self):
        back_stack = []
        self.start = choice(self.unvisited)
        current = self.start
        self.visit_cell(current)
        while len(self.unvisited) > 0:
            unvisited_neighbors = self.get_unvisited_neighbors(current)
            if len(unvisited_neighbors) > 0:
                neighbor = choice(unvisited_neighbors)
                back_stack.append(current)
                self.remove_wall_between(current, neighbor)
                current = neighbor
                self.visit_cell(current)
            elif len(back_stack) > 0:
                current = back_stack.pop()
            else:
                current = choice(self.unvisited)
                self.visit_cell(current)
        self.end = current
        #self.remove_wall(self.start, WEST)
        #self.remove_wall((self.nrows - 1, self.ncols -1), SOUTH)

    def get_unvisited_neighbors(self, (x, y)):
        all_neighbors = [(x+dx, y+dy) for dx, dy in DELTAS]
        return [(a, b) for a, b in all_neighbors if (a, b) in self.unvisited]

    def visit_cell(self, (row, col)):
        self.unvisited.remove((row, col))

    def remove_wall(self, (row, col), direction):
        self.cells[row][col][direction] = 0

    def remove_wall_between(self, (row, col), (nrow, ncol)):
        direction = DELTAS.index((nrow - row, ncol - col))
        self.remove_wall((row, col), direction)
        self.remove_wall((nrow, ncol), OPPOSITE[direction])

    def __str__(self):
        result = ""
        for row in self.cells:
            top = ""
            middle = ""
            for cell in row:
                if cell[NORTH]:
                    top += "+ -- "
                else:
                    top += "+    "
                if cell[WEST]:
                    middle += "|    "
                else:
                    middle += "     "
            result += top + "+\n" + middle + "|\n"
        #result += "+ -- " * (self.ncols - 1) + "+    +\n"
        result += "+ -- " * self.ncols + "+\n"
        return result

    def __repr__(self):
        return str(self)

DEFAULT_ROWS = 4
DEFAULT_COLS = 4

if __name__ == "__main__":
    if len(sys.argv) == 1:
        maze = Maze(DEFAULT_ROWS, DEFAULT_COLS)
    elif len(sys.argv) == 3:
        rows, cols = [int(x) for x in sys.argv[1:]]
        maze = Maze(rows, cols)
    else:
        sys.exit()

    maze.build()
    print maze
    print "Start: %r\nEnd: %r" %(maze.start, maze.end)

