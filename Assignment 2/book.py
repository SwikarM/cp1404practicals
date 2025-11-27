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

    def __str__(self):
        """Return a readable representation of the book."""
        mark = "*" if self.status == "u" else " "
        return f"{mark} {self.title} by {self.author} {self.num_pages} pages"

    def mark_completed(self):
        """Mark the book as completed/read."""
        self.status = "r"

    def mark_unread(self):
        """Mark the book as unread."""
        self.status = "u"

    def is_long(self) -> bool:
        """Return True if the book is considered long (>= 500 pages)."""
        return self.num_pages >= 500

    def to_dict(self) -> dict:
        """Return serializable dictionary representation for JSON storage."""
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.num_pages,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Book instance from a dictionary (as read from JSON)."""
        return cls(data["title"], data["author"], data["pages"], data.get("status", "u"))