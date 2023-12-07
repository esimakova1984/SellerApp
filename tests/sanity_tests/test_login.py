
import allure
import pytest
from base.base_test import BaseTest
from config.data import Data


@allure.feature("Sanity testing")
class TestSanity(BaseTest):

    @allure.title("Successfull login")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_succeccfull_login(self, login):
        self.inventory_page.is_opened()

    @allure.title("Unsuccessfull login")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_unsuccessfull_login(self):
        self.login_page.open()
        self.login_page.enter_login(Data.INVALID_LOGIN)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.select_checkbox()
        self.login_page.click_submit_button()
        self.login_page.is_error_message_appeared()


