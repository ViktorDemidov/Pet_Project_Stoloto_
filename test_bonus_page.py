from page.bonus_page import BonusPage
from page.main_page import MainPage
import time


def test_check_bonus(browser):
    link = "https://tifa.stoloto.ru/"
    page = MainPage(browser, link)  # обращаемся к классу
    page.open()
    page.auth_page()
    page.check_bonus_page()


def test_buy_bonus_3(browser):
    link = "https://tifa.stoloto.ru/"
    page = MainPage(browser, link)
    page.open()
    page.auth_page()
    #page.check_bonus_page()
    page.buy_bonus_3()
