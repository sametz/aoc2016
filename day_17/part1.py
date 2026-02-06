import hashlib
from queue import Queue

U = 0 - 1j
D = 0 + 1j
L = -1 + 0j
R = 1 + 0j

UDLR = [U, D, L, R]
UDLR_DICT = {U: "U", D: "D", L: "L", R: "R"}


def read_input():
    # So my input is not revealed on GitHub
    with open("input.txt") as f:
        hash_ = f.read().strip()
    return hash_


def open_doors(h):
    udlr = hashlib.md5(h.encode()).hexdigest()[:4]
    udlr_bool = []
    for c in udlr:
        udlr_bool.append(c in "bcdef")
    return udlr_bool


def in_bounds(c):
    return c.real in range(4) and c.imag in range(4)


def next_states(state):
    # state will be pos, old hash
    # return will be new_pos, new_hash
    old_pos, old_hash = state
    new_states = []
    egress = open_doors(old_hash)
    # print("egress: ", egress)
    allowed_egress = [dir_ for dir_, is_open in zip(UDLR, egress) if is_open]
    # print("allowed egress: ", allowed_egress)
    for dir_ in allowed_egress:
        new_pos = old_pos + dir_
        if in_bounds(new_pos):
            new_hash = old_hash + UDLR_DICT[dir_]
            new_states.append((new_pos, new_hash))
    return new_states


def main(h):
    pos = 0 + 0j
    visited_states = [(0 + 0j, h)]
    complete_paths = []
    frontier = Queue()
    frontier.put((pos, h))
    # need to implement queue
    while not frontier.empty():
        ns = next_states((frontier.get()))
        for next_state in ns:
            next_pos, next_h = next_state
            if next_state in visited_states:
                continue
            if next_pos == 3 + 3j:
                complete_paths.append(next_h[len(h):])
            else:
                frontier.put(next_state)
            visited_states.append(next_state)
    assert complete_paths
    return min(complete_paths, key=len)


if __name__ == '__main__':
    print(f"shortest path: {main(read_input())}")
