from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button[type='submit']")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p[class='price_color']")
    PRICE_BASKET = (By.CSS_SELECTOR, "div[class='alertinner '] p > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div[class='alertinner '] > strong")
