import os

import library


def show_bookshelf(bookshelf):
    print("=" * os.get_terminal_size().columns)
    print(
        f"Bookshelf '{bookshelf.name}' has {len(bookshelf.books)} books".center(
            os.get_terminal_size().columns
        )
    )

    # Loop through the books with an easy-to-read syntax (same as `bookshelf.books` but easier to read and understand)
    for book in bookshelf:
        print(f"--> {book} <--".center(os.get_terminal_size().columns))

    print("=" * os.get_terminal_size().columns)
    print("\n")


if __name__ == "__main__":
    # Create a bookshelf with some books
    thrillers = library.BookShelf(
        "Thrillers",
        [
            # All positional arguments
            library.Book("The Da Vinci Code", "Dan Brown", 2003),
            # All named arguments
            library.Book(title="The Martian", author="Andy Weir", year=2011),
            # Mixed positional and named arguments
            library.Book("It", author="Stephen King", year=1986),
        ],
    )

    show_bookshelf(thrillers)

    # Add books using both methods
    thrillers.add_book(
        library.Book(title="The Shining", author="Stephen King", year=1977)
    )
    thrillers += library.Book("Casino Royale", "Ian Fleming", 1953)

    show_bookshelf(thrillers)

    # Sell a book
    thrillers.remove_book(library.Book("The Martian", "Andy Weir", 2011))

    show_bookshelf(thrillers)

    # Play around with the bookshelf
    the_shining = thrillers.find_book(title="The Shining")
    print("Searching 'The Shining':\n\t" + the_shining)
    print(
        "Is it still in the shelf?\n\t" + ("Yes" if the_shining in thrillers else "No")
    )
    print(
        "Books from the same author as 'The Shining' (Stephen King) \n\t"
        + str(thrillers.find_books(author=the_shining.author))
    )
