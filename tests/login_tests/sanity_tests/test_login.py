import allure
import pytest
from base.base_test import BaseTest
from config.data import Data


@allure.feature("Sanity testing")
class TestSanity(BaseTest):

    @allure.title("Successfull login")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_login(self, login):
        self.inventory_page.is_opened()



