import random

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            print(f"Opening URL: {self.PAGE_URL}")
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
             self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def generate_unic_number(self):
        generated_numbers = []
        random_number = ''.join(random.choices('1234567899', k=10))
        while random_number in generated_numbers:
            random_number = ''.join(random.choices('1234567899', k=10))
        generated_numbers.append(random_number)
        return random_number

    def generate_random_index(self):
        return random.randint(2, 100)

    def generate_random_word(self):
        fake = Faker()
        random_word = fake.word()
        return random_word

    def generate_random_word_list(self):
        fake = Faker()
        random_words_list = [fake.word() for _ in range(5)]
        return random_words_list

    def generate_random_username(self):
        return f"tester{random.randint(1,1000)}@gmail.com"
