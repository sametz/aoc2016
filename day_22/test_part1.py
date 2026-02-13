from part1 import parse_input


def test_parse_input():
    node_data = parse_input("input.txt")
    assert node_data[0] == ((0, 0), 91, 66, 25, 72)
    assert node_data[-1] == ((36, 24), 88, 66, 22, 75)
