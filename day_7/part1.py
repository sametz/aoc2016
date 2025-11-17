def read_input(filename):
    with open(filename) as f:
        ips = f.read().splitlines()
    return ips


def has_abba(s):
    if len(s) < 4:
        return False
    for i in range(len(s) - 3):
        chunk = s[i : i + 4]
        if chunk == chunk[::-1] and chunk[0] != chunk[1]:
            return True
    return False


def supports_tls(ip):
    chunks = ip.split("]")
    outer_abba = False
    for chunk in chunks:
        if "[" in chunk:
            outer, inner = chunk.split("[")
        else:
            outer, inner = chunk, ""
        if has_abba(inner):
            return False
        if has_abba(outer):
            outer_abba = True
    return outer_abba


def count_tls_ips(ips):
    valid = 0
    for ip in ips:
        if supports_tls(ip):
            valid += 1
    return valid


if __name__ == "__main__":
    ips = read_input("input.txt")
    print(f"IPs supporting TLS: {count_tls_ips(ips)}")
