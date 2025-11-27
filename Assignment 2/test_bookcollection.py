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