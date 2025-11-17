def read_input(filename):
    with open(filename) as f:
        ips = f.read().splitlines()
    return ips


# def has_aba(s):
#     if len(s) < 3:
#         return False
#     for i in range(len(s) - 2):
#         chunk = s[i : i + 3]
#         if chunk == chunk[::-1] and chunk[0] != chunk[1]:
#             return chunk
#     return None


def supports_ssl(ip):
    chunks = ip.split("]")
    supernets = []
    hypernets = []
    for chunk in chunks:
        if "[" in chunk:
            outer, inner = chunk.split("[")
        else:
            outer, inner = chunk, ""
        if len(outer) >= 3:
            supernets.append(outer)
        if len(inner) >= 3:
            hypernets.append(inner)
    for s in supernets:
        for i in range(len(s) - 2):
            chunk = s[i : i + 3]
            if chunk == chunk[::-1] and chunk[0] != chunk[1]:
                bab = chunk[1] + chunk[0] + chunk[1]
                for h in hypernets:
                    if bab in h:
                        return True
    return False


def count_ssl_ips(ips):
    valid = 0
    for ip in ips:
        if supports_ssl(ip):
            valid += 1
    return valid


if __name__ == "__main__":
    ips = read_input("input.txt")
    print(f"IPs supporting TLS: {count_ssl_ips(ips)}")
