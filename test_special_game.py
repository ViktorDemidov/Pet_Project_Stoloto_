import pytest

from page.bonus_page import BonusPage
from page.main_page import MainPage
from page.locators import BuyTicketSpecialGameLocators
from page.special_game_page import SpecialGamePage


def test_buy_ticket(browser):
    link = "https://tifa.stoloto.ru/"
    page = MainPage(browser, link)
    page.open()
    page.auth_page()
    page = SpecialGamePage(browser, link)
    page.buy_ticket_5_card()
