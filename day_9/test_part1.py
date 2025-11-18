import pytest

from part1 import data_regex, marker_regex, read_input, decompress


def test_read_input():
    s = read_input()
    assert s.startswith("(172x1)")
    assert s.endswith("INZFFT")


def test_regex_truthiness():
    marker_test = "(6x1)(1x3)A"
    data_test = "A(1x5)BC"
    assert data_regex.search(data_test)
    print(data_regex.search(data_test).groups())
    assert not data_regex.search(marker_test)
    assert marker_regex.search(marker_test)
    print(marker_regex.search(marker_test).groups())
    assert not marker_regex.search(data_test)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ADVENT", "ADVENT"),
        ("A(1x5)BC", "ABBBBBC"),
        ("(3x3)XYZ", "XYZXYZXYZ"),
        ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"),
        ("(6x1)(1x3)A", "(1x3)A"),
        ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"),
    ],
)
def test_decompress(s, expected):
    assert decompress(s) == expected
