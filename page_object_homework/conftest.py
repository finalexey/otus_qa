import os
import pytest

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Documents/Programs/otus/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="http://192.168.0.103:8081/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    elif _browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")

    if maximized:
        driver.maximize_window()

    driver.maximize_window()
    driver.implicitly_wait(5)

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver
