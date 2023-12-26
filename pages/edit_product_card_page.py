import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class EditProductPage(BasePage):
    PAGE_URL = Links.EDIT_PRODUCT_PAGE
    BARCODE_FIELD = ("xpath", "//input[@id='edit-product_barcode']")
    PRODUCT_NAME_FIELD = ("xpath", "//input[@id='edit-product_name']")
    AVAILABLE_QUANTITY_FIELD = ("xpath", "//input[@id='edit-product_stock_quantity']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    SET_CATEGORY = ("xpath", "//input[@id='edit-product_treeCategory']")
    SOFT_DRINKS_CATEGORY = ("xpath", "//span[contains(@class,'ant-select-tree-node-content-wrapper "
                                     "ant-select-tree-node-content-wrapper-normal')]")

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

    @allure.step("Select Set category")
    def select_set_category(self, text):
        self.wait.until(EC.element_to_be_clickable(self.SET_CATEGORY)).send_keys(text)
        element = self.wait.until(EC.visibility_of_element_located(self.SOFT_DRINKS_CATEGORY))
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
