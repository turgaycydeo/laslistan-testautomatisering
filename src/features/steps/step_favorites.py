from behave import then
from playwright.sync_api import expect


@then(u'ska meddelandet om att inga favoriter finns visas')
def step_empty_message_visible(context):
    expect(context.favorites.empty_message).to_be_visible()


@then(u'ska meddelandet om att inga favoriter finns inte visas')
def step_empty_message_hidden(context):
    expect(context.favorites.empty_message).not_to_be_visible()
    expect(context.favorites.list_heading).to_be_visible()


@then(u'ska listan med favoriter innehålla {count:d} böcker')
def step_favorites_count(context, count):
    expect(context.favorites.items).to_have_count(count)


@then(u'ska "{title}" finnas bland mina böcker')
def step_in_favorites(context, title):
    item = context.favorites.item(title)
    expect(item).to_be_visible()
    expect(item).to_have_text(title)


@then(u'ska "{title}" inte finnas bland mina böcker')
def step_not_in_favorites(context, title):
    expect(context.favorites.item(title)).to_have_count(0)
