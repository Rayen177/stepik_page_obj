from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_loging_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer '
    page = MainPage(browser, link)
    page.open()

    page.should_be_login_link()

def test_url_location(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()

    page.go_to_loging_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_url()
    login.should_be_login_form()
    login.should_be_register_form()
    login.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    basket = BasketPage(browser, link)
    basket.open()

    basket.open_basket_page()
    basket.should_not_be_items_in_basket()


