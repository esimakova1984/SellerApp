import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Sanity testing")
class TestStoreTesting(BaseTest):

    @allure.title("Store settings")
    @allure.severity("Critical")
    @pytest.mark.sanyti
    def test_store_settings(self, login):
        self.store_settings_page.open_store_settings_page()
        self.store_settings_page.is_opened()
        self.store_settings_page.open_edit_form()
        self.store_settings_page.fill_name_field()
        self.store_settings_page.fill_phone_field()
        expected_email = self.store_settings_page.fill_email_field()
        self.store_settings_page.fill_description()
        self.store_settings_page.submit_edit_form()
        self.store_settings_page.logout()
        self.login_page.open()
        self.login_page.quick_login()
        self.store_settings_page.open_store_settings_page()
        actual_email = self.store_settings_page.get_email()
        assert actual_email == expected_email, f"Email {actual_email} is not equal to the expected value: {expected_email}"
