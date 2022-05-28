import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.actual_time = time.time()

    def generate_current_timestamp(self):
        return str(round(self.actual_time * 1000))

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def type_in_field(self, locator, word):
        field = self.browser.find_element(*locator)
        field.clear()
        field.send_keys(word)

    def click_button(self, locator):
        button = self.browser.find_element(*locator)
        button.click()

    def accept_alert(self):
        WebDriverWait(self.browser, 2).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        alert.accept()
