import allure
import pytest

from Pages.home_page import HomePage
from Tests.test_base import TestBase
from Utils.excel_reader import ExcelReader


class TestLogin(TestBase):
    excel_data = ExcelReader()
    login_details = excel_data.get_data("TestData", "Login")
    login = login_details[0]

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Login to the application')
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.positive
    def test_login(self, init_driver):
        home_page = HomePage(init_driver)
        login_page = home_page.click_sign_in()
        my_account_page = login_page.login(self.login['User Name'], self.login['Password'])
        assert my_account_page.get_my_account_page_title() == "My account - My Store", "Login is not successful"
        home_page.click_sign_out()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Login to the application with no email and password')
    @pytest.mark.negative
    @pytest.mark.regression
    def test_login_with_no_email(self, init_driver):
        home_page = HomePage(init_driver)
        login_page = home_page.click_sign_in()
        login_page.login("", "")
        assert login_page.is_login_error_displayed(), "Login Error is displayed"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Login to the application with email and no password')
    @pytest.mark.negative
    @pytest.mark.regression
    def test_login_with_no_password(self, init_driver):
        home_page = HomePage(init_driver)
        login_page = home_page.click_sign_in()
        login_page.login("test@test.com", "")
        assert login_page.is_login_error_displayed(), "Login Error is displayed"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Login to the application with email and wrong password')
    @pytest.mark.negative
    @pytest.mark.regression
    def test_login_with_wrong_password(self, init_driver):
        home_page = HomePage(init_driver)
        login_page = home_page.click_sign_in()
        login_page.login(self.login['User Name'], "WrongPassword")
        assert login_page.is_login_error_displayed(), "Login Error is displayed"
