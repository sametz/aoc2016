import pytest

from part2 import play_game


@pytest.mark.parametrize("n, expected", [(5, 2), (7, 5),])
def test_play_game(n, expected):
    players = list(range(1, n + 1))
    assert play_game(players) == expected
