import re

data_regex = re.compile(r"^(\w[^(]*)(.*)")
marker_regex = re.compile(r"^\((\d+)x(\d+)\)(.*)")
single_marker_regex = re.compile(r"^\w*\((\d+)x(\d+)\)(\w[^(]+)")


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
            total += c * r
            s = remainder[c:]
            continue
        if not m:
            raise Exception(f"no match for {s}")

        c_str, r_str, remainder = m.groups()
        c = int(c_str)
        r = int(r_str)
        total += decompress(remainder[:c]) * r + decompress(remainder[c:])
        completed = True
    return total


# def decompress(s):
#     remaining = s[:]
#     length = 0
#     completed = False
#     while not completed:
#         data_prefix = data_regex.search(remaining)
#         marker_prefix = marker_regex.search(remaining)
#         if not data_prefix and not marker_prefix:
#             completed = True
#         elif data_prefix:
#
#             data, rest = data_prefix.groups()
#             result += data
#             remaining = rest
#         else:
#             c_str, n_str, suffix = marker_prefix.groups()
#             c = int(c_str)
#             n = int(n_str)
#             repeat_unit = suffix[:c] * n
#             result += repeat_unit
#             remaining = suffix[c:]
#     return result


if __name__ == "__main__":
    pass  # not solved yet
    # print(f"Decompressed length: {len(decompress(read_input()))}")
