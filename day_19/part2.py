import math


def read_input():
    with open("input.txt", "r") as f:
        n_str = f.read().strip()
        return int(n_str)


def play_game(players):
    """This is a slow algorithm that closely models a game."""
    while len(players) > 1:
        if players[0] == min(players):
            print(f"start: {len(players)} players: \n{players}")
        loser = len(players) // 2
        print(f"dropping: {players[loser]}")
        players = players[1:loser] + players[loser + 1 :] + players[0:1]
    return players[0]


# tested play_game with 100 players to detect pattern
def find_pattern():
    results = []
    for i in range(2, 101):
        players = list(range(1, i + 1))
        results.append((i, play_game(players)))
    for game in results:
        print(game)


def survivor_from_pattern(n):
    low_power = math.floor(math.log(n, 3))
    low_n = 3**low_power
    high_n = 3 ** (low_power + 1)

    if low_n == n:
        return n
    if n > low_n and n <= (high_n - low_n):
        return n - low_n
    return 2 * n - high_n


if __name__ == "__main__":
    secret_number = read_input()
    print(f"Survivor: {survivor_from_pattern(secret_number)}")
