from part1 import read_grid, main


def test_read_grid():
    grid, dims, digits, origin = read_grid("test_input.txt")
    assert dims == (11, 5)
    assert digits == {"1", "2", "3", "4"}
    assert origin == 1 + 1j
    assert grid[0 + 0j] == "#"
    assert grid[1 + 1j] == "0"
    assert grid[9 + 3j] == "3"
    assert grid[8 + 3j] == "."
    assert grid[10 + 4j] == "#"


def test_main():
    args = read_grid("test_input.txt")
    assert main(*args) == 14
