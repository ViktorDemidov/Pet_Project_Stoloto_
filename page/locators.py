from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//span[@class="iconic iconic-user"]')
    AUTH_LOGIN = (By.XPATH, '//input[@id="auth_login"]')
    AUTH_PASSWORD = (By.XPATH, '//input[@id="auth_password"]')
    LOGIN_ENTER = (By.XPATH, '//span[@class="submit_button_container"]')


class NickPageLocators:
    NICK = (By.XPATH, '//a[@href="/private"]')


class BonusPageLocators:
    LINK_BONUS = (By.XPATH, '//span[@class="available"]/a[@class="with_extra_active_area"]')
    CHECK_BONUS = (By.XPATH, '//div[@class="balance alt_links"]/p[@class="value"]/ins[@class="refresh_bonus_sum pseudo"]')
