import random
import time
import functools

# Funktionen zur Zuordnung von Symbolen und Farben zu Karten
def WhichSymbol(oneCard):
    symbol = oneCard % 13
    return symbol

def WhichColor(oneCard):
    color = oneCard // 13
    return color

# Funktion zum Ziehen von 5 zufälligen Karten
def Pick5Cards():
    random.shuffle(cards)
    hand = cards[:5]
    return hand

# Dekorator für die Zeitmessung von Funktionen
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

# Konstanten und Initialisierung
amountDeck = 52
draws = 100000
statistics = {"HighCard": 0, "Pair": 0, "TwoPair": 0, "ThreeOfAKind": 0, "Straight": 0, "Flush": 0, "FullHouse": 0, "FourOfAKind": 0, "StraightFlush": 0, "RoyalFlush": 0}

# Initialisieren Sie die 'cards'-Liste außerhalb der 'main()' Funktion
cards = list(range(amountDeck))

# Funktionen für Pokerhände
def OnePair(drawnHand):
    symbols = [WhichSymbol(card) for card in drawnHand]
    symbol_counts = {symbol: symbols.count(symbol) for symbol in symbols}
    return 2 in symbol_counts.values()

def TwoPair(drawnHand):
    symbols = [WhichSymbol(card) for card in drawnHand]
    symbol_counts = {symbol: symbols.count(symbol) for symbol in symbols}
    return list(symbol_counts.values()).count(2) == 2

def ThreeOfAKind(drawnHand):
    symbols = [WhichSymbol(card) for card in drawnHand]
    symbol_counts = {symbol: symbols.count(symbol) for symbol in symbols}
    return 3 in symbol_counts.values()

def FourOfAKind(drawnHand):
    symbols = [WhichSymbol(card) for card in drawnHand]
    symbol_counts = {symbol: symbols.count(symbol) for symbol in symbols}
    return 4 in symbol_counts.values()

def FullHouse(drawnHand):
    symbols = [WhichSymbol(card) for card in drawnHand]
    symbol_counts = {symbol: symbols.count(symbol) for symbol in symbols}
    return 3 in symbol_counts.values() and 2 in symbol_counts.values()

def Straight(yHands):
    symbols = [WhichSymbol(card) for card in yHands]
    sorted_symbols = sorted(symbols)
    return sorted_symbols[-1] - sorted_symbols[0] == 4 and len(set(sorted_symbols)) == 5

def Flush(yHands):
    colors = [WhichColor(card) for card in yHands]
    return len(set(colors)) == 1

def StraightFlush(yHands):
    return Straight(yHands) and Flush(yHands)

def RoyalFlush(yHands):
    symbols = [WhichSymbol(card) for card in yHands]
    colors = [WhichColor(card) for card in yHands]

    if len(set(colors)) == 1:
        sorted_symbols = sorted(symbols)
        if sorted_symbols == [8, 9, 10, 11, 12]:
            return True
    return False

# Funktion zur Überprüfung der Pokerhand
def checkHand(yHand):
    global statistics
    if RoyalFlush(yHand):
        statistics["RoyalFlush"] += 1
    elif StraightFlush(yHand):
        statistics["StraightFlush"] += 1
    elif FourOfAKind(yHand):
        statistics["FourOfAKind"] += 1
    elif FullHouse(yHand):
        statistics["FullHouse"] += 1
    elif Flush(yHand):
        statistics["Flush"] += 1
    elif Straight(yHand):
        statistics["Straight"] += 1
    elif ThreeOfAKind(yHand):
        statistics["ThreeOfAKind"] += 1
    elif TwoPair(yHand):
        statistics["TwoPair"] += 1
    elif OnePair(yHand):
        statistics["Pair"] += 1
    else:
        statistics["HighCard"] += 1

# Funktion zur Initialisierung und Auswertung des Spiels
@timer
def main():
    for i in range(0, draws):
        hand = Pick5Cards()
        checkHand(hand)

    for key, value in statistics.items():
        statistics[key] = (value / draws) * 100

    print(statistics)

if __name__ == '__main__':
    main()