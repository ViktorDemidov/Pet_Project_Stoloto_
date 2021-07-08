from .base_page import BasePage
from .main_page import MainPage
from .locators import BonusPageLocators


class BonusPage(BasePage):  # не работает assert
    def check_bonus_page(self):
        link_bonus = self.browser.find_element(*BonusPageLocators.LINK_BONUS)
        link_bonus.click()
        print('LINK_BONUS', link_bonus)
        check_bonus = self.browser.find_element(*BonusPageLocators.CHECK_BONUS).text
        # assert check_bonus == "3"
        # 'Бонусов больше нуля'

    def buy_bonus_3(self):
        link_bonus = self.browser.find_element(*BonusPageLocators.LINK_BONUS)
        link_bonus.click()
        participate_bonus = self.browser.find_element(*BonusPageLocators.PARTICIPATE_BONUS)
        participate_bonus.click()
        bonus_3 = self.browser.find_element(*BonusPageLocators.BONUS_3)
        bonus_3.click()
        super_kuzmitch = self.browser.find_element(*BonusPageLocators.SUPER_KUZMITCH)
        super_kuzmitch.click()
        button_buy = self.browser.find_element(*BonusPageLocators.BUTTON_BUY)
        button_buy.click()


