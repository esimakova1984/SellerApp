import pytest
from config.data import Data
from pages.add_product_page import AddProductPage
from pages.api import Api
from pages.edit_product_card_page import EditProductPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.order_page import OrderDetailsPage
from pages.signup_onboarding_page import OnboardingPage
from pages.signup_page import SignUpPage
from pages.store_settings_page import StoreSettingsPage
from pages.web_view_page import WebViewPage


class BaseTest:
    data: Data

    login_page: LoginPage
    inventory_page: InventoryPage
    edit_product_card_page: EditProductPage
    signup_page: SignUpPage
    signup_onboarding_page: OnboardingPage
    add_product_page: AddProductPage
    store_settings_page: StoreSettingsPage
    api: Api
    web_view_page: WebViewPage
    order_page: OrderDetailsPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.inventory_page = InventoryPage(driver)
        request.cls.edit_product_card_page = EditProductPage(driver)
        request.cls.signup_page = SignUpPage(driver)
        request.cls.signup_onboarding_page = OnboardingPage(driver)
        request.cls.add_product_page = AddProductPage(driver)
        request.cls.store_settings_page = StoreSettingsPage(driver)
        request.cls.web_view_page = WebViewPage(driver)
        request.cls.order_page = OrderDetailsPage(driver)
        request.cls.api = Api(driver)
