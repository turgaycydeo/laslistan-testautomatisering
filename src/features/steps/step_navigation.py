from behave import given, step, then
from playwright.sync_api import expect


@given(u'att jag är på Läslistans startsida')
def step_start_page(context):
    context.header.navigate()
    context.current_view = "Katalog"


@step(u'jag går till vyn "{view}"')
def step_go_to_view(context, view):
    context.header.go_to(view)
    context.current_view = view


@then(u'ska rubriken "Läslistan" visas')
def step_heading_visible(context):
    expect(context.header.heading).to_be_visible()


@then(u'ska vyn "{view}" vara vald')
def step_view_selected(context, view):
    expect(context.header.nav_button(view)).to_be_disabled()


@then(u'ska de andra navigeringsknapparna gå att klicka på')
def step_other_buttons_enabled(context):
    for view in context.views:
        if view != context.current_view:
            expect(context.header.nav_button(view)).to_be_enabled()


@then(u'ska innehållet för "{view}" visas')
def step_view_content_visible(context, view):
    expect(context.views[view].content()).to_be_visible()


@then(u'ska innehållet för "{view}" inte visas')
def step_view_content_hidden(context, view):
    expect(context.views[view].content()).not_to_be_visible()
