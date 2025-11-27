"""
book.py
CP1404 Assignment 2 - Book class

Author: Swikar Mainali
"""


class Book:
    """Represent a single book."""

    def __init__(self, title: str, author: str, num_pages: int, status: str = "u"):
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.num_pages = int(num_pages)
        self.status = status if status in ("r", "u") else "u"