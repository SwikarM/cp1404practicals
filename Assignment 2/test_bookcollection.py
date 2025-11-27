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


def test_save_load_books():
    """Test saving and loading books from JSON file."""
    collection = BookCollection()
    collection.add_book(Book("Title1", "Author1", 100, "u"))
    collection.add_book(Book("Title2", "Author2", 200, "r"))

    # Save to temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        temp_filename = f.name

    try:
        collection.save_books(temp_filename)

        # Load into new collection
        new_collection = BookCollection()
        new_collection.load_books(temp_filename)

        assert len(new_collection.books) == 2
        assert new_collection.books[0].title == "Title1"
        assert new_collection.books[1].title == "Title2"
        print("✓ Save/load test passed")
    finally:
        os.unlink(temp_filename)


def test_sorting():
    """Test sorting functionality."""
    collection = BookCollection()
    collection.add_book(Book("C Book", "Charlie", 300))
    collection.add_book(Book("A Book", "Alice", 100))
    collection.add_book(Book("B Book", "Bob", 200))


    collection.sort("author")
    authors = [book.author for book in collection.books]
    assert authors == ["Alice", "Bob", "Charlie"]
    print("✓ Sorting test passed")


if __name__ == "__main__":
    test_collection_basics()
    test_page_counts()
    test_save_load_books()
    test_sorting()
    print("All BookCollection tests passed! ✅")
