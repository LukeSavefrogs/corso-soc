from library.book import Book

class BookShelf(object):
    def __init__(self, name=None, books=None):
        """Initialize a new BookShelf instance.

        Args:
            name: The name of the bookshelf.
            books: A list of books on the bookshelf.
        """
        self.name = name if name is not None else ""
        self.books = books if books is not None else []

    def __str__(self):
        return f"BookShelf '{self.name}' has {len(self.books)} books"

    def __repr__(self):
        return f"BookShelf({self.books})"

    def add_book(self, book):
        """Add a book to the shelf."""
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added to the shelf.")

        self.books.append(book)

    def remove_book(self, book):
        """Remove a book from the shelf."""
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be removed from the shelf.")

        self.books.remove(book)

    def find_books(self, title=None, author=None, year=None) -> list[Book]:
        """Find books in the shelf matching the given criteria.

        Args:
            title: The title of the book.
            author: The author of the book.
            year: The year the book was published.

        Returns:
            A list of books that match the given criteria.
        """
        return [
            book
            for book in self.books
            if all(
                [
                    title is None or book.title == title,
                    author is None or book.author == author,
                    year is None or book.year == year,
                ]
            )
        ]

    def find_book(self, title=None, author=None, year=None) -> Book:
        """Find a book in the shelf matching the given criteria.

        Args:
            title: The title of the book.
            author: The author of the book.
            year: The year the book was published.

        Returns:
            The first book that matches the given criteria.
        """
        books = self.find_books(title, author, year)
        
        if not books:
            raise ValueError("No book found matching the given criteria.")
        
        return books[0]

    def __len__(self):
        return len(self.books)

    def __iter__(self):
        return iter(self.books)

    def __getitem__(self, index):
        return self.books[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Book):
            raise TypeError("Only Book instances can be added to the shelf.")

        self.books[index] = value

    def __delitem__(self, index):
        del self.books[index]

    def __contains__(self, book):
        return book in self.books

    def __eq__(self, other):
        return isinstance(other, BookShelf) and self.books == other.books

    def __add__(self, other):
        if isinstance(other, Book):
            return BookShelf(name=self.name, books=self.books + [other])
        elif isinstance(other, BookShelf):
            return BookShelf(name=f"{self.name} + {other.name}", books=self.books + other.books)
        elif isinstance(other, list):
            return BookShelf(name=self.name, books=self.books + other)
        else:
            raise TypeError(
                "Only Book or BookShelf instances can be added to the shelf."
            )
    
    def __sub__(self, other):
        if isinstance(other, Book):
            return BookShelf(name=self.name, books=[book for book in self.books if book != other])
        elif isinstance(other, BookShelf):
            return BookShelf(name=self.name.replace(other.name, "").replace(" + + ", " + "), books=[book for book in self.books if book not in other.books])
        else:
            raise TypeError(
                "Only Book or BookShelf instances can be removed from the shelf."
            )

    def __bool__(self):
        return bool(self.books)