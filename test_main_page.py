from page.main_page import MainPage
import time


def test_login_page(browser):
    link = 'https://tifa.stoloto.ru/'
    page = MainPage(browser, link)
    page.open()
    page.auth_page()
    time.sleep(15)
