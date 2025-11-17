import numpy as np

from part1 import compile_input, do_operation, swipe_card, main


def test_compile_input():
    result = compile_input("test_input.txt")
    assert result == [
        ("rect", 3, 2),
        ("rotate", "column", 1, 1),
        ("rotate", "row", 0, 4),
        ("rotate", "column", 1, 1),
    ]


def test_rect():
    a = np.zeros((3, 7), dtype=bool)
    do_operation(a, ("rect", 3, 2))
    expected = np.array([[True] * 3 + [False] * 4] * 2 + [[False] * 7])
    assert np.array_equal(a, expected)


def test_rotate_column():
    a = np.array([[True] * 3 + [False] * 4] * 2 + [[False] * 7])
    do_operation(a, ("rotate", "column", 1, 1))
    expected = np.array(
        [
            [True, False, True] + [False] * 4,
            [True] * 3 + [False] * 4,
            [False, True] + [False] * 5,
        ]
    )
    assert np.array_equal(a, expected)


def test_rotate_row():
    a = np.array(
        [
            [True, False, True] + [False] * 4,
            [True] * 3 + [False] * 4,
            [False, True] + [False] * 5,
        ]
    )
    do_operation(a, ("rotate", "row", 0, 4))
    expected = np.array(
        [
            [False] * 4 + [True, False, True],
            [True] * 3 + [False] * 4,
            [False, True] + [False] * 5,
        ]
    )
    assert np.array_equal(a, expected)


def test_swipe_card():
    instructions = compile_input("test_input.txt")
    screen = swipe_card(3, 7, instructions)
    expected = np.array(
        [
            [False, True, False, False, True, False, True],
            [True, False, True] + [False] * 4,
            [False, True] + [False] * 5,
        ]
    )
    assert np.array_equal(screen, expected)


def test_main():
    assert main(3, 7, "test_input.txt") == 6
