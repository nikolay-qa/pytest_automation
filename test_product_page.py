from pages.product_page import ProductPage
import pytest


product_link_base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_link_base}/?promo=offer{number}" for number in range(10) if number != 7]
# adding number of offer to the base link and excluding 7 test

xfail_link = pytest.param([f"{product_link_base}/?promo=offer7"], marks=pytest.mark.xfail(reason="Mistake on the page"))
# marking offer7 test as xfail

links.insert(7, xfail_link)
print(links)
# adding test that marked as xfail to the all links to get all the tests in the pytest report


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

