from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//span[@class="iconic iconic-user"]')
    AUTH_LOGIN = (By.XPATH, '//input[@id="auth_login"]')
    AUTH_PASSWORD = (By.XPATH, '//input[@id="auth_password"]')
    LOGIN_ENTER = (By.XPATH, '//span[@class="submit_button_container"]')


class BonusPageLocators:
    LINK_BONUS = (By.XPATH, '//span[@class="available"]/a[@class="with_extra_active_area"]')
    CHECK_BONUS = (By.XPATH, '//div[@class="balance alt_links"]/p[@class="value"]/ins[@class="refresh_bonus_sum pseudo"]')
    PARTICIPATE_BONUS = (By.XPATH, '//div[@class="games_teaser pseudo"]/div[@class="bg"]')
    BONUS_3 = (By.XPATH, '//*[@id="gameguide__composter"]/div/div[2]')
    BONUS_9 = (By.XPATH, '//*[@id="gameguide__composter"]/div/div[3]')
    BONUS_30 = (By.XPATH, '//*[@id="gameguide__composter"]/div/div[4]')
    BONUS_90 = (By.XPATH, '//*[@id="gameguide__composter"]/div/div[5]')
    SUPER_KUZMITCH_3 = (By.XPATH, '//div[@class="_104VHXFQ"]/div[@class="_3aUAViRB"]/div[@name="naperstki_bonusk"]')
    SUPER_KUZMITCH_9 = (By.XPATH, '//div[@class="_1ZkJouxb _3NMn0dQs _2P0RqsEQ"]')
    SUPER_KUZMITCH_30 = (By.XPATH, '//div[@class="_3aUAViRB"]/div[@class="_1ZkJouxb _3NMn0dQs _2P0RqsEQ"]')
    SUPER_KUZMITCH_90 = (By.XPATH, '//div[@name="naperstki_bonusn"]')
    BUTTON_BUY = (By.XPATH, '//div[@class="C94ZXURa"]/button[@class="qkhhnR9C GXU9otnQ eyU4tGLN"]')
    BUTTON_CONTINUE = (By.XPATH, '//div[@class="f6K2DpdV"]/button[@class="gameguide__btn qkhhnR9C GXU9otnQ eyU4tGLN"]')
    BUTTON_START_GAME = (By.XPATH, '//div[@class="f6K2DpdV"]/button[@class="gameguide__btn qkhhnR9C GXU9otnQ eyU4tGLN"]')
    BUTTON_UNDERSTAND = (By.XPATH, '//button[text()="Понятно"]')
    BUTTON_GAME = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/main/div/div[2]/a')
    BUTTON_GAME_1 = (By.XPATH, '//button[text()="Играть"]')


class BuyTicketSpecialGameLocators:#Специгра
    TICKET_SPECIALGAME = (By.XPATH, '//a[@href="/spec/game?draw=771"]')
    QUANTITY_5 = (By.XPATH, '//*[@id="desktop-coupon"]/div/div/div/div/div[1]/div/div/div/div[2]/div/div[2]/label[1]/div/span')
    BUTTON_PAYMENT_CARD = (By.XPATH, '//button[@class="dxyire-1 CMeWh"]')
    BUTTON_VISA = (By.XPATH, '//button[@class="styles_bindingButton__2woLh"]')
    INPUT_VISA = (By.XPATH, '//input[@id="cvc"]')
    BUTTON_PAY = (By.XPATH, '//button[@data-test-id="cvc-submit"]')
    CONFIRMATION_OF_PAYMENT = (By.XPATH, '//input[@id="password"]')

