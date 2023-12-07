import random

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC



def generate_random_index():
    return random.randint(1, 1000)


class OnboardingPage(BasePage):
    PAGE_URL = Links.ONBOARDING_PAGE
    FIND_YOURE_STORE_FIELD = ("xpath", "//input[@id='contacts_search']")
    STORE_NAME = ("xpath", "//input[@id='contacts_storeName']")
    DROPDOWN_LIST_FIRST_ITEM = ("xpath", "//div[@class='rc-virtual-list-holder-inner']/div[1]")
    STORE_NAME_FIELD = ("xpath", "//input[@id='contacts_storeName']")
    CITY_FIELD = ("xpath", "//input[@id='contacts_address_city']")
    STREET_FIELD = ("xpath", "//input[@id='contacts_address_street']")
    STREET_NUMBER_FIELD = ("xpath", "//input[@id='contacts_address_streetNumber']")
    PHONE_NUMBER_FIELD = ("xpath", "//input[@id='contacts_phone']")
    SAVE_BUTTON = ("xpath", "//button[.='Save & Proceed']")
    DEFAULT_BANNER_BUTTON = ("xpath", "//button[.='Use default image']")
    DEFAULT_AVATAR_BUTTON = ("xpath", "//button[.='Use default avatar']")
    DESCRIPTION_FIELD = ("xpath", "//textarea[@id='storefront_description']")
    FINISH_BUTTON = ("xpath", "//button[contains(.,'Finish')]")
    SUCCESSFULL_CREATE_BUTTON = ("xpath", "//button[.='Ok']")

    def fillOnboardingForm(self, storeName, city, street, phoneNumber):
        index = generate_random_index()
        store_name = self.wait.until(EC.element_to_be_clickable(self.STORE_NAME))
        store_name.clear()
        store_name.send_keys(storeName + f"{index}")
        self.wait.until(EC.element_to_be_clickable(self.CITY_FIELD)).send_keys(city)
        self.wait.until(EC.element_to_be_clickable(self.STREET_FIELD)).send_keys(street)
        self.wait.until(EC.element_to_be_clickable(self.STREET_NUMBER_FIELD)).send_keys(index)
        self.wait.until(EC.element_to_be_clickable(self.PHONE_NUMBER_FIELD)).send_keys(phoneNumber + f"{index}")
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def addPhotoAndDescription(self, text):
        index = generate_random_index()
        self.wait.until(EC.element_to_be_clickable(self.DEFAULT_BANNER_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.DEFAULT_AVATAR_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION_FIELD)).send_keys(text + f"{index}")
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.SUCCESSFULL_CREATE_BUTTON)).click()




