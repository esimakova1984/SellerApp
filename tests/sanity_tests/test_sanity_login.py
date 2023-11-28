import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Sanity testing")
class TestSanityLogin(BaseTest):

    @allure.title("Login sanity test")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_succeccfull_login(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.select_checkbox()
        self.login_page.click_submit_button()
        self.inventory_page.is_opened()
