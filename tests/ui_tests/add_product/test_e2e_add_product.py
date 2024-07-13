import allure
import pytest

from base.base_test import BaseTest

@allure.feature('Add product E2E')
class TestE2EAddProduct(BaseTest):

    @allure.title("Add product to the sellerApp and check on Shopper")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_add_product(self, login):
        self.add_product_page.open_add_page()
        self.add_product_page.enter_barcode()
        generated_name = self.add_product_page.enter_name()
        self.add_product_page.enter_description()
        self.add_product_page.select_set_category("שתיה קלה")
        self.add_product_page.enter_price()
        self.add_product_page.click_done_button()
        self.inventory_page.is_added_product_saved(generated_name)
        
