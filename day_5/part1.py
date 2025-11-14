import hashlib


def read_input():
    # So my input is not revealed on GitHub
    with open("input.txt") as f:
        hash = f.read().strip()
    return hash


# See AOC2015 Day 4 for example of using hashlib
def main():
    key = read_input()
    n = 1
    password = ""
    while len(password) < 8:
        h = hashlib.md5((key + str(n)).encode()).hexdigest()
        if h[:5] == "00000":
            password += h[5]
        n += 1

    print('answer: ', password)


if __name__ == '__main__':
    main()
