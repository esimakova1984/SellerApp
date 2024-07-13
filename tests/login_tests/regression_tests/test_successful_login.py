
import allure
import pytest
from base.base_test import BaseTest
from config.data import Data


@allure.feature('Registration tests')
class TestSuccessfulLogin(BaseTest):


    @allure.title("Successfull login")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_successful_login(self):
        self.login_page.open()
        self.login_page.enter_login(Data.LOGIN)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.select_checkbox()
        self.login_page.click_submit_button()
        self.inventory_page.is_opened()
