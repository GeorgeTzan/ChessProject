from my_re_functions import *


def main():
    file_path = "WorldChamp2023.pgn"

    with open(file_path, "r") as file:
        pgn_text = file.read().strip()

    games = pgn_text.split("\n\n")

    for iter in range(len(games)):

        if iter % 2 == 0 or iter == 0:
            winner = get_winner(games[iter])
            elo_diff = get_elo_diff(games[iter])
            date = get_date(games[iter])
            moves_count = get_moves(games[iter + 1])
            print("Winner:", winner)
            print("Elo Difference:", elo_diff)
            print("Game Date:", date)
            print("Moves Count:", moves_count)
            print("-------------")


if __name__ == "__main__":
    main()
