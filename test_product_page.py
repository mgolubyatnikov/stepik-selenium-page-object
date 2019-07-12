import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time

coders_at_work_207_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.login_user
class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'FakePassword2019'
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, coders_at_work_207_product_page)
        page.open()
        page.add_product_to_cart()
        page.should_be_product_added_to_cart_message()
        page.should_be_basket_price_message()

    def test_user_cant_see_success_message(self, browser): 
        page = ProductPage(browser, coders_at_work_207_product_page)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, coders_at_work_207_product_page)
    page.open()
    page.add_product_to_cart()
    page.should_be_product_added_to_cart_message()
    page.should_be_basket_price_message()

def test_guest_cant_see_success_message(browser): 
    page = ProductPage(browser, coders_at_work_207_product_page)
    page.open()
    page.should_not_be_success_message()

the_city_and_the_stars_95_product_page = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, the_city_and_the_stars_95_product_page)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, the_city_and_the_stars_95_product_page)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, the_city_and_the_stars_95_product_page)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_basket_is_empty()
