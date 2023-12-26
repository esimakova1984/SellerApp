import time

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestEditProductCard(BaseTest):

    @allure.title("Edit product card")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_product_edit(self, login):
        if not self.inventory_page.is_product_present():
            self.inventory_page.is_opened()
            self.add_product_page.open()
            self.add_product_page.enter_barcode()
            generated_name = self.add_product_page.enter_name()
            self.add_product_page.enter_description()
            self.add_product_page.select_set_category("שתיה קלה")
            generated_price = self.add_product_page.enter_price()
            self.add_product_page.enter_sale_price(generated_price)
            self.add_product_page.enter_available_quantity()
            self.add_product_page.click_done_button()
            self.inventory_page.is_added_product_saved(generated_name)
        else:
            self.inventory_page.open_product_card()
            self.inventory_page.open_edit_card()
            generated_name = self.edit_product_card_page.change_product_name()
            self.edit_product_card_page.select_set_category("שתיה קלה")
            generated_quantity = self.edit_product_card_page.change_product_quantity()
            self.edit_product_card_page.save_changes()
            self.inventory_page.is_quantity_changes_saved(generated_quantity)
            self.inventory_page.is_name_changes_saved(generated_name)

