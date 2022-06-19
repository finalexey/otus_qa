import allure
from selenium.webdriver.common.by import By
from allure_reports_homework.page_objects.base_page import BasePage


class AdminProductsPage(BasePage):
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Delete"]')
    FILTER_PRODUCT_FIELD = (By.CSS_SELECTOR, '[name="filter_name"]')
    FILTER_BUTTON = (By.CSS_SELECTOR, '#button-filter')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

    def selector_with_insert(self, word):
        return By.XPATH, f"//td[contains(text(),{word})]/../td/input"

    @allure.step
    def enter_to_adding_product(self):
        self.click_button(self.ADD_NEW_BUTTON)

    @allure.step
    def filter_search(self, word):
        self.type_in_field(self.FILTER_PRODUCT_FIELD, word)
        self.click_button(self.FILTER_BUTTON)

    @allure.step
    def delete_product(self, word):
        self.click_button(self.selector_with_insert(word))
        self.click_button(self.DELETE_BUTTON)
        self.accept_alert()
        assert 'Success' in self.browser.find_element(*self.SUCCESS_MESSAGE).text, \
            'Check notification text'
