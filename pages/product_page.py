from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        product_link.click()
        self.solve_quiz_and_get_code()
        book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_ADDED)
        added = self.browser.find_element(*ProductPageLocators.SUCCESS_ADDED_TEXT)
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)

        assert price_of_book.text == price_in_basket.text
        assert book.text == book_name
        assert 'added to your basket' in added.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_TEXT), "Success message is presented, but should not be"