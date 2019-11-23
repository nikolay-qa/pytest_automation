from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    ITEM_NAME = (By.XPATH, "(//div[@class='alert alert-safe alert-noicon alert-success  fade in']/div[@class='alertinner ']/strong)[1]")
    ITEM_PRICE = (By.XPATH, "//div[@class='alertinner ']//p//strong")
    INPUT_ITEM_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    INPUT_ITEM_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')

