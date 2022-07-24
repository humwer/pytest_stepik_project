from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket_button.click()
        print("[+] Successful transition to basket")

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS, 4), "Basket isn't empty"
        print("[+] Basket is empty")

    def should_be_basket_text_if_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS, 4), "Basket hasn't text about absence"
        print("[+] Basket has text about absence")
