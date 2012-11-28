import sys
from random import choice

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
VISITED = 4
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
                new_row.append([1]*4 + [0]) # [ N E S W VISITED]
                self.unvisited.append((row, col))
            self.cells.append(new_row)

    def get_unvisited_neighbors(self, (x, y)):
        all_neighbors = [(x+dx, y+dy) for dx, dy in DELTAS]
        return [(a, b) for a, b in all_neighbors if (a, b) in self.unvisited]

    def visit_cell(self, (row, col)):
        #self.cells[row][col][VISITED] = 1
        self.unvisited.remove((row, col))

    def remove_wall(self, (a, b), (c, d)):
        wall = DELTAS.index((c-a, d-b))
        self.cells[a][b][wall] = 0
        self.cells[c][d][OPPOSITE[wall]] = 0

    def __str__(self):
        result = ""
        for row in maze.cells:
            top = ""
            middle = ""
            bottom = ""
            for cell in row:
                if cell[NORTH]:
                    top += "+----+ "
                else:
                    top += "+    + "
                if cell[WEST]:
                    middle += "|    "
                else:
                    middle += "     "
                if cell[EAST]:
                    middle += "| "
                else:
                    middle += "  "
                if cell[SOUTH]:
                    bottom += "+----+ "
                else:
                    bottom += "+    + "
            result += top + "\n" + middle + "\n" + bottom + "\n"
        return result

DEFAULT_DIMS = (4, 4)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        maze = Maze(DEFAULT_DIMS)
    elif len(sys.argv) == 3:
        rows, cols = [int(x) for x in sys.argv[1:]]
        maze = Maze((rows, cols))
    else:
        sys.exit()

    the_stack = []
    current = (0, 0)
    maze.visit_cell(current)
    while len(maze.unvisited) > 0:
        unvisited = maze.get_unvisited_neighbors(current)
        if len(unvisited) > 0:
            neighbor = choice(unvisited)
            the_stack.append(current)
            maze.remove_wall(current, neighbor)
            current = neighbor
            maze.visit_cell(current)
        elif len(the_stack) > 0:
            current = the_stack.pop()
        else:
            current = choice(maze.unvisited)
            maze.visit_cell(current)
    print maze
