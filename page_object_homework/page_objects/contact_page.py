from selenium.webdriver.common.by import By
from page_object_homework.page_objects.base_page import BasePage


class ContactPage(BasePage):
    NAME_FIELD = (By.CSS_SELECTOR, '#input-name')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    ENQUIRY_FIELD = (By.CSS_SELECTOR, '#input-enquiry')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[value="Submit"]')
    HOME_BUTTON = (By.CSS_SELECTOR, '.fa-home')

    locators = [NAME_FIELD, EMAIL_FIELD, ENQUIRY_FIELD, SUBMIT_BUTTON, HOME_BUTTON]

    def asserting_checking_elements(self, locator):
        assert self.is_element_present(*locator), f'Element {locator[0]} not found'
