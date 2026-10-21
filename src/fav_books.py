
class FavoriteBooks:
    """Användarens favoritböcker - motsvarar vyn "Mina böcker"."""

    def __init__(self):
        self.books = []

    def add(self, book):
        """Lägg till en bok bland favoriterna.
        Samma bok (samma id) läggs aldrig till två gånger."""
        if not self.contains(book):
            self.books.append(book)

    def remove(self, book):
        """Ta bort en bok från favoriterna.
        Om boken inte finns bland favoriterna händer ingenting."""
        self.books = [b for b in self.books if b.id != book.id]

    def contains(self, book):
        return any(b.id == book.id for b in self.books)

    def get_books(self):
        # Returnera en kopia, så att listan inte kan ändras utifrån
        return list(self.books)

    def count(self):
        return len(self.books)
