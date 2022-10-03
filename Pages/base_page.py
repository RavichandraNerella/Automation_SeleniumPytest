from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from Utils.Logs.logger import logger

"""
    Base Page class to initialize with driver instance and web actions
"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        try:
            self.wait_for_element(element).click()
            logger.info(f'Clicked on element {element}')
        except Exception:
            message = f"Clicking on element {element} failed"
            logger.exception(message)
            raise Exception(message)

    def js_click(self, element):
        web_element = self.wait_for_element(element)
        try:
            self.driver.execute_script("arguments[0].click();", web_element)
            logger.info(f'Clicked on element using javascript {element}')
        except Exception:
            message = f"js clicking on element {element} failed"
            logger.exception(message)
            raise Exception(message)

    def enter_text(self, element, text):
        try:
            self.wait_for_element(element).send_keys(text)
            logger.info(f'Typed {text} in element {element}')
        except Exception:
            message = f"Typing in element {element} failed"
            logger.exception(message)
            raise Exception(message)

    def clear_text(self, element):
        try:
            self.wait_for_element(element).clear()
            logger.info(f'Cleared in element {element}')
        except Exception:
            message = f"Clearing data in element {element} failed"
            logger.exception(message)
            raise Exception(message)

    def select_value(self, element, text):
        try:
            web_element = self.wait_for_element_visible(element)
            select = Select(web_element)
            select.select_by_value(str(text))
            logger.info(f'Selected {text} from element {element}')
        except Exception as ex:
            message = f"{text} is not present in element {element} failed or not selected"
            logger.exception(message)
            raise Exception(message)

    def select_visible_text(self, element, text):
        try:
            web_element = self.wait_for_element_visible(element)
            select = Select(web_element)
            select.select_by_visible_text(text)
            logger.info(f'Selected {text} from element {element}')
        except Exception as ex:
            message = f"{text} is not present in element {element} failed or not selected"
            logger.exception(message)
            raise Exception(message)

    def is_element_displayed(self, element):
        try:
            return bool(
                WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element)))
        except Exception:
            message = f"Element {element} is not displayed"
            logger.exception(message)
            raise Exception(message)

    def wait_for_element(self, element):
        try:
            return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        except Exception:
            message = f"Element {element} was not found"
            logger.exception(message)
            raise Exception(message)

    def wait_for_element_visible(self, element):
        try:
            return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(element))
        except Exception:
            message = f"Element {element} was not found"
            logger.exception(message)
            raise Exception(message)

    def get_page_title(self):
        logger.info(f'Page title is "{self.driver.title}"')
        return self.driver.title

    def get_page_url(self):
        logger.info(f'Page URL is "{self.driver.current_url}"')
        return self.driver.current_url

    def scroll_to(self, element):
        web_element = self.wait_for_element(element)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                       web_element)
            logger.info(f'Scrolled to element using javascript {element}')
        except Exception:
            message = f"js scrolled on element {element} failed"
            logger.exception(message)
            raise Exception(message)
