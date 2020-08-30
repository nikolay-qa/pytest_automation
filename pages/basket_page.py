from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_no_items_in_basket(self):
        empty_basket = self.browser.find_element(*BasketPageLocators.NO_ITEMS_IN_BASKET).text
        assert "Your basket is empty." in empty_basket, 'The "Your basket is empty" message is not shown'

    def is_not_present_quantity_of_first_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.QUANTITY_OF_FIRST_ITEM_IN_BASKET)

    def added_item_is_shown_on_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.ONE_ADDED_ITEM_IN_BASKET)

