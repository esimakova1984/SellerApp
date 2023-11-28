import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class BaseTest:
    data: Data

    login_page: LoginPage
    inventory_page: InventoryPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.inventory_page = InventoryPage(driver)
