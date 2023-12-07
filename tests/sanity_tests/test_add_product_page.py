import time

import allure
import pytest

from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestAddProduct(BaseTest):

    @allure.title("Add product")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_product(self, login):
        self.inventory_page.open_add_product_page()
        self.add_product_page.is_opened()