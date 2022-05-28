from page_object_homework.page_objects.admin_login_page import AdminLoginPage
from page_object_homework.page_objects.admin_page import AdminPage
from page_object_homework.page_objects.admin_products_page import AdminProductsPage
from page_object_homework.page_objects.admin_add_product_page import AdminAddProductPage
from page_object_homework.page_objects.objects.topbar import TopBar
from page_object_homework.page_objects.register_page import RegisterPage
from page_object_homework.page_objects.contact_page import ContactPage


def test_asserting_checking_elements(browser, url):
    contact_page = ContactPage(browser)
    browser.get(url + 'index.php?route=information/contact')
    for locator in contact_page.locators:
        contact_page.asserting_checking_elements(locator)


def test_add_new_product(browser, url):
    admin_login_page = AdminLoginPage(browser)
    admin_page = AdminPage(browser)
    admin_products_page = AdminProductsPage(browser)
    admin_add_product_page = AdminAddProductPage(browser)
    browser.get(url + 'admin/')
    admin_login_page.login_user()
    admin_page.enter_to_products()
    admin_products_page.enter_to_adding_product()
    admin_add_product_page.filling_fields()


def test_delete_new_product(browser, url):
    admin_page = AdminPage(browser)
    admin_login_page = AdminLoginPage(browser)
    admin_products_page = AdminProductsPage(browser)
    browser.get(url + 'admin/')
    admin_login_page.login_user()
    admin_page.enter_to_products()
    admin_products_page.filter_search('testproduct2')
    admin_products_page.delete_product('testproduct2')


def test_register_user(browser, url):
    register_page = RegisterPage(browser)
    topbar = TopBar(browser)
    browser.get(url)
    topbar.enter_to_register()
    register_page.filling_fields_register()


def test_change_currency(browser, url):
    topbar = TopBar(browser)
    browser.get(url)
    topbar.change_currency('euro')
