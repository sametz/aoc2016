import pytest

from part2 import read_input, find_next_number, find_code


def test_read_input():
    instructions = read_input("test_input.txt")
    assert len(instructions) == 4
    assert instructions[0] == "ULL"
    assert instructions[-1][-1] == "D"


@pytest.mark.parametrize(
    "pos, steps, expected",
    [
        (-2 + 0j, "ULL", (-2 + 0j, "5")),
        (-2 + 0j, "RRDDD", (0 + 2j, "D")),
        (0 + 2j, "LURDL", (0 + 1j, "B")),
        (0 + 1j, "UUUUD", (0 - 1j, "3")),
    ],
)
def test_find_next_number(pos, steps, expected):
    result = find_next_number(pos, steps)
    assert result == expected


def test_find_code():
    assert find_code(read_input("test_input.txt")) == "5DB3"
