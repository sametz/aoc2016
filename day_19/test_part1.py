import pytest

from part1 import next_round, play_game


def test_next_round():
    assert next_round(0, True) == 1


@pytest.mark.parametrize("n, expected", [(5, 3), (7, 7), (11, 7), (13, 11)])
def test_play_game(n, expected):
    players = range(1, n + 1)
    assert play_game(players) == expected
