import allure
import pytest

from base.base_test import BaseTest
from config.data import Data

@allure.feature('Registration tests')
class TestUnsuccessfulLogin(BaseTest):

    @allure.title("Unsuccessful login")
    @allure.severity("Critical")
    @pytest.mark.parametrize("login, password, expected_result, empty_field, invalid_input, checkbox_not_checked", [
        (Data.LOGIN, "", "Password is required", "password", None, False),
        ("", Data.PASSWORD, "username is required", "username", None, True),
        (Data.INVALID_LOGIN, Data.PASSWORD, "Invalid username or password.", None, "invalid_user", False),
        (Data.LOGIN, Data.INVALID_PASSWORD, "Invalid username or password.", None, "invalid_password", False),
        (Data.LOGIN, Data.PASSWORD, "Should accept agreement", None, None, True),
    ])
    @pytest.mark.sanity
    def test_unsuccessful_login(self, login, password, expected_result, empty_field, invalid_input, checkbox_not_checked):
        with allure.step("Open the login page and perform login actions"):
            self.login_page.open()
            self.login_page.enter_login(login)
            self.login_page.enter_password(password)
            if not checkbox_not_checked:
                self.login_page.select_checkbox()
            self.login_page.click_submit_button()

        with allure.step("Check the error message"):
            error_message = self.login_page.get_unsuccseful_login_result(empty_field=empty_field, invalid_input=invalid_input, checkbox_not_checked=checkbox_not_checked)
        with allure.step("Assert the error message"):
            assert error_message == expected_result, f"Expected: {expected_result}, Actual: {error_message}"

