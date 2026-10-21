class Book:
    def __init__(self, book_id, title, author, fav=False):
        self.id = book_id
        self.title = title
        self.author = author
        self.fav = fav

    def __repr__(self):
        return f'Book({self.id}, "{self.title}", {self.author}, fav={self.fav})'
