import re

from src.features.pages.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.intro = page.get_by_text("Sidan för dig som gillar att läsa")
        self.stars = page.get_by_test_id(re.compile(r"^star-"))
        self.selected_stars = self.stars.and_(page.locator(".selected"))

    def content(self):
        return self.intro

    def star(self, title):
        return self.page.get_by_test_id(f"star-{title}")

    def toggle_favorite(self, title):
        self.star(title).click()

    def mark_first_books(self, count):
        for i in range(count):
            self.stars.nth(i).click()

    def book_entry(self, title, author):
        return self.page.get_by_text(f'"{title}", {author}')
