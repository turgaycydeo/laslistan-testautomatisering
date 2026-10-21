from src.features.pages.base_page import BasePage


class StatsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.book_count = page.get_by_test_id("book-count")
        self.stars_count = page.get_by_test_id("stars-count")

    def content(self):
        return self.book_count
