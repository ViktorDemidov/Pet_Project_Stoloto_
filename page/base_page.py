from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException: #указывает на найденную ошибку, которая указана в скобках
            return False
        return True

    def is_not_element_present(self, how, what,
                               timeout=4):  # проверяет, что элемент не появляется на странице в течение заданного времени.Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        try:
            print(how, what)
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

