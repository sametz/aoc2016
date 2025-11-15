import sys
from collections import defaultdict
import hashlib


def read_input():
    # So my input is not revealed on GitHub
    with open("input.txt") as f:
        hash = f.read().strip()
    return hash


# See AOC2015 Day 4 for example of using hashlib
def main():
    id = read_input()
    password_dict = defaultdict(lambda: None)
    password = ""
    n = 1
    while len(password_dict) < 8:
        h = hashlib.md5((id + str(n)).encode()).hexdigest()
        if h[:5] == "00000" and len(h) >= 7 and h[5] in "01234567":
            key, val = h[5], h[6]
            if password_dict[key] is None:
                password_dict[key] = val
        n += 1
    print(password_dict)
    for i in range(8):
        password += password_dict[str(i)]
    print("answer: ", password)


if __name__ == "__main__":
    main()
