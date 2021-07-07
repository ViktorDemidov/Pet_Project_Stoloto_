from .base_page import BasePage
from .main_page import MainPage
from .locators import BonusPageLocators


class BonusPage(MainPage):
    def check_bonus(self):
        link_bonus = self.browser.find_element(*BonusPageLocators.LINK_BONUS)
        link_bonus.click()
        #assert "3" <= link_bonus
