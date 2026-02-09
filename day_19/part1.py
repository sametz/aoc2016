# I think this can be done with clever slicing. The basic algorithm would be:
# - start with a [1::2] slice
# - if the last slice item is the last item of the list, next slice is [1::2],
# otherwise next slice is [::2]


def read_input():
    with open("input.txt", "r") as f:
        n_str = f.read().strip()
        return int(n_str)


def next_round(previous_n, previous_players_odd):
    if previous_players_odd and previous_n == 0:  # slice ended on last item:
        return 1  # the first player will be skipped
    elif not previous_players_odd and previous_n == 1:  # ditto
        return 1
    return 0


def play_game(players):
    n = 0
    while len(players) > 1:
        odd_players = len(players) % 2 == 1
        players = players[n::2]
        n = next_round(n, odd_players)
    return players[0]


if __name__ == "__main__":
    secret_number = read_input()
    print(f"Winner: {play_game(range(1, secret_number + 1))}")
