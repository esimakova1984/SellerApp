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
        # Check if any product is present
        if not self.inventory_page.is_product_present():
            self.add_product_page.open_add_page()
            self.inventory_page.deny_webpusher_notification_if_present()
            self.add_product_page.enter_name()  # Retrieve the product name after entering it
            self.add_product_page.enter_barcode()
            self.add_product_page.enter_description()
            self.add_product_page.select_set_category("שתיה קלה")
            generated_price = self.add_product_page.enter_price()
            self.add_product_page.enter_sale_price(generated_price)
            self.add_product_page.enter_available_quantity()
            self.add_product_page.click_done_button()
            # Ensure the product is added
            assert self.inventory_page.is_product_present(), "Product was not added successfully."

        self.inventory_page.deny_webpusher_notification_if_present()
        self.inventory_page.open_product_card()  # Open the first product card by default
        self.inventory_page.open_edit_card()
        new_generated_name = self.edit_product_card_page.change_product_name()
        self.edit_product_card_page.change_description()
        self.edit_product_card_page.select_set_category("כללי")
        self.edit_product_card_page.save_changes()
        self.inventory_page.scroll_to_top()
        time.sleep(7)
        self.inventory_page.is_name_changes_saved(new_generated_name)
