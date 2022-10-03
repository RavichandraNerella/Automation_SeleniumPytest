from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.myaccount_page import MyAccountPage
from Pages.registration_page import RegistrationPage


class LoginPage(BasePage):
    LOGIN_EMAIL = (By.ID, "email")
    LOGIN_PASSWORD = (By.XPATH, "//input[@id='passwd']")
    SIGNIN_BUTTON = (By.XPATH, "//button[@id = 'SubmitLogin']")
    CREATE_EMAIL_ID = (By.XPATH, "//input[@id='email_create']")
    CREATE_BUTTON = (By.XPATH, "//button[@id='SubmitCreate']")
    CREATE_ERROR = (By.ID, "create_account_error")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Forgot your password?']")
    LOGIN_ERROR = (By.XPATH, "//h1[text()='Authentication']//following-sibling::div[@class='alert alert-danger']/ol")

    def get_login_page_title(self):
        return self.get_page_title()

    def login(self, username, password):
        self.enter_text(self.LOGIN_EMAIL, username)
        self.enter_text(self.LOGIN_PASSWORD, password)
        self.click(self.SIGNIN_BUTTON)
        return MyAccountPage(self.driver)

    def is_create_an_account_displayed(self):
        return self.is_element_displayed(self.CREATE_BUTTON)

    def create_an_account(self):
        self.click(self.CREATE_BUTTON)
        return RegistrationPage(self.driver)

    def enter_create_email_id(self, text):
        self.enter_text(self.CREATE_EMAIL_ID, text)

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    def is_error_displayed(self):
        return self.is_element_displayed(self.CREATE_ERROR)

    def is_login_error_displayed(self):
        return self.is_element_displayed(self.LOGIN_ERROR)
