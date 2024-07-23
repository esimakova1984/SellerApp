import time

import allure
import pyautogui
import pyperclip
from selenium.common import NoAlertPresentException, ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AddProductPage(BasePage):
    PAGE_URL = Links.ADD_PRODUCT_PAGE_STG
    ADD_PRODUCT_BUTTON = ("xpath", "//li[@id='add']")
    CONTAINER = ("xpath", "//div[@class='ant-card ant-card-bordered']")
    CHECKBOX_NO_BARCODE = ("xpath", "//input[@id='add-product_no-barcode']")
    ADD_BARCODE_FIELD = ("xpath", "//input[@id='add-product_barcode']")
    NAME_FIELD = ("xpath", "//input[@id='add-product_name']")
    DESCRIPTION_FIELD = ("xpath", "//textarea[@id='add-product_description']")
    SET_CATEGORY = ("xpath", "//input[@id='add-product_category']")
    SOFT_DRINKS_CATEGORY = ("xpath", "//span[@title='שתיה קלה']")
    PRICE = ("xpath", "//input[@id='add-product_regular_price']")
    SALE_PRICE = ("xpath", "//input[@id='add-product_sale_price']")
    AVAILABLE_QUANTITY = ("xpath", "//input[@id='stock_quantity']")
    DONE_BUTTON = ("xpath", "//button[@type='submit']")
    IMAGE_PLACEHOLDER = ("xpath", "//div[@class='image-placeholder']")
    image_path_doll3 = '/Users/olegnarushevich/Downloads/doll.jpeg'
    image_path_doll = '/Users/olegnarushevich/Downloads/doll4.jpeg'
    SEARCH_BARCODE_ICON = ("xpath", "//span[@class='anticon anticon-search']")
    RESULTS_PRODUCT_LIST_2 = ("xpath", "//li[@class='ant-list-item'][2]")
    ADDITIONAL_INFO = ("xpath", "//div[@class='ant-collapse-item ant-collapse-no-arrow']")
    BADGE_FIELD = ("xpath", "//input[@id='badge']")


    @allure.step("Open  add page")
    def open_add_page(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT_BUTTON)).click()

    @allure.step("Select 'no barcode' checkbox")
    def select_checkbox_no_barckode(self):
        # try:
        #     alert = self.driver.switch_to.alert
        #     alert.accept()
        # except:
        checkbox = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_NO_BARCODE))
        ActionChains(self.driver).move_to_element(checkbox).click().perform()

    @allure.step("Enter unic barcode")
    def enter_barcode(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BARCODE_FIELD)).send_keys(self.generate_unic_number())

    @allure.step("Enter barcode autocomplete")
    def enter_barcode_autocomplete(self, barcode):
        added_barcode = self.wait.until(EC.element_to_be_clickable(self.ADD_BARCODE_FIELD)).send_keys(barcode)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BARCODE_ICON)).click()
        return added_barcode

    @allure.step("Select product from product list autocomplete")
    def select_product_autocomplete(self):
        self.wait.until(EC.element_to_be_clickable(self.RESULTS_PRODUCT_LIST_2)).click()

    @allure.step("Get name from name field")
    def get_name(self):
        try:
            name_element = self.wait.until(EC.presence_of_element_located(self.NAME_FIELD))
            print("Element found:", name_element)
            name = name_element.text
            print("Name text found:", name)
            return name
        except Exception as e:
            print(f"Error while getting name: {e}")
            raise

    @allure.step("Enter name")
    def enter_name(self):
        random_name = self.generate_random_word()
        self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(random_name)
        return random_name

    @allure.step("Enter description")
    def enter_description(self):
        self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION_FIELD)).send_keys(self.generate_random_word_list())

    @allure.step("Select Set category")
    def select_set_category(self, text):
        self.wait.until(EC.element_to_be_clickable(self.SET_CATEGORY)).send_keys(text)
        element = self.wait.until(EC.visibility_of_element_located(self.SOFT_DRINKS_CATEGORY))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Enter price")
    def enter_price(self):
        price = self.generate_random_index()
        self.wait.until(EC.element_to_be_clickable(self.PRICE)).send_keys(price)
        return price

    @allure.step("Enter sale price")
    def enter_sale_price(self, price):
        self.wait.until(EC.element_to_be_clickable(self.SALE_PRICE)).send_keys(price - 1)

    @allure.step("Enter available quantity")
    def enter_available_quantity(self):
        self.wait.until(EC.element_to_be_clickable(self.AVAILABLE_QUANTITY)).send_keys(self.generate_random_index())

    @allure.step("Click Done button")
    def click_done_button(self):
        done_button = self.wait.until(EC.element_to_be_clickable(self.DONE_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView();", done_button)
        done_button.click()
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
        except Exception as e:
            print(f"Error: {e}")

    # def add_image(self):
    #     add_image = self.wait.until(EC.presence_of_element_located(self.IMAGE_PLACEHOLDER))
    #     self.driver.execute_script("arguments[0].scrollIntoView();", add_image)
    #     self.driver.execute_script("arguments[0].style='display: block;';", add_image)
    #     add_image.send_keys(self.image_path_doll3)
    #     time.sleep(3)  # Подставьте свой необходимый интервал ожидания
    #     self.driver.execute_script("arguments[0].style='';", add_image)
    #     # add_image = self.wait.until(EC.element_to_be_clickable(self.IMAGE_PLACEHOLDER))
    #     # self.driver.execute_script("arguments[0].scrollIntoView();", add_image)
    #     # add_image.click()
    #     # js_script = "arguments[0].style='display: block;';"
    #     # banner_input = self.wait.until(EC.presence_of_element_located(self.BANNER_INPUT))
    #     # self.driver.execute_script(js_script, banner_input)
    #     # banner_input.send_keys(self.banner_image_path)
    #     # time.sleep(3)
    #     # js_script = "arguments[0].style='';"
    #     # self.driver.execute_script(js_script, banner_input)

    def add_image(self):
        image_placeholder = self.wait.until(EC.presence_of_element_located(self.IMAGE_PLACEHOLDER))
        self.driver.execute_script("arguments[0].scrollIntoView();", image_placeholder)
        js_script = "arguments[0].style='display: block;';"
        self.driver.execute_script(js_script, image_placeholder)
        image_placeholder.send_keys(self.image_path_doll)
        time.sleep(3)
        js_script = "arguments[0].style='';"
        self.driver.execute_script(js_script, image_placeholder)

    def scroll_to_element(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    @allure.step("Open additional information")
    def open_additional_information(self):
        additional_info_button = self.wait.until(EC.element_to_be_clickable(self.ADDITIONAL_INFO))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", additional_info_button)
        try:
            additional_info_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", additional_info_button)
            self.driver.execute_script("arguments[0].focus();", additional_info_button)
            additional_info_button.click()

    def add_badge(self, badge_text):
        self.scroll_to_element(self.BADGE_FIELD)
        badge_field = self.wait.until(EC.visibility_of_element_located(self.BADGE_FIELD))
        badge_field.clear()
        badge_field.send_keys(badge_text)
        allure.attach(badge_text, name="Badge Text", attachment_type=allure.attachment_type.TEXT)
        allure.attach(self.driver.get_screenshot_as_png(), name="Badge Field Screenshot", attachment_type=allure.attachment_type.PNG)
        return badge_text

    @allure.step("Check if add badge field is disabled")
    def is_add_badge_disabled(self):
        add_badge_field = self.wait.until(EC.presence_of_element_located(self.BADGE_FIELD))
        is_disabled = not add_badge_field.is_enabled()
        allure.attach(f"Add badge field enabled status: {is_disabled}", name="Add Badge Field Status", attachment_type=allure.attachment_type.TEXT)
        return is_disabled
