from selenium.webdriver.common.by import By
from page_object_homework.page_objects.base_page import BasePage


class BottomBar(BasePage):
    ABOUT_US_BUTTON = (By.CSS_SELECTOR, '[href$="information_id=4"]')
    DELIVERY_BUTTON = (By.CSS_SELECTOR, '[href$="information_id=6"]')
    PRIVACY_BUTTON = (By.CSS_SELECTOR, '[href$="information_id=3"]')
    TERMS_BUTTON = (By.CSS_SELECTOR, '[href$="information_id=5"]')
    CONTACT_BOTTOM_BUTTON = (By.CSS_SELECTOR, '.list-unstyled [href$="contact"]')
    RETURNS_BUTTON = (By.CSS_SELECTOR, '[href$="add"]')
    SITEMAP_BUTTON = (By.CSS_SELECTOR, '[href$="sitemap"]')
    BRANDS_BUTTON = (By.CSS_SELECTOR, '[href$="manufacturer"]')
    GIFT_BUTTON = (By.CSS_SELECTOR, '[href$="voucher"]')
    AFFILIATE_BUTTON = (By.CSS_SELECTOR, '[href$="affiliate/login"]')
    SPECIALS_BUTTON = (By.CSS_SELECTOR, '[href$="special"]')
    ACCOUNT_BOTTOM_BUTTON = (By.CSS_SELECTOR, '[href$="account"]')
    ORDERS_BUTTON = (By.CSS_SELECTOR, '[href$="order"]')
    WISHLIST_BOTTOM_BUTTON = (By.CSS_SELECTOR, '.list-unstyled [href$="wishlist"]')
    NEWSLETTER_BUTTON = (By.CSS_SELECTOR, '[href$="newsletter"]')
