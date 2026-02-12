from itertools import pairwise


def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f.readlines():
            low_str, high_str = line.split("-")
            result.append([int(low_str), int(high_str)])
    return result


def condense_ranges(ip_list):
    ip_list.sort()
    n = len(ip_list)
    result = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if ip_list[j][0] > ip_list[i][1]:
                break
            if ip_list[j][0] < ip_list[i][1]:
                if ip_list[j][1] > ip_list[i][1]:
                    ip_list[i][1] = ip_list[j][1]
        result.append(ip_list[i])
    return result


def lowest_allowed(forbidden):
    if forbidden[0][0] != 0:  # we know there is a zero though
        return 0  # but including this safeguard anyways
    for range1, range2 in pairwise(forbidden):
        candidate = range1[1] + 1
        if candidate < range2[0]:
            return candidate
    return 4294967295  # everything forbidden


def main(filename):
    forbidden = read_input(filename)
    return lowest_allowed(condense_ranges(forbidden))


if __name__ == "__main__":
    print(f"Lowest-valued IP: {main('input.txt')}")
