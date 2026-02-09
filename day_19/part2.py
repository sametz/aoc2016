# Algorithm: len(players) // 2 is player to eliminate


def read_input():
    with open("input.txt", "r") as f:
        n_str = f.read().strip()
        return int(n_str)


def play_game(players):
    while len(players) > 1:
        loser = len(players) // 2
        players = players[1:loser] + players[loser + 1:] + players[0:1]
    return players[0]


if __name__ == "__main__":
    secret_number = read_input()
    print(f"Winner: {play_game(list(range(1, secret_number + 1)))}")
