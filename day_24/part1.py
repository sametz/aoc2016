# Top answers on Reddit seem to compute all pairwise distances, then solve
# a TSP (travelling salesman problem).

# I want to see if just BFS can be used if the state for "seen" includes
# coord, # of steps, and numbers visited, e.g.
# (1 + 1j, 1, {1, 3})

# FLAW: visited not a state function but depends on path. Minimizing visits to
# a digit coordinate does not necessarily correspond to minimal total path.

from collections import defaultdict
from queue import Queue

N = 0 - 1j
S = 0 + 1j
W = -1 + 0j
E = 1 + 0j


def read_grid(filename):
    grid = defaultdict(lambda: "#")
    with open(filename) as f:
        lines = f.read().splitlines()
    y_max = len(lines)
    x_max = len(lines[0])
    digits = set()
    origin = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "#":
                grid[x + 1j * y] = char
                if char.isdigit():
                    assert char not in digits
                    if char == "0":
                        origin = x + 1j * y
                    else:
                        digits.add(char)
    return grid, (x_max, y_max), digits, origin
    # my input: (181, 43), 1-7, 171 + 7j


def main(grid, dims, digits, origin):
    pos = origin
    moves = 0
    frontier = Queue()
    all_digits = tuple(sorted(digits))
    visited = ()
    best_length = (dims[0]+dims[1]) * len(digits)  # should be ceiling value
    seen = defaultdict(lambda: best_length)  # key = (pos, (visited)), val = moves
    frontier.put((pos, moves, visited))
    while not frontier.empty():
        pos, moves, visited = frontier.get()
        if visited == all_digits:
            if moves < best_length:
                best_length = moves
            continue
        if seen[(pos, visited)] > moves:
            seen[(pos, visited)] = moves
            for direction in (N, S, W, E):
                next_pos = pos + direction
                next_char = grid[next_pos]
                if next_char != "#":
                    if next_char.isdigit():
                        next_visited = tuple(sorted(visited + (next_char,)))
                    else:
                        next_visited = visited
                    frontier.put((next_pos, moves + 1, next_visited))
    return best_length




if __name__ == "__main__":
    grid, dims, digits, origin = read_grid("input.txt")
    print(dims)
    print(digits)
    print(origin)
