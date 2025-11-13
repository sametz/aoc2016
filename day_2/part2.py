from collections import defaultdict

U = 0 - 1j
D = 0 + 1j
R = 1 + 0j
L = -1 + 0j

moves = {"U": U, "D": D, "L": L, "R": R}


# Arbitrarily assigning 5 key the 0 + 0j coordinate
keypad = defaultdict(lambda: None)
keypad[0 + 0j] = "7"
keypad[0 - 2j] = "1"
keypad[-1 - 1j] = "2"
keypad[0 - 1j] = "3"
keypad[1 - 1j] = "4"
keypad[-2 + 0j] = "5"
keypad[-1 + 0j] = "6"
keypad[1 + 0j] = "8"
keypad[2 + 0j] = "9"
keypad[-1 + 1j] = "A"
keypad[0 + 1j] = "B"
keypad[1 + 1j] = "C"
keypad[0 + 2j] = "D"


def read_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def find_next_number(pos, steps):
    for step in steps:
        next_pos = pos + moves[step]
        if keypad[next_pos]:
            pos = next_pos
    return pos, keypad[pos]


def find_code(steps):
    pos = -2 + 0j  # 5
    code = ""
    for step in steps:
        pos, number = find_next_number(pos, step)
        code += number
    return code


if __name__ == "__main__":
    code = find_code(read_input("input.txt"))
    print("Bathroom code: ", code)
