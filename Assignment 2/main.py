"""
main.py
CP1404 Assignment 2 - Kivy GUI for Books to Read 2.0

Author: Swikar Mainali
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty
from kivy.core.window import Window

from bookcollection import BookCollection
from book import Book

# Constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
COLOR_UNREAD = [0.2, 0.6, 0.8, 1]  # Blue
COLOR_COMPLETED = [0.3, 0.7, 0.3, 1]  # Green
COLOR_LONG_BOOK = [0.9, 0.5, 0.1, 1]  # Orange

Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)


class BooksApp(App):
    """Main Kivy App for Books To Read 2.0."""

    # Kivy properties for data binding
    status_top = StringProperty("Pages to read: 0")
    status_bottom = StringProperty("Welcome to Books To Read 2.0")
    sort_options = ListProperty(['author', 'title', 'pages'])

    def build(self):
        """Build the app UI and load books."""
        self.collection = BookCollection()
        self.collection.load_books("books.json")
        self.root = Builder.load_file("app.kv")

        # Schedule the initial update after the UI is fully built
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.update_books_display(), 0.1)

        return self.root

    def update_books_display(self):
        """Update the books display area with current books."""
        if not self.root:
            return

        sort_key = self.root.ids.sort_spinner.text
        self.collection.sort(sort_key)

        # Clear existing book buttons
        books_grid = self.root.ids.books_grid
        books_grid.clear_widgets()

        # Add book buttons
        for book in self.collection.books:
            # Create button text
            button_text = f"{book.title} by {book.author} ({book.num_pages} pages)"
            if book.is_long():
                button_text += " [LONG]"

            # Create button
            btn = Button(
                text=button_text,
                size_hint_y=None,
                height=40
            )

            # Set button color based on status and length
            if book.status == "r":
                btn.background_color = COLOR_COMPLETED
            elif book.is_long():
                btn.background_color = COLOR_LONG_BOOK
            else:
                btn.background_color = COLOR_UNREAD

            # Bind button to book action
            btn.book = book  # Store reference to the book object
            btn.bind(on_press=self.on_book_click)

            books_grid.add_widget(btn)

        # Update top status
        unread_pages = self.collection.unread_pages()
        self.status_top = f"Pages to read: {unread_pages}"

    def on_book_click(self, instance):
        """Handle book button clicks - toggle completion status."""
        book = instance.book

        if book.status == "u":
            book.mark_completed()
            if book.is_long():
                self.status_bottom = f"Congratulations! You completed {book.title}, a long book!"
            else:
                self.status_bottom = f"Completed {book.title}"
        else:
            book.mark_unread()
            self.status_bottom = f"{book.title} marked as unread"

        self.update_books_display()

    def add_book(self):
        """Add a new book from the input fields."""
        title = self.root.ids.title_input.text.strip()
        author = self.root.ids.author_input.text.strip()
        pages_text = self.root.ids.pages_input.text.strip()

        # Validation
        if not title or not author or not pages_text:
            self.status_bottom = "Please complete all fields."
            return

        try:
            pages = int(pages_text)
            if pages <= 0:
                self.status_bottom = "The book must have some pages!"
                return
        except ValueError:
            self.status_bottom = "Please enter a valid number"
            return

        # Add the book
        new_book = Book(title, author, pages, "u")
        self.collection.add_book(new_book)
        self.status_bottom = f"{title} added to reading list"

        # Clear inputs and update display
        self.clear_inputs()
        self.update_books_display()

    def clear_inputs(self):
        """Clear all input fields and status message."""
        self.root.ids.title_input.text = ""
        self.root.ids.author_input.text = ""
        self.root.ids.pages_input.text = ""
        self.status_bottom = ""

    def on_sort_change(self):
        """Handle sort spinner changes."""
        self.update_books_display()

    def on_stop(self):
        """Save books when app closes."""
        self.collection.save_books("books.json")


if __name__ == "__main__":
    BooksApp().run()