"""
CP1404/CP5632 Practical
My Guitars program to read, display, and manage guitar collection
"""

from guitar import Guitar


def main():
    """Main program to manage guitar collection."""
    guitars = load_guitars()

    print("All guitars:")
    display_guitars(guitars)

    # Sort by year
    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    # Add new guitars
    add_new_guitars(guitars)

    # Save all guitars back to file
    save_guitars(guitars)
    print("Guitars saved to file.")


def load_guitars():
    """Load guitars from guitars.csv file."""
    guitars = []
    try:
        with open('guitars.csv', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name = parts[0]
                    year = int(parts[1])
                    cost = float(parts[2])
                    guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print("No existing guitar file found. Starting with empty collection.")
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")


def add_new_guitars(guitars):
    """Allow user to add new guitars to the collection."""
    print("\nAdd new guitars (enter blank name to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break

        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} added successfully!\n")
        except ValueError:
            print("Invalid input. Please try again.\n")


def save_guitars(guitars):
    """Save all guitars to guitars.csv file."""
    with open('guitars.csv', 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()