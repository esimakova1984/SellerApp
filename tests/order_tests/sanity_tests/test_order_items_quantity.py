import time

import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing. Orders page")
class TestOrderItemsQuantity(BaseTest):
    @allure.title("Items quantity")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_verify_total_quantity_of_items_in_order(self, login):
        self.order_page.open()
        self.order_page.select_order_by_index(1)
        time.sleep(5)
        total_items_header = self.order_page.get_total_items_from_header()
        assert total_items_header is not None, "Total items header should not be None."

        total_items_quantity = self.order_page.count_order_items_quantity()
        assert total_items_quantity is not None, "Total items quantity should not be None."

        assert total_items_header == total_items_quantity, f"Expected total items: {total_items_header}, but got: {total_items_quantity}"

