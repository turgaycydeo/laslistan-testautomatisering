import re

from src.features.pages.base_page import BasePage


class FavoritesPage(BasePage):
    """Vyn "Mina böcker": en numrerad lista med favoritböckerna."""

    def __init__(self, page):
        super().__init__(page)
        self.empty_message = page.get_by_text("När du valt, kommer dina favoritböcker att visas här.")
        self.list_heading = page.get_by_text("Dina favoriter:")
        self.items = page.get_by_test_id("book-list").get_by_role("listitem")

    def content(self):
        # Antingen tom-meddelandet eller rubriken för listan visas
        return self.page.get_by_text(re.compile("När du valt, kommer dina favoritböcker|Dina favoriter:"))

    def item(self, title):
        return self.page.get_by_test_id(f"fav-{title}")
