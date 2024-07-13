import time
import allure
from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import Keys

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class EditProductPage(BasePage):
    PAGE_URL = Links.EDIT_PRODUCT_PAGE_STG
    BARCODE_FIELD = ("xpath", "//input[@id='edit-product_barcode']")
    PRODUCT_NAME_FIELD = ("xpath", "//input[@id='edit-product_name']")
    DESCRIPTION_FIELD = ("xpath", "//textarea[@id='edit-product_description']")
    AVAILABLE_QUANTITY_FIELD = ("xpath", "//input[@id='stock_quantity']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    SET_CATEGORY = ("xpath", "//input[@id='edit-product_category']")
    GENERAL_CATEGORY = ("xpath", "//span[@title='כללי']")
    EDIT_SALE_PRICE = ("xpath", "//input[@id='edit-product_sale_price']")
    BADGE_FIELD = ("xpath", "//input[@id='badge']")

    @allure.step("Change product name")
    def change_product_name(self):
        time.sleep(5)
        new_name = self.generate_random_word()
        product_name_field = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_NAME_FIELD))
        product_name_field.click()
        self.driver.execute_script("arguments[0].value = '';", product_name_field)
        product_name_field.send_keys(new_name)
        self.name = new_name
        return new_name

    def change_description(self):
        new_description = self.generate_random_word_list()
        description_field = self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION_FIELD))
        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", description_field)
        try:
            # Click the description field
            description_field.click()
        except ElementClickInterceptedException:
            # Use JavaScript to focus on the field if click is intercepted
            self.driver.execute_script("arguments[0].focus();", description_field)
        # Clear the field using JavaScript
        self.driver.execute_script("arguments[0].value = '';", description_field)
        # Send keys to the description field
        description_field.send_keys(new_description)
        self.description = new_description
        return new_description

    @allure.step("Select Set category")
    def select_set_category(self, text):
        self.wait.until(EC.element_to_be_clickable(self.SET_CATEGORY)).send_keys(text)
        element = self.wait.until(EC.visibility_of_element_located(self.GENERAL_CATEGORY))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Change product quantity")
    def change_product_quantity(self):
        quantity = self.generate_random_index()
        quantity_field = self.wait.until(EC.element_to_be_clickable(self.AVAILABLE_QUANTITY_FIELD))
        self.driver.execute_script("arguments[0].scrollIntoView();", quantity_field)
        quantity_field.click()
        self.driver.execute_script("arguments[0].value = '';", quantity_field)
        quantity_field.send_keys(quantity)
        self.quantity = quantity
        return quantity

    @allure.step("Save changes")
    def save_changes(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView();", save_button)
        save_button.click()


