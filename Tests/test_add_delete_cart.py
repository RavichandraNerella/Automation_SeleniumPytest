import allure
import pytest

from Pages.home_page import HomePage
from Tests.test_base import TestBase
from Utils.excel_reader import ExcelReader


class TestAddDeleteCart(TestBase):
    excel_data = ExcelReader()
    login_details = excel_data.get_data("TestData", "Login")
    login = login_details[0]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Login to the application')
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.regression
    def test_add_delete_cart(self, init_driver):
        home_page = HomePage(init_driver)
        login_page = home_page.click_sign_in()
        my_account_page = login_page.login(self.login['User Name'], self.login['Password'])
        my_account_page.go_to_home_page()
        cart_page = home_page.add_to_cart()
        cart_page.is_cart_summary_present()
        assert cart_page.is_product_added(), "Product is not added to the cart"
        cart_page.delete_item()
        assert cart_page.is_product_deleted(), "Product is not deleted successfully"
        home_page.click_sign_out()

