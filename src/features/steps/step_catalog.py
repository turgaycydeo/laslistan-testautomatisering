import re

from behave import step, then
from playwright.sync_api import expect

SELECTED = re.compile(r"\bselected\b")


@step(u'jag klickar på hjärtat för "{title}"')
def step_click_star(context, title):
    context.catalog.toggle_favorite(title)


@step(u'jag klickar på hjärtat för "{title}" {times:d} gånger')
def step_click_star_many_times(context, title, times):
    for _ in range(times):
        context.catalog.toggle_favorite(title)


@step(u'jag hjärtmarkerar de {count:d} första böckerna')
def step_mark_first_books(context, count):
    context.catalog.mark_first_books(count)


@then(u'ska katalogen visa {count:d} böcker')
def step_catalog_count(context, count):
    expect(context.catalog.stars).to_have_count(count)


@then(u'ska inga böcker vara hjärtmarkerade')
def step_no_books_marked(context):
    expect(context.page.locator(".star.selected")).to_have_count(0)


@then(u'ska hjärtat för "{title}" vara {state}')
def step_star_state(context, title, state):
    star = context.catalog.star(title)
    if state == "markerat":
        expect(star).to_have_class(SELECTED)
    elif state == "omarkerat":
        expect(star).not_to_have_class(SELECTED)
    else:
        raise ValueError(f'Okänd status: "{state}". Använd "markerat" eller "omarkerat".')


@then(u'ska boken "{title}" av "{author}" finnas i katalogen')
def step_book_in_catalog(context, title, author):
    expect(context.catalog.book_entry(title, author)).to_be_visible()
