class Book(object):
    """
    class to represent a book
    demo for understanding docstrings in a class

    Attributes:
        name (str): the name of the book
        pages (int): number of pages of the book
        genre (str): genre this book belongs to
    """

    def __init__(self, name, pages, genre):
        """
        initialise method for book classs
        Args:
            name (str): initialises the 'name' attribute
            pages (int): initialise the 'pages' attribute
            genre (str): initialise the 'genre' attribute
        """
        self.name = name
        self.pages = pages
        self.genre = genre

help(Book)
print(Book.__init__.__doc__)
