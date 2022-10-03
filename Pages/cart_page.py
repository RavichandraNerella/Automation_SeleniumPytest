import time
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class CartPage(BasePage):
    DELETE_BUTTON = (By.XPATH, "//a[@title='Delete']")
    PRODUCT_LIST = (By.XPATH, "//table[@id='cart_summary']/tbody/tr")
    SUMMARY_TITLE = (By.XPATH, "//h1[@id='cart_title']")

    def get_cart_page_title(self):
        return self.get_page_title()

    def delete_item(self):
        self.click(self.DELETE_BUTTON)

    def is_cart_summary_present(self):
        self.wait_for_element_visible(self.SUMMARY_TITLE)

    def is_product_added(self):
        elements = self.driver.find_elements(self.PRODUCT_LIST[0], self.PRODUCT_LIST[1])
        if len(elements) > 0:
            return True
        else:
            return False

    def is_product_deleted(self):
        time.sleep(4)
        elements = self.driver.find_elements(self.PRODUCT_LIST[0], self.PRODUCT_LIST[1])
        if len(elements) > 0:
            return False
        else:
            return True
