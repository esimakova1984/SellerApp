import time
import allure
import pytest
from selenium.common import TimeoutException
from base.base_test import BaseTest


@allure.feature("Sanity testing. Orders page")
class TestDeleteOrderItem(BaseTest):
    @allure.title("Delete item from order")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_order_item(self, login):
        self.order_page.open()
        self.order_page.select_order_by_index(1)

        initial_quantity = self.order_page.get_total_items_from_header()
        time.sleep(3)

        try:
            self.order_page.click_edit_button()
        except TimeoutException:
            print("Edit button not found, proceeding to delete the item directly.")

        self.order_page.delete_item_by_index(0)
        self.order_page.confirm_item_deletion()
        time.sleep(5)

        new_quantity = self.order_page.get_total_items_from_header()
        assert new_quantity == initial_quantity - 1, f"Expected {initial_quantity - 1} items, but got {new_quantity}"




