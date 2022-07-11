URL = "https://epos.erply.com/"


class ORLogin:
    clientcode = '[data-testid="clientCode"]'
    username = '[data-testid="username"]'
    password = '[data-testid="password"]'
    signin_button = '[data-testid="login-clockin-button"]'
    pos_item = '[data-testid="pos-item"]'

class ORApplication:
    employee_name = '[data-testid="employee-name"]'
    product_search_field = '[placeholder="Products"]'
    first_item_receipt_list = '[data-test-key="product-name-1"]'
    search_close_field_button = '//*[@id="product-search-container"]/div[1]/div/div/button'
    search_result_item_search_button = '//*[@id="product-search-container"]/div[2]/div/div[1]/table/tbody/tr/td[3]'
    search_result_title = 'div.modal-title.h4'
    quality_field_1_receipt_list = '//div[3]/table/tbody/tr[1]/td[3]/input'
    quality_field_2_receipt_list = '//div[3]/table/tbody/tr[2]/td[3]/input'