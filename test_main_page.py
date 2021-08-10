from page.main_page import MainPage
import time
import pytest
from page.application import Application



@pytest.fixture()
def app(request):
    fixture = Application()#инициализация создание фикстуры
    request.addfinalizer(fixture.destroy)#указание как должна фикстура быть разрушена
    return fixture

def test_login_page(app):#тестовый метод принимающий в себя фикстуру
    link = 'https://tifa.stoloto.ru/'
    app.open()
    app.auth_page()

@pytest.mark.skip
def test_change_nick(browser):#проверка ника
    link = 'https://tifa.stoloto.ru/'
    app.open()
    app.auth_page()
    # time.sleep(5)
    #page.change_nick()
    #time.sleep(5)