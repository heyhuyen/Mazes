import sys
from random import choice, shuffle
import numpy

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N E S W
OPPOSITE= { NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}

class Maze:
    def __init__(self, size):
        self.nrows, self.ncols = size
        self.setup_cells()

    def setup_cells(self):
        self.cells = []
        self.unvisited = []
        for row in range(self.nrows):
            new_row = []
            for col in range(self.ncols):
                new_cell = Cell((row, col))
                new_row.append(new_cell)
                self.unvisited.append(new_cell)
            self.cells.append(new_row)

    def get_unvisited_neighbors(self, (x, y)):
        neighbor_coords = [(x+dx, y+dy) for dx, dy in DELTAS]
        return [self.cells[x][y] for x, y in neighbor_coords if x in range(self.nrows) and y in range(self.ncols) and not self.cells[x][y].visited]

    def visit_cell(self, cell):
        cell.visited = True
        self.unvisited.remove(cell)

    def __str__(self):
        result = ""
        for row in maze.cells:
            top = ""
            middle = ""
            bottom = ""
            for col in row:
                if col.walls[0]:
                    top += "+----+ "
                else:
                    top += "+    + "
                if col.walls[3]:
                    middle += "|    "
                else:
                    middle += "     "
                if col.walls[1]:
                    middle += "| "
                else:
                    middle += "  "
                if col.walls[2]:
                    bottom += "+----+ "
                else:
                    bottom += "+    + "
            result += top + "\n" + middle + "\n" + bottom + "\n"
        return result

class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.visited = False
        self.walls = [1]*4

    def remove_wall(self, wall):
        self.walls[wall] = 0

DEFAULT_DIMS = (4, 4)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        maze = Maze(DEFAULT_DIMS)
    elif len(sys.argv) == 3:
        rows, cols = [int(x) for x in sys.argv[1:]]
        maze = Maze((rows, cols))
    else:
        sys.exit()
    total_cells = maze.ncols * maze.nrows
    the_stack = []
    current = maze.cells[0][0]
    maze.visit_cell(current)
    while len(maze.unvisited) > 0:
        unvisited = maze.get_unvisited_neighbors(current.pos)
        if len(unvisited) > 0:
            neighbor = choice(unvisited)
            if not neighbor.visited:
                the_stack.append(current)
                test = numpy.asarray(neighbor.pos) - numpy.asarray(current.pos)
                direction = DELTAS.index((test[0], test[1]))
                current.remove_wall(direction)
                neighbor.remove_wall(OPPOSITE[direction])
                current = neighbor
                maze.visit_cell(current)
        elif len(the_stack) > 0:
            current = the_stack.pop()
        else:
            current = choice(maze.unvisited)
            maze.visit_cell(current)
    print maze
