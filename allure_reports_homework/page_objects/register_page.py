import allure
from selenium.webdriver.common.by import By
from allure_reports_homework.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME_FIELD = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_FIELD = (By. CSS_SELECTOR, '#input-email')
    PHONE_FIELD = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, '#input-confirm')
    AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, '[name="agree"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[value="Continue"]')
    CREATION_TEXT = (By.CSS_SELECTOR, '#content > h1')

    @allure.step
    def filling_fields_register(self):
        current_ts = self.generate_current_timestamp()
        self.type_in_field(self.FIRSTNAME_FIELD, 'user' + current_ts)
        self.type_in_field(self.LASTNAME_FIELD, 'test' + current_ts)
        self.type_in_field(self.EMAIL_FIELD, current_ts + '@aaa.com')
        self.type_in_field(self.PHONE_FIELD, '1232323')
        self.type_in_field(self.PASSWORD_FIELD, 'qwerty1-')
        self.type_in_field(self.PASSWORD_CONFIRM_FIELD, 'qwerty1-')
        self.click_button(self.AGREEMENT_CHECKBOX)
        self.click_button(self.CONTINUE_BUTTON)
        assert 'Your Account Has Been Created!' in self.browser.find_element(By.CSS_SELECTOR, '#content').text, \
            'Check user creation notification'
