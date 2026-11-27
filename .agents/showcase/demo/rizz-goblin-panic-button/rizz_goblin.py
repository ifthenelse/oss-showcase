"""Turn fictional desk chaos into a goblin alert."""
import argparse

SIGNALS = {"cold-pizza": 1, "keyboard-crumbs": 2, "cursed-tabs": 3}


def report(signals):
    score = sum(SIGNALS[signal] for signal in signals)
    level = "TOUCH GRASS" if score >= 5 else "VIBES INTACT"
    return f"Goblin alert: {level} ({score} chaos points)"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("signals", nargs="+", choices=tuple(SIGNALS))
    print(report(parser.parse_args().signals))
