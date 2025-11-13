import pytest

from part1 import read_input, follow_directions, manhattan_d


def test_read_input():
    result = read_input()
    assert result[0] == ("L", 3)
    assert result[-1] == ("L", 1)


@pytest.mark.parametrize(
    "steps, expected",
    [
        ([("R", 2), ("L", 3)], (2 - 3j, 0 - 1j)),
        ([("R", 2), ("R", 2), ("R", 2)], (0 + 2j, -1 + 0j)),
        ([("R", 5), ("L", 5), ("R", 5), ("R", 3)], (10 - 2j, 0 + 1j)),
    ],
)
def test_follow_directions(steps, expected):
    assert follow_directions(steps) == expected


@pytest.mark.parametrize(
    "coord, expected",
    [
        (2 - 3j, 5),
        (0 + 2j, 2),
        (10 - 2j, 12),
    ],
)
def test_manhattan_d(coord, expected):
    assert manhattan_d(coord) == expected
