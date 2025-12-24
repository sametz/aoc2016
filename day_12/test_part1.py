from part1 import read_input, main


def test_read_input():
    assembly = read_input("test_input.txt")
    assert assembly[0] == ["cpy", 41, "a"]
    assert assembly[4] == ["jnz", "a", 2]
    assert assembly[-1] == ["dec", "a"]


def test_main():
    assert main("test_input.txt") == 42
