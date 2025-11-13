import pytest

from part2 import parse_input, checksum, valid_rooms, rot_n


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
    assert rooms[0][0] == "aaaaa-bbb-z-y-x"
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


def test_valid_rooms():
    v = valid_rooms(parse_input("test_input.txt"))
    assert v == [
        ("aaaaa-bbb-z-y-x", 123),
        ("a-b-c-d-e-f-g-h", 987),
        ("not-a-real-room", 404),
    ]


def test_rot_n():
    assert rot_n("qzmt-zixmtkozy-ivhz", 343) == "very-encrypted-name"
