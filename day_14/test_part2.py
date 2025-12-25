from part2 import find_triplet, long_hash, main


# Found reason why test answer was my 68th key not my 64th:
# "Only consider the first such triplet in a hash"
# e.g. 534 is 4fc7df57777400b3eeef5350a6eecbdf so it counts the 7 not the 3


def test_find_triplet():
    assert find_triplet("44fc7df57777400b3eeef5350a6eecbdf") == "7"


def test_long_hash():
    assert long_hash("abc0") == "a107ff634856bb300138cac6568c0f24"


def test_main():
    assert main("abc") == 22551
