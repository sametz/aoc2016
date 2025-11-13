import re


triangle_regex = re.compile(r"^\s*(\d+)\s+(\d+)\s+(\d+)")


def read_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            line_parsed = [int(t) for t in triangle_regex.match(line).groups()]
            data.append(line_parsed)
    return data


def triangles(data):
    triangles = []
    # matrix transpose data
    t = list(zip(*data))
    for line in t:
        by_threes = list(zip(*[iter(line)] * 3))  # TIL
        triangles.extend(by_threes)
    return triangles


def valid_triangles(triangles):
    t = []
    for triangle in triangles:
        sorted_t = sorted(triangle)
        if sum(sorted_t[:2]) > sorted_t[2]:
            t.append(triangle)
    return len(t)


if __name__ == "__main__":
    print(valid_triangles(triangles(read_input("input.txt"))))
