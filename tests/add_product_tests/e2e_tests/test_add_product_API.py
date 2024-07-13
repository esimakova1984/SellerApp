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

        # with allure.step("Open add product page"):
        #     self.add_product_page.open_add_page()
        #
        # with allure.step("Enter barcode and select product"):
        #     expected_sku = self.add_product_page.enter_barcode_autocomplete(6912301014638)
        #     self.add_product_page.select_product_autocomplete()
        #     self.add_product_page.click_done_button()

        with allure.step("Wait for API response"):
            # Увеличьте время ожидания для обновления данных
            time.sleep(10)

        # with allure.step("Get product name"):
        #     product_name = self.add_product_page.get_name()
        #     allure.attach(product_name, name="מערבל בטון צהוב – MKמקט:6912301014638", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Check if product is added to store"):
            expected_sku = 6912301014638
            product = self.api.get_product_by_sku(expected_sku)
            if product is None:
                allure.attach(f"Product with SKU {expected_sku} not found in store", name="Product Not Found", attachment_type=allure.attachment_type.TEXT)
            else:
                allure.attach(str(product.get('id')), name="Product ID", attachment_type=allure.attachment_type.TEXT)
            assert product is not None, f"Product with SKU {expected_sku} not found in store"
            assert product.get('id') is not None, "Product ID is missing"