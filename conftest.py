from selenium import webdriver
import pytest



@pytest.fixture
def browser():
    browser = webdriver.Chrome(r"C:\Users\v.demidov\PycharmProjects\chromedriver.exe")
    browser.maximize_window()
    login = "***"
    password = "***"
    browser.get("https://{}:{}@tifa.stoloto.ru/".format(login, password))#обход алерта
    return browser
