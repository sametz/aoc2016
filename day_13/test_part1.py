from part1 import is_wall, main


def test_is_wall():
    assert not is_wall(1, 1, 10)
    assert is_wall(1, 0, 10)
    assert not is_wall(0, 1, 10)


def test_main():
    assert main(10, 7, 4) == 11
