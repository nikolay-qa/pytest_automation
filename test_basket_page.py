from pages.basket_page import BasketPage
from pages.product_page import ProductPage

product_link_base = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, product_link_base)
    page.open()
    page.open_basket()
    page.is_not_present_quantity_of_first_item_in_basket()
    page.should_be_message_no_items_in_basket()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    page.is_not_present_quantity_of_first_item_in_basket()
    page.should_be_message_no_items_in_basket()

def test_guest_can_see_added_product_in_basket_after_adding_one_item_and_clicking_on_view_basket(browser):
    page = BasketPage(browser, product_link_base)
    page.open()
    page.add_item_to_cart()
    page.open_basket()
    page.added_item_is_shown_on_basket_page()

def test_guest_can_delete_one_added_product_from_basket(browser):
    pass

def test_guest_can_procced_to_checkout_after_adding_item_to_basket(browser):
    pass

def test_guest_can_increment_already_added_item_by_one(browser):
    pass

def test_guest_can_add_two_different_items_to_basket(browser):
    pass

def test_guest_can_delete_two_added_products_from_basket(browser):
    pass

def test_negative_guest_cant_fill_in_quantity_field_with_float_amount_of_added_to_basket_item(browser):
    pass
