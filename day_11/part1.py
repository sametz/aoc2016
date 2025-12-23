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
moves = 0
move_dict = {INITIAL_TEST_STATE: moves}
frontier = Queue()


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
        next_states += move_double_chips(state, f)
        next_states += move_double_generators(state, f)
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


def move_single_generators(state, f): pass


def move_double_chips(state, f): pass


def move_double_generators(state, f): pass


def old_next_states(state):
    current_floor = state[-1]
    doodads = list(state[:-1])
    if set(doodads) == {(4, 4)}:
        return None  # end goal achieved
    next_floors = {current_floor - 1, current_floor + 1} & {1, 2, 3, 4}
    next_states = []
    for f in next_floors:
        movable_chips = []  # indices for movable chips
        movable_generators = []  # indices for movable generators
        for i in range(len(doodads)):
            # safely move a pair, or move to create a pair
            if (
                    doodads[i] == (current_floor, current_floor)
                    or doodads[i] == (current_floor, f)
                    or doodads[i] == (f, current_floor)
            ):
                next_state = tuple(doodads[:i] + [(f, f)] + doodads[i + 1:] + [f])
                if is_safe(next_state) and next_state not in next_states:
                    next_states.append(next_state)
            # other_doodads = doodads[:i] + doodads[i + 1:]
            # other_generator_floors = [g for _, g in other_doodads]
            # if f not in other_generator_floors:
            #     new_doodad_state = (f, doodads[i][1])
            #     next_state = tuple(doodads[:i] + new_doodad_state + doodads[i + 1:] + [f])
            #     if next_state not in old_next_states:
            #         old_next_states.append(next_state)

            # single chip move
            next_state = tuple(
                doodads[:i] + [(f, doodads[i][1])] + doodads[i + 1:] + [f]
            )
            if (
                    doodads[i][0] == current_floor
                    and is_safe(next_state)
                    and next_state not in next_states
            ):
                next_states.append(next_state)
                movable_chips.append(i)
            # single generator move
            next_state = tuple(doodads[:i] + [(doodads[0], f)] + doodads[i + 1:] + [f])
            if (
                    doodads[i][1] == current_floor
                    and is_safe(next_state)
                    and next_state not in next_states
            ):
                next_states.append(next_state)
                movable_generators.append(i)
            # double chip move
            if len(movable_chips) > 1:
                pairs = combinations(movable_chips, 2)
                for i1, i2 in pairs:
                    new_state = tuple(
                        doodads[:i1]
                        + [(f, doodads[i1][1])]
                        + doodads[i1 + 1: i2]
                        + [(f, doodads[i2][1])]
                        + doodads[i2 + 1:]
                        + [f]
                    )
                    if is_safe(new_state) and new_state not in next_states:
                        next_states.append(new_state)
            # double generator move
            if len(movable_generators) > 1:
                pairs = combinations(movable_generators, 2)
                for i1, i2 in pairs:
                    new_state = tuple(
                        doodads[:i1]
                        + [(doodads[i1][0], f)]
                        + doodads[i1 + 1: i2]
                        + [(doodads[i2][0], f)]
                        + doodads[i2 + 1:]
                        + [f]
                    )
                    if is_safe(new_state) and new_state not in next_states:
                        next_states.append(new_state)
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
