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

    def buy_bonus(self, price, super_kuzmitch):
        self.browser.find_element(*BonusPageLocators.LINK_BONUS).click()
        self.browser.find_element(*BonusPageLocators.PARTICIPATE_BONUS).click()
        time.sleep(3)# изменить на ожидание
        button_continue = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE)
        for i in range(7):  # нажатие кнопки подрят 6 раз
            button_continue.click()
        self.browser.find_element(*BonusPageLocators.BUTTON_START_GAME).click()
        self.browser.find_element(*price).click()
        #добавить проверки с assert
        self.browser.find_element(*super_kuzmitch).click()
        self.browser.find_element(*BonusPageLocators.BUTTON_BUY).click()



