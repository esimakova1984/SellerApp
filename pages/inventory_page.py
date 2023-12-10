import time

import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    PAGE_URL = Links.INVENTORY_PAGE
    HEADER_LOCATOR = ("xpath", "//div[@class='header-text']")
    PRODUCT_CARD = ("xpath", "//div[@class='ant-collapse-item'][1]")
    EDIT_BUTTON = ("xpath", "//button[.='Edit']")
    ADD_PRODUCT_BUTTON = ("xpath", "//li[@id='add']//*[name()='svg']")
    PRODUCT_NAME = ("xpath", "//*[@class='name']")
    PRODUCT_QUANTITY = ("xpath", "//*[@class='quantity']")
    DELETE_BUTTON = ("xpath", "//button[.='Delete']")
    CONFIRM_DELETION = ("xpath", "//button[.='Yes']")

    @allure.step("Open product card")
    def open_product_card(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_CARD)).click()

    @allure.step("Open edit card")
    def open_edit_card(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_BUTTON)).click()

    @allure.step("Get product quantity")
    def get_product_quantity(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_QUANTITY)).text

    def get_product_name(self):
        product_list = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAME))
        assert product_list, "Empty list"
        first_product_name = product_list[0].text
        return first_product_name

    @allure.step("Are quantity changes saved")
    def is_quantity_changes_saved(self, quantity):
        current_quantity = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_QUANTITY))
        time.sleep(5)
        expected_quantity = int(quantity)
        actual_quantity = int(current_quantity[0].text)
        assert actual_quantity == expected_quantity, f"Expected product quantity: {expected_quantity}, Actual product " \
                                                     f"quantity: {actual_quantity} "

    @allure.step("Open Add product page")
    def open_add_product_page(self):
        element = self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT_BUTTON))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        offset_y = -element.size['height'] / 2
        actions.move_by_offset(0, offset_y).click().perform()

    @allure.step("Is added product saved")
    def is_added_product_saved(self, name):
        product_name = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAME))
        assert product_name[
                   0].text == name, f"Expected product name: {name}, Actual product name: {product_name[0].text}"

    @allure.step("Find product by name")
    def find_product_by_name(self, name):
        product_list = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAME))
        for product in product_list:
            if product.text == name:
                return product
        return None

    @allure.step("Delete added product")
    def delete_added_product(self, name):
        product = self.find_product_by_name(name)
        if product:
            delete_button = self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON))
            delete_button.click()
            self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETION)).click()
        else:
            raise NoSuchElementException(f"Product with name '{name}' not found")

    @allure.step("Is product deleted")
    def is_product_deleted(self, name):
        try:
            self.wait.until(EC.invisibility_of_element_located(("xpath", f"//*[contains(text(), '{name}')]")))
            return True
        except TimeoutException:
            return False
