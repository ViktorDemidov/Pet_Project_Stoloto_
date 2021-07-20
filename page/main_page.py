from .base_page import BasePage
from .locators import LoginPageLocators, BonusPageLocators


class MainPage(BasePage):
    def auth_page(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        auth_login = self.browser.find_element(*LoginPageLocators.AUTH_LOGIN)
        auth_login.send_keys(str('79777772233@mailinator.com'))
        auth_password = self.browser.find_element(*LoginPageLocators.AUTH_PASSWORD)
        auth_password.send_keys(str("Test2020"))
        login_enter = self.browser.find_element(*LoginPageLocators.LOGIN_ENTER)
        login_enter.click()


    def check_bonus_page(self):
        link_bonus = self.browser.find_element(*BonusPageLocators.LINK_BONUS)
        link_bonus.click()
        print('LINK_BONUS', link_bonus)


