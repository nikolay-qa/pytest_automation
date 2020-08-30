from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


product_link_base = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
login_link_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
links = [f"{product_link_base}/?promo=offer{number}" for number in range(10) if number != 7]
# adding number of offer to the base link and excluding 7 test

xfail_link = pytest.param([f"{product_link_base}/?promo=offer7"], marks=pytest.mark.xfail(reason="Mistake on the page"))
# marking offer7 test as xfail

links.insert(7, xfail_link)
# adding test that marked as xfail to the all links to get all the tests in the pytest report


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    input_name = page.input_item_name()
    input_price = page.input_item_price()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.item_should_be_in_cart_with_correct_name(input_name)
    page.item_price_should_be_correct(input_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link_base)
    page.open()
    page.add_item_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link_base)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_success_message_is_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link_base)
    page.open()
    page.add_item_to_cart()
    page.message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link_base)
    page.open()
    page.open_basket()
    page.is_not_present_quantity_of_first_item_in_basket()
    page.should_be_message_no_items_in_basket()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    page.is_not_present_quantity_of_first_item_in_basket()
    page.should_be_message_no_items_in_basket()


def test_guest_can_see_added_product_in_basket_after_adding_one_item_and_clicking_on_view_basket(browser):
    page = ProductPage(browser, product_link_base)
    page.open()
    page.add_item_to_cart()
    page.open_basket()
    page.added_item_is_shown_on_basket_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link_page)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, login_link_page)
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link_base)
        page.open()
        input_name = page.input_item_name()
        input_price = page.input_item_price()
        page.add_item_to_cart()
        page.item_should_be_in_cart_with_correct_name(input_name)
        page.item_price_should_be_correct(input_price)
