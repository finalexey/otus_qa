from selenium.webdriver.common.by import By
from page_object_homework.page_objects.base_page import BasePage


class TopBar(BasePage):
    INTERACTIVE_CART_BUTTON = (By.CSS_SELECTOR, '#cart-total')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[name="search"]')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, '#form-currency')
    EURO_BUTTON = (By.CSS_SELECTOR, '[name="EUR"]')
    POUND_BUTTON = (By.CSS_SELECTOR, '[name="GBP"]')
    DOLLAR_BUTTON = (By.CSS_SELECTOR, '[name="USD"]')
    CURRENCY_SYMBOL = (By.CSS_SELECTOR, '[data-toggle="dropdown"] > strong')
    CONTACT_TOP_BUTTON = (By.CSS_SELECTOR, '.fa-phone')
    ACCOUNT_TOP_BUTTON = (By.CSS_SELECTOR, '[title="My Account"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[href$="/register"]')
    WISHLIST_TOP_BUTTON = (By.CSS_SELECTOR, '#wishlist-total')
    CART_BUTTON = (By.CSS_SELECTOR, '[title="Shopping Cart"]')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[title="Checkout"]')
    LOGO_BUTTON = (By.CSS_SELECTOR, '#logo')

    DESKTOPS_BUTTON = (By.CSS_SELECTOR, '[href$="path=20"].dropdown-toggle')
    LAPTOPS_BUTTON = (By.CSS_SELECTOR, '[href$="path=18"].dropdown-toggle')
    COMPONENTS_BUTTON = (By.CSS_SELECTOR, '[href$="path=25"].dropdown-toggle')
    TABLETS_BUTTON = (By.CSS_SELECTOR, '[href$="path=57"].dropdown-toggle')
    SOFTWARE_BUTTON = (By.CSS_SELECTOR, '[href$="path=17"].dropdown-toggle')
    PHONES_BUTTON = (By.CSS_SELECTOR, '[href$="path=24"].dropdown-toggle')
    CAMERAS_BUTTON = (By.CSS_SELECTOR, '[href$="path=33"].dropdown-toggle')
    PLAYERS_BUTTON = (By.CSS_SELECTOR, '[href$="path=34"].dropdown-toggle')

    def change_currency(self, currency):
        self.click_button(self.CURRENCY_BUTTON)
        if currency == 'dollar':
            self.click_button(self.DOLLAR_BUTTON)
            currency_symbol = self.browser.find_element(*self.CURRENCY_SYMBOL)
            assert currency_symbol.text == '$', 'Check currency symbol'
        elif currency == 'euro':
            self.click_button(self.EURO_BUTTON)
            currency_symbol = self.browser.find_element(*self.CURRENCY_SYMBOL)
            assert currency_symbol.text == '€', 'Check currency symbol'
        elif currency == 'pound':
            self.click_button(self.POUND_BUTTON)
            currency_symbol = self.browser.find_element(*self.CURRENCY_SYMBOL)
            assert currency_symbol.text == '£', 'Check currency symbol'

    def enter_to_register(self):
        self.click_button(self.ACCOUNT_TOP_BUTTON)
        self.click_button(self.REGISTER_BUTTON)
