from conftest import browser
from .base_page import BasePage
from .locators import BuyTicketSpecialGameLocators
import time
from selenium.webdriver.common.keys import Keys


class SpecialGamePage(BasePage):
    def buy_ticket_5_card(self):
        self.browser.execute_script("window.scrollBy (0, 200);")
        self.browser.find_element(*BuyTicketSpecialGameLocators.TICKET_SPECIALGAME).click()
        self.browser.find_element(*BuyTicketSpecialGameLocators.QUANTITY_5).click()
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_ALL_WAYS).click()
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_BANK_CARD).click()
        time.sleep(10)
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_NUMBER_CARD).send_keys("4111111111111111")
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_MONTH_CARD).send_keys("12")
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_YEARS_CARD).send_keys("24")
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_CVC_CARD).send_keys("123")
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_PAY).click()
        assert self.is_element_present(*BuyTicketSpecialGameLocators.PAYMENT), "Very well"