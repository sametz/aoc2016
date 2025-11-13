import pytest

from part2 import read_input, follow_directions, manhattan_d


def test_read_input():
    result = read_input()
    assert result[0] == ("L", 3)
    assert result[-1] == ("L", 1)


@pytest.mark.parametrize("steps, expected",
                         [
                             ([("R", 2), ("L", 3)], (None, None)),
                             ([
                                  ("R", 8),
                                  ("R", 4),
                                  ("R", 4),
                                  ("R", 8)
                              ], (4 +0j, 0 - 1j))
                         ])
def test_follow_directions(steps, expected):
    assert follow_directions(steps) == expected


@pytest.mark.parametrize("coord, expected", [
    (2 - 3j, 5),
    (0 + 2j, 2),
    (10 - 2j, 12),
]
                         )
def test_manhattan_d(coord, expected):
    assert manhattan_d(coord) == expected
