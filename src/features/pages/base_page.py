from playwright.sync_api import Page

BASE_URL = "https://tap-vt26-testautomatisering.github.io/exam/"


class BasePage:
    NAV_TEST_IDS = {
        "Katalog": "catalog",
        "Lägg till bok": "add-book",
        "Mina böcker": "favorites",
        "Statistik": "statistics",
    }

    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Läslistan")

    def navigate(self):
        self.page.goto(BASE_URL, timeout=30_000)

    def nav_button(self, view):
        return self.page.get_by_test_id(self.NAV_TEST_IDS[view])

    def go_to(self, view):
        self.nav_button(view).click()

    def content(self):
        raise NotImplementedError
