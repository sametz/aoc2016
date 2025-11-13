from part2 import read_input, triangles, valid_triangles


def test_read_input():
    input_data = read_input("test_input2.txt")
    assert len(input_data) == 3
    assert input_data[0] == [1, 2, 3]
    assert input_data[-1] == [7, 8, 9]


def test_triangles():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    c = [9, 10, 11, 12]
    t = triangles([a, b, c])
    assert t == [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


def test_valid_triangles():
    t = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    assert valid_triangles(t) == 2
