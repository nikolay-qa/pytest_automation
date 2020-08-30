from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # wrong link for testing correctness of assertion message
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")  # The View basket button
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT_FIELD = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTER_PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@id='id_registration-password1']")
    REGISTER_CONFIRM_PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@id='id_registration-password2']")
    REGISTER_FORM_SUBMIT_BUTTON = (By.XPATH, "//button[@name='registration_submit']")



class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    ITEM_NAME = (By.XPATH, "(//div[@class='alert alert-safe alert-noicon alert-success  fade in']/div[@class='alertinner ']/strong)[1]")
    ITEM_PRICE = (By.XPATH, "//div[@class='alertinner ']//p//strong")
    INPUT_ITEM_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    INPUT_ITEM_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    SUCCESS_MESSAGE = (By.XPATH, "(//div[@class='alert alert-safe alert-noicon alert-success  fade in']/div[@class='alertinner ']/strong)[1]")


class BasketPageLocators:
    NO_ITEMS_IN_BASKET = (By.XPATH, "//div[@id='content_inner']/p")
    QUANTITY_OF_FIRST_ITEM_IN_BASKET = (By.XPATH, "//input[@id='id_form-0-quantity']")
    ONE_ADDED_ITEM_IN_BASKET = (By.XPATH, "// a[text() = 'Coders at Work']")

