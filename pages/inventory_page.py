import time

import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    PAGE_URL = Links.INVENTORY_PAGE
    HEADER_LOCATOR = ("xpath", "//div[@class='header-text']")
    PRODUCT_CARD = ("xpath", "//div[@class='ant-collapse-item'][1]")
    EDIT_BUTTON = ("xpath", "//button[.='Edit']")
    ADD_PRODUCT_BUTTON = ("xpath", "//li[@id='add']//*[name()='svg']")

    @allure.step("Open product card")
    def open_product_card(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_CARD)).click()

    @allure.step("Open edit card")
    def open_edit_card(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_BUTTON)).click()

    # @allure.step("Get product quantity")
    # def get_product_quantity(self):
    #     return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_QUANTITY)).text

    @allure.step("Is quantity changes saved")
    def is_quantity_changes_saved(self, quantity):
        get_current_quantity = self.get_product_quantity()
        assert get_current_quantity == quantity
        time.sleep(3)


    @allure.step("Open 'Add product page'")
    def open_add_product_page(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT_BUTTON)).click()


