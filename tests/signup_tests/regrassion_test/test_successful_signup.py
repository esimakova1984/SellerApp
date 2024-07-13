import time

import allure
import pytest

from base.base_test import BaseTest
from config.data import Data


@allure.feature('Registration tests')
class TestSuccessfulSignUp(BaseTest):

    @allure.title("Successful signup")
    @allure.severity("Critical")
    @pytest.mark.parametrize("email, password, confirm_password",[
        ("user@sub.example.com", Data.PASSWORD, Data.PASSWORD), #Valid email with a subdomain
        ("user123@example.com", Data.PASSWORD, Data.PASSWORD), # Numbers in the local part of the email
        ("user.name+tag@example.com", Data.PASSWORD, Data.PASSWORD), #Special characters in the local part
        ("test999@gmail.com", "short6", "short6"), # Valid password with permissible minimum 6 characters
        ("test999@gmail.com", "qwertyuiopasdfghjklzxcvbnm", "qwertyuiopasdfghjklzxcvbnm"), # Valid password with permissible maximum 26 characters.
        ("test999@gmail.com", "test1%", "test1%"), # Security check (letters, numbers, and special characters)
        ("test999@gmail.com", "TesteR", "TesteR"), # Password camelcase check
    ])
    @pytest.mark.sanity
    def test_successful_signup_with_valid_data(self, email, password, confirm_password):
        with allure.step("Open the signup page and perform signup actions"):
            self.signup_page.open()
            self.signup_page.enter_email(email)
            time.sleep(3)
            self.signup_page.enter_password(password)
            time.sleep(3)
            self.signup_page.enter_confirm_password(confirm_password)
            self.signup_page.submit_form()
            self.signup_onboarding_page.is_opened()







