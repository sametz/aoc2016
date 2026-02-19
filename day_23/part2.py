# Part 2 is intended for you to optimize the algorithm, but I left my computer
# unattended and the unoptimized code still produced a result.

def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            line_parts = line.strip().split(" ")
            if line_parts[0] in ["cpy", "jnz"] and str(line_parts[1]) not in "abcd":
                line_parts[1] = int(line_parts[1])
            if line_parts[0] == "jnz" and str(line_parts[2]) not in "abcd":
                line_parts[2] = int(line_parts[2])
            result.append(line_parts)
    return result


def main(filename, a):
    assembly = read_input(filename)
    registers = {"a": a, "b": 0, "c": 1, "d": 0}
    toggle_dict = {"inc": "dec", "dec": "inc", "tgl": "inc", "jnz": "cpy", "cpy": "jnz"}
    i = 0
    i_max = len(assembly)
    while i < i_max:
        cmd = assembly[i][0]
        match cmd:
            case "cpy":
                if str(assembly[i][2]) in "abcd":  # in case of a toggle from jnz
                    if str(assembly[i][1]) in "abcd":
                        registers[assembly[i][2]] = registers[assembly[i][1]]
                    else:
                        registers[assembly[i][2]] = assembly[i][1]
                i += 1
            case "inc":
                registers[assembly[i][1]] += 1
                i += 1
            case "dec":
                registers[assembly[i][1]] -= 1
                i += 1
            case "tgl":
                assert assembly[i][1] in "abcd"
                n = registers[assembly[i][1]]
                if i + n < i_max:
                    assembly[i + n][0] = toggle_dict[assembly[i + n][0]]
                i += 1
            case "jnz":
                if isinstance(assembly[i][1], int):
                    n = assembly[i][1]
                else:
                    n = registers[assembly[i][1]]
                if n != 0:
                    if isinstance(assembly[i][2], int):
                        i += assembly[i][2]
                    else:
                        i += registers[assembly[i][2]]
                else:
                    i += 1
            case _:
                raise Exception("Should not reach here with cmd: ", cmd)
    return registers["a"]


if __name__ == "__main__":
    print(f"Value: {main('input.txt', 12)}")
