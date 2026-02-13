from itertools import permutations


def parse_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f][2:]
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


if __name__ == "__main__":
    print(count_viable_pairs())
