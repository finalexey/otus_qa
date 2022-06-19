import time
import logging
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)
        self.actual_time = time.time()

    @allure.step
    def generate_current_timestamp(self):
        self.logger.info('Generating current timestamp')
        return str(round(self.actual_time * 1000))

    @allure.step
    def is_element_present(self, how, what, timeout=5):
        self.logger.info(f'Checking element {what} is present')
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            screenshot = f'./tests/logs/element_not_found_{self.generate_current_timestamp()}.png'
            self.browser.save_screenshot(screenshot)
            allure.attach.file(
                source=screenshot,
                attachment_type=allure.attachment_type.PNG
            )
            return False

        return True

    @allure.step
    def type_in_field(self, locator, word):
        self.logger.info(f'Typing word "{word}" in field {locator}')
        field = self.browser.find_element(*locator)
        field.clear()
        field.send_keys(word)

    @allure.step
    def click_button(self, locator):
        self.logger.info(f'Clicking element {locator}')
        button = self.browser.find_element(*locator)
        button.click()

    @allure.step
    def accept_alert(self):
        self.logger.info('Accepting alert')
        WebDriverWait(self.browser, 2).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        alert.accept()
