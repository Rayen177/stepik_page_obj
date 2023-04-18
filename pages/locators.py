from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators:
    REGISTRATION_FROM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_OF_BOOK_ADDED = (By.XPATH, '//div[@class="alertinner "]/strong')
    SUCCESS_ADDED_TEXT = (By.XPATH, '//div[@class="alertinner "]')
    BOOK_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRICE_OF_BOOK = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p')
    PRICE_IN_BASKET = (By.XPATH, '//div[@class="alertinner "]/p/strong')