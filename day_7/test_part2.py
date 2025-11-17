import pytest

from part2 import read_input, supports_ssl, count_ssl_ips


def test_read_input():
    ips = read_input("test_input.txt")
    assert ips[0] == "abba[mnop]qrst"
    assert ips[-1] == "ioxxoj[asdfgh]zxcvbn"


# def test_has_abba():
#     s = "ioxxoj"
#     assert has_abba(s)
#     s2 = "aaaabb"
#     assert not has_abba(s2)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ],
)
def test_supports_ssl(s, expected):
    assert supports_ssl(s) == expected


def test_count_ssl_ips():
    ips = read_input("test_input2.txt")
    assert count_ssl_ips(ips) == 3
