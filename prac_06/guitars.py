"""
CP1404/CP5632 Practical - Client code to use the Guitar class.
Estimate: 35 minutes
Actual: 65 min
"""

from guitar import Guitar


def main():
    """Program to store and display user's guitar collection."""
    print("My guitars!")
    guitars = []

    # Uncomment the following section for manual input
    """
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
    """

    # For testing - comment out when using manual input
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        # Using ternary operator for vintage string
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()