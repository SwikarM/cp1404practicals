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