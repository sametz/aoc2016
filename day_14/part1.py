from collections import Counter, defaultdict, deque
import hashlib


def read_secret_key(filename):
    with open(filename) as f:
        return f.read().strip()


def has_triplet(c, s):
    return c * 3 in s


def in_history(c, history):
    for h in history:
        if c in h:
            return True
    return False


def main(key):
    i = 0
    history = deque(maxlen=1001)
    keys = []
    fives = defaultdict(list)
    while len(keys) < 100:
        if i == 39 or i == 816 or i == 1039:
            pass
        h = hashlib.md5((key + str(i)).encode()).hexdigest()
        c = Counter(h)
        maybe5 = [k for k, v in c.items() if v > 4]
        for m5 in maybe5:
            if m5 * 5 in h:
                fives[m5].append(i)
        maybe3 = [k for k, v in c.items() if v > 2]
        threes = []
        for m3 in maybe3:
            if m3 * 3 in h:
                threes.append(m3)
        history.append((i, threes))
        if i >= 1000:
            if history[0][1]:
                three_loc, threes = history[0]
                for t in threes:
                    if t in fives:
                        fives[t] = [s for s in fives[t] if s > three_loc]
                        if fives[t] and fives[t][0] <= three_loc + 1000:
                            keys.append(three_loc)
                            print(
                                f"i = {three_loc} has three {t} in {hashlib.md5((key + str(three_loc)).encode()).hexdigest()} and five {t} in {hashlib.md5((key + str(fives[t][0])).encode()).hexdigest()}")
        i += 1
    print(keys)
    print(len(keys))
    return (keys[63])


if __name__ == "__main__":
    key = "abc"
    n = 18
    h = hashlib.md5((key + str(n)).encode()).hexdigest()
    print(h)
    c = Counter(h)
    print(c)
    maybe3 = [k for k, v in c.items() if v > 2]
    threes = [m for m in maybe3 if m * 3 in h]
    print(threes)
