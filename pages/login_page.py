import allure
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = (By.XPATH, "//input[@id='sign-in_username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='sign-in_password']")
    CHECKBOX_TERMS_OF_USE = (By.XPATH, "(//span[contains(text(),'I accept the')])[1]")
    SUBMIT_LOGIN = (By.XPATH, "//button[@type='submit']")

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






