from selenium.webdriver.common.by import By
from page_object_homework.page_objects.base_page import BasePage


class AdminAddProductPage(BasePage):
    GENERAL_TAB = (By.CSS_SELECTOR, '[href$="#tab-general"]')
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name1')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, '.note-editable')
    META_TAG_TITLE_FIELD = (By.CSS_SELECTOR, '#input-meta-title1')
    META_TAGE_DESCRIPTION_FIELD = (By.CSS_SELECTOR, '#input-meta-description1')
    META_TAG_KEYWORDS_FIELD = (By.CSS_SELECTOR, '#input-meta-keyword1')
    PRODUCT_TAGS_FIELD = (By.CSS_SELECTOR, '#input-tag1')
    DATA_TAB = (By.CSS_SELECTOR, '[href$="#tab-data"]')
    MODEL_FIELD = (By.CSS_SELECTOR, '#input-model')
    LOCATION_FIELD = (By.CSS_SELECTOR, '#input-location')
    PRICE_FIELD = (By.CSS_SELECTOR, '#input-price')
    QUANTITY_FIELD = (By.CSS_SELECTOR, '#input-quantity')
    STATUS_DROPDOWN_LIST = (By.CSS_SELECTOR, '#input-status')
    IMAGE_TAB = (By.CSS_SELECTOR, '[href$="#tab-image"]')
    IMAGE_FIELD = (By.CSS_SELECTOR, '#thumb-image')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.fa-save')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '.fa-reply')

    def filling_fields(self):
        self.type_in_field(self.PRODUCT_NAME_FIELD, 'testproduct2')
        self.type_in_field(self.META_TAG_TITLE_FIELD, 'testtag2')
        self.click_button(self.DATA_TAB)
        self.type_in_field(self.MODEL_FIELD, 'testmodel2')
        self.type_in_field(self.PRICE_FIELD, '120')
        self.type_in_field(self.QUANTITY_FIELD, '4')
        self.click_button(self.SAVE_BUTTON)
        notification_text = self.browser.find_element(By.CSS_SELECTOR, '.alert-success').text
        assert 'Success' in notification_text, 'Check notification text'
