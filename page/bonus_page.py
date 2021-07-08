from .base_page import BasePage
from .main_page import MainPage
from .locators import BonusPageLocators
import time

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
        time.sleep(2)
        button_continue = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE)
        button_continue.click()
        button_continue_1 = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE_1)
        button_continue_1.click()
        button_continue_2 = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE_2)
        button_continue_2.click()
        button_continue_3 = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE_3)
        button_continue_3.click()
        button_continue_4 = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE_4)
        button_continue_4.click()
        button_continue_5 = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE_5)
        button_continue_5.click()
        button_continue_6 = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE_6)
        button_continue_6.click()
        button_start_game = self.browser.find_element(*BonusPageLocators.BUTTON_START_GAME)
        button_start_game.click()
        bonus_3 = self.browser.find_element(*BonusPageLocators.BONUS_3)
        bonus_3.click()
        super_kuzmitch = self.browser.find_element(*BonusPageLocators.SUPER_KUZMITCH)
        super_kuzmitch.click()
        button_buy = self.browser.find_element(*BonusPageLocators.BUTTON_BUY)
        button_buy.click()


