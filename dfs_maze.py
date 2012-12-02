import time
import sys
from random import choice

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
MARK = 4
DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N E S W
OPPOSITE= { NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}

class Maze:
    def __init__(self, rows, cols):
        self.nrows = rows
        self.ncols = cols
        self.cells = []
        self.unvisited = []
        self.setup_cells()

    def setup_cells(self):
        for row in range(self.nrows):
            new_row = []
            for col in range(self.ncols):
                new_row.append([1]*4 + [0]) # [ N E S W MARK]
                self.unvisited.append((row, col))
            self.cells.append(new_row)

    def build(self):
        back_stack = []
        current = choice(self.unvisited)
        self.visit_cell(current)
        print self
        while len(self.unvisited) > 0:
            unvisited_neighbors = self.get_unvisited_neighbors(current)
            if len(unvisited_neighbors) > 0:
                neighbor = choice(unvisited_neighbors)
                back_stack.append(current)
                self.remove_wall_between(current, neighbor)
                current = neighbor
                self.visit_cell(current)
                time.sleep(0.5)
                print self
            elif len(back_stack) > 0:
                current = back_stack.pop()
            else:
                current = choice(self.unvisited)
                self.visit_cell(current)

    def solve(self, start, end):
        back_stack = []
        current = start
        self.mark(current)
        print self
        while current != end:
            moves = self.moves(current)
            if len(moves) > 0:
                back_stack.append(current)
                current = choice(moves)
                self.mark(current)
            else:
                self.mark(current)
                current = back_stack.pop()
            time.sleep(0.5)
            print self

    def visit_cell(self, (row, col)):
        self.unvisited.remove((row, col))

    def mark(self, (row, col)):
        self.cells[row][col][MARK] += 1

    def get_unvisited_neighbors(self, (row, col)):
        all_neighbors = [(row+dr, col+dc) for dr, dc in DELTAS]
        return [(a, b) for a, b in all_neighbors if (a, b) in self.unvisited]

    def moves(self, (row, col)):
        walls = self.cells[row][col][:4]
        open_walls = [wall for wall, up in enumerate(walls) if not up]
        directions_to_explore = [DELTAS[i] for i in open_walls]
        path_neighbors = [(row+dr, col+dc) for dr, dc in directions_to_explore]
        return [(a, b) for a, b in path_neighbors if not self.cells[a][b][MARK]]

    def remove_wall_between(self, (row, col), (nrow, ncol)):
        wall_dir = DELTAS.index((nrow - row, ncol - col))
        self.cells[row][col][wall_dir] = 0
        self.cells[nrow][ncol][OPPOSITE[wall_dir]] = 0

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
                    middle += "| "
                else:
                    middle += "  "
                if cell[MARK] == 1:
                    middle +=  "[]"
                elif cell[MARK] == 2:
                    middle += "xx"
                else:
                    middle += "  "
                middle += " "
            result += top + "+\n" + middle + "|\n"
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
        print "Usage: dfs_maze.py #rows #cols"
        sys.exit()

    print maze
    raw_input("Hit <ENTER> to generate maze>")
    maze.build()
    raw_input("Hit <ENTER> to solve>")
    maze.solve((0,0), (rows - 1,cols - 1))
