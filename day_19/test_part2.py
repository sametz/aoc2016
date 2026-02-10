import pytest

from part2 import play_game, survivor_from_pattern


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 2),
        (7, 5),
    ],
)
def test_play_game(n, expected):
    players = list(range(1, n + 1))
    assert play_game(players) == expected


def test_survivor_from_pattern():
    for i in range(2, 100):
        expected = play_game(list(range(1, i + 1)))
        result = survivor_from_pattern(i)
        assert result == expected
