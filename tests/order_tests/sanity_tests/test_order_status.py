
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing. Orders page")
class TestOrderStatus(BaseTest):
    @allure.title("Order status")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_verify_order_status(self, login):
        self.order_page.open()
        self.order_page.select_order_by_index(1)
        status_text = self.order_page.get_order_status()
        print(f"Order status: {status_text}")
        valid_statuses = ["New", "Ready for Pickup", "Done", "Cancelled"]

        assert status_text in valid_statuses, f"Invalid order status: {status_text}"

        assert status_text, "Order status should not be empty"
