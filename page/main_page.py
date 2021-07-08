from .base_page import BasePage
from .locators import LoginPageLocators, NickPageLocators, BonusPageLocators


class MainPage(BasePage):
    def auth_page(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        auth_login = self.browser.find_element(*LoginPageLocators.AUTH_LOGIN)
        auth_login.send_keys(str('not_ident@mailinator.com'))
        auth_password = self.browser.find_element(*LoginPageLocators.AUTH_PASSWORD)
        auth_password.send_keys(str("Test2020"))
        login_enter = self.browser.find_element(*LoginPageLocators.LOGIN_ENTER)
        login_enter.click()

    def change_nick(self):
        nick_icon = self.browser.find_element(*NickPageLocators.NICK).text
        print('NICK',nick_icon)
        assert "NotIdentt" == nick_icon



    def check_bonus_page(self):
        pass


    def buy_bonus_3(self) -> object:
        pass


