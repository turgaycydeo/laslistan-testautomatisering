import re

from src.features.pages.base_page import BasePage


class FavoritesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.empty_message = page.get_by_text("När du valt, kommer dina favoritböcker att visas här.")
        self.list_heading = page.get_by_text("Dina favoriter:")
        self.items = page.get_by_test_id("book-list").get_by_role("listitem")

    def content(self):
        return self.page.get_by_text(re.compile("När du valt, kommer dina favoritböcker|Dina favoriter:"))

    def item(self, title):
        return self.page.get_by_test_id(f"fav-{title}")
