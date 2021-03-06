import pytest

from page.bonus_page import BonusPage
from page.locators import BonusPageLocators
from page.main_page import MainPage




def test_check_bonus(browser):
    link = "https://tifa.stoloto.ru/"
    page = MainPage(browser, link)  # обращаемся к классу
    page.open()
    page.auth_page()
    page.check_bonus_page()

#@pytest.mark.skip
@pytest.mark.parametrize('price, super_kuzmitch', [#использовал parametrize т.к у кнопки BONUS одинаковый локатор, а у игры Кузьмич, разные локаторы.Нажатик кнопок идет друг за другом
    (BonusPageLocators.BONUS_3, BonusPageLocators.SUPER_KUZMITCH_3),
    (BonusPageLocators.BONUS_9, BonusPageLocators.SUPER_KUZMITCH_9),
    (BonusPageLocators.BONUS_30, BonusPageLocators.SUPER_KUZMITCH_30),
    (BonusPageLocators.BONUS_90, BonusPageLocators.SUPER_KUZMITCH_90)])
def test_buy_bonus(browser, price, super_kuzmitch):
    link = "https://tifa.stoloto.ru/"
    page = MainPage(browser, link)
    page.open()
    page.auth_page()
    page = BonusPage(browser, link)
    page.buy_bonus(price, super_kuzmitch)


