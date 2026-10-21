from behave import step, then, when
from playwright.sync_api import expect


def _field(context, name):
    fields = {
        "Titel": context.add_book.title_input,
        "Författare": context.add_book.author_input,
    }
    return fields[name]


@when(u'jag bara fyller i fältet "{name}" med "{text}"')
def step_fill_one_field(context, name, text):
    _field(context, name).fill(text)


@step(u'jag fyller i titeln "{title}" och författaren "{author}"')
def step_fill_form(context, title, author):
    context.add_book.fill_form(title, author)


@when(u'jag tömmer fältet "{name}"')
def step_clear_field(context, name):
    _field(context, name).clear()


@step(u'jag lägger till boken "{title}" av "{author}"')
def step_add_book(context, title, author):
    context.add_book.add_book(title, author)


@step(u'jag lägger till {count:d} nya böcker')
def step_add_many_books(context, count):
    for i in range(1, count + 1):
        context.add_book.add_book(f"Testbok {i}", f"Testförfattare {i}")


@then(u'ska formulärets fält vara tomma')
def step_form_empty(context):
    expect(context.add_book.title_input).to_have_value("")
    expect(context.add_book.author_input).to_have_value("")


@then(u'ska knappen "Lägg till ny bok" vara {state}')
def step_submit_state(context, state):
    button = context.add_book.submit_button
    if state == "aktiv":
        expect(button).to_be_enabled()
    elif state == "inaktiv":
        expect(button).to_be_disabled()
    else:
        raise ValueError(f'Okänd status: "{state}". Använd "aktiv" eller "inaktiv".')
