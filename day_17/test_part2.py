from part2 import read_input, open_doors, in_bounds, next_states, main


def test_read_input():
    i = read_input()
    assert len(i) == 8
    assert i.startswith("g")
    assert i.endswith("y")


def test_open_doors():
    assert open_doors("hijkl") == [True, True, True, False]


def test_in_bounds():
    assert in_bounds(0 + 0j)
    assert in_bounds(3 + 3j)
    assert not in_bounds(-1 + 0j)
    assert not in_bounds(4 + 0j)
    assert not in_bounds(0 - 1j)
    assert not in_bounds(0 + 4j)


def test_next_states():
    assert next_states((0 + 0j, "hijkl")) == [(0 + 1j, "hijklD")]


def test_main():
    assert main("ihgpwlah") == 370
    assert main("kglvqrro") == 492
    assert main("ulqzkmiv") == 830
