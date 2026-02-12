from part2 import read_input, condense_ranges, count_allowed, main


def test_read_input():
    result = read_input("test_input.txt")
    assert result == [[5, 8], [0, 2], [4, 7]]
    result.sort()
    assert result[0] == [0, 2]


def test_condense_ranges():
    ips = read_input("test_input.txt")
    result = condense_ranges(ips)
    assert result == [[0, 2], [4, 8]]


def test_count_allowed():
    assert count_allowed([[0, 2], [4, 8]], 9) == 2

def test_main():
    assert main("test_input.txt", 9) == 2
