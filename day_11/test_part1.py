import pytest

from part1 import next_states


def test_final_state():
    state = ((4, 4), (4, 4), 4)
    assert next_states(state) is None


def test_duo_move():
    state = ((2, 2), (1, 3), 2)
    assert ((3, 3), (1, 3), 3) in next_states(state)
    assert ((1, 1), (1, 3), 1) not in next_states(state)
    state = ((3, 1), (2, 2), 2)
    assert ((3, 1), (1, 1), 1) in next_states(state)
    assert ((3, 1), (3, 3), 3) not in next_states(state)


@pytest.mark.parametrize(
    "state1, state2",
    [
        # (((1, 2), (1, 3), 1), ((2, 2), (1, 3), 2)),
        # (((2, 2), (1, 3), 2), ((3, 3), (1, 3), 3)),
        # (((3, 3), (1, 3), 3), ((2, 3), (1, 3), 2)),
        # (((2, 3), (1, 3), 2), ((1, 3), (1, 3), 1)),
        # (((1, 3), (1, 3), 1), ((2, 3), (2, 3), 2)),
        (((2, 3), (2, 3), 2), ((3, 3), (3, 3), 3)),
    ],
)
def test_steps(state1, state2):
    assert state2 in next_states(state1)
