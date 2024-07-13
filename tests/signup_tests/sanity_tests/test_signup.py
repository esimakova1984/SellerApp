import time
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestSignup(BaseTest):

    def signup_and_fill_onboarding(self, use_default_images=False):
        self.signup_page.open()
        generated_username = self.signup_page.fillSignupForm()
        self.signup_onboarding_page.is_opened()
        self.signup_onboarding_page.fillOnboardingForm("Hero", "Ashkelon", "Hashaetet", "999")

        if use_default_images:
            self.signup_onboarding_page.addDefaultBannerAndAvatarImages()
        else:
            self.signup_onboarding_page.addBannerAndAvatarImages()
            time.sleep(5)

        self.signup_onboarding_page.addDescription()
        self.signup_onboarding_page.submitOnboardingForm()
        return generated_username

    def login_and_goto_store_settings(self, generated_username):
        self.login_page.is_opened()
        self.login_page.login_with_generated_username(generated_username)
        self.inventory_page.is_opened()
        self.store_settings_page.open_store_settings_page()
        time.sleep(3)

    @allure.title("Successful signup with default banner and avatar images")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_successful_signup_with_default_images(self):
        generated_username = self.signup_and_fill_onboarding(use_default_images=True)
        self.login_and_goto_store_settings(generated_username)

    @allure.title("Successful signup with images")
    @allure.severity("Critical")
    @pytest.mark.sanity
    def test_successful_signup_with_images(self):
        generated_username = self.signup_and_fill_onboarding(use_default_images=False)
        self.login_and_goto_store_settings(generated_username)
