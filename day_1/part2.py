N = 0 - 1j
S = 0 + 1j
E = 1 + 0j
W = -1 + 0j

left_turn = 0 - 1j
right_turn = 0 + 1j


def read_input():
    with open('input.txt') as f:
        steps = f.read().split(", ")
        return [(step[0], int(step[1:])) for step in steps]


# Could either simulate step by step, or count the total number
# ouf N, S, E, and W steps. I don't think counting number of N/S/E/W
# steps is more efficient than just adding at each direction,
# so try the obvious solution.

def follow_directions(steps):
    pos = 0 + 0j
    direction = N
    seen = []
    for turn, d in steps:
        match turn:
            case "L":
                direction *= left_turn
            case "R":
                direction *= right_turn
            case _:
                raise Exception(f"Illegal move: {turn}{d}")
        for i in range(d):
            pos += direction
            if pos in seen:
                return pos, direction
            seen.append(pos)
    return None, None  # never repeated position


def manhattan_d(coord):
    # writing and testing a function that's one line of math is bad practice
    return abs(coord.real) + abs(coord.imag)


def main():
    steps = read_input()
    pos, dir = follow_directions(steps)
    return manhattan_d(pos), pos, dir


if __name__ == "__main__":
    d, pos, _ = main()
    print(f"Bunny HQ is {d} blocks away, at {pos}.")
