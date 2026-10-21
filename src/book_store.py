from src.book import Book
from src.fav_books import FavoriteBooks
from src.initial_books import INITIAL_BOOKS


class BookStore:
    """Katalogen med alla böcker i Läslistan.

    BookStore är beroende av FavoriteBooks. Beroendet skickas in i konstruktorn,
    så att det kan bytas ut mot en mock i enhetstesterna."""

    def __init__(self, favorites=None, books=None):
        if books is None:
            books = [Book(book_id, title, author) for book_id, title, author in INITIAL_BOOKS]
        self.books = books
        self.favorites = favorites if favorites is not None else FavoriteBooks()

    def addBook(self, author, title):
        """Lägg till en ny bok i katalogen och returnera den.
        Både författare och titel måste vara ifyllda, precis som på webbsidan."""
        if not author or not title:
            raise ValueError("Både författare och titel måste anges")

        book = Book(self._make_id(), title, author)
        self.books.append(book)
        return book

    def toggleFavorite(self, book_id):
        """Växla favoritmarkeringen för en bok.
        Returnerar True om boken nu är favorit, annars False."""
        book = self.get_book(book_id)
        book.fav = not book.fav

        if book.fav:
            self.favorites.add(book)
        else:
            self.favorites.remove(book)
        return book.fav

    def get_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        raise KeyError(f"Det finns ingen bok med id {book_id}")

    def count(self):
        return len(self.books)

    def _make_id(self):
        # Samma regel som webbsidan: högsta befintliga id + 1
        return max((b.id for b in self.books), default=0) + 1
