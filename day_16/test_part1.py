import pytest

from part1 import read_input, dragon_curve, space_filler, checksum, main


def test_read_input():
    s = read_input()
    assert s.startswith("1")
    assert s.endswith("0")
    assert len(s) == 17


@pytest.mark.parametrize(
    "a, b",
    [
        ("1", "100"),
        ("0", "001"),
        ("11111", "11111000000"),
        ("111100001010", "1111000010100101011110000"),
    ],
)
def test_dragon_curve(a, b):
    assert dragon_curve(a) == b


def test_space_filler():
    assert space_filler("11", 6) == "11000011100"


def test_checksum():
    assert checksum("110010110100") == "100"


def test_main():
    assert main("10000", 20) == "01100"
