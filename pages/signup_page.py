import allure
from base.base_page import BasePage
from config.data import Data
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage(BasePage):
    PAGE_URL = Links.SIGNUP_PAGE_TNG
    EMAIL_FIELD = ("xpath", "//input[@id='basic_email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='basic_password']")
    CONFIRM_PASSWORD_FIELD = ("xpath", "//input[@id='basic_confirmPassword']")
    SUBMIT_BUTTON = ("xpath", "//button[.='Submit']")

    @allure.step("Fill signup form")
    def fillSignupForm(self):
        login = self.generate_random_username()
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(login)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(Data.PASSWORD)
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_FIELD)).send_keys(Data.PASSWORD)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        return login











