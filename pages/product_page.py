from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        #self.solve_quiz_and_get_code()

    def should_be_product_added_to_cart_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_messages = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        found = False
        for success_message in success_messages:
            if f"{product_name} has been added to your basket." == success_message.text.strip():
                found = True
        assert found, "No product added to cart message"

    def should_be_basket_price_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        info_messages = self.browser.find_elements(*ProductPageLocators.INFO_MESSAGE)
        found = False
        print(product_price)
        for info_message in info_messages:
            if f"Your basket total is now {product_price}" == info_message.text.strip():
                found = True
        assert found, "No basket price message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
