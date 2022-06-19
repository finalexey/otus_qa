import logging
import os
import pytest
from selenium import webdriver

DRIVERS = os.path.expanduser("~/Documents/Programs/otus/drivers")

logging.basicConfig(level=logging.INFO, filename='tests/logs/test_log.log')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.0.103:8081/")
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--bversion", action='store', default='96.0')
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption('--browser')
    executor = request.config.getoption('--executor')
    version = request.config.getoption('--bversion')
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info(f':::: Test "{test_name}" started ::::')

    driver = None

    if executor == "localhost":
        if _browser == "chrome":
            driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
        elif _browser == "opera":
            driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
        elif _browser == "firefox":
            driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": _browser,
            "browserVersion": version,
            "screenResolution": "1280x1024",
            "name": "demo cart tests",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            }
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    driver.maximize_window()
    driver.implicitly_wait(5)
    logger.info(f'Browser {_browser} started with {driver.desired_capabilities}')

    def final():
        with open('allure-results/environment.properties', 'w') as f:
            f.write(f'Browser={_browser}\n')
            f.write(f'Browser.Version={version}\n')
            f.write(f'Executor={executor}')
        driver.quit()
        logger.info(f':::: Test "{test_name}" finished ::::')

    request.addfinalizer(final)

    return driver
