import pytest

from src.book import Book
from src.book_store import BookStore
from src.fav_books import FavoriteBooks


@pytest.fixture
def book():
    return Book(1, "Clean Code", "Robert C. Martin")


@pytest.fixture
def other_book():
    return Book(2, "The Pragmatic Programmer", "Dave Thomas")


@pytest.fixture
def favorites():
    return FavoriteBooks()


@pytest.fixture
def mock_favorites(mocker):
    # "mocker" är en fixture som kommer från pytest-mock
    return mocker.Mock(spec=FavoriteBooks)


@pytest.fixture
def store_with_mock(mock_favorites):
    """BookStore med startdata, där FavoriteBooks är utbytt mot en mock."""
    return BookStore(favorites=mock_favorites)
