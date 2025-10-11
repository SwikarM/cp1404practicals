"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random

# ----- CONSTANTS -----
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Ask user for number of quick picks and display them neatly."""
    number_of_picks = int(input("How many quick picks? "))

    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))


def generate_quick_pick():
    """Generate one quick pick (a sorted list of unique random numbers)."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


main()
