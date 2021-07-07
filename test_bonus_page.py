from page.bonus_page import BonusPage
from page.main_page import MainPage


def test_check_bonus(browser):
    link = "https://tifa.stoloto.ru/"
    page = MainPage(browser, link)
    page.open()
    page.auth_page()
    page.check_bonus()