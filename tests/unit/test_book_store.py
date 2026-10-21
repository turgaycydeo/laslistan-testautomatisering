import pytest

from src.book import Book
from src.book_store import BookStore


# Enhetstest: BookStore testas separat. FavoriteBooks är utbytt mot en mock.

# ---------- addBook ----------

@pytest.mark.unit
def test_add_book__increases_count(store_with_mock):
    before = store_with_mock.count()

    store_with_mock.addBook("Robert C. Martin", "Clean Code")

    assert store_with_mock.count() == before + 1


@pytest.mark.unit
def test_add_book__stores_title_and_author(store_with_mock):
    book = store_with_mock.addBook("Robert C. Martin", "Clean Code")

    assert book.title == "Clean Code"
    assert book.author == "Robert C. Martin"
    assert book in store_with_mock.books


@pytest.mark.unit
def test_add_book__is_not_favorite(store_with_mock):
    book = store_with_mock.addBook("Robert C. Martin", "Clean Code")

    assert book.fav is False


@pytest.mark.unit
def test_add_book__id_is_highest_id_plus_one(store_with_mock):
    # Startdatans högsta id är 115, trots att det bara finns 13 böcker
    book = store_with_mock.addBook("Robert C. Martin", "Clean Code")

    assert book.id == 116


@pytest.mark.unit
def test_add_book__ids_are_unique(store_with_mock):
    first = store_with_mock.addBook("Författare 1", "Titel 1")
    second = store_with_mock.addBook("Författare 2", "Titel 2")

    assert second.id == first.id + 1


@pytest.mark.unit
def test_add_book__to_empty_store_gets_id_1(mock_favorites):
    store = BookStore(favorites=mock_favorites, books=[])

    book = store.addBook("Robert C. Martin", "Clean Code")

    assert book.id == 1


@pytest.mark.unit
@pytest.mark.parametrize("author, title", [
    ("", "Clean Code"),
    ("Robert C. Martin", ""),
    ("", ""),
    (None, "Clean Code"),
])
def test_add_book__missing_field_raises(store_with_mock, author, title):
    before = store_with_mock.count()

    with pytest.raises(ValueError):
        store_with_mock.addBook(author, title)

    assert store_with_mock.count() == before


@pytest.mark.unit
def test_add_book__does_not_use_favorites(store_with_mock, mock_favorites):
    store_with_mock.addBook("Robert C. Martin", "Clean Code")

    assert not mock_favorites.add.called
    assert not mock_favorites.remove.called


# ---------- toggleFavorite ----------

@pytest.mark.unit
def test_toggle_favorite__marks_book(store_with_mock):
    result = store_with_mock.toggleFavorite(100)

    assert result is True
    assert store_with_mock.get_book(100).fav is True


@pytest.mark.unit
def test_toggle_favorite__adds_to_favorites(store_with_mock, mock_favorites):
    store_with_mock.toggleFavorite(100)

    book = store_with_mock.get_book(100)
    mock_favorites.add.assert_called_once_with(book)
    assert not mock_favorites.remove.called


@pytest.mark.unit
def test_toggle_favorite__twice_removes_from_favorites(store_with_mock, mock_favorites):
    store_with_mock.toggleFavorite(100)
    result = store_with_mock.toggleFavorite(100)

    book = store_with_mock.get_book(100)
    assert result is False
    assert book.fav is False
    mock_favorites.remove.assert_called_once_with(book)


@pytest.mark.unit
@pytest.mark.parametrize("clicks, expected", [(1, True), (2, False), (3, True), (4, False)])
def test_toggle_favorite__alternates(store_with_mock, mock_favorites, clicks, expected):
    for _ in range(clicks):
        store_with_mock.toggleFavorite(100)

    assert store_with_mock.get_book(100).fav is expected
    assert mock_favorites.add.call_count + mock_favorites.remove.call_count == clicks


@pytest.mark.unit
def test_toggle_favorite__only_affects_chosen_book(store_with_mock):
    store_with_mock.toggleFavorite(100)

    others = [b for b in store_with_mock.books if b.id != 100]
    assert all(b.fav is False for b in others)


@pytest.mark.unit
def test_toggle_favorite__unknown_id_raises(store_with_mock, mock_favorites):
    with pytest.raises(KeyError):
        store_with_mock.toggleFavorite(999)

    assert not mock_favorites.add.called


@pytest.mark.unit
def test_toggle_favorite__works_on_added_book(store_with_mock, mock_favorites):
    book = store_with_mock.addBook("Robert C. Martin", "Clean Code")

    store_with_mock.toggleFavorite(book.id)

    assert book.fav is True
    mock_favorites.add.assert_called_once_with(book)


@pytest.mark.unit
def test_initial_data__has_13_books(store_with_mock):
    assert store_with_mock.count() == 13
    assert all(isinstance(b, Book) for b in store_with_mock.books)
