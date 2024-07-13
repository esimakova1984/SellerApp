import time

import allure
import logging
logging.basicConfig(filename='/Users/ekaterinasimakova/QA_automation/SellerApp/logs/test.log', level=logging.INFO)
from base.base_page import BasePage
from config.data import Data
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE_STG
    USERNAME_FIELD = ("xpath", "//*[@id='sign-in_username']")
    PASSWORD_FIELD = ("xpath", "//*[@id='sign-in_password']")
    CHECKBOX_TERMS_OF_USE = ("xpath", "(//span[contains(text(),'I accept the')])[1]")
    SUBMIT_LOGIN = ("xpath", "//button[@type='submit']")
    INVALID_DATA = ("xpath", "//div[text()='Invalid username or password.']")
    INVALID_USERNAME = ("xpath", "//div[text()='username is required']")
    INVALID_PASSWORD = ("xpath", "//div[text()='Password is required']")
    ERROR_MESSAGE_CHECKBOX_NOT_CHECKED = ("xpath", "//div[text()='Should accept agreement']")
    DENY_WEBPUSHER_NOTIFICATION = ("xpath", "//webpushrpromptbtndeny2[@id='webpushr-deny-button']")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Select checkbox")
    def select_checkbox(self):
        checkbox = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_TERMS_OF_USE))
        self.driver.execute_script("arguments[0].click();", checkbox)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_LOGIN)).click()
        time.sleep(5)

    @allure.step("Is error message appeared")
    def is_error_message_appeared(self):
        assert self.wait.until(EC.visibility_of_element_located(self.INVALID_DATA)), "Invalid username or password."

    @allure.step("Login with generated username")
    def login_with_generated_username(self, username):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(Data.PASSWORD)
        checkbox = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_TERMS_OF_USE))
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_LOGIN)).click()

    @allure.step("Quick login")
    def quick_login(self):
        self.wait.until(EC.url_to_be(Links.LOGIN_PAGE_TNG))
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(Data.LOGIN)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(Data.PASSWORD)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_LOGIN)).click()

    @allure.step("get unsuccessful login result")
    def get_unsuccseful_login_result(self, empty_field=None, invalid_input=None, checkbox_not_checked=False):
        error_message = None

        if empty_field:
            if empty_field == "username":
                error_message = self.wait.until(EC.presence_of_element_located(self.INVALID_USERNAME))
            elif empty_field == "password":
                error_message = self.wait.until(EC.presence_of_element_located(self.INVALID_PASSWORD))
        elif invalid_input:
            if invalid_input == "invalid_user" or invalid_input == "invalid_password":
                error_message = self.wait.until(EC.presence_of_element_located(self.INVALID_DATA))
        elif checkbox_not_checked:
            error_message = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE_CHECKBOX_NOT_CHECKED))

        if error_message is not None:
            print(f"Error Message Text: {error_message.text}")
        else:
            print("Error Message is None")

        return error_message.text

    @allure.step("Deny web pusher notification if present")
    def deny_webpusher_notification_if_present(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.DENY_WEBPUSHER_NOTIFICATION)).click()
        except Exception:
            pass  # If the web pusher notification is not present, do nothing











