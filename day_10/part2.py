# In retrospect, should have read input with numbers as ints instead of strings.
# I thought they'd mainly be used as dict keys, but ended up doing substantial
# math with them.

from collections import defaultdict
import re

add_value_regex = re.compile(r"value (\d+) goes to bot (\d+)")
split_regex = re.compile(
    r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
)

bots = defaultdict(list)
outputs = defaultdict(list)
receivers = {"bot": bots, "output": outputs}

TARGET_COMPARISON_TEST = {5, 2}
TARGET_COMPARISON = {61, 17}


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


def dispatch(instruction, r, target):
    if len(instruction) == 2:
        chip, bot = instruction
        if len(r["bot"][bot]) < 2:
            r["bot"][bot].append(chip)
            print(f"bot {bot} was given chip {chip}")
            return True
        else:
            return False

    compare_bot, low_holder, low_n, high_holder, high_n = instruction
    if len(r["bot"][compare_bot]) != 2:
        return False
    if len(r[low_holder][low_n]) >= 2 or len(r[high_holder][high_n]) >= 2:
        return False
    chips = [int(chip) for chip in r["bot"][compare_bot]]
    low_chip = min(chips)
    high_chip = max(chips)

    r[low_holder][low_n].append(str(low_chip))
    r[high_holder][high_n].append(str(high_chip))
    r["bot"][compare_bot] = list()
    print(
        f"{low_holder} {low_n} received {low_chip}; {high_holder} {high_n} received {high_chip}"
    )
    if low_chip == 2 and high_chip == 5:
        pass
    if {low_chip, high_chip} == target:
        print(f"bot {compare_bot} is comparing {low_chip} and {high_chip}")
        return compare_bot
    return True


def main(filename, target):
    instructions = compile_instructions(filename)
    passes = 1
    complete = False
    part1_bot = None
    while not complete:
        print(f"{'='*10} Pass {passes} {'='*10}")
        next_instructions = []
        for instruction in instructions:
            result = dispatch(instruction, receivers, target=target)
            if isinstance(result, str):
                part1_bot = result
            if not result:
                # print(f"impossible instruction: {instruction}")
                next_instructions.append(instruction)

        passes += 1
        if len(instructions) == len(next_instructions):
            print("No more instructions")
            complete = True
        instructions = next_instructions
    print(f"{receivers['output']['0']}, {receivers['output']['1']}, {receivers['output']['2']}")
    print(receivers)
    return part1_bot

if __name__ == "__main__":
    main("input.txt", TARGET_COMPARISON)
    print(f"Part 2 answer: {int(receivers['output']['0'][0]) * int(receivers['output']['1'][0]) * int(receivers['output']['2'][0])}")