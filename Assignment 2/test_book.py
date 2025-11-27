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