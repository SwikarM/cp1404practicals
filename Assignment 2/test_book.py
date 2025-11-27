"""
test_book.py
Simple tests for Book class
"""

from book import Book

def test_book_creation():
    """Test basic book creation and attributes."""
    book = Book("Test Title", "Test Author", 100, "u")
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.num_pages == 100
    assert book.status == "u"
    print("✓ Book creation test passed")


def test_book_string_representation():
    """Test the string representation of books."""
    unread_book = Book("Title1", "Author1", 200, "u")
    read_book = Book("Title2", "Author2", 300, "r")

    assert "*" in str(unread_book)
    assert "*" not in str(read_book)
    print("✓ Book string representation test passed")