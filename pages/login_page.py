from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "No 'login' in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        email_input = register_form.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password1_input = register_form.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD1)
        password2_input = register_form.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2)
        submit_button = register_form.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON)
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        submit_button.click()
        