from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_BUTTON = (By.XPATH, '//span[@class="iconic iconic-user"]')
    AUTH_LOGIN = (By.XPATH, '//input[@id="auth_login"]')
    AUTH_PASSWORD = (By.XPATH, '//input[@id="auth_password"]')
    LOGIN_ENTER = (By.XPATH, '//span[@class="submit_button_container"]')


