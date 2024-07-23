import time

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestAddProduct(BaseTest):

    @allure.title("Add product")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_product(self, login):
        self.inventory_page.is_opened()
        self.inventory_page.deny_webpusher_notification_if_present()
        self.add_product_page.open_add_page()
        self.add_product_page.enter_barcode()
        generated_name = self.add_product_page.enter_name()
        self.add_product_page.enter_description()
        self.add_product_page.select_set_category("שתיה קלה")
        generated_price = self.add_product_page.enter_price()
        self.add_product_page.enter_sale_price(generated_price)
        time.sleep(3)
        self.add_product_page.click_done_button()
        self.inventory_page.is_added_product_saved(generated_name)
        # self.inventory_page.delete_added_product_by_name(generated_name)
        # self.inventory_page.is_product_deleted(generated_name)
