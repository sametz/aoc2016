def read_input():
    with open("input.txt") as f:
        return f.read().strip()


def is_trap(triad):
    match triad:
        case "^^.":
            return True
        case ".^^":
            return True
        case "^..":
            return True
        case "..^":
            return True
        case _:
            return False


def next_row(row):
    padded_row = "." + row + "."
    new_row = ""
    for i in range(len(padded_row) - 2):
        triad = padded_row[i : i + 3]
        if is_trap(triad):
            new_row += "^"
        else:
            new_row += "."
    return new_row


def tile_grid(first_row, total_rows):
    tiles = [first_row]
    current_row = first_row
    while len(tiles) < total_rows:
        current_row = next_row(current_row)
        tiles.append(current_row)
    return tiles


def safe_tiles(grid):
    return sum(row.count(".") for row in grid)


if __name__ == "__main__":
    print(f"Safe tiles: {safe_tiles(tile_grid(read_input(), 40))}")
