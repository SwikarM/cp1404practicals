# 1. 1 and 20 with a space between each one.

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# 2.  count in 10s from 0 to 100

for i in range(0, 101, 10):
    print(i, end=' ')
print()

#3. count down from 20 to 1:

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# 4. Print a number of stars

number_of_stars = int(input("Enter a number: "))
print("*" * number_of_stars)

# 5. print lines of increasing stars

number_of_lines = int(input("Enter number of lines: "))

for i in range(1, number_of_lines + 1):
    print("*" * i)