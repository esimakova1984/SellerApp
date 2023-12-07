import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class EditProductPage(BasePage):
    PAGE_URL = Links.EDIT_PRODUCT_PAGE
    PRODUCT_NAME_FIELD = ("xpath", "//input[@id='edit-product_name']")
    AVAILABLE_QUANTITY_FIELD = ("xpath", "//input[@placeholder='Available quantity']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Change product name")
    def change_product_name(self, new_name):
        product_name_field = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_NAME_FIELD))
        product_name_field.clear()
        assert product_name_field.get_attribute("value") == "", "There is a text"
        product_name_field.send_keys(new_name)
        self.wait.until(EC.text_to_be_present_in_element_value(self.PRODUCT_NAME_FIELD, new_name))
        self.name = new_name

    @allure.step("Change product quantity")
    def change_product_quantity(self, quantity):
        quantity_field = self.wait.until(EC.element_to_be_clickable(self.AVAILABLE_QUANTITY_FIELD))
        quantity_field.clear()
        assert quantity_field.get_attribute("value") == "", "There is a text"
        quantity_field.send_keys(quantity)
        self.quantity = quantity
        time.sleep(5)

    @allure.step("Save changes")
    def save_changes(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView();", save_button)
        save_button.click()
        time.sleep(3)
