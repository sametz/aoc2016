import pytest

from part1 import read_input, has_abba, supports_tls, count_tls_ips


def test_read_input():
    ips = read_input("test_input.txt")
    assert ips[0] == "abba[mnop]qrst"
    assert ips[-1] == "ioxxoj[asdfgh]zxcvbn"


def test_has_abba():
    s = "ioxxoj"
    assert has_abba(s)
    s2 = "aaaabb"
    assert not has_abba(s2)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ],
)
def test_supports_tls(s, expected):
    assert supports_tls(s) == expected


def test_count_tls_ips():
    ips = read_input("test_input.txt")
    assert count_tls_ips(ips) == 2
