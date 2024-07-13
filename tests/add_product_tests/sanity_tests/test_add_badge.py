import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestAddBadge(BaseTest):
    @allure.title("Add badge")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_add_badge(self, login, add_product):
        add_product_page, actual_name = add_product
        self.inventory_page.deny_webpusher_notification_if_present()
        add_product_page.open_additional_information()
        badge_text = self.add_product_page.add_badge("SALE")
        add_product_page.click_done_button()

        product_name_1 = self.inventory_page.get_product_name()
        assert product_name_1 == actual_name, f"Expected product name: {product_name_1}, Actual product name: {actual_name} "
        self.web_view_page.go_to_product_page(product_name_1)
        self.web_view_page.close_cookies()
        badge_present = self.web_view_page.is_badge_present(badge_text)
        assert badge_present, f"Badge with text '{badge_text}' not found on the product page"




