import pytest

from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == LoginPageLocators.LOGIN_URL, f"Login url incorrect. " \
                                                                        f"Current url: {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form is not presented'

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.INPUT_CONFIRM_PASSWORD)
        input_confirm_password.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()
        print(f'[+] User registered: {email}:{password}')
