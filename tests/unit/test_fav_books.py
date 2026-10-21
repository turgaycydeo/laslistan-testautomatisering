import pytest

from src.book import Book


@pytest.mark.unit
def test_new_favorites__is_empty(favorites):
    assert favorites.count() == 0
    assert favorites.get_books() == []


@pytest.mark.unit
def test_add__book_is_in_favorites(favorites, book):
    favorites.add(book)

    assert favorites.contains(book)
    assert favorites.count() == 1


@pytest.mark.unit
def test_add__several_books_keeps_order(favorites, book, other_book):
    favorites.add(book)
    favorites.add(other_book)

    assert favorites.get_books() == [book, other_book]


@pytest.mark.unit
def test_add__same_book_twice_is_not_duplicated(favorites, book):
    favorites.add(book)
    favorites.add(book)

    assert favorites.count() == 1


@pytest.mark.unit
def test_add__book_with_same_id_is_not_duplicated(favorites, book):
    copy = Book(book.id, book.title, book.author)

    favorites.add(book)
    favorites.add(copy)

    assert favorites.count() == 1


@pytest.mark.unit
def test_remove__book_is_removed(favorites, book):
    favorites.add(book)

    favorites.remove(book)

    assert not favorites.contains(book)
    assert favorites.count() == 0


@pytest.mark.unit
def test_remove__only_removes_chosen_book(favorites, book, other_book):
    favorites.add(book)
    favorites.add(other_book)

    favorites.remove(book)

    assert favorites.get_books() == [other_book]


@pytest.mark.unit
def test_remove__book_not_in_favorites_does_nothing(favorites, book, other_book):
    favorites.add(book)

    favorites.remove(other_book)

    assert favorites.get_books() == [book]


@pytest.mark.unit
def test_remove__from_empty_favorites_does_nothing(favorites, book):
    favorites.remove(book)

    assert favorites.count() == 0


@pytest.mark.unit
def test_get_books__returns_copy(favorites, book):
    favorites.add(book)

    favorites.get_books().clear()

    assert favorites.count() == 1
