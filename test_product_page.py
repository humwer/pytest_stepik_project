from .pages.product_page import ProductPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
promo_links = [f'{link}?promo=offer{i}' for i in range(10)]
bad_link = promo_links[7]
promo_links[7] = pytest.param(bad_link, marks=pytest.mark.xfail)


@pytest.mark.parametrize('url', promo_links)
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_backet()
    page.solve_quiz_and_get_code()
    page.product_name_equals_product_name_in_basket()
    page.price_product_equals_price_basket()
