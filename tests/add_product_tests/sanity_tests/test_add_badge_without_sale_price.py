import time

import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Sanity testing")
class TestAddBadge(BaseTest):

    @allure.title("Edit badge")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_badge_without_sale_price(self, login):
        self.add_product_page.open_add_page()
        self.inventory_page.deny_webpusher_notification_if_present()
        self.add_product_page.enter_barcode()
        self.add_product_page.enter_description()
        self.add_product_page.select_set_category("שתיה קלה")
        self.add_product_page.enter_price()
        self.add_product_page.open_additional_information()

        is_disabled = self.add_product_page.is_add_badge_disabled()
        assert is_disabled, "Add badge field should be disabled when sale price is cleared."