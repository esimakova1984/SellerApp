import time

import allure
from selenium.common import StaleElementReferenceException, TimeoutException
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class StoreSettingsPage(BasePage):
    PAGE_URL = Links.STORE_SETTINGS_PAGE_STG
    BURGER_MENU = ("xpath", "//button[@class='ant-btn ant-btn-text ant-btn-circle ant-btn-icon-only']")
    SETTINGS_FROM_BURGER_MENU = ("xpath", "//*[@class='anticon anticon-setting ant-menu-item-icon']")
    # EDIT_SETTINGS_BUTTON = ("xpath", "//*[name()='svg' and @data-icon='edit']")
    EDIT_SETTINGS_BUTTON = ("xpath", "//button[@class='ant-btn ant-btn-lg ant-btn-icon-only']")
    NAME_FIELD = ("xpath", "//input[@id='name']")
    PHONE_FIELD = ("xpath", "//input[@id='phone']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    EMAIL_TEXT = ("xpath", "//*[@id='root']/div/div[2]/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr[4]/td/div/span[2]/div")
    DESCRIPTION_FIELD = ("xpath", "//textarea[@id='description']")
    SAVE_CHANGES_BUTTON = ("xpath", "//button[@type='submit']")
    PROFILE_ICON = ("xpath", "//span[@class='ant-avatar ant-avatar-sm ant-avatar-circle ant-avatar-image']")
    TITLE = ("xpath", "//*[@class='ant-col ant-col-24']")
    LOGOUT = ("xpath", "//span[.='Logout']")

    @allure.step("Open store settings page")
    def open_store_settings_page(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_ICON)).click()

    @allure.step("Open store settings from burger menu")
    def open_store_setting_from_burger_menu(self):
        def perform_open_store_settings():
            self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU)).click()
            self.wait.until(EC.element_to_be_clickable(self.SETTINGS_FROM_BURGER_MENU)).click()

        try:
            perform_open_store_settings()
        except (StaleElementReferenceException, TimeoutException):
            perform_open_store_settings()

    @allure.step("Open edit settings form")
    def open_edit_form(self):
        try:
            edit_button = self.wait.until(EC.element_to_be_clickable(self.EDIT_SETTINGS_BUTTON))
            edit_button.click()
        except (StaleElementReferenceException, TimeoutException):
            edit_button = self.wait.until(EC.element_to_be_clickable(self.EDIT_SETTINGS_BUTTON))
            edit_button.click()

    @allure.step("Fill name field")
    def fill_name_field(self):
        try:
            new_name = self.generate_random_word()
            name_field = self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD))
            self.driver.execute_script("arguments[0].scrollIntoView();", name_field)
            name_field.click()
            self.driver.execute_script("arguments[0].value = '';", name_field)
            name_field.send_keys(new_name)
            self.new_name = new_name
            return new_name
        except (StaleElementReferenceException, TimeoutException):
            new_name = self.generate_random_word()
            name_field = self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD))
            self.driver.execute_script("arguments[0].scrollIntoView();", name_field)
            name_field.click()
            self.driver.execute_script("arguments[0].value = '';", name_field)
            name_field.send_keys(new_name)
            self.new_name = new_name
            return new_name

    @allure.step("Fill email field")
    def fill_email_field(self):
        try:
            new_email = self.generate_random_username()
            email_field = self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD))
            self.driver.execute_script("arguments[0].scrollIntoView();", email_field)
            email_field.click()
            self.driver.execute_script("arguments[0].value = '';", email_field)
            email_field.send_keys(new_email)
            self.new_email = new_email
            return new_email
        except (StaleElementReferenceException, TimeoutException):
            new_email = self.generate_random_username()
            email_field = self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD))
            self.driver.execute_script("arguments[0].scrollIntoView();", email_field)
            email_field.click()
            self.driver.execute_script("arguments[0].value = '';", email_field)
            email_field.send_keys(new_email)
            self.new_email = new_email
            return new_email

    @allure.step("Fill phone field")
    def fill_phone_field(self):
        try:
            new_phone = self.generate_unic_number()
            phone_field = self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD))
            phone_field.click()
            self.driver.execute_script("arguments[0].value = '';", phone_field)
            phone_field.send_keys(new_phone)
            self.new_phone = new_phone
            return new_phone
        except (StaleElementReferenceException, TimeoutException):
            new_phone = self.generate_unic_number()
            phone_field = self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD))
            phone_field.click()
            self.driver.execute_script("arguments[0].value = '';", phone_field)
            phone_field.send_keys(new_phone)
            self.new_phone = new_phone
            return new_phone

    @allure.step("Fill description")
    def fill_description(self):
        try:
            new_description = self.generate_random_word_list()
            description_field = self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION_FIELD))
            description_field.click()
            description_field.clear()
            description_field.send_keys(new_description)
            self.new_description = new_description
            time.sleep(3)
        except (StaleElementReferenceException, TimeoutException):
            new_description = self.generate_random_word_list()
            description_field = self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION_FIELD))
            description_field.click()
            description_field.clear()
            description_field.send_keys(new_description)
            self.new_description = new_description
            time.sleep(3)

    @allure.step("Submit edit form")
    def submit_edit_form(self):
        try:
            submit_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_CHANGES_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            submit_button.click()
            time.sleep(3)
        except (StaleElementReferenceException, TimeoutException):
            submit_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_CHANGES_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            submit_button.click()
            time.sleep(3)

    @allure.step("Logout")
    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()

    @allure.step("Get name")
    def get_name(self):
        name_field = self.wait.until(EC.presence_of_element_located(self.NAME_FIELD))
        return name_field.text

    @allure.step("Get phone")
    def get_phone(self):
        phone_field = self.wait.until(EC.presence_of_element_located(self.PHONE_FIELD))
        return phone_field.text

    @allure.step("Get email")
    def get_email(self):
        email = self.wait.until(EC.presence_of_element_located(self.EMAIL_TEXT)).text
        return email

    @allure.step("Get description")
    def get_description(self):
        description_field = self.wait.until(EC.presence_of_element_located(self.DESCRIPTION_FIELD))
        return description_field.text
