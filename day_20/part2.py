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
    ignore = []
    for i in range(n - 1):
        # i_tuple = ip_list[i]  # for debugging
        if ip_list[i] in ignore:
            continue
        for j in range(i + 1, n):
            # j_tuple = ip_list[j]  # for debugging
            if ip_list[j][0] > ip_list[i][1] + 1:
                break
            elif ip_list[j][1] > ip_list[i][1]:
                ip_list[i][1] = ip_list[j][1]
            ignore.append(ip_list[j])
        result.append(ip_list[i])
    if ip_list[-1][0] > result[-1][1] + 1:
        result.append(ip_list[-1])

    return result


def count_allowed(forbidden, max_value):
    sum = 0
    if forbidden[0][0] > 0:  # not true for my data however
        sum += forbidden[0][0]
    for range1, range2 in pairwise(forbidden):
        sum += range2[0] - range1[1] - 1
    if forbidden[-1][1] < max_value:
        sum += max_value - forbidden[-1][1]
    return sum


def main(filename, max_value):
    forbidden = read_input(filename)
    print(len(forbidden))
    forbidden_condensed = condense_ranges(forbidden)
    print(len(forbidden_condensed))
    return count_allowed(forbidden_condensed, max_value)


if __name__ == "__main__":
    print(f"Number of valid IPs: {main('input.txt', 4294967295)}")
