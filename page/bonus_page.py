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
        check_bonus = self.browser.find_element(*BonusPageLocators.CHECK_BONUS).text
        # assert check_bonus == "3"
        # 'Бонусов больше нуля'

    def buy_bonus(self, price, super_kuzmitch):  # бонусы на сайте временно не работают
        self.browser.find_element(*BonusPageLocators.LINK_BONUS).click()
        self.browser.find_element(*BonusPageLocators.PARTICIPATE_BONUS).click()
        time.sleep(3)  # изменить на ожидание
        button_continue = self.browser.find_element(*BonusPageLocators.BUTTON_CONTINUE)
        for i in range(7):  # нажатие кнопки подрят 6 раз
            button_continue.click()
        self.browser.find_element(*BonusPageLocators.BUTTON_START_GAME).click()
        self.browser.find_element(*price).click()
        # добавить проверки с assert
        self.browser.find_element(*super_kuzmitch).click()
        self.browser.find_element(*BonusPageLocators.BUTTON_BUY).click()
        #time.sleep(10)#сделать явное ожидаие
        button_1 = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="_1Ht_WDf2 qkhhnR9C GXU9otnQ eyU4tGLN"]')))
        button_1.click()
        print(button_1)
        #bot_1 = self.browser.find_element(*BonusPageLocators.BUTTON_UNDERSTAND)
        #bot_1.click()# жду появление кнопки

        button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="qkhhnR9C GXU9otnQ eyU4tGLN _1FOkYbwB ysSC7RPq"]')))
        button.click()
        print(button)
        #self.browser.find_element(*BonusPageLocators.BUTTON_UNDERSTAND).click()# для нее сделать ожидание
        #time.sleep(20)
        #self.browser.find_element(*BonusPageLocators.BUTTON_GAME_1).click()
        #time.sleep(3)


