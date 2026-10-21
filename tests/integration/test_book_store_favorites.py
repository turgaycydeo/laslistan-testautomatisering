import pytest

from src.book_store import BookStore


# Integrationstest: testar att BookStore och FavoriteBooks fungerar tillsammans.
# Mocka inte, använd riktiga klasser i stället. Fixturen "favorites" finns i conftest.py.

@pytest.fixture
def store(favorites):
    return BookStore(favorites=favorites)


@pytest.mark.integration
def test_toggle_favorite__book_appears_in_favorites(store, favorites):
    store.toggleFavorite(100)

    assert favorites.contains(store.get_book(100))
    assert favorites.count() == 1


@pytest.mark.integration
def test_toggle_favorite_twice__book_disappears_from_favorites(store, favorites):
    store.toggleFavorite(100)
    store.toggleFavorite(100)

    assert not favorites.contains(store.get_book(100))
    assert favorites.count() == 0


@pytest.mark.integration
@pytest.mark.parametrize("clicks, expected_count", [(1, 1), (2, 0), (3, 1), (4, 0)])
def test_toggle_favorite_many_times__favorites_follow(store, favorites, clicks, expected_count):
    for _ in range(clicks):
        store.toggleFavorite(100)

    assert favorites.count() == expected_count
    assert store.get_book(100).fav == (expected_count == 1)


@pytest.mark.integration
def test_several_favorites__only_unmarked_book_is_removed(store, favorites):
    store.toggleFavorite(100)
    store.toggleFavorite(102)
    store.toggleFavorite(103)

    store.toggleFavorite(102)

    assert [b.id for b in favorites.get_books()] == [100, 103]


@pytest.mark.integration
def test_added_book__can_become_favorite(store, favorites):
    book = store.addBook("Robert C. Martin", "Clean Code")

    store.toggleFavorite(book.id)

    assert favorites.get_books() == [book]


@pytest.mark.integration
def test_favorites_match_marked_books_in_store(store, favorites):
    for book_id in (100, 105, 115):
        store.toggleFavorite(book_id)
    store.toggleFavorite(105)

    marked = [b for b in store.books if b.fav]
    assert favorites.get_books() == marked


@pytest.mark.integration
def test_new_store__has_no_favorites(store, favorites):
    assert favorites.count() == 0
    assert not any(b.fav for b in store.books)
