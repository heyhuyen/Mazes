import sys

"""
Randomized Kruskal's Minimum Spanning Tree Algorithm for Maze Generation.
"""

class Wall:
    def __init__(self, a, b):
        self.removed = False
        self.a = a
        self.b = b

    def __repr__(self):
        return repr((self.removed, self.a, self.b))

def print_maze(num_rows, num_cols, walls):
    result = ""
    result += " _" * num_cols + "\n|" # top border + next row's left border wall
    for wall in walls:
        if not wall.removed:
            if wall.b - wall.a > 1:
                result += "_" # horizontal wall
                if wall.a % num_cols == num_cols - 1:
                    result += "|\n|" # last cell in row + next row left border wall
            else:
                if wall.a / num_rows == num_rows - 1:
                    result += "_" # bottom row cell
                result += "|" # vertical wall
        else:
            result += " " # removed wall
    result += "_|" # last bottom right cell
    print result

DEFAULT_ROWS = 2
DEFAULT_COLS = 3

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # default
        num_rows = DEFAULT_ROWS
        num_cols = DEFAULT_COLS
    elif len(sys.argv) == 3:
        # got two args
        num_rows, num_cols = [int(x) for x in sys.argv[1:]]
    else:
        sys.exit()

    # create cells
    cells = range(num_rows * num_cols)

    # create path sets and walls
    sets = []
    walls = []
    for cell in cells:
        sets.append(set([cell]))
        if cell / (num_cols * (num_rows - 1)) < 1:
            # add bottom wall
            walls.append(Wall(cells[cell], cells[cell + num_cols]))
        if cell % num_cols < num_cols - 1:
            # add right wall
            walls.append(Wall(cells[cell], cells[cell + 1]))

    print "Before knocking down walls:"
    print_maze(num_rows, num_cols, walls)

        
