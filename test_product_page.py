from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
import faker
import pytest

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_basket()
    product_page.is_not_element_present(*ProductPageLocators.NAME_OF_BOOK_ADDED)

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.is_not_element_present(*ProductPageLocators.NAME_OF_BOOK_ADDED)

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_basket()
    product_page.is_disappeared(*ProductPageLocators.NAME_OF_BOOK_ADDED)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_loging_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    basket_page = BasketPage(browser, link)
    basket_page.open()

    basket_page.open_basket_page()
    basket_page.should_not_be_items_in_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        self.email = f.email()
        self.password = f.password()

        self.link = 'http://selenium1py.pythonanywhere.com/'
        login_page = LoginPage(browser, self.link)
        login_page.open()
        login_page.go_to_loging_page()
        login_page.register_new_user(self.email, self.password)
        login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        product_page = ProductPage(browser, self.link)
        product_page.open()

        product_page.is_not_element_present(*ProductPageLocators.NAME_OF_BOOK_ADDED)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

        product_page = ProductPage(browser, self.link)
        product_page.open()

        product_page.add_product_to_basket()
