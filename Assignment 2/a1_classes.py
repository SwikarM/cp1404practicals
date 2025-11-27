"""
a1_classes.py
Console program for Assignment 2 using Book and BookCollection.

Author: Swikar Mainali
"""

from book import Book
from bookcollection import BookCollection

MENU = """Menu:
D - Display books
A - Add new book
C - Complete a book
Q - Quit
"""

def get_valid_number(prompt):
    """Return a valid positive integer using a controlled loop ."""
    value = input(prompt)
    valid = False

    while not valid:
        if value.isdigit() and int(value) > 0:
            valid = True
        else:
            if not value.isdigit():
                print("Invalid input; enter a valid number")
            elif int(value) <= 0:
                print("Number must be > 0")
            value = input(prompt)

    return int(value)

def display_books(collection: BookCollection):
    """Display books sorted by author first name, aligned nicely."""
    if not collection.books:
        print("No books found.")
        return

    collection.sort("author")

    max_title = max(len(b.title) for b in collection.books)
    max_author = max(len(b.author) for b in collection.books)

    unread_count = 0

    for i, b in enumerate(collection.books, start=1):
        star = "*" if b.status == "u" else " "
        print(f"{star} {i}. {b.title:<{max_title}} by {b.author:<{max_author}} {b.num_pages} pages")
        if b.status == "u":
            unread_count += 1

    if unread_count == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still have {unread_count} books to read.")

