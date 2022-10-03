from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_page import BasePage
from Pages.myaccount_page import MyAccountPage


class RegistrationPage(BasePage):

    """    By Locators of the Registration Page    """

    TITLE_RADIO_MR = (By.XPATH, "//input[@id = 'id_gender1']")
    TITLE_RADIO_MRS = (By.XPATH, "//input[@id = 'id_gender2']")
    FIRSTNAME_TEXT = (By.XPATH, "//input[@id = 'customer_firstname']")
    LASTNAME_TEXT = (By.XPATH, "//input[@id = 'customer_lastname']")
    EMAIL_TEXT = (By.XPATH, "//input[@id = 'email']")
    PASSWORD_TEXT = (By.XPATH, "//input[@id = 'passwd']")
    DAYS_DROPDOWN = (By.XPATH, "//select[@id = 'days']")
    MONTHS_DROPDOWN = (By.XPATH, "//select[@id = 'months']")
    YEARS_DROPDOWN = (By.XPATH, "//select[@id = 'years']")
    NEWSLETTER_CHECK = (By.XPATH, "//input[@id = 'newsletter']")
    OFFERS_CHECK = (By.XPATH, "//input[@id = 'optin']")
    ADD_FIRSTNAME_TEXT = (By.XPATH, "//input[@id = 'firstname']")
    ADD_LASTNAME_TEXT = (By.XPATH, "//input[@id = 'lastname']")
    COMPANY_TEXT = (By.XPATH, "//input[@id = 'company']")
    ADDRESS_TEXT = (By.XPATH, "//input[@id = 'address1']")
    ADDRESS_2_TEXT = (By.XPATH, "//input[@id = 'address2']")
    CITY_TEXT = (By.XPATH, "//input[@id = 'city']")
    STATE_DROPDOWN = (By.XPATH, "//select[@id='id_state']")
    ZIPCODE_TEXT = (By.XPATH, "//input[@id = 'postcode']")
    COUNTRY_TEXT = (By.XPATH, "//select[@id = 'id_country']")
    ADDINFO_TEXT = (By.XPATH, "//textarea[@id='other']")
    HOME_PHONE_TEXT = (By.XPATH, "//input[@id='phone']")
    MOBILE_PHONE_TEXT = (By.XPATH, "//input[@id='phone_mobile']")
    ASSIGN_TEXT = (By.XPATH, "//input[@id='alias']")
    REGISTER_BUTTON = (By.XPATH, "//button[@id='submitAccount']")
    CREATE_TITLE = (By.XPATH,"//h1[text()='Create an account']")

    """    Functions within Registration page    """

    def get_registration_page_title(self):
        return self.get_page_title()

    def select_title(self, text):
        self.scroll_to(self.TITLE_RADIO_MR)
        if text.upper() == "MR":
            self.click(self.TITLE_RADIO_MR)
        else:
            self.click(self.TITLE_RADIO_MRS)

    def enter_firstname(self, text):
        self.scroll_to(self.FIRSTNAME_TEXT)
        self.enter_text(self.FIRSTNAME_TEXT, text)

    def enter_lastname(self, text):
        self.scroll_to(self.LASTNAME_TEXT)
        self.enter_text(self.LASTNAME_TEXT, text)

    def enter_email(self, text):
        self.scroll_to(self.EMAIL_TEXT)
        self.clear_text(self.EMAIL_TEXT)
        self.enter_text(self.EMAIL_TEXT, text)

    def enter_password(self, text):
        self.scroll_to(self.PASSWORD_TEXT)
        self.enter_text(self.PASSWORD_TEXT, text)

    def select_date_of_birth(self, text):
        self.select_value(self.DAYS_DROPDOWN, text.day)
        self.select_value(self.MONTHS_DROPDOWN, text.month)
        self.select_value(self.YEARS_DROPDOWN, text.year)

    def select_newsletter(self):
        self.scroll_to(self.NEWSLETTER_CHECK)
        self.click(self.NEWSLETTER_CHECK)

    def select_offers(self):
        self.scroll_to(self.OFFERS_CHECK)
        self.click(self.OFFERS_CHECK)

    def enter_address_firstname(self, text):
        self.enter_text(self.ADD_FIRSTNAME_TEXT, text)

    def enter_address_lastname(self, text):
        self.enter_text(self.ADD_LASTNAME_TEXT, text)

    def enter_company(self, text):
        self.enter_text(self.COMPANY_TEXT, text)

    def enter_address(self, text):
        self.enter_text(self.ADDRESS_TEXT, text)

    def enter_address_line2(self, text):
        self.enter_text(self.ADDRESS_2_TEXT, text)

    def enter_city(self, text):
        self.enter_text(self.CITY_TEXT, text)

    def select_state(self, text):
        self.select_visible_text(self.STATE_DROPDOWN, text)

    def enter_zipcode(self, text):
        self.enter_text(self.ZIPCODE_TEXT, text)

    def select_country(self, text):
        self.select_visible_text(self.COUNTRY_TEXT, text)

    def enter_additional_info(self, text):
        self.enter_text(self.ADDINFO_TEXT, text)

    def enter_home_phone(self, text):
        if text is not None:
            self.enter_text(self.HOME_PHONE_TEXT, text)

    def enter_mobile_phone(self, text):
        self.enter_text(self.MOBILE_PHONE_TEXT, text)

    def enter_assign_address(self, text):
        self.enter_text(self.ASSIGN_TEXT, text)

    def click_register(self):
        self.click(self.REGISTER_BUTTON)
        return MyAccountPage(self.driver)

    def is_create_an_account_displayed(self):
        return self.is_element_displayed(self.CREATE_BUTTON)

    def is_create_account_title_displayed(self):
        try:
            element = self.driver.find_element(self.CREATE_TITLE[0], self.CREATE_TITLE[1])
            return bool(WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(element)))
        except Exception:
            return False

