import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing. Orders page")
class TestPaymentStatus(BaseTest):
    @allure.title("Payment status")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_payment_status(self, login):
        self.order_page.open()
        current_url = self.order_page.get_current_url()
        expected_status = self.order_page.get_expected_payment_statuses(current_url)
        payment_status = self.order_page.get_order_payment_status_by_index(1)

        assert payment_status in expected_status, f"Expected payment status to be one of {expected_status}, but got: {payment_status}"

