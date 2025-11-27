"""
CP1404/CP5632 Practical - Testing the Guitar class.
Estimate: 35 minutes
Actual: 50 min
"""

from guitar import Guitar


def main():
    """Test the Guitar class methods."""
    # Test guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 899.99)

    # Test get_age() method
    print(f"{guitar1.name} get_age() - Expected 102. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 11. Got {guitar2.get_age()}")

    # Test is_vintage() method
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

    # Additional test cases
    guitar3 = Guitar("50-year old guitar", 1974, 1200.00)
    print(f"{guitar3.name} is_vintage() - Expected True. Got {guitar3.is_vintage()}")


if __name__ == "__main__":
    main()