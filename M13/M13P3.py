# Module 13 - Problem 3
# Piotr Olechno
# Loads 10 player last names and batting averages from players.txt
# into a dictionary, then prints them in two columns.

FILE_NAME = "players.txt"


def load_players(file_name):
    """Read 'name,average' lines from the file into a dictionary."""
    players = {}
    with open(file_name, "r") as infile:
        for line in infile:
            line = line.strip()
            if line:
                name, average = line.split(",")
                players[name] = float(average)
    return players


def print_players(players):
    """Print player names and batting averages in two columns."""
    print(f"{'Player':<15}{'Average':>10}")
    print("-" * 25)
    for name, average in players.items():
        print(f"{name:<15}{average:>10.3f}")


def main():
    try:
        players = load_players(FILE_NAME)
        print_players(players)
    except FileNotFoundError:
        print(f"Error: could not find {FILE_NAME}")
    except ValueError:
        print(f"Error: {FILE_NAME} has a line that is not in name,average format")


main()