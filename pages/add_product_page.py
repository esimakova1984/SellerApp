import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AddProductPage(BasePage):
    PAGE_URL = Links.ADD_PRODUCT_PAGE
    ADD_PRODUCT_BUTTON = ("xpath", "//*[local-name()='svg' and @data-icon='plus']")
    CHECKBOX_NO_BARCODE = ("xpath", "//*[@id='add-product_no-barcode']")
    NAME_FIELD = ("xpath", "//input[@id='add-product_name']")
    DESCRIPTION_FIELD = ("xpath", "//textarea[@id='add-product_description']")
    SET_CATEGORY = ("xpath", "//input[@id='add-product_treeCategory']")

    @allure.step("Select 'no barcode' checkbox")
    def select_checkbox_no_barckode(self):
        checkbox = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_NO_BARCODE))
        self.driver.execute_script("arguments[0].click();", checkbox)
