"""
CP1404 Assignment 1 - Books to Read
Name: Your Name
Date Started: 28/10/2025
GitHub URL: https://github.com/cp1404-students/a1-books-SwikarM
"""

import csv

MENU = """Menu:
D - Display books
A - Add new book
C - Complete a book
Q - Quit
"""

def main():
    """Run the main Books To Read program."""
    print("Books To Read 1.0 - by Swikar Mainali")

    books = load_books("books.csv")
    print(f"{len(books)} books loaded")

    choice = ""   # initialise before loop to avoid “referenced before assignment”

    while choice != "Q":
        choice = input(MENU).strip().upper()

        if choice == "D":
            display_books(books)
        elif choice == "A":
            add_book(books)
        elif choice == "C":
            complete_book(books)
        elif choice == "Q":
            save_books("books.csv", books)
            print(f"{len(books)} books saved to books.csv")
            print("Have a nice day :)")
        else:
            print("Invalid menu choice")


    save_books("books.csv", books)
    print(f"{len(books)} books saved to books.csv")
    print("Have a nice day :)")


def load_books(filename):
    """Load books from a CSV file into a list of lists."""
    rows = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            title, author, pages, status = row
            rows.append([title, author, int(pages), status])
    return rows


def save_books(filename, books):
    """Save books back to the CSV file."""
    with open(filename, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(books)


def display_books(books):
    """Display all books neatly lined up and show unread count."""
    if not books:
        print("No books found.")
        return

    sorted_books = sorted(books, key=lambda b: b[1])  # sort by author

    max_title = max(len(b[0]) for b in sorted_books)
    max_author = max(len(b[1]) for b in sorted_books)

    unread_count = 0

    for i, book in enumerate(sorted_books, start=1):
        star = "*" if book[3] == "u" else " "
        print(f"{star} {i}. {book[0]:<{max_title}} by {book[1]:<{max_author}} {book[2]} pages")
        if book[3] == "u":
            unread_count += 1

    if unread_count == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still have {unread_count} books to read.")


def add_book(books):
    """Add a new book to the list with input validation."""
    title = input("Title: ").strip()
    while title == "":
        print("Input cannot be blank")
        title = input("Title: ").strip()

    author = input("Author: ").strip()
    while author == "":
        print("Input cannot be blank")
        author = input("Author: ").strip()

    num_pages = get_valid_number("Pages: ")

    books.append([title, author, num_pages, "u"])
    print(f"{title} by {author} ({num_pages} pages) added to reading list.")


def get_valid_number(prompt):
    """Return a valid positive integer using CP1404 error-checking pattern."""
    number = input(prompt)
    while True:
        try:
            number = int(number)
            if number > 0:
                return number
            print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")
        number = input(prompt)


def complete_book(books):
    """Mark an unread book as completed."""
    unread_books = [b for b in books if b[3] == "u"]

    if not unread_books:
        print("No unread books")
        return

    display_books(books)

    book_number = get_valid_number("Enter the number of a book to complete: ")

    sorted_books = sorted(books, key=lambda b: b[1])

    if book_number < 1 or book_number > len(sorted_books):
        print("Invalid book number")
        return

    selected_book = sorted_books[book_number - 1]

    if selected_book[3] == "r":
        print("That book is already completed")
    else:
        selected_book[3] = "r"
        print(f"{selected_book[0]} by {selected_book[1]} completed!")

    # update original list correctly
    for book in books:
        if book[0] == selected_book[0] and book[1] == selected_book[1]:
            book[3] = "r"
            break


if __name__ == "__main__":
    main()
