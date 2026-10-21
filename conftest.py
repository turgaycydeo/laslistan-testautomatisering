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
    return mocker.Mock(spec=FavoriteBooks)


@pytest.fixture
def store_with_mock(mock_favorites):
    return BookStore(favorites=mock_favorites)
