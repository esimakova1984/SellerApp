from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class StoreSettingsPage(BasePage):
    PAGE_URL = Links.STORE_SETTINGS_PAGE
    BURGER_MENU = ("xpath", "//*[name()='svg' and @data-icon='menu']")
    SETTINGS_FROM_BURGER_MENU = ("xpath", "//*[@class='anticon anticon-setting ant-menu-item-icon']")
    EDIT_SETTINGS_BUTTON = ("xpath", "//*[name()='svg' and @data-icon='edit']")

    def open_store_settings_page_from_burger_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU)).click()
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS_FROM_BURGER_MENU)).click()
        self.wait.until(EC.element_to_be_clickable(self.EDIT_SETTINGS_BUTTON)).click()






