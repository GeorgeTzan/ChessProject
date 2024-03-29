import re


def get_winner(text):
    """
    Extracts the winner of the chess game from the PGN.
    Args:
        text(str): The PGN text.
    Returns
        str: the winner of the game (ΛΕΥΚΑ, ΜΑΥΡΑ OR ΙΣΟΠΑΛΙΑ)
    """
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
    """
    Extracts the elo rating difference between the two players.
    Args:
        text(str): The PGN text.
    Returns
        int: The absolute Elo rating difference of the two players.
    """
    elo_pattern = r'\[WhiteElo "(.+)"', r'\[BlackElo "(.+)"'
    match = re.search(elo_pattern[0], text), re.search(elo_pattern[1], text)
    if match:
        return abs(int(match[0].group(1)) - int(match[1].group(1)))


def get_date(text):
    """
    Extracts the date of the match.
    Args:
        text(str): The PGN text.
    Returns
        str: The date in a ΗΗ-ΜΜ-ΕΕΕΕ format.
    """
    date_pattern = r'\[Date "(.+)"'
    match = re.search(date_pattern, text)
    if match:
        date = match.group(1).replace(".", "-")
        date = date[-2:] + "-" + date[-5:-3] + "-" + date[:4]
        return date


def get_moves(text):
    """
    Extracts total moves of the game
    Args:
        text(str): The PGN text.
    Returns
        int: The total moves played in the game.
    """
    moves_pattern = r"\d+\.[a-zA-Z]+"
    match = re.findall(moves_pattern, text)
    return len(match)
