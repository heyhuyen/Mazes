import sys
from random import shuffle

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
    result += " _" * num_cols + "\n|" # top border + next row's left border
    last_row = range((num_rows - 1) * num_cols, num_rows * num_cols)
    for wall in walls:
        if wall.a in last_row:
            result += "_" # bottom border
        if wall.removed:
            result += " " # removed wall
        elif wall.b - wall.a > 1:
            result += "_" # horizontal wall
        else:
            result += "|" # vertical wall
        if wall.a % num_cols == num_cols - 1:
            result += "|\n|" # row's right border + next row's left border
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

    wall_indices = range(len(walls))
    shuffle(wall_indices)
    for index in wall_indices:
        wall = walls[index]
        print "Before: Wall %r" % wall
        for s in sets:
            if wall.a in s:
                a_set = s
            if wall.b in s:
                b_set = s
        if a_set.isdisjoint(b_set):
            sets.append(a_set.union(b_set))
            sets.remove(a_set)
            sets.remove(b_set)
            wall.removed = True
        print "After: Wall %r" % wall
        print_maze(num_rows, num_cols, walls)
        raw_input(">")
