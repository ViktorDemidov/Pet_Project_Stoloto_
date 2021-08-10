from .base_page import BasePage
from .locators import BuyWalletLocators
from .locators import BuyTicketSpecialGameLocators
import time


class WalletPage(BasePage):
    def buy_of_wallet(self):
        self.browser.find_element(*BuyWalletLocators.HOUSING_LOTTERY).click()
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_ALL_WAYS).click()
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_BANK_CARD).click()
        time.sleep(10)
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_NUMBER_CARD).send_keys("4111111111111111")
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_MONTH_CARD).send_keys("12")
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_YEARS_CARD).send_keys("24")
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_CVC_CARD).send_keys("123")
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_PAY).click()

