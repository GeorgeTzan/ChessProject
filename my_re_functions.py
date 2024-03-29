import re


def get_winner(text):
    match = re.search(r'\[Result "(.+)"', text)
    if match:
        match = match.group(1)
        if match == "1-0":
            return "ΛΕΥΚΑ"
        elif match == "0-1":
            return "ΜΑΥΡΑ"
        elif match == "1/2-1/2":
            return "ΙΣΟΠΑΛΙΑ"


def get_elo_diff(text):
    elo_pattern = r'\[WhiteElo "(.+)"', r'\[BlackElo "(.+)"'
    match = re.search(elo_pattern[0], text), re.search(elo_pattern[1], text)
    if match:
        return abs(int(match[0].group(1)) - int(match[1].group(1)))


def get_date(text):
    date_pattern = r'\[Date "(.+)"'
    match = re.search(date_pattern, text)
    if match:
        date = match.group(1).replace(".", "-")
        date = date[-2:] + "-" + date[-5:-3] + "-" + date[:4]
        return date


def get_moves(text):
    moves_pattern = r"\d+\.[a-zA-Z]+"
    match = re.findall(moves_pattern, text)
    return len(match)
