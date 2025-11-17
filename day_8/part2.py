import matplotlib.pyplot as plt
import numpy as np


def compile_input(filename):
    with open(filename) as f:
        return [parse_instruction(line) for line in f]


def parse_instruction(line):
    chunks = line.split(" ")
    if len(chunks) == 2:
        assert chunks[0] == "rect"
        c, r = chunks[1].split("x")
        return chunks[0], int(c), int(r)
    assert len(chunks) == 5
    assert chunks[0] == "rotate"
    assert chunks[1] == "row" or chunks[1] == "column"
    i = int(chunks[2].split("=")[1])
    n = int(chunks[4])
    return (
        chunks[0],
        chunks[1],
        int(chunks[2].split("=")[1]),
        int(chunks[4]),
    )  # command, direction, index, amount


def do_operation(a, operation):
    if operation[0] == "rect":
        c, r = operation[1:]
        a[:r, :c] = True
    elif operation[1] == "row":
        r, n = operation[2:]
        a[r] = np.roll(a[r], n)
    elif operation[1] == "column":
        c, n = operation[2:]
        a[:, c] = np.roll(a[:, c], n)
    else:
        raise Exception("Unknown operation")


def swipe_card(r, c, instructions):
    screen = np.zeros((r, c), dtype=bool)
    for operation in instructions:
        do_operation(screen, operation)
    return screen


def answer_screen(r, c, filename):
    instructions = compile_input(filename)
    return swipe_card(r, c, instructions)


if __name__ == "__main__":
    test_case = False
    test_args = (3, 7, "test_input.txt")
    real_args = (6, 50, "input.txt")
    args = test_args if test_case else real_args
    screen = answer_screen(*args)

    plt.imshow(screen, cmap="Greys", interpolation="nearest")
    plt.show()
