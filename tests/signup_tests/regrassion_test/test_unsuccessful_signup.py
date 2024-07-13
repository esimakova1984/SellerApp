import time

import allure
import pytest

from base.base_test import BaseTest
from config.data import Data


@allure.feature('Registration tests')
class TestUnsuccessfulSignUp(BaseTest):

    @allure.title("Unsuccessful signup - invalid data")
    @allure.severity("Critical")
    @pytest.mark.parametrize("email, password, confirm_password, expected_result, empty_field, invalid_input",[
                            ("", Data.PASSWORD, Data.PASSWORD, "Email is required", "email", None), #Empty email field
                            ("invalidemail.com", Data.PASSWORD, Data.PASSWORD, "Email is not valid", None, "invalid_email"), # Invalid email address without '@'
                            ("user@gmail..com", Data.PASSWORD, Data.PASSWORD, "Email is not valid", None, "invalid_email"), # Email address with double dots in domain
                            ("user@com", Data.PASSWORD, Data.PASSWORD, "Email is not valid", None, "invalid_email"), # Email without top-level domain
                            ("user@com@extra.com", Data.PASSWORD, Data.PASSWORD, "Email is not valid", None, "invalid_email"), # Email with multiple "@" characters.
                            ("    @example.com", Data.PASSWORD, Data.PASSWORD, "Email is not valid", None, "invalid_email"),# Email with spaces
                            ("test999@gmail.com", "", Data.PASSWORD, "Password is required", "password", None), # Empty password
     # ("test999@gmail.com", "      ", "      ", "Password is required"), # Password with spaces
                            ("test999@gmail.com", "short", "short", "Password must be between 6 and 26 characters long", None, "invalid_password"), # Password length is less than the minimum
                            ("test999@gmail.com", "qwertyuiopasdfghjkl;zxcvbnm", "qwertyuiopasdfghjkl;zxcvbnm", "Password must be between 6 and 26 characters long", None, "invalid_password"), # Password exceeds maximum length
                            ("test999@gmail.com", "password", "otherpassword", "Password doesn't match", None, "invalid_confirm_password"),
                                # Password and confirmation mismatch
     # ("ekaterina_test@gmail.com", "password", "password", "Username already exists"), # Already existing username
                            ("test999@gmail.com", "password", "", "confirm password is required", "confirm_password", None), # Password confirmation is empty
    ])
    @pytest.mark.sanity
    def test_invalid_data_in_signup(self, email, password, confirm_password, expected_result, empty_field, invalid_input):
        with allure.step("Open the signup page and perform signup actions"):
            self.signup_page.open()
            self.signup_page.enter_email(email)
            time.sleep(3)
            self.signup_page.enter_password(password)
            time.sleep(3)
            self.signup_page.enter_confirm_password(confirm_password)
            self.signup_page.submit_form()

        with allure.step("Check the error message"):
            error_message = self.signup_page.get_unsuccseful_signup_result(empty_field=empty_field, invalid_input=invalid_input)
        with allure.step("Assert the error message"):
            assert error_message == expected_result, f"Expected: {expected_result}, Actual: {error_message}"




