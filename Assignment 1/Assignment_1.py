"""
CP1404 Assignment 1 - Books to Read
Name: Your Name
Date Started: 28/10/2025
GitHub URL: https://github.com/cp1404-students/a1-books-SwikarM
"""

import csv


def main():
    """Main function to run the Books To Read program."""
    print("Books To Read 1.0 - by Your Name")

    books = load_books("books.csv")
    print(f"{len(books)} books loaded")

    while True:
        print("\nMenu:")
        print("L - List all books")
        print("A - Add new book")
        print("M - Mark a book as completed")
        print("Q - Quit")

        choice = input(">>> ").strip().upper()
        if choice == "L":
            list_books(books)
        elif choice == "A":
            add_book(books)
        elif choice == "M":
            mark_book(books)
        elif choice == "Q":
            save_books("books.csv", books)
            print(f"{len(books)} books saved to books.csv")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def load_books(filename):
    """Load books from a CSV file into a list of lists."""
    books = []
    try:
        with open(filename, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            for row in reader:
                title, author, pages, status = row
                books.append([title, author, int(pages), status])
    except FileNotFoundError:
        print("File not found. Starting with an empty book list.")
    return books


def save_books(filename, books):
    """Save books back to the CSV file."""
    with open(filename, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(books)


def list_books(books):
    """Display all books neatly lined up and show unread count."""
    if not books:
        print("No books found.")
        return

    title_width = max(len(book[0]) for book in books)
    author_width = max(len(book[1]) for book in books)
    unread_count = 0

    for i, book in enumerate(books, start=1):
        mark = "*" if book[3] == "u" else " "
        print(f"{i}. {book[0]:<{title_width}} by {book[1]:<{author_width}} "
              f"({book[2]:>3} pages){mark}")
        if book[3] == "u":
            unread_count += 1

    if unread_count == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still have {unread_count} books to read.")


def add_book(books):
    """Add a new book to the list with input validation."""
    title = input("Title: ").strip()
    while not title:
        print("Input cannot be blank")
        title = input("Title: ").strip()

    author = input("Author: ").strip()
    while not author:
        print("Input cannot be blank")
        author = input("Author: ").strip()

    pages = get_positive_int("Pages: ")

    books.append([title, author, pages, "u"])
    print(f"{title} by {author} ({pages} pages) added to reading list.")


def get_positive_int(prompt):
    """Get a valid positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Number must be > 0")
            else:
                return value
        except ValueError:
            print("Invalid input; enter a valid number")


def mark_book(books):
    """Mark one book as completed."""
    unread_books = [b for b in books if b[3] == "u"]

    if not unread_books:
        print("No unread books to mark.")
        return

    list_books(books)
    choice = get_positive_int("Enter the number of a book to mark as completed: ")

    if 1 <= choice <= len(books):
        book = books[choice - 1]
        if book[3] == "r":
            print(f"You have already completed {book[0]}")
        else:
            book[3] = "r"
            print(f"{book[0]} by {book[1]} marked as completed.")
    else:
        print("Invalid book number")


if __name__ == "__main__":
    main()
