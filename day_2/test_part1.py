import pytest

from part1 import read_input, find_next_number, find_code


def test_read_input():
    instructions = read_input("test_input.txt")
    assert len(instructions) == 4
    assert instructions[0] == "ULL"
    assert instructions[-1][-1] == "D"


@pytest.mark.parametrize(
    "pos, steps, expected",
    [
        (0 + 0j, "ULL", (-1 - 1j, "1")),
        (-1 - 1j, "RRDDD", (1 + 1j, "9")),
        (1 + 1j, "LURDL", (0 + 1j, "8")),
        (0 + 1j, "UUUUD", (0 + 0j, "5")),
    ],
)
def test_find_next_number(pos, steps, expected):
    result = find_next_number(pos, steps)
    assert result == expected


def test_find_code():
    assert find_code(read_input("test_input.txt")) == "1985"
