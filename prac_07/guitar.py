"""
CP1404/CP5632 Practical
Guitar class
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return string representation for reproducing object."""
        return f"Guitar('{self.name}', {self.year}, {self.cost})"

    def __lt__(self, other):
        """Less than comparison based on year."""
        return self.year < other.year

    def get_age(self):
        """Get the age of the guitar based on the current year."""
        current_year = 2024  # You can update this or use datetime
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50 or more years old)."""
        return self.get_age() >= 50