import allure
import pytest

from Pages.home_page import HomePage
from Tests.test_base import TestBase
from Utils.excel_reader import ExcelReader


class TestRegistration(TestBase):
    excel_data = ExcelReader()
    CUSTOMERS = excel_data.get_data("TestData", "Registration")
    login_details = excel_data.get_data("TestData", "Login")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Submitting the new customer registration details')
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_if_registration_is_successful(self, init_driver):
        home_page = HomePage(init_driver)
        for i in range(0, len(self.CUSTOMERS)):
            login_page = home_page.click_sign_in()
            login_page.enter_create_email_id(self.CUSTOMERS[i]['Email'])
            registration_page = login_page.create_an_account()
            if registration_page.is_create_account_title_displayed():
                registration_page.select_title(self.CUSTOMERS[i]['Title'])
                registration_page.enter_firstname(self.CUSTOMERS[i]['First Name'])
                registration_page.enter_lastname(self.CUSTOMERS[i]['Last Name'])
                registration_page.enter_email(self.CUSTOMERS[i]['Email'])
                registration_page.enter_password(self.CUSTOMERS[i]['Password'])
                registration_page.select_date_of_birth(self.CUSTOMERS[i]['Date of Birth'])
                registration_page.enter_address_firstname(self.CUSTOMERS[i]['First Name'])
                registration_page.enter_address_lastname(self.CUSTOMERS[i]['Last Name'])
                registration_page.enter_company(self.CUSTOMERS[i]['Company'])
                registration_page.enter_address(self.CUSTOMERS[i]['Address'])
                registration_page.enter_address_line2(self.CUSTOMERS[i]['Address Line2'])
                registration_page.enter_city(self.CUSTOMERS[i]['City'])
                registration_page.select_state(self.CUSTOMERS[i]['State'])
                registration_page.enter_zipcode(self.CUSTOMERS[i]['ZipCode'])
                registration_page.select_country(self.CUSTOMERS[i]['Country'])
                registration_page.enter_additional_info(self.CUSTOMERS[i]['Additional Information'])
                registration_page.enter_home_phone(self.CUSTOMERS[i]['Home Phone'])
                registration_page.enter_mobile_phone(self.CUSTOMERS[i]['Mobile Phone'])
                registration_page.enter_assign_address(self.CUSTOMERS[i]['Assign address'])
                my_account_page = registration_page.click_register()
                assert my_account_page.get_my_account_page_title() == "My account - My Store", "Customer registration is not successful "
                home_page.click_sign_out()
            else:
                assert False, "{} is already exist or enter valid email".format(self.CUSTOMERS[i]['Email'])

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Creating new account with registered email')
    @pytest.mark.negative
    @pytest.mark.regression
    def test_if_error_registering_with_existing_email(self, init_driver):
        home_page = HomePage(init_driver)
        login_page = home_page.click_sign_in()
        login_page.enter_create_email_id(self.login_details[0]['User Name'])
        login_page.create_an_account()
        assert login_page.is_error_displayed(), "Error Message is not displayed"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Creating new account with no email')
    @pytest.mark.negative
    @pytest.mark.regression
    def test_if_error_registering_with_no_email(self, init_driver):
        home_page = HomePage(init_driver)
        login_page = home_page.click_sign_in()
        login_page.create_an_account()
        assert login_page.is_error_displayed(), "Error Message is not displayed"
