import allure

from base.base_test import BaseTest


class TestSuccessfulSignupOnboarding(BaseTest):

    def test_successful_signup_onboarding(self):
        with allure.step("Open the onboarding signup page and perform signup actions"):
            self.signup_page.open()
            self.signup_page.fillSignupForm()
            self.signup_onboarding_page.is_opened()
            self.signup_onboarding_page.fillOnboardingForm()






