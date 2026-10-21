class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add(self, book):
        if not self.contains(book):
            self.books.append(book)

    def remove(self, book):
        self.books = [b for b in self.books if b.id != book.id]

    def contains(self, book):
        return any(b.id == book.id for b in self.books)

    def get_books(self):
        return list(self.books)

    def count(self):
        return len(self.books)
