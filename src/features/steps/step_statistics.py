import re

from behave import then
from playwright.sync_api import expect


@then(u'ska statistiken visa att listan har {count:d} böcker')
def step_book_count(context, count):
    expect(context.stats.book_count).to_have_text(re.compile(rf"Listan har {count}\b böcker"))


@then(u'ska statistiken visa att {count:d} böcker är hjärtmarkerade')
def step_stars_count(context, count):
    expect(context.stats.stars_count).to_have_text(re.compile(rf"hjärtmarkerat {count}\b böcker"))
