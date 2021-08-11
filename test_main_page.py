from page.main_page import MainPage
import time


def test_login_page(browser):
    link = 'https://tifa.stoloto.ru/'
    page = MainPage(browser, link)
    page.open()
    page.auth_page()


def test_change_nick(browser):#проверка ника
    link = 'https://tifa.stoloto.ru/'
    page = MainPage(browser, link)
    page.open()
    page.auth_page()
    time.sleep(5)
    page.change_nick()
    time.sleep(5)