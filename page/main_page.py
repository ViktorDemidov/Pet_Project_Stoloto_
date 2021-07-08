from .base_page import BasePage
from .locators import LoginPageLocators, BonusPageLocators


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


    def check_bonus_page(self):
        link_bonus = self.browser.find_element(*BonusPageLocators.LINK_BONUS)
        link_bonus.click()
        print('LINK_BONUS', link_bonus)
        check_bonus = self.browser.find_element(*BonusPageLocators.CHECK_BONUS).text

    def buy_bonus_3(self):
        link_bonus = self.browser.find_element(*BonusPageLocators.LINK_BONUS)
        link_bonus.click()
        participate_bonus = self.browser.find_element(*BonusPageLocators.PARTICIPATE_BONUS)
        participate_bonus.click()
        button_continue = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE)
        button_continue.click()
        button_start_game = self.browser.find_element(*BonusPageLocators.BUTTON_START_GAME)
        button_start_game.click()
        bonus_3 = self.browser.find_element(*BonusPageLocators.BONUS_3)
        bonus_3.click()
        super_kuzmitch = self.browser.find_element(*BonusPageLocators.SUPER_KUZMITCH)
        super_kuzmitch.click()
        button_buy = self.browser.find_element(*BonusPageLocators.BUTTON_BUY)
        button_buy.click()


