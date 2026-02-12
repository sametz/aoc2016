def parse_line(s):
    s_split = s.split(" ")
    if s.startswith("swap position"):
        x = int(s_split[2])
        y = int(s_split[5])
        return "swap_pos", x, y
    if s.startswith("swap letter"):
        x = s_split[2]
        y = s_split[5]
        return "swap_letter", x, y
    if s.startswith("rotate"):
        if s_split[1] in ["left", "right"]:
            return "rotate", s_split[1], int(s_split[2])
        return "rotate_from", s_split[6]
    if s.startswith("reverse"):
        return "reverse", int(s_split[2]), int(s_split[4])
    if s.startswith("move"):
        return "move", int(s_split[2]), int(s_split[5])
    raise Exception("Line could not be parsed.")


def parse_input(file_name):
    result = []
    with open(file_name) as f:
        for line in f:
            result.append(parse_line(line.strip()))
    return result


def swap_pos(s, x, y):
    lo, hi = min(x, y), max(x, y)
    return s[:lo] + s[hi] + s[lo + 1 : hi] + s[lo] + s[hi + 1 :]


def swap_letter(s, x, y):
    x_pos = s.index(x)
    y_pos = s.index(y)
    return swap_pos(s, x_pos, y_pos)


def rotate(s, direction, n):
    if n > len(s):
        n = n % len(s)
    if direction == "left":
        return s[n:] + s[:n]
    return s[-n:] + s[:-n]


def rotate_from(s, x):
    x_pos = s.index(x)
    n = 1 + x_pos
    if x_pos >= 4:
        n += 1
    return rotate(s, "right", n)


def reverse(s, x, y):
    lo, hi = min(x, y), max(x, y)
    reverse_slice = s[lo : hi + 1][::-1]
    return s[:lo] + reverse_slice + s[hi + 1 :]


def move(s, x, y):
    removed = s[:x] + s[x + 1 :]
    return removed[:y] + s[x] + removed[y:]


def main(filename, s):
    f_dict = {
        "swap_pos": swap_pos,
        "swap_letter": swap_letter,
        "rotate": rotate,
        "rotate_from": rotate_from,
        "reverse": reverse,
        "move": move,
    }
    operations = parse_input(filename)
    for operation in operations:
        f, args = operation[0], operation[1:]
        s = f_dict[f](s, *args)
        print(s)
    return s


if __name__ == "__main__":
    filename = "input.txt"
    s = "abcdefgh"
    print(f"Result: {main(filename, s)}")
