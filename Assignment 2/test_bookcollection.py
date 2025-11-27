"""
test_bookcollection.py
Simple tests for BookCollection class
"""

import os
import tempfile
from book import Book
from bookcollection import BookCollection


def test_collection_basics():
    """Test basic collection operations."""
    collection = BookCollection()
    assert len(collection.books) == 0

    book = Book("Test", "Author", 100)
    collection.add_book(book)
    assert len(collection.books) == 1
    print("✓ Collection basics test passed")


def test_page_counts():
    """Test unread and completed page counts."""
    collection = BookCollection()
    collection.add_book(Book("Book1", "Author1", 100, "u"))
    collection.add_book(Book("Book2", "Author2", 200, "r"))
    collection.add_book(Book("Book3", "Author3", 150, "u"))

    assert collection.unread_pages() == 250
    assert collection.completed_pages() == 200
    print("✓ Page counts test passed")