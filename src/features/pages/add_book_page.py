from src.features.pages.base_page import BasePage


class AddBookPage(BasePage):
    """Vyn "Lägg till bok": formulär med titel och författare."""

    def __init__(self, page):
        super().__init__(page)
        self.title_input = page.get_by_test_id("add-input-title")
        self.author_input = page.get_by_test_id("add-input-author")
        self.submit_button = page.get_by_test_id("add-submit")

    def content(self):
        return self.title_input

    def fill_form(self, title, author):
        self.title_input.fill(title)
        self.author_input.fill(author)

    def add_book(self, title, author):
        self.fill_form(title, author)
        self.submit_button.click()
