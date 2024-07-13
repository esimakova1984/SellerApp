import re
import time
import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    PAGE_URL = Links.INVENTORY_PAGE_STG
    HEADER_LOCATOR = ("xpath", "//div[@class='header-text']")
    PRODUCT_CARD = ("xpath", "//div[@class='ant-collapse-item'][1]")
    EDIT_BUTTON = ("xpath", "//button[.='Edit']")
    ADD_PRODUCT_BUTTON = ("xpath", "//li[@id='add']//*[name()='svg']")
    PRODUCT_NAME_ITEM = ("xpath", "//div[@class='name']")
    PRODUCT_NAME = ("xpath",
                    "/html[1]/body[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]")
    PRODUCT_QUANTITY = ("xpath", "//div[substring-after(text(),'Quantity: ')]")
    DELETE_BUTTON = ("xpath", "//span[.='Delete']")
    CONFIRM_DELETION = ("xpath", "//button[.='Yes']")
    DENY_WEBPUSHER_NOTIFICATION = ("xpath", "//webpushrpromptbtndeny2[@id='webpushr-deny-button']")
    WEB_VIEW = ("xpatn", "/html[1]/body[1]/div[3]/div[1]/div[1]")

    @allure.step("Check if any product is present")
    def is_product_present(self):
        try:
            # Adjust the locator to match the product card elements on the inventory page
            self.wait.until(EC.visibility_of_element_located(self.PRODUCT_CARD))
            return True
        except Exception:
            return False

    @allure.step("Get the name of the first product")
    def get_first_product_name(self):
        product_name_element = self.wait.until(EC.presence_of_element_located(self.PRODUCT_NAME))
        return product_name_element.text

    @allure.step("Open product card")
    def open_product_card(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_CARD)).click()

    @allure.step("Open edit card")
    def open_edit_card(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_BUTTON)).click()

    @allure.step("Get product quantity")
    def get_product_quantity(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_QUANTITY)).text

    @allure.step("Get product name")
    def get_product_name(self):
        product_list = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAME))
        assert product_list, "Empty list"
        first_product_name = product_list[0].text
        return first_product_name

    @allure.step("Is quantity change saved")
    def is_quantity_changes_saved(self, quantity):
        current_quantity = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_QUANTITY))
        quantity_str = str(quantity)
        self.wait.until(EC.text_to_be_present_in_element(self.PRODUCT_QUANTITY, quantity_str),
                        f"Expected product quantity: {quantity_str}, Actual product quantity: {current_quantity[0].text}")
        actual_quantity_text = current_quantity[0].text
        actual_quantity_digits = re.sub(r'\D', '', actual_quantity_text)
        actual_quantity = int(actual_quantity_digits)
        expected_quantity = int(quantity)
        assert actual_quantity == expected_quantity, f"Expected product quantity: {expected_quantity}, Actual product " \
                                                     f"quantity: {actual_quantity} "

    # @allure.step("Is name change save")
    # def is_name_changes_saved(self, name):
    #     current_name = self.wait.until(EC.presence_of_element_located(self.PRODUCT_NAME))
    #
    #     expected_name = name
    #     actual_name = current_name.text
    #     assert actual_name == expected_name, f"Expected product name: {expected_name}, Actual product " \
    #                                          f"name: {actual_name} "

    @allure.step("Is name change saved")
    def is_name_changes_saved(self, name):
        # Locate all elements matching the locator
        product_name_elements = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAME_ITEM))
        # Access the first element in the list
        first_product_name_element = product_name_elements[0]
        # Wait until the text in the first element matches the expected name
        self.wait.until(EC.text_to_be_present_in_element(self.PRODUCT_NAME_ITEM, name),
                        f"Expected product name: {name}, but it was not found in the element.")
        # Get the text of the first element
        actual_name = first_product_name_element.text.strip()
        # Compare the actual name with the expected name
        assert actual_name == name, f"Expected product name: {name}, but found: {actual_name}"

    @allure.step("Open Add product page")
    def open_add_product_page(self):
        element = self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT_BUTTON))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        offset_y = -element.size['height'] / 2
        actions.move_by_offset(0, offset_y).click().perform()

    @allure.step("Is added product saved")
    def is_added_product_saved(self, name):
        product_name = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAME_ITEM))
        assert product_name[
                   0].text == name, f"Expected product name: {name}, Actual product name: {product_name[0].text}"

    @allure.step("Find product by name")
    def find_product_by_name(self, name):
        product_list = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAME))
        for product in product_list:
            if product.text == name:
                return product
        return None

    # @allure.step("Delete added product")
    # def delete_added_product(self):
    #     self.wait.until(EC.element_to_be_clickable(self.PRODUCT_CARD)).click()
    #     delete_button = self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON))
    #     delete_button.click()
    #     self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETION)).click()

    @allure.step("Delete added product by name")
    def delete_added_product_by_name(self, product_name):
        product_element = self.wait.until(
            EC.element_to_be_clickable(("xpath", f"//*[contains(text(), '{product_name}')]")))

        product_element.click()
        delete_button = self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON))
        delete_button.click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETION)).click()

    @allure.step("Is product deleted")
    def is_product_deleted(self, name):
        try:
            self.wait.until(EC.invisibility_of_element_located(("xpath", f"//*[contains(text(), '{name}')]")))
            return True
        except TimeoutException:
            return False

    @allure.step("Deny web pusher notification if present")
    def deny_webpusher_notification_if_present(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.DENY_WEBPUSHER_NOTIFICATION)).click()
        except Exception:
            pass  # If the web pusher notification is not present, do nothing

    def open_web_view(self):
        self.wait.until(EC.element_to_be_clickable(self.WEB_VIEW)).click()

    @allure.step("Scroll to the top of the page")
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
