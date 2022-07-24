from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link_success = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
link_login = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
promo_links = [f'{link}?promo=offer{i}' for i in range(10)]
bad_link = promo_links[7]
promo_links[7] = pytest.param(bad_link, marks=pytest.mark.xfail)


@pytest.mark.parametrize('url', promo_links)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_backet()
    page.solve_quiz_and_get_code()
    page.product_name_equals_product_name_in_basket()
    page.price_product_equals_price_basket()


@pytest.mark.skip(reason='')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_success)
    page.open()
    page.add_to_backet()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_success)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_success)
    page.open()
    page.add_to_backet()
    page.should_success_message_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link_success)
    page.open()
    page.should_be_basket_is_empty()
    page.should_be_basket_text_if_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.authuser
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link_login)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, 'TestingPassword')

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_success)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_success)
        page.open()
        page.add_to_backet()
        page.product_name_equals_product_name_in_basket()
        page.price_product_equals_price_basket()
