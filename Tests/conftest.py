import pytest
import json
from Config.Browsers.browser_factory import BrowserFactory
from Config.Browsers.supported_browsers import SupportedBrowsers
from Tests.test_base import TestBase
from Utils.Logs.logger import logger

CONFIG_PATH = 'Config/config.json'

"""
       This method created driver instance and quits after every test
"""


@pytest.fixture()
def init_driver(read_config_file, config_browser, request):
    browser = BrowserFactory.get_browser(config_browser)
    driver = browser.init_browser()
    logger.info("Driver was initialized")
    driver.implicitly_wait(10)
    driver.maximize_window()
    logger.info("Browser's window was maximized")
    driver.get(TestBase.get_data('baseUrl'))
    logger.info(f"Navigated to {TestBase.get_data('baseUrl')}")

    yield driver

    if driver:
        driver.quit()
        logger.info("Driver was closed")


"""
        This method is used for loading json data
        :return: it returns json data
"""


@pytest.fixture(scope='class', autouse=True)
def read_config_file():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    logger.info("Read configuration file")
    return data


"""
        This method is used for getting the type of browser from config.json file
        :return: it returns the respective browser driver instance
"""


@pytest.fixture(scope='class')
def config_browser(read_config_file):
    # Validate and return the browser choice from the config data
    if 'browser' not in read_config_file:
        error = 'The config file does not contain "browser"'
        logger.error(error)
        raise Exception(error)
    elif read_config_file['browser'] not in SupportedBrowsers.__members__:
        error = f'"{read_config_file["browser"]}" is not a supported browser'
        logger.error(error)
        raise Exception(error)
    logger.info(f"{read_config_file['browser']} browser configured")
    return read_config_file['browser']
