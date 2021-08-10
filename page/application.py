from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from .locators import LoginPageLocators, BonusPageLocators


class Application:

    def __init__(self):
        self.wd = WebDriver()

    def auth_page(self):
        wd = self.wd
        wd.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wd.find_element(*LoginPageLocators.AUTH_LOGIN).send_keys(str('79777772233@mailinator.com'))
        wd.find_element(*LoginPageLocators.AUTH_PASSWORD).send_keys(str("Test2020"))
        wd.find_element(*LoginPageLocators.LOGIN_ENTER).click()


    def check_bonus_page(self):
        wd = self.wd
        wd.find_element(*BonusPageLocators.LINK_BONUS).click()
        #print('LINK_BONUS', link_bonus)

    def destroy(self):
        self.wd.quit()

