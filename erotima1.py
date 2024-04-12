import argparse

from my_re_functions import *


def main(file_path):

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
    parser = argparse.ArgumentParser(description="Process a PGN file.")
    parser.add_argument(
        "-i", "--input", type=str, help="The path to the PGN file", required=True
    )

    args = parser.parse_args()

    main(args.input)
