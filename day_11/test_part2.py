import pytest

from part2 import (occupied_floors, active_floors, next_states, move_duos,
                   move_single_chips, move_single_generators, move_two_chips,
                   move_two_generators, INITIAL_TEST_STATE, FINAL_TEST_STATE,
                   main)


def test_occupied_floors():
    state = ((2, 3), (3, 4), 1)
    assert occupied_floors(state) == {2, 3, 4}


def test_remaining_floors():
    state = ((2, 3), (3, 4), 2)
    assert active_floors(state) == {2, 3, 4}


def test_final_state():
    state = ((4, 4), (4, 4), 4)
    assert next_states(state) is None


def test_move_duos():
    state = ((1, 3), (2, 2), 2)
    assert ((1, 3), (3, 3), 3) in move_duos(state, 3)
    assert ((1, 1), (1, 3), 1) not in move_duos(state, 1)
    state = ((2, 2), (3, 1), 2)
    assert ((1, 1), (3, 1), 1) in move_duos(state, 1)
    assert ((3, 1), (3, 3), 3) not in move_duos(state, 3)


def test_move_single_chips():
    state = ((2, 3), (4, 1), 2)
    assert move_single_chips(state, 3) == [((3, 3), (4, 1), 3)]
    state = ((2, 3), (4, 1), 2)
    assert move_single_chips(state, 1) == []


def test_move_single_generators():
    state = ((3, 2), (4, 1), 2)
    assert move_single_generators(state, 3) == [((3, 3), (4, 1), 3)]
    state = ((1, 4), (3, 2), 2)
    assert move_single_generators(state, 1) == []
    assert move_single_generators(state, 3) == [((1, 4), (3, 3), 3)]


def test_move_two_chips():
    state = ((2, 3), (2, 3), 2)
    assert move_two_chips(state, 3) == [((3, 3), (3, 3), 3)]


def test_move_two_generators():
    state = ((2, 3), (2, 3), 3)
    assert move_two_generators(state, 2) == [((2, 2), (2, 2), 2)]


@pytest.mark.parametrize(
    "state1, state2",
    [
        (((1, 2), (1, 3), 1), ((1, 3), (2, 2), 2)),
        (((1, 3), (2, 2), 2), ((1, 3), (3, 3), 3)),
        (((1, 3), (3, 3), 3), ((1, 3), (2, 3), 2)),
        (((1, 3), (2, 3), 2), ((1, 3), (1, 3), 1)),
        (((1, 3), (1, 3), 1), ((2, 3), (2, 3), 2)),
        (((2, 3), (2, 3), 2), ((3, 3), (3, 3), 3)),
        (((3, 3), (3, 3), 3), ((4, 3), (4, 3), 4)),
        (((4, 3), (4, 3), 4), ((3, 3), (4, 3), 3)),
        (((3, 3), (4, 3), 3), ((3, 4), (4, 4), 4)),
        (((3, 4), (4, 4), 4), ((3, 4), (3, 4), 3)),
        (((3, 4), (3, 4), 3), ((4, 4), (4, 4), 4)),
    ],
)
def test_steps(state1, state2):
    assert state2 in next_states(state1)


def test_main():
    assert main(INITIAL_TEST_STATE, FINAL_TEST_STATE) == 11
