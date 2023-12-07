import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.data import Data
from pages.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=390,844")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(request, driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login(Data.LOGIN)
    login_page.enter_password(Data.PASSWORD)
    login_page.select_checkbox()
    login_page.click_submit_button()

    request.cls.login = login_page
