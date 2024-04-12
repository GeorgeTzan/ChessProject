# Chess Game Analyzer 
[Github/ChessProject](https://github.com/georgetzan/ChessProject)

## Εισαγωγή

Αυτό το πρόγραμμα αναλύει παιχνίδια σκακιού από ένα αρχείο PGN και επεξεργάζεται τα δεδομένα ώστε να παρουσιάσει πληροφορίες όπως τον νικητή, η διαφορά τους στα Elo ratings, η ημερομηνία και τον αριθμό των κινήσεων για κάθε παιχνίδι.

## Introduction

This program analyzes chess games from a PGN file and processes the data to present information such as the winner, their Elo rating difference, the date, and the number of moves for each game.

## Προεπισκόπηση

Το πρόγραμμα αποτελείται από τέσσερα βασικά αρχεία:

- `erotima1.py`: Κύριο αρχείο που εκτελεί την ανάλυση των παιχνιδιών.
- `erotima2.py`: Δευτερέυον αρχείο το οποιο εκτελέι ανάλυση ημερομηνιών σε 54727 παρτίδες με γραφικά αποτελέσματα.
- `my_re_functions.py`: Περιέχει τις συναρτήσεις για την επεξεργασία των δεδομένων PGN χρησιμοποιώντας τη βιβλιοθήκη `re`.
- `test_my_re_functions.py`: Περιέχει κώδικα unittest το οποίο δοκιμάζει τις συναρτήσεις ενός παιχνιδιού.

## Preview

The program consists of four main files:

- `erotima1.py`: Main file that performs the game analysis.
- `erotima2.py`: second file that performs date analysis on 54727 games and shows statistical graph.
- `my_re_functions.py`: Contains functions for processing PGN data using the `re` library.
- `test_my_re_functions.py`: Contains unittests that perform tests on a game.


## Installation - Εγκατάσταση
```bash
pip install -r requirements.txt
```

## Run - Εκτέλεση
```bash 
python erotima1.py -i/--input WorldChamp2023.pgn
python erotima2.py -i/--input RetiKIA.pgn
python test_my_re_functions.py
```
## Άδεια Χρήσης

Το πρόγραμμα διατίθεται υπό την άδεια MIT. Δείτε το αρχείο [LICENSE](LICENSE) για περισσότερες πληροφορίες.

## License

This program is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
