import argparse
from datetime import datetime

import matplotlib.pyplot as plt

from my_re_functions import *

days_names = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
days = [0, 0, 0, 0, 0, 0, 0]


def main(file_path):

    with open(file_path, "r") as file:
        pgn_text = file.read().strip()

    games = pgn_text.split("\n\n")

    for iter in range(len(games)):
        if iter % 2 == 0 or iter == 0:
            date = get_date(games[iter])
            try:
                date_obj = datetime.strptime(date, "%d-%m-%Y")
                days[date_obj.weekday()] += 1
            except ValueError:
                continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a PGN file.")
    parser.add_argument(
        "-i", "--input", type=str, help="The path to the PGN file", required=True
    )

    args = parser.parse_args()

    main(args.input)
    print(days)
    fig, ax = plt.subplots()
    ax.bar(days_names, days)

    ax.set_title("Games played for each day")
    ax.set_xlabel("Day of the week")
    ax.set_ylabel("Times played")
    plt.show()
