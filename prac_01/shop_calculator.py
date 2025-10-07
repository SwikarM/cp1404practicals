

"""
CP1404/CP5632 - Practical
Shop Calculator
"""


def main():
    # Get valid number of items
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total_price = 0
    for i in range(number_of_items):
        price = float(input("Price of item: "))
        total_price += price

    # Apply discount if total > $100
    if total_price > 100:
        total_price *= 0.9  # 10% discount

    print(f"Total price for {number_of_items} items is ${total_price:.2f}")

main()