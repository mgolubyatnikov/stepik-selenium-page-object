import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_be_product_added_to_cart_message()
    page.should_be_basket_price_message()

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_cart_with_promo(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_cart()
#     page.should_be_product_added_to_cart_message()
#     page.should_be_basket_price_message()

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser): 
#     page = ProductPage(browser, product_link)
#     page.open()
#     page.add_product_to_cart()
#     page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser): 
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()


# def test_message_dissapeared_after_adding_product_to_cart(browser):  
#     page = ProductPage(browser, product_link)
#     page.open()
#     page.add_product_to_cart()
#     page.should_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
