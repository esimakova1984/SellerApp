import time

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestAddProduct(BaseTest):

    @allure.title("Add product")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_add_product(self, login):
        self.inventory_page.is_opened()
        # for _ in range(10):
        self.add_product_page.open_add_page()
        self.add_product_page.enter_barcode()
        time.sleep(3)
        self.add_product_page.add_image()
        time.sleep(3)
        generated_name = self.add_product_page.enter_name()
        self.add_product_page.enter_description()
        self.add_product_page.select_set_category("שתיה קלה")
        self.add_product_page.enter_price()
        self.add_product_page.click_done_button()
        time.sleep(5)
        # self.inventory_page.is_added_product_saved(generated_name)