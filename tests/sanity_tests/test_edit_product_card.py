import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestEditProductCard(BaseTest):

    @allure.title("Edit product card")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_product_edit(self, login):
        self.inventory_page.open_product_card()
        self.inventory_page.open_edit_card()
        self.edit_product_card_page.change_product_name()
        self.edit_product_card_page.select_set_category("שתיה קלה")
        generated_quantity = self.edit_product_card_page.change_product_quantity()
        self.edit_product_card_page.save_changes()
        self.inventory_page.is_quantity_changes_saved(generated_quantity)
