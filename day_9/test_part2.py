import re

import pytest

from part2 import data_regex, marker_regex, read_input


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


def test_assumptions():
    t = read_input()
    # test if text between markers is always longer
    # than character number in previous marker

    single_marker_regex = re.compile(r"^\w*\((\d+)x(\d+)\)(\w[^\(]+)")
    # t = "abcd(2x3)ef(3x4)ghijk"
    # t = "(172x1)(3x7)XPJ"
    consumed  = False
    while not consumed:
        d = data_regex.search(t)
        if d:
            _, t = d.groups()  # trim leading non-marker characters
        if not t:
            consumed = True
            continue
        m = marker_regex.search(t)
        sm = single_marker_regex.search(t)
        if m and not sm:  # trim first marker of a double marker
            t = m.groups()[2]
            continue

        assert t.startswith("(")
        try:
            c_str, n_str, text = sm.groups()
        except AttributeError:
            print(f"regex failed for {t}")
            assert 1 == 2
        c = int(c_str)
        assert len(text) >= c
        t = text[c:]



# @pytest.mark.parametrize(
#     "s, expected",
#     [
#         ("ADVENT", "ADVENT"),
#         ("A(1x5)BC", "ABBBBBC"),
#         ("(3x3)XYZ", "XYZXYZXYZ"),
#         ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"),
#         ("(6x1)(1x3)A", "(1x3)A"),
#         ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"),
#     ],
# )
# def test_decompress(s, expected):
#     assert decompress(s) == expected
