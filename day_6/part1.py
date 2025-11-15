from collections import Counter


def read_input(filename):
    with open(filename) as f:
        messages = f.read().splitlines()
    return messages


def transpose(m):
    return list(zip(*m))


def denoise(m):
    consensus = ""
    for column in transpose(m):
        c = Counter(column)
        consensus += c.most_common()[0][0]
    return consensus


if __name__ == "__main__":
    print(f"message: {denoise(read_input('input.txt'))}")
