from part1 import read_input, triangle_data


def test_read_input():
    triangles = read_input("test_input.txt")
    assert len(triangles) == 2
    assert triangles[0] == [5, 10, 25]
    assert triangles[-1] == [3, 4, 5]


def test_triangle_data():
    assert triangle_data(read_input("test_input.txt")) == 1
