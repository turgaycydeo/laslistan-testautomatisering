from playwright.sync_api import sync_playwright

from src.features.pages.add_book_page import AddBookPage
from src.features.pages.base_page import BasePage
from src.features.pages.catalog_page import CatalogPage
from src.features.pages.favorites_page import FavoritesPage
from src.features.pages.stats_page import StatsPage


# Körs före alla scenarier
def before_all(context):
    # Headless som standard. Visa webbläsaren med: behave -D headless=false
    headless = context.config.userdata.getbool("headless", True)

    # Starta Playwright och webbläsaren - stängs i after_all
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=headless)


# Körs i början av varje scenario
def before_scenario(context, scenario):
    # Ny sida för varje scenario, så att data inte läcker mellan testen.
    # Appen sparar ingenting - varje scenario börjar med samma 13 böcker.
    context.page = context.browser.new_page()
    context.page.set_default_timeout(3_000)

    # Sidhuvudet med rubriken och navigeringen, som finns i alla vyer
    context.header = BasePage(context.page)

    # Page Object för varje vy
    context.catalog = CatalogPage(context.page)
    context.add_book = AddBookPage(context.page)
    context.favorites = FavoritesPage(context.page)
    context.stats = StatsPage(context.page)
    context.views = {
        "Katalog": context.catalog,
        "Lägg till bok": context.add_book,
        "Mina böcker": context.favorites,
        "Statistik": context.stats,
    }


# Körs direkt efter varje scenario - städa för att undvika minnesläckor
def after_scenario(context, scenario):
    if context.page:
        context.page.close()


# Körs efter att alla scenarier är klara - städa
def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
