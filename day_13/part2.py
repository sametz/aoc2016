from queue import Queue
import sys


def is_wall(x, y, favorite_number):
    if x < 0 or y < 0:
        return True
    n = x * x + 3 * x + 2 * x * y + y + y * y + favorite_number
    return n.bit_count() % 2 == 1


def main(favorite_number):
    starting_pos = 1 + 1j
    moves = 0
    move_dict = {starting_pos: moves}
    frontier = Queue()
    frontier.put(1 + 1j)

    while not frontier.empty():
        current_pos = frontier.get()
        moves = move_dict[current_pos]
        if moves + 1 > 50:
            continue
        next_pos = [current_pos - 1, current_pos + 1, current_pos - 1j, current_pos + 1j]
        for p in next_pos:
            if not is_wall(int(p.real), int(p.imag), favorite_number):
                better_p = False
                if p not in move_dict:
                    better_p = True
                elif move_dict[p] > moves + 1:
                    better_p = True
                if better_p:
                    move_dict[p] = moves + 1
                    frontier.put(p)
    return len(move_dict.keys())


if __name__ == "__main__":
    with open("input.txt") as f:
        secret_number = int(f.read().strip())
    print(f"Answer: {main(secret_number)}")
