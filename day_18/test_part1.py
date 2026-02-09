from part1 import read_input, next_row, tile_grid, safe_tiles


def test_read_input():
    i = read_input()
    assert i.startswith(".")
    assert i.endswith("^")


def test_next_row():
    assert next_row("..^^.") == ".^^^^"


def test_tile_grid():
    assert tile_grid("..^^.", 3) == ["..^^.", ".^^^^", "^^..^"]


def test_safe_tiles():
    assert safe_tiles(tile_grid(".^^.^.^^^^", 10)) == 38
