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


def next_states(state):
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
                next_state = tuple(doodads[:i] + [(f, f)] + doodads[i + 1 :] + [f])
                if is_safe(next_state) and next_state not in next_states:
                    next_states.append(next_state)
            # other_doodads = doodads[:i] + doodads[i + 1:]
            # other_generator_floors = [g for _, g in other_doodads]
            # if f not in other_generator_floors:
            #     new_doodad_state = (f, doodads[i][1])
            #     next_state = tuple(doodads[:i] + new_doodad_state + doodads[i + 1:] + [f])
            #     if next_state not in next_states:
            #         next_states.append(next_state)

            # single chip move
            next_state = tuple(
                doodads[:i] + [(f, doodads[i][1])] + doodads[i + 1 :] + [f]
            )
            if (
                doodads[i][0] == current_floor
                and is_safe(next_state)
                and next_state not in next_states
            ):
                next_states.append(next_state)
                movable_chips.append(i)
            # single generator move
            next_state = tuple(doodads[:i] + [(doodads[0], f)] + doodads[i + 1 :] + [f])
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
                        + doodads[i1 + 1 : i2]
                        + [(f, doodads[i2][1])]
                        + doodads[i2 + 1 :]
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
                        + doodads[i1 + 1 : i2]
                        + [(doodads[i2][0], f)]
                        + doodads[i2 + 1 :]
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


def move_duos(state):
    pass
