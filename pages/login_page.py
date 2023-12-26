import allure
from base.base_page import BasePage
from config.data import Data
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE
    USERNAME_FIELD = ("xpath", "//*[@id='sign-in_username']")
    PASSWORD_FIELD = ("xpath", "//*[@id='sign-in_password']")
    CHECKBOX_TERMS_OF_USE = ("xpath", "(//span[contains(text(),'I accept the')])[1]")
    SUBMIT_LOGIN = ("xpath", "//button[@type='submit']")
    ERROR_MESSAGE = ("xpath", "(//*[@class='ant-alert-content'])[1]")

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

    @allure.step("Is error message appeared")
    def is_error_message_appeared(self):
        assert self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)), "Invalid username or password."

    @allure.step("Login with generated username")
    def login_with_generated_username(self, username):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(Data.PASSWORD)
        checkbox = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_TERMS_OF_USE))
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_LOGIN)).click()

    @allure.step("Quick login")
    def quick_login(self):
        self.wait.until(EC.url_to_be(Links.LOGIN_PAGE))
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(Data.LOGIN)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(Data.PASSWORD)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_LOGIN)).click()






