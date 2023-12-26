import allure
from selenium.webdriver import Keys, ActionChains
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AddProductPage(BasePage):
    PAGE_URL = Links.ADD_PRODUCT_PAGE
    ADD_PRODUCT_BUTTON = ("xpath", "//*[local-name()='svg' and @data-icon='plus']")
    CONTAINER = ("xpath", "//div[@class='ant-card ant-card-bordered']")
    CHECKBOX_NO_BARCODE = ("xpath", "//input[@id='add-product_no-barcode']")
    ADD_BARCODE_FIELD = ("xpath", "//input[@id='add-product_barcode']")
    NAME_FIELD = ("xpath", "//input[@id='add-product_name']")
    DESCRIPTION_FIELD = ("xpath", "//textarea[@id='add-product_description']")
    SET_CATEGORY = ("xpath", "//input[@id='add-product_treeCategory']")
    SOFT_DRINKS_CATEGORY = ("xpath", "//span[@title='שתיה קלה']")
    PRICE = ("xpath", "//input[@id='add-product_regular_price']")
    SALE_PRICE = ("xpath", "//input[@id='add-product_sale_price']")
    AVAILABLE_QUANTITY = ("xpath", "//input[@id='add-product_stock_quantity']")
    DONE_BUTTON = ("xpath", "//button[@type='submit']")

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
        self.wait.until(EC.element_to_be_clickable(self.SALE_PRICE)).send_keys(price - 0.1)

    @allure.step("Enter available quantity")
    def enter_available_quantity(self):
        self.wait.until(EC.element_to_be_clickable(self.AVAILABLE_QUANTITY)).send_keys(self.generate_random_index())

    @allure.step("Click Done button")
    def click_done_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DONE_BUTTON)).click()
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
        except Exception as e:
            print(f"Error: {e}")



            
