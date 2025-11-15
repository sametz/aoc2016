from part1 import read_input, transpose, denoise


def test_read_input():
    messages = read_input("test_input.txt")
    n = len(messages[0])
    for m in messages[1:]:
        assert len(m) == n
    assert messages[0] == "eedadn"
    assert messages[-1] == "enarar"


def test_transpose():
    m = ["abc", "def", "ghi"]
    assert transpose(m) == [("a", "d", "g"), ("b", "e", "h"), ("c", "f", "i")]


def test_denoise():
    m = read_input("test_input.txt")
    assert denoise(m) == "easter"
