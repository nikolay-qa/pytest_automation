from pages.base_page import BasePage
from .locators import LoginPageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url does not have login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self):
        test_data = faker.Faker()
        test_password = test_data.password()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT_FIELD).send_keys(test_data.email())
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT_FIELD).send_keys(test_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_INPUT_FIELD).send_keys(test_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON).click()
