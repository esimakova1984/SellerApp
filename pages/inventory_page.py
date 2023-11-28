from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    PAGE_URL = Links.INVENTORY_PAGE
