"""
CP1404 - Practical
Sales Bonus

"""


MAXIMUM_BONUS = 0.15
MINIMUM_BONUS = 0.10
sales = float(input("Enter sales: $"))

while sales >= 0:
    # Calculate bonus based on sales amount
    if sales < 1000:
        bonus = sales * MINIMUM_BONUS  # 10% bonus
    else:
        bonus = sales * MAXIMUM_BONUS  # 15% bonus

    print(f"Bonus: ${bonus:.2f}")

    sales = float(input("Enter sales: $"))

print("Thank you for using the sales bonus calculator!")