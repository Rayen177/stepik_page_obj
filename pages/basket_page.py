from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def open_basket_page(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_PAGE)
        basket.click()

    def should_not_be_items_in_basket(self):
        empty_text = self.browser.find_element(*BasketPageLocators.EMPTY_TEXT)
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_ABSENT), 'Your basket contains items'
        assert 'Ваша корзина пуста' in empty_text.text or 'Your basket is empty.' in empty_text.text, "Your basket is not empty"
