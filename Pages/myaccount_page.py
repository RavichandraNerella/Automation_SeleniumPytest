from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class MyAccountPage(BasePage):

    HOME_BUTTON = (By.XPATH, "//a[@title='Home']")

    def get_my_account_page_title(self):
        return self.get_page_title()

    def go_to_home_page(self):
        self.click(self.HOME_BUTTON)

