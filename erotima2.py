from my_re_functions import *
from datetime import datetime
import matplotlib.pyplot as plt

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


def main():
    file_path = "RetiKIA.pgn"

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
    main()
    print(days)
    fig, ax = plt.subplots()
    ax.bar(days_names, days)

    ax.set_title("Games played for each day")
    ax.set_xlabel("Day of the week")
    ax.set_ylabel("Times played")
    plt.show()
