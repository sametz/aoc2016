import pytest

from part1 import (
    parse_line,
    parse_input,
    swap_pos,
    swap_letter,
    rotate,
    rotate_from,
    reverse,
    move,
    main,
)


def test_parse_line_exception():
    with pytest.raises(Exception):
        assert parse_line("spam") is None


def test_parse_input():
    result = parse_input("test_input.txt")
    expected = [
        ("swap_pos", 4, 0),
        ("swap_letter", "d", "b"),
        ("reverse", 0, 4),
        ("rotate", "left", 1),
        ("move", 1, 4),
        ("move", 3, 0),
        ("rotate_from", "b"),
        ("rotate_from", "d"),
    ]
    assert result == expected


def test_swap_pos():
    assert swap_pos("abcde", 4, 0) == "ebcda"


def test_swap_letter():
    assert swap_letter("ebcda", "d", "b") == "edcba"


def test_rotate():
    assert rotate("abcd", "right", 1) == "dabc"
    assert rotate("abcde", "left", 1) == "bcdea"


def test_rotate_from():
    assert rotate_from("abdec", "b") == "ecabd"
    assert rotate_from("ecabd", "d") == "decab"


def test_reverse():
    assert reverse("edcba", 0, 4) == "abcde"
    assert reverse("abcde", 1, 3) == "adcbe"


def test_move():
    assert move("bcdea", 1, 4) == "bdeac"
    assert move("bdeac", 3, 0) == "abdec"


def test_main():
    filename = "test_input.txt"
    s = "abcde"
    assert main(filename, s) == "decab"
