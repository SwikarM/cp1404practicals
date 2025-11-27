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

def main():
    """Main program for Books To Read 2.0 console version."""
    print("Books To Read 2.0 - by Swikar Mainali")

    collection = BookCollection()
    collection.load_books("books.json")
    print(f"{len(collection.books)} books loaded")

    choice = ""
    while choice != "Q":
        choice = input(MENU).strip().upper()

        if choice == "D":
            display_books(collection)
        elif choice == "A":
            add_book_interactive(collection)
        elif choice == "C":
            complete_book_interactive(collection)
        elif choice == "Q":
            collection.save_books("books.json")
            print(f"{len(collection.books)} books saved to books.json")
            print("Goodbye!")
        else:
            print("Invalid menu choice")




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

def add_book_interactive(collection: BookCollection):
    """Prompt user for book fields and add a new unread Book."""
    title = input("Title: ").strip()
    while title == "":
        print("Input cannot be blank")
        title = input("Title: ").strip()

    author = input("Author: ").strip()
    while author == "":
        print("Input cannot be blank")
        author = input("Author: ").strip()

    pages = get_valid_number("Pages: ")

    collection.add_book(Book(title, author, pages, "u"))
    print(f"{title} by {author} added to reading list.")

def complete_book_interactive(collection: BookCollection):
    """Mark one unread book as completed."""
    unread = [b for b in collection.books if b.status == "u"]
    if not unread:
        print("No unread books")
        return

    display_books(collection)

    choice = get_valid_number("Enter the number of a book to complete: ")

    try:
        book = collection.find_by_index_in_sorted(choice, key="author")
    except IndexError:
        print("Invalid book number")
        return

    if book.status == "r":
        print("That book is already completed")
    else:
        book.mark_completed()
        print(f"{book.title} by {book.author} completed!")




if __name__ == "__main__":
    main()