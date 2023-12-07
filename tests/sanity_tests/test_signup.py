import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestSignup(BaseTest):

    @allure.title("Successfull signup")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_successful_signup(self):
        self.signup_page.open()
        generated_username = self.signup_page.fillSignupForm()
        self.signup_onboarding_page.is_opened()
        self.signup_onboarding_page.fillOnboardingForm("Hero", "Ashkelon", "Hashaetet", "0999")
        self.signup_onboarding_page.addPhotoAndDescription("This test is working")
        self.login_page.is_opened()
        self.login_page.login_with_generated_username(generated_username)
        self.inventory_page.is_opened()
