from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart.click()

    def input_item_name(self):
        input_item_name = self.browser.find_element(*ProductPageLocators.INPUT_ITEM_NAME).text
        return input_item_name

    def input_item_price(self):
        input_item_price = self.browser.find_element(*ProductPageLocators.INPUT_ITEM_PRICE).text
        return input_item_price

    def item_should_be_in_cart_with_correct_name(self, input_name):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert input_name == item_name, "Item name is not equal"

    def item_price_should_be_correct(self, input_price):
        item_price_value = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert input_price == item_price_value, "item price is not equal"