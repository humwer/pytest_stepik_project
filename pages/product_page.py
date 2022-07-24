from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_backet(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        print('[+] Product added to basket')

    def product_name_equals_product_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name in product_name_in_basket, f"Incorrect! Price product: {product_name}, " \
                                                       f"price basket: {product_name_in_basket}"
        print('[+] Product name equals product name in basket')

    def price_product_equals_price_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_product in price_basket, f"Incorrect! Price product: {price_product}, price basket: {price_basket}"
        print('[+] Price of product equals price of basket')
