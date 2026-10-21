from playwright.sync_api import Page

BASE_URL = "https://tap-vt26-testautomatisering.github.io/exam/"


class BasePage:
    """Det som är gemensamt för alla vyer: sidhuvudet med navigeringen."""

    # Namnet på vyn och test-id för dess knapp i navigeringen
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
        """Ett element som bara finns i den här vyn. Implementeras av varje vy."""
        raise NotImplementedError
