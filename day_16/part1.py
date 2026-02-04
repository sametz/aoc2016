# If Python 3.12 or newer, could use:
# from itertools import batched


def read_input():
    with open("input.txt") as f:
        return f.read().strip()


def dragon_curve(a):
    b = a[::-1]
    not_b = [str(int(c) ^ 1) for c in b]
    not_b_str = "".join(not_b)
    return a + "0" + not_b_str


def space_filler(seed, length):
    while len(seed) < length:
        seed = dragon_curve(seed)
    return seed


def checksum(n):
    if len(n) % 2 == 1:
        return n
    next_n = ""
    # the following would require python 3.12 or newer
    # for pair in batched(n, 2):

    # Instead for older python:
    pairs = zip(n[::2], n[1::2])
    for pair in pairs:
        if pair[::-1] == pair:
            next_n += "1"
        else:
            next_n += "0"
    return checksum(next_n)


def main(seed, length):
    filler = space_filler(seed, length)[:length]
    return checksum(filler)


if __name__ == "__main__":
    seed = read_input()
    print("Checksum: ", main(seed, 272))
