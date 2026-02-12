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
    # swaps, reverses work both ways
    # rotations: swap "left" for "right" and vice versa
    # moves: swap the numbers
    # rotate based on index is trickier:
    # consider the result of rotating abcdefgh:
    # letter / n right rot/ result/ final index of letter
    # a 1 habcdefg 1
    # b 2 ghabcdef 3
    # c 3 fghabcde 5
    # d 4 efghabcd 7
    # e 6 cdefghab 2
    # f 7 bcdefgha 4
    # g 8 abcdefgh 6
    # h 9 habcdefg 0
    # so by finding index of letter, know how many left rotations needed to reverse

    operations = parse_input(filename)
    for operation in operations[::-1]:
        f, args = operation[0], operation[1:]
        match f:
            case "swap_pos":
                s = swap_pos(s, *args)
            case "swap_letter":
                s = swap_letter(s, *args)
            case "rotate":
                direction, n = args
                if direction == "left":
                    s = rotate(s, "right", args[-1])
                else:
                    s = rotate(s, "left", args[-1])
            case "rotate_from":
                final_index = s.index(args[0])
                reverse_index_dict = {  # final index: size rotation
                    1:1,
                    3:2,
                    5:3,
                    7:4,
                    2:6,
                    4:7,
                    6:8,
                    0:9,
                }
                s = rotate(s, "left", reverse_index_dict[final_index])
            case "reverse":
                s = reverse(s, *args)
            case "move":
                initial_index, final_index = args
                s = move(s, final_index, initial_index)

    return s


if __name__ == "__main__":
    filename = "input.txt"
    s = "fbgdceah"
    print(f"Result: {main(filename, s)}")
