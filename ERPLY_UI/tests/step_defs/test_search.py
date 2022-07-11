from pytest_bdd import scenarios, given, when, then, parsers
import time
from ERPLY_UI.tests import page_object
from playwright.sync_api import expect

# Scenarios

scenarios('../features/search.feature')


# Login into application with valid credentials
@given('the home page is displayed')
def disply_home(page):
    page.set_viewport_size({'width': 1536, 'height': 960})
    page.set_default_timeout(10000)
    URL = page_object.URL
    page.goto(URL)
    # assert page.inner_text('[data-testid="title"]', timeout=10000) == 'Sign In'


@when(parsers.parse('fill "{clientcode}" and  "{username}" then "{password}"'))
def login_apllication(page, clientcode, username, password):
    page.fill(page_object.ORLogin.clientcode, clientcode)
    page.fill(page_object.ORLogin.username, username)
    page.fill(page_object.ORLogin.password, password)
    page.click(page_object.ORLogin.signin_button)
    page.click(page_object.ORLogin.pos_item)


@then(parsers.parse('verify applicaiton is rendered'))
def check_application(page):
    time.sleep(5)
    assert page.inner_text(page_object.ORApplication.employee_name) == 'Test User'


# verify search for the product


@given(parsers.parse('the search function with {some} value'))
def search_function(page, some):
    if some.lower() == 'empty':
        page.click(page_object.ORApplication.product_search_field)
    else:
        if '"' in some:
            some = some.replace('"', ' ')
        page.click(page_object.ORApplication.product_search_field)
        page.fill(page_object.ORApplication.product_search_field, some)


@when(parsers.parse('maximum {rows} displayed'))
def result_lookout(page, rows):
    expect(page.locator(
        '//*[@id="product-search-container"]/div[2]/div/div[1]/table/tbody/tr[' + rows + ']')).to_be_visible()
    expect(page.locator('//*[@id="product-search-container"]/div[2]/div/div[1]/table/tbody/tr[' + str(
        int(rows) + 1) + ']')).not_to_be_visible()


@then(parsers.parse('select the {product}'))
def select_product(page, product):
    page.click('text={}'.format(product))


@then(parsers.parse('verify the {product} result'))
def verify_outcome(page, product):
    if product != 'No results found.':
        expect(page.locator(page_object.ORApplication.first_item_receipt_list)).to_contain_text(product)
    else:
        expect(page.locator(page_object.ORApplication.first_item_receipt_list)).not_to_be_visible()


# verify exit-X button at search for the product
@when('clicking at x button')
def close_search(page):
    page.click(page_object.ORApplication.search_close_field_button)


@then('searched product should not be added')
def verify_result(page):
    expect(page.locator(page_object.ORApplication.first_item_receipt_list)).not_to_be_visible()


# verify search icon functionality from the result
@when('clicking at search icon button')
def click_search_icon(page):
    time.sleep(4)
    page.click(page_object.ORApplication.search_result_item_search_button)


@then('product details should be displayed')
def verify_search_product(page):
    expect(page.locator(page_object.ORApplication.search_result_title)).to_contain_text('Product details')


# verify selected search item is addition into receipt
@then(parsers.parse('the search function with {some} value'))
def search_items(page, some):
    search_function(page, some)


@then(parsers.parse('check {total} quatities added into receipt'))
def check_total(page, total):
    # time.sleep(5)
    # assert page.get_attribute('//*[@id="autoFocusInput"]', "value") == total
    assert page.get_attribute(page_object.ORApplication.quality_field_1_receipt_list, "value") == total


# verify multiple selected search item is addition into receipt
@then(parsers.parse('check {total} quatities of Strawberry-Banana Margarita added into receipt'))
def check_multiple_item_total(page, total):
    assert page.get_attribute(page_object.ORApplication.quality_field_2_receipt_list, "value") == total


# search with accessibility F9
@given(parsers.parse('the accessibility functionality through {key}'))
def accessibility_search(page, key):
    page.keyboard.press(key)


@then(parsers.parse('enter {product} into the product search box'))
def accessibility_type(page, product):
    page.keyboard.type(product)

@then(parsers.parse('select the {brand} product'))
def accessibility_type(page, brand):
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")