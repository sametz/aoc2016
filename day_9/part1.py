import re

data_regex = re.compile(r"^(\w[^\(]*)(.*)")
marker_regex = re.compile(r"^\((\d+)x(\d+)\)(.*)")


def read_input():
    with open("input.txt") as f:
        return f.read().strip()


def decompress(s):
    remaining = s[:]
    result = ""
    completed = False
    while not completed:
        data_prefix = data_regex.search(remaining)
        marker_prefix = marker_regex.search(remaining)
        if not data_prefix and not marker_prefix:
            completed = True
        elif data_prefix:
            data, rest = data_prefix.groups()
            result += data
            remaining = rest
        else:
            c_str, n_str, suffix = marker_prefix.groups()
            c = int(c_str)
            n = int(n_str)
            repeat_unit = suffix[:c] * n
            result += repeat_unit
            remaining = suffix[c:]
    return result


if __name__ == "__main__":
    print(f"Decompressed length: {len(decompress(read_input()))}")
