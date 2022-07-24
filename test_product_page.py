from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_backet()
    page.solve_quiz_and_get_code()
    page.product_name_equals_product_name_in_basket()
    page.price_product_equals_price_basket()

