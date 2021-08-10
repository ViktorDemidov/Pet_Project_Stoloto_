from conftest import browser
from .base_page import BasePage
from .main_page import MainPage
from .locators import BonusPageLocators
from .locators import BuyTicketSpecialGameLocators
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BonusPage(BasePage):  # не работает assert
    def check_bonus_page(self):
        link_bonus = self.browser.find_element(*BonusPageLocators.LINK_BONUS)
        link_bonus.click()
        print('LINK_BONUS', link_bonus)


    def buy_bonus(self, price, super_kuzmitch):  # бонусы на сайте временно не работают
        self.browser.find_element(*BonusPageLocators.LINK_BONUS).click()
        self.browser.find_element(*BonusPageLocators.PARTICIPATE_BONUS).click()
        time.sleep(3)
        button_continue = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="f6K2DpdV"]/button[@class="gameguide__btn qkhhnR9C GXU9otnQ eyU4tGLN"]')))
        for i in range(7):  # нажатие кнопки подрят 6 раз
            button_continue.click()
        self.browser.find_element(*BonusPageLocators.BUTTON_START_GAME).click()
        self.browser.find_element(*price).click()
        self.browser.find_element(*super_kuzmitch).click()
        self.browser.find_element(*BonusPageLocators.BUTTON_BUY).click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Понятно"]'))).click()
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Играть"]'))).click()
        assert self.is_element_present(*BonusPageLocators.RULES), 'Very well'



        



