import random
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestEditProductCard(BaseTest):

    @allure.title("Edit product card")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_product_edit(self, login):
        self.inventory_page.open_product_card()
        self.inventory_page.open_edit_card()
        self.edit_product_card_page.change_product_name(f"לחם בריוש{random.randint(1, 1000)}")
        self.edit_product_card_page.change_product_quantity(f"{random.randint(1, 1000)}")
        self.edit_product_card_page.save_changes()
        self.inventory_page.is_quantity_changes_saved(self.inventory_page.get_product_quantity())
