class Book(object):
    """A book in a library."""

    def __init__(self, title: str, author: str, year: int):
        """ Create a new book.

        Args:
            title: The title of the book.
            author: The author of the book.
            year: The year the book was published.
        """
        if None in [title, author, year]:
            raise ValueError('All arguments must be provided.')
        
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """ Return a string representation of the book.
        
        The string representation is in the form: `title by author (year)`
        """
        return f'{self.title} by {self.author} ({self.year})'
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year='{self.year}')"
    
    def __eq__(self, other):
        """Check if two books are equal.
        
        Two books are equal if they have the same title, author and year.
        """
        if not isinstance(other, Book):
            return False
            
        return all([
            self.title == other.title,
            self.author == other.author,
            self.year == other.year,
        ])
    
    def __add__(self, other):
        if isinstance(other, str):
            return str(self) + other
        
        raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")

    def __radd__(self, other):
        if isinstance(other, str):
            return other + str(self)
        
        raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")