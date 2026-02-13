from collections import defaultdict
from itertools import permutations


def parse_input(filename, header_rows=2):
    with open(filename) as f:
        lines = [line.strip() for line in f][header_rows:]
    result = []
    for line in lines:
        filesystem, size_str, used_str, available_str, percent_str = line.split()
        x_str, y_str = filesystem.split("-")[-2:]
        x = int(x_str[1:])
        y = int(y_str[1:])
        size = int(size_str[:-1])
        used = int(used_str[:-1])
        available = int(available_str[:-1])
        percent = int(percent_str[:-1])
        result.append(((x, y), size, used, available, percent))
    return result


def count_viable_pairs():
    nodes = parse_input("input.txt")
    viable_pairs = 0
    for a, b in permutations(nodes, 2):
        assert a[0] != b[0]
        if a[2] != 0 and a[2] <= b[3]:
            viable_pairs += 1
    return viable_pairs


def map_paths(nodes):
    grid = defaultdict(lambda: ".")
    for a, b in permutations(nodes, 2):
        b_coord = b[0][0] + 1j * b[0][1]
        if sum(a[0]) > sum(b[0]):
            if b[2] == 0:
                grid[b_coord] = "_"
            elif a[2] != 0 and a[2] <= b[3]:
                grid[b_coord] = "*"
            elif b[-1] > 90:
                grid[b_coord] = "#"
    return grid


def print_grid(grid, x_max, y_max):
    print("\n")
    for y in range(y_max + 1):
        row = ""
        for x in range(x_max + 1):
            row += grid[x + 1j * y]
        print(row)


def grid_dimensions(nodes):
    x_max = max([node[0][0] for node in nodes])
    y_max = max([node[0][1] for node in nodes])
    return x_max, y_max  # 36, 24


def nodes_by_capacity(nodes):
    return sorted(nodes, key=lambda node: node[-1])


def empty_coord(nodes):
    empty_nodes = [node for node in nodes if node[2] == 0]
    assert len(empty_nodes) == 1
    return empty_nodes[0][0]

# inspecting grid: horizontal wall starts at (14, 7) and extends to right
# shuffle empty node to x = 13, then shuffle it to top row (y = 0)
# then shuffle until just left of top right corner
# once there, shuffle so empty node moves:
# - one right
# - one down
# - two left
# - one up
# repeat until empty node at 0, 0. Then, one more move to complete.
def cheat(nodes, x_max, y_max):
    empty_x, empty_y = empty_coord(nodes)
    moves = 0
    moves += empty_x - 13  # move past horizontal barrier
    moves += empty_y  # vertical moves to top row
    moves += x_max - 1 - 13  # horizontal moves to just left of upper right corner
    moves += (x_max - 1) * 5  # move empty to upper left
    moves += 1
    return moves


if __name__ == "__main__":
    nodes = parse_input("input.txt")
    grid = map_paths(nodes)
    x_max, y_max = grid_dimensions(nodes)
    print_grid(grid, x_max, y_max)
    print(f"Answer by cheating: {cheat(nodes, x_max, y_max)}")
# 194 is too low
