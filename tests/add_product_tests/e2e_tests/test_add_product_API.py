import time
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("E2E")
class TestAddProductE2E(BaseTest):

    @allure.title("Add product and check")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_add_product_e2e(self, login):
        with allure.step("Open inventory page"):
            self.inventory_page.is_opened()

        with allure.step("Check if product is added to store"):
            self.inventory_page.open_product_card()
            self.inventory_page.open_edit_card()
            time.sleep(5)
            sku = self.edit_product_card_page.get_barcode()
            assert sku, "SKU is empty"
            allure.attach(sku, name="Product SKU", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Check if product is added to store via API"):
            product = self.api.get_product_by_sku(sku)
            assert product, f"Product with SKU {sku} not found in store"
            allure.attach(str(product), name="Product Details", attachment_type=allure.attachment_type.JSON)
