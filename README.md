Some "perfect" maze generating and solving in [Python](http://www.python.org).

Written during [Hacker School](https://www.hackerschool.com/), Batch[4], Fall 2012.

## Depth-First Search with Backtracking
 **dfs_maze.py** generates and solves a perfect maze, step by step. Starting with cells, each containing 4 walls, visit cells and knock down walls to add unvisited cells to the network until all cells have been visited.

### Usage
Run this command:

    python dfs_maze.py

Optionally, to specify the maze dimensions you can pass in the desired number of rows and columns. This command creates a maze with 3 rows and 4 columns. 

    python dfs_maze.py 3 4

The solver solves the maze from the top left corner to the bottom right corner. The solved maze will look something like this:

    + -- + -- + -- + -- +
    | [] | xx   xx   xx |
    +    + -- + -- +    +
    | []   []   []   [] |
    + -- + -- + -- +    +
    |                [] |
    + -- + -- + -- + -- +

- Walls denoted by `--` and `|`
- Solution path marked by `[]`
- Paths visited but not in solution marked by `xx`

## Kruskal's Algorithm
**random\_kruskal\_maze.py** generates (but doesn't solve... yet!) a perfect maze using a randomized version of Kruskal's minimum spanning tree algorithm. Start out with all walls and randomly knock down walls if they separate cells in disjoint sets until only one set remains.

### Usage
Run this command:

    python random_kruskal_maze.py

Or with specified numbers of rows and columns:

    python random_kruskal_maze.py <rows> <cols>

Sample 6 x 8 maze:

     _ _ _ _ _ _ _ _
    |    _ _  | | | |
    | |_  |_  | |  _|
    | |_ _  |  _ _| |
    |_|_ _  |_ _ _  |
    |_ _   _|  _| | |
    |_ _ _ _ _ _|_ _|

- Walls denoted by `-` and `|`

## Resources
- ThinkLabrynth's [Maze Classification](http://www.astrolog.org/labyrnth/algrithm.htm)

- Wikipedia article on [maze generating algorithms](http://en.wikipedia.org/wiki/Maze_generation_algorithm)

- MazeWorks [How to Build a Maze](http://www.mazeworks.com/mazegen/mazetut/index.htm)

## Todo/Extensions
- write solver for kruskal
- try other algorithms
- allow human solving
