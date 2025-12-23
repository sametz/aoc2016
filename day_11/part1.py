# until I've decided on a state representation,
# hard-coding some for test and actual cases

# state may need to be hashable, but I wanted mutability.
from itertools import combinations
from queue import Queue

INITIAL_TEST_STATE = (
    (1, 2),  # hydrogen chip, hydrogen generator floors
    (1, 3),  # lithium
    1,  # current floor
)

INITIAL_STATE = (
    (1, 1),
    (2, 1),
    (2, 1),
    (3, 3),
    (3, 3),
    1
)

FINAL_TEST_STATE = (
    (4, 4),
    (4, 4),
    4
)

FINAL_STATE = (
    (4, 4),
    (4, 4),
    (4, 4),
    (4, 4),
    (4, 4),
    4
)


def occupied_floors(state):
    doodads = state[:-1]
    chip_floors = [d[0] for d in doodads]
    generator_floors = [d[1] for d in doodads]
    return set(chip_floors + generator_floors)


def active_floors(state):
    floors = [1, 2, 3, 4]
    occupied = occupied_floors(state)
    remaining_floors = []
    for i, floor in enumerate(floors):
        if floor not in occupied:
            continue
        else:
            remaining_floors += floors[i:]
            break
    return set(remaining_floors)


def next_states(state):
    doodads = state[:-1]
    if set(doodads) == {(4, 4)}:
        return None
    current_floor = state[-1]
    remaining_floors = active_floors(state)
    next_floors = {current_floor - 1, current_floor + 1} & remaining_floors
    next_states = []
    for f in next_floors:
        next_states += move_duos(state, f)
        next_states += move_single_chips(state, f)
        next_states += move_single_generators(state, f)
        next_states += move_two_chips(state, f)
        next_states += move_two_generators(state, f)
    return next_states


def move_duos(state, f):
    doodads, current_floor = list(state[:-1]), state[-1]
    next_states = []
    for i, doodad in enumerate(doodads):
        if (
                doodad == (current_floor, current_floor)
                or doodad == (current_floor, f)
                or doodad == (f, current_floor)
        ):
            next_doodads = doodads[:i] + [(f, f)] + doodads[i + 1:]
            next_state = tuple(sorted(next_doodads) + [f])
            if is_safe(next_state) and next_state not in next_states:
                next_states.append(next_state)
    return next_states


def move_single_chips(state, f):
    doodads, current_floor = list(state[:-1]), state[-1]
    next_states = []
    for i, doodad in enumerate(doodads):
        if doodad[0] == current_floor:
            next_doodads = doodads[:i] + [(f, doodad[1])] + doodads[i + 1:]
            next_state = tuple(sorted(next_doodads) + [f])
            if (is_safe(next_state) and next_state not in next_states
            ):
                next_states.append(next_state)
    return next_states


def move_single_generators(state, f):
    doodads, current_floor = list(state[:-1]), state[-1]
    next_states = []
    for i, doodad in enumerate(doodads):
        if doodad[1] == current_floor:
            next_doodads = doodads[:i] + [(doodad[0], f)] + doodads[i + 1:]
            next_state = tuple(sorted(next_doodads) + [f])
            if is_safe(next_state) and next_state not in next_states:
                next_states.append(next_state)
    return next_states


def move_two_chips(state, f):
    doodads, current_floor = list(state[:-1]), state[-1]
    next_states = []
    movable_chip_locs = []
    for i, doodad in enumerate(doodads):
        if doodad[0] == current_floor:
            movable_chip_locs.append(i)
    if len(movable_chip_locs) > 1:
        for i1, i2 in combinations(movable_chip_locs, 2):
            new_doodad_1 = (f, doodads[i1][1])
            new_doodad_2 = (f, doodads[i2][1])
            next_doodads = (
                    doodads[:i1]
                    + [new_doodad_1]
                    + doodads[i1 + 1: i2]
                    + [new_doodad_2]
                    + doodads[i2 + 1:]
            )
            next_state = tuple(sorted(next_doodads) + [f])
            if is_safe(next_state) and next_state not in next_states:
                next_states.append(next_state)
    return next_states


def move_two_generators(state, f):
    doodads, current_floor = list(state[:-1]), state[-1]
    next_states = []
    movable_generator_locs = []
    for i, doodad in enumerate(doodads):
        if doodad[1] == current_floor:
            movable_generator_locs.append(i)
    if len(movable_generator_locs) > 1:
        for i1, i2 in combinations(movable_generator_locs, 2):
            new_doodad_1 = (doodads[i1][0], f)
            new_doodad_2 = (doodads[i2][0], f)
            next_doodads = (
                    doodads[:i1]
                    + [new_doodad_1]
                    + doodads[i1 + 1: i2]
                    + [new_doodad_2]
                    + doodads[i2 + 1:]
            )
            next_state = tuple(sorted(next_doodads) + [f])
            if is_safe(next_state) and next_state not in next_states:
                next_states.append(next_state)
    return next_states


def is_safe(state):
    doodads = state[:-1]
    generator_locs = generator_floors(doodads)
    for doodad in doodads:
        if doodad[0] != doodad[1] and doodad[0] in generator_locs:
            return False
    return True


def generator_floors(doodads):
    return [f for _, f in doodads]


def main(initial_state, final_state):
    moves = 0
    move_dict = {initial_state: moves}
    frontier = Queue()
    frontier.put(initial_state)

    while not frontier.empty():
        state = frontier.get()
        moves = move_dict[state]
        ns = next_states(state)
        if not ns:
            continue
        for next_state in ns:
            if next_state not in move_dict or move_dict[next_state] > moves + 1:
                move_dict[next_state] = moves + 1
                frontier.put(next_state)
    return move_dict[final_state]


if __name__ == "__main__":
    print(f"Number of steps needed: {main(INITIAL_STATE, FINAL_STATE)}")
