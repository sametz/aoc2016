import pytest

from part1 import parse_input, checksum, valid_ids


def test_mississippi():
    from collections import Counter

    c = Counter("mississippi").most_common()
    # -x[1] results in numbers sorted largest to smallest
    c_sorted = sorted(c, key=lambda x: (-x[1], x[0]))
    assert c_sorted[0] == ("i", 4)
    assert c_sorted[1] == ("s", 4)
    assert c_sorted[-1] == ("m", 1)


def test_parse_input():
    rooms = parse_input("test_input.txt")
    assert rooms[0][0] == "aaaaabbbzyx"
    assert rooms[0][1] == 123
    assert rooms[0][2] == "abxyz"
    assert rooms[-1][-1] == "decoy"


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aaaaabbbzyx", "abxyz"),
        ("abcdefgh", "abcde"),
        ("notarealroom", "oarel"),
    ],
)
def test_checksum(s, expected):
    assert checksum(s) == expected


def test_valid_ids():
    v = valid_ids(parse_input("test_input.txt"))
    assert v == [123, 987, 404]
