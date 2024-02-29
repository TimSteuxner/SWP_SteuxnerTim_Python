import random
import requests

# Definition der Symbole mit Namen
symbols = ["Stein", "Papier", "Schere", "Echse", "Spock"]

# Statistiken initialisieren
stats = {"player_wins": 0, "comp_wins": 0, "draws": 0, "symbol_counts": {symbol: 0 for symbol in symbols}}


def check_winner(player, comp):
    winning_conditions = [(player + 2) % 5 == comp, (player - 1) % 5 == comp]
    if any(winning_conditions):
        return "player"
    elif player == comp:
        return "draw"
    else:
        return "comp"


def update_stats(winner,comp_choice ):
    if winner == "draw":
        stats["draws"] += 1
    else:
        stats[winner + "_wins"] += 1
    stats["symbol_counts"][symbols[comp_choice]] += 1


def display_stats():
    print("\nStatistiken:")
    for key, value in stats.items():
        print(f"{key}: {value}")


def main_menu():
    while True:
        print("\nHauptmenü:\n1. Spielen\n2. Statistiken anzeigen\n3. Beenden")
        choice = input("Wähle eine Option: ")
        if choice == "1":
            play_game()
        elif choice == "2":
            display_stats()
        elif choice == "3":
            # Flask
            url = 'http://127.0.0.1:5000/datasql'
            res = requests.post(url, data=stats)
            print(res.text)
            break
        else:
            print("Ungültige Auswahl, bitte erneut versuchen.")


def play_game():
    # Vereinfachte Darstellung der Symbolauswahl
    for i, name in enumerate(symbols, 1):
        print(f"{i}. {name}")
    player_choice = int(input("Wähle ein Symbol (1-5): ")) - 1
    comp_choice = random.randint(0, 4)
    print(f"Computer wählt: {symbols[comp_choice]}")

    winner = check_winner(player_choice, comp_choice)
    result_messages = {"player": "Du gewinnst!", "comp": "Computer gewinnt!", "draw": "Unentschieden!"}
    print(result_messages[winner])

    update_stats(winner, comp_choice)


if __name__ == "__main__":
    main_menu()
