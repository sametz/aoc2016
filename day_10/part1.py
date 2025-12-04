from collections import defaultdict
import re

add_value_regex = re.compile(r"value (\d+) goes to bot (\d+)")
split_regex = re.compile(
    r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
)

bots = defaultdict(list)
outputs = defaultdict(list)
receivers = {"bot": bots, "output": outputs}

TARGET_COMPARISON_TEST = {"5", "2"}
TARGET_COMPARISON = {"61", "17"}


def read_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def compile_instructions(filename):
    text_instructions = read_input(filename)
    result = []
    for text in text_instructions:
        if text.startswith("value"):
            result.append(add_value_regex.match(text).groups())
        else:
            result.append(split_regex.match(text).groups())
    return result


def dispatch(instruction, r, target=TARGET_COMPARISON):
    if len(instruction) == 2:
        chip, bot = instruction
        if len(r["bot"][bot]) < 2:
            r["bot"][bot].append(chip)
            return True
        else:
            return False

    compare_bot, low_holder, low_n, high_holder, high_n = instruction
    if len(r["bot"][compare_bot]) != 2:
        return False
    if len(r[low_holder][low_n]) >= 2 or len(r[high_holder][high_n]) >= 2:
        return False
    low_chip = min(r["bot"][compare_bot])
    high_chip = max(r["bot"][compare_bot])
    if {low_chip, high_chip} == target:
        print(f"bot {compare_bot} is comparing {low_chip} and {high_chip}")
        return compare_bot
    r[low_holder][low_n].append(low_chip)
    r[high_holder][high_n].append(high_chip)
    r["bot"][compare_bot] = list()
    return True


def main(filename, target):
    instructions = compile_instructions(filename)
    complete = False
    while not complete:
        next_instructions = []
        for instruction in instructions:
            result = dispatch(instruction, receivers, target=target)
            if isinstance(result, str):
                return result
            if not result:
                next_instructions.append(instruction)
        instructions = next_instructions
        if len(instructions) == 0:
            print("No more instructions")
            complete = True


if __name__ == "__main__":
    main("input.txt", TARGET_COMPARISON)  # 89 is not the answer
