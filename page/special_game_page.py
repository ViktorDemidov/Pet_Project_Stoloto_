from conftest import browser
from .base_page import BasePage
from .locators import BuyTicketSpecialGameLocators




class SpecialGamePage(BasePage):
    def buy_ticket_5(self):
        self.browser.execute_script("window.scrollBy (0, 200);")
        self.browser.find_element(*BuyTicketSpecialGameLocators.TICKET_SPECIALGAME).click()
