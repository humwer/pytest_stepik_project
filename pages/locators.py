from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button[type='submit']")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p[class='price_color']")
    PRICE_BASKET = (By.CSS_SELECTOR, "div[class='alertinner '] p > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div[class='alertinner '] > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini > .btn-group > a")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket-title > .row")
    BASKET_TEXT_IF_EMPTY = (By.CSS_SELECTOR, "div[id='content_inner'] > p > a")
