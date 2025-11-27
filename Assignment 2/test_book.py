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


def test_book_marking():
    """Test marking books as completed/unread."""
    book = Book("Test", "Author", 100, "u")
    book.mark_completed()
    assert book.status == "r"

    book.mark_unread()
    assert book.status == "u"
    print("✓ Book marking test passed")


def test_long_book_detection():
    """Test detection of long books."""
    short_book = Book("Short", "Author", 499)
    long_book = Book("Long", "Author", 500)

    assert not short_book.is_long()
    assert long_book.is_long()
    print("✓ Long book detection test passed")

    if __name__ == "__main__":
        test_book_creation()
        test_book_string_representation()
        test_book_marking()
        test_long_book_detection()
        print("All Book tests passed!")