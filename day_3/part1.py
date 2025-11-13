import re


triangle_regex = re.compile(r"^\s*(\d+)\s+(\d+)\s+(\d+)")


def read_input(filename):
    triangles = []
    with open(filename) as f:
        for line in f:
            triangle = [int(t) for t in triangle_regex.match(line).groups()]
            triangle.sort()
            triangles.append(triangle)
    return triangles


def triangle_data(triangles):
    valid_triangles = []
    for triangle in triangles:
        if sum(triangle[:2]) > triangle[2]:
            valid_triangles.append(tuple(triangle))
    return len(valid_triangles)


if __name__ == "__main__":
    print(triangle_data(read_input("input.txt")))
