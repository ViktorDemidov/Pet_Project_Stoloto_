from selenium import webdriver
import pytest



@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(r"C:\Users\v.demidov\PycharmProjects\chromedriver.exe")
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
