"""
Wimbledon
Estimate: 25 minutes
Actual:   (record your actual time here)
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data and display champions and countries."""
    records = load_data(FILENAME)
    champion_to_wins, countries = process_data(records)

    display_champions(champion_to_wins)
    display_countries(countries)


def load_data(filename):
    """Read data from the Wimbledon CSV file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header line
        records = [line.strip().split(",") for line in in_file]
    return records

def process_data(records):
    """Process records to count champions' wins and collect countries."""
    champion_to_wins = {}
    countries = set()

    for record in records:
        champion = record[2]
        country = record[1]
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1

    return champion_to_wins, countries

def display_champions(champion_to_wins):
    """Display champions and their number of wins."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion:20} {wins}")


def display_countries(countries):
    """Display all unique countries in alphabetical order."""
    sorted_countries = sorted(countries)
    print()
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


main()