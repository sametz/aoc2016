from collections import Counter
import re
import string

room_regex = re.compile(r"^(\D+)-(\d+)\[(\w+)\]")


def parse_input(filename):
    rooms = []
    with open(filename) as f:
        for line in f:
            body, id, checksum = room_regex.match(line).groups()
            # body = raw_body.replace("-", "")
            rooms.append((body, int(id), checksum))
    return rooms


def checksum(s):
    s_stripped = s.replace("-", "")
    c = Counter(s_stripped).most_common()
    # -x[1] results in numbers sorted largest to smallest
    c_sorted = sorted(c, key=lambda x: (-x[1], x[0]))  # TIL
    checksum = ""
    for letter, _ in c_sorted[:5]:
        checksum += letter
    return checksum


def valid_rooms(r):
    rooms = []
    for s, id, c in r:
        if checksum(s) == c:
            rooms.append((s, id))
    return rooms


def rot_n(s, n):
    a = string.ascii_lowercase
    shift = n % 26
    rot_n_table = str.maketrans(a, a[shift:] + a[:shift])
    return s.translate(rot_n_table)


def main(filename):
    rooms = parse_input(filename)
    v = valid_rooms(rooms)
    for room_name, id in v:
        decoded_name = rot_n(room_name, id)
        if "north" in decoded_name:
            print(decoded_name, id)


if __name__ == "__main__":
    main("input.txt")
