import pytest
from page.bonus_page import BonusPage
from page.locators import BuyWalletLocators
from page.main_page import MainPage
#from page.

def test_wallet_page(browser):
    link = "https://tifa.stoloto.ru/"
    page = MainPage(browser, link)  # обращаемся к классу
    page.open()
    page.auth_page()
    #page = Wallet