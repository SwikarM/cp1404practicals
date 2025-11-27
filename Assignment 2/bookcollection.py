"""
bookcollection.py
CP1404 Assignment 2 - BookCollection class

Author: Swikar Mainali
"""

import json
import os
from typing import List
from book import Book

class BookCollection:
    """Manage a collection (list) of Book objects."""

    def __init__(self):
        """Initialize with an empty book list."""
        self.books: List[Book] = []

    def add_book(self, book: Book):
        """Add a Book object to the collection."""
        self.books.append(book)

    def unread_pages(self) -> int:
        """Return total pages of unread books."""
        return sum(b.num_pages for b in self.books if b.status == "u")

    def completed_pages(self) -> int:
        """Return total pages of completed books."""
        return sum(b.num_pages for b in self.books if b.status == "r")

    def load_books(self, filename: str):
        """Load books from a JSON file into self.books (creating Book objects)."""
        path = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = [Book.from_dict(item) for item in data]
        except FileNotFoundError:
            self.books = []

    def save_books(self, filename: str):
        """Save current books to JSON file (serialize as list of dicts)."""
        path = os.path.join(os.path.dirname(__file__), filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)

    def sort(self, key: str = "author"):
        """Sort books in-place by the given key, then by title."""
        if key == "author":
            def author_key(b: Book):
                parts = b.author.split()
                first_name = parts[0] if parts else b.author
                return (first_name.lower(), b.title.lower())

            self.books.sort(key=author_key)
        elif key == "title":
            self.books.sort(key=lambda b: (b.title.lower(), b.author.lower()))
        elif key == "pages":
            self.books.sort(key=lambda b: (b.num_pages, b.title.lower()))
        else:
            self.books.sort(key=lambda b: (b.title.lower(), b.author.lower()))

    def find_by_index_in_sorted(self, index: int, key: str = "author") -> Book:
        """Return the Book object corresponding to `index` in the sorted list."""
        self.sort(key)
        if index < 1 or index > len(self.books):
            raise IndexError("Book index out of range.")
        return self.books[index - 1]