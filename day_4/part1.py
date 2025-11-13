from collections import Counter
import re

room_regex = re.compile(r"^(\D+)-(\d+)\[(\w+)\]")


def parse_input(filename):
    rooms = []
    with open(filename) as f:
        for line in f:
            raw_body, id, checksum = room_regex.match(line).groups()
            body = raw_body.replace("-", "")
            rooms.append((body, int(id), checksum))
    return rooms


def checksum(s):
    c = Counter(s).most_common()
    # -x[1] results in numbers sorted largest to smallest
    c_sorted = sorted(c, key=lambda x: (-x[1], x[0]))  # TIL
    checksum = ""
    for letter, _ in c_sorted[:5]:
        checksum += letter
    return checksum


def valid_ids(rooms):
    valid_ids = []
    for s, id, c in rooms:
        if checksum(s) == c:
            valid_ids.append(id)
    return valid_ids


def main(filename):
    rooms = parse_input(filename)
    print(sum(valid_ids(rooms)))


if __name__ == "__main__":
    main("input.txt")
