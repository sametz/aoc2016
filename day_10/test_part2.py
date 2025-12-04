from part2 import (
    receivers,
    TARGET_COMPARISON_TEST,
    read_input,
    compile_instructions,
    dispatch,
    main,
)


def test_read_input():
    result = read_input("test_input.txt")
    assert result[-1] == "value 2 goes to bot 2"


def test_compile_instructions():
    result = compile_instructions("test_input.txt")
    assert result == [
        ("5", "2"),
        ("2", "bot", "1", "bot", "0"),
        ("3", "1"),
        ("1", "output", "1", "bot", "0"),
        ("0", "output", "2", "output", "0"),
        ("2", "2"),
    ]


def test_dispatch():
    assert len(receivers["bot"]["2"]) == 0
    assert dispatch(("5", "2"), receivers, target=TARGET_COMPARISON_TEST)
    assert receivers["bot"]["2"] == ["5"]
    assert not dispatch(("2", "bot", "1", "bot", "0"), receivers, target=TARGET_COMPARISON_TEST)
    assert dispatch(("3", "1"), receivers, target=TARGET_COMPARISON_TEST)
    assert receivers["bot"]["1"] == ["3"]
    assert not dispatch(("1", "output", "1", "bot", "0"), receivers, target=TARGET_COMPARISON_TEST)
    assert not dispatch(("0", "output", "2", "output", "0"), receivers, target=TARGET_COMPARISON_TEST)
    assert dispatch(("2", "2"), receivers, target=TARGET_COMPARISON_TEST)
    assert receivers["bot"]["2"] == ["5", "2"]

    assert dispatch(("2", "bot", "1", "bot", "0"), receivers, target=TARGET_COMPARISON_TEST)
    assert receivers["bot"]["2"] == []
    assert receivers["bot"]["1"] == ["3", "2"]
    assert receivers["bot"]["0"] == ["5"]
    assert dispatch(("1", "output", "1", "bot", "0"), receivers, target=TARGET_COMPARISON_TEST)
    assert receivers["bot"]["1"] == []
    assert receivers["output"]["1"] == ["2"]
    assert receivers["bot"]["0"] == ["5", "3"]
    assert dispatch(("0", "output", "2", "output", "0"), receivers, target=TARGET_COMPARISON_TEST)
    assert receivers["bot"]["0"] == []
    assert receivers["output"]["2"] == ["3"]
    assert receivers["output"]["0"] == ["5"]


def test_main():
    assert main("test_input.txt", target=TARGET_COMPARISON_TEST) == "2"
