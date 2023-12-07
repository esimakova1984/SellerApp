import time

import allure
import pytest

from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestStoreTesting(BaseTest):

    @allure.title("Successfull signup")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_store_settings(self, login):
        self.store_settings_page.open_store_settings_page_from_burger_menu()
        self.store_settings_page.is_opened()
        time.sleep(3)
