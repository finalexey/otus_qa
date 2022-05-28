from selenium.webdriver.common.by import By
from page_object_homework.page_objects.base_page import BasePage


class AdminPage(BasePage):
    MENU_CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    MENU_CATALOG_PRODUCTS = (By.CSS_SELECTOR, '[href*="product"]')

    def enter_to_products(self):
        self.click_button(self.MENU_CATALOG)
        self.click_button(self.MENU_CATALOG_PRODUCTS)
