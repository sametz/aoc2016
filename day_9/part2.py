import re

data_regex = re.compile(r"^(\w[^(]*)(.*)")
marker_regex = re.compile(r"^\((\d+)x(\d+)\)(.*)")
# single_marker_regex = re.compile(r"^\w*\((\d+)x(\d+)\)(\w[^(]+)")
single_marker_regex = re.compile(r"^\((\d+)x(\d+)\)(\w[^(].*)")


def read_input():
    with open("input.txt") as f:
        return f.read().strip()


# def process_marker(c, n, remainder):
#     if "(" not in remainder:
#         return c * n, remainder[c:]


def decompress(s):
    total = 0
    completed = False
    while not completed:
        if not s:
            completed = True
            continue
        d = data_regex.search(s)
        if d:
            prefix, s = d.groups()
            total += len(prefix)
            continue
        m = marker_regex.search(s)
        sm = single_marker_regex.search(s)
        if sm:
            c_str, r_str, remainder = sm.groups()
            c = int(c_str)
            r = int(r_str)
            assert "(" not in remainder[:c]
            total += c * r + decompress(remainder[c:])
            # s = remainder[c:]
            completed = True
            continue
        if not m:
            raise Exception(f"no match for {s}")

        c_str, r_str, remainder = m.groups()
        c = int(c_str)
        r = int(r_str)
        total += decompress(remainder[:c]) * r + decompress(remainder[c:])
        completed = True
    return total


if __name__ == "__main__":
    print(f"Decompressed length: {decompress(read_input())}")
