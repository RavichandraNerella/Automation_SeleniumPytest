from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.cart_page import CartPage
from Pages.login_page import LoginPage


class HomePage(BasePage):

    SIGN_IN_LINK = (By.XPATH, "//a[contains(text(),'Sign in')]")
    SIGN_OUT_LINK = (By.XPATH, "//*[@class = 'header_user_info']//a[contains(text(),'Sign out')]")
    PRODUCT_IMG = (By.XPATH, "//ul[@id='homefeatured']/li[1]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[@title='Add to cart']")
    PROCEED_BUTTON = (By.XPATH, "//a[@title='Proceed to checkout']")

    def click_sign_in(self):
        self.click(self.SIGN_IN_LINK)
        return LoginPage(self.driver)

    def click_sign_out(self):
        self.scroll_to(self.SIGN_OUT_LINK)
        self.click(self.SIGN_OUT_LINK)
        return LoginPage(self.driver)

    def add_to_cart(self):
        action = ActionChains(self.driver)
        ele = self.driver.find_element(self.PRODUCT_IMG[0], self.PRODUCT_IMG[1])
        self.scroll_to(ele)
        action.move_to_element(ele).click(self.driver.find_element(self.ADD_TO_CART_BUTTON[0], self.ADD_TO_CART_BUTTON[1])).perform()
        self.click(self.PROCEED_BUTTON)
        return CartPage(self.driver)
