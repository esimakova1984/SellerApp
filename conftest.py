import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.data import Data
from pages.add_product_page import AddProductPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=390,1020 ")
    options.add_argument("--lang=en")
    # driver_path = '/Users/ekaterinasimakova/QA_automation/SellerApp/chromedriver'
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(5)
    login_page.enter_login(Data.LOGIN)
    login_page.enter_password(Data.PASSWORD)
    login_page.select_checkbox()
    login_page.click_submit_button()
    login_page.deny_webpusher_notification_if_present()
    return login_page
    # request.cls.login = login_page


@pytest.fixture(scope="function")
def add_product(driver):
    add_product_page = AddProductPage(driver)
    add_product_page.open_add_page()
    add_product_page.enter_barcode()
    actual_name= add_product_page.enter_name()
    add_product_page.enter_description()
    add_product_page.select_set_category("שתיה קלה")
    price = add_product_page.enter_price()
    add_product_page.enter_sale_price(price)
    return add_product_page, actual_name
