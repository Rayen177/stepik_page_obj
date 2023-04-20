from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTRATION_FROM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    EMAIL_FIELD = (By.XPATH, '//*[@id="id_registration-email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="id_registration-password1"]')
    PASSWORD_FIELD_REPEAT = (By.XPATH, '//*[@id="id_registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_OF_BOOK_ADDED = (By.XPATH, '//div[@class="alertinner "]/strong')
    SUCCESS_ADDED_TEXT = (By.XPATH, '//div[@class="alertinner "]')
    BOOK_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRICE_OF_BOOK = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p')
    PRICE_IN_BASKET = (By.XPATH, '//div[@class="alertinner "]/p/strong')


class BasketPageLocators:
    BASKET_PAGE = (By.CSS_SELECTOR, 'span a.btn.btn-default')
    EMPTY_TEXT = (By.CSS_SELECTOR, 'div#content_inner p:nth-child(1)')
    ITEMS_ABSENT = (By.CSS_SELECTOR, 'div.basket-items')
