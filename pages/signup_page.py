import allure
from base.base_page import BasePage
from config.data import Data
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage(BasePage):
    PAGE_URL = Links.SIGNUP_PAGE_STG
    EMAIL_FIELD = ("xpath", "//input[@id='basic_email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='basic_password']")
    CONFIRM_PASSWORD_FIELD = ("xpath", "//input[@id='basic_confirmPassword']")
    SUBMIT_BUTTON = ("xpath", "//button[.='Submit']")
    EMPTY_EMAIL_ERROR_MESSAGE = ("xpath", "//div[text()='Email is required']")
    EMPTY_PASSWORD_ERROR_MESSAGE = ("xpath", "//div[text()='Password is required']")
    EMPTY_CONFIRM_PASSWORD_ERROR_MESSAGE = ("xpath", "//div[text()='confirm password is required']")
    INVALID_EMAIL = ("xpath", "//div[text()='Email is not valid']")
    INVALID_PASSWORD = ("xpath", "//div[contains(text(),'Password must be between')]")
    MISMATCHED_PASSWORD = ("xpath", "//div[contains(text(),'Password doesn')]")


    @allure.step("Fill signup form")
    def fillSignupForm(self):
        login = self.generate_random_username()
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(login)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(Data.PASSWORD)
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_FIELD)).send_keys(Data.PASSWORD)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        return login

    @allure.step("Enter email")
    def enter_email(self, login):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Confirm password")
    def enter_confirm_password(self, confirm_password):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_FIELD)).send_keys(confirm_password)

    @allure.step("Submit signup form")
    def submit_form(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Error message")
    def get_unsuccseful_signup_result(self, empty_field=None, invalid_input=None):
        error_message = None

        if empty_field:
            if empty_field == "email":
                error_message = self.wait.until(EC.presence_of_element_located(self.EMPTY_EMAIL_ERROR_MESSAGE))
            elif empty_field == "password":
                error_message = self.wait.until(EC.presence_of_element_located(self.EMPTY_PASSWORD_ERROR_MESSAGE))
            elif empty_field == "confirm_password":
                error_message = self.wait.until(EC.presence_of_element_located(self.EMPTY_CONFIRM_PASSWORD_ERROR_MESSAGE))
        elif invalid_input:
            if invalid_input == "invalid_email":
                error_message = self.wait.until(EC.presence_of_element_located(self.INVALID_EMAIL))
            elif invalid_input == "invalid_password":
                error_message = self.wait.until(EC.presence_of_element_located(self.INVALID_PASSWORD))
            elif invalid_input == "invalid_confirm_password":
                error_message= self.wait.until(EC.presence_of_element_located(self.MISMATCHED_PASSWORD))

        if error_message is not None:
            print(f"Error Message Text: {error_message.text}")
        else:
            print("Error Message is None")

        return error_message.text





















