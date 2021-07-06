from .base_page import BasePage
from .locators import LoginPageLocators


class MainPage(BasePage):
    def auth_page(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        auth_login = self.browser.find_element(*LoginPageLocators.AUTH_LOGIN)
        auth_login.send_keys(str('***'))
        auth_password = self.browser.find_element(*LoginPageLocators.AUTH_PASSWORD)
        auth_password.send_keys(str("***"))
        login_enter = self.browser.find_element(*LoginPageLocators.LOGIN_ENTER)
        login_enter.click()
