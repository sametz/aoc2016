from collections import Counter, defaultdict, deque
import hashlib
import re


def find_triplet(s):
    triplet_regex = re.compile(r"(\w)\1{2}")
    match = triplet_regex.search(s)
    if match:
        return match.group()[0]
    return None


def long_hash(s):
    h = s
    for _ in range(2017):
        h = hashlib.md5(h.encode()).hexdigest()
    return h


def read_secret_key(filename):
    with open(filename) as f:
        return f.read().strip()


def main(key):
    i = 0
    history = deque(maxlen=1001)
    keys = []
    fives = defaultdict(list)
    while len(keys) < 100:
        if i == 10:
            pass
        h = long_hash(key + str(i))
        c = Counter(h)
        maybe5 = [k for k, v in c.items() if v > 4]
        for m5 in maybe5:
            if m5 * 5 in h:
                fives[m5].append(i)
        history.append((i, find_triplet(h)))
        if i >= 1000:
            if history[0][1]:
                three_loc, c = history[0]
                if c in fives:
                    fives[c] = [s for s in fives[c] if s > three_loc]
                    if fives[c] and fives[c][0] <= three_loc + 1000:
                        keys.append(three_loc)
                        # print(
                        #     f"i = {three_loc} has three {c} in {hashlib.md5((key + str(three_loc)).encode()).hexdigest()} and five {c} in {hashlib.md5((key + str(fives[c][0])).encode()).hexdigest()}")
        i += 1
    print(keys)
    print(len(keys))
    return (keys[63])


if __name__ == "__main__":
    # key = "abc"
    key = read_secret_key("input.txt")
    print(f"64th key is: {main(key)}")
