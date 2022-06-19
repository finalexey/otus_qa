import allure
from selenium.webdriver.common.by import By
from allure_reports_homework.page_objects.base_page import BasePage


class AdminLoginPage(BasePage):
    USERNAME = 'user'
    PASSWORD = 'bitnami'
    USERNAME_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.help-block a')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn-primary')
    TITLE_BUTTON = (By.CSS_SELECTOR, '[title="OpenCart"]')

    @allure.step
    def login_user(self):
        self.type_in_field(self.USERNAME_FIELD, self.USERNAME)
        self.type_in_field(self.PASSWORD_FIELD, self.PASSWORD)
        self.click_button(self.LOGIN_BUTTON)
