from conftest import browser
from .base_page import BasePage
from .locators import BuyTicketSpecialGameLocators
import time
from selenium.webdriver.common.keys import Keys


class SpecialGamePage(BasePage):
    def buy_ticket_5(self):
        self.browser.execute_script("window.scrollBy (0, 200);")
        self.browser.find_element(*BuyTicketSpecialGameLocators.TICKET_SPECIALGAME).click()
        self.browser.find_element(*BuyTicketSpecialGameLocators.QUANTITY_5).click()
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_PAYMENT_CARD).click()
        time.sleep(7)#изменить на неявное ожидание
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_VISA).click()
        self.browser.find_element(*BuyTicketSpecialGameLocators.INPUT_VISA).send_keys(Keys.COMMAND + '123')#имитация клавиатуры
        self.browser.find_element(*BuyTicketSpecialGameLocators.BUTTON_PAY).click()
        confirmation_of_payment = self.browser.find_element(BuyTicketSpecialGameLocators.CONFIRMATION_OF_PAYMENT).click()
        confirmation_of_payment.send_keys(Keys.COMMAND + "12345678")