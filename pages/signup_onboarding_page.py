import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


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
    BANNER_INPUT = ("xpath", "//input[@type='file'][@id='storefront']")
    AVATAR_INPUT = ("xpath", "//input[@type='file'][@id='avatar']")
    DEFAULT_BANNER_BUTTON = ("xpath", "//button[.='Use default image']")
    DEFAULT_AVATAR_BUTTON = ("xpath", "//button[.='Use default avatar']")
    DESCRIPTION_FIELD = ("xpath", "//textarea[@id='storefront_description']")
    FINISH_BUTTON = ("xpath", "//button[contains(.,'Finish')]")
    SUCCESSFULL_CREATE_BUTTON = ("xpath", "//button[.='Ok']")
    banner_image_path = "/Users/olegnarushevich/Desktop/Screen Shot 2022-03-29 at 18.35.10.png"
    avatar_image_path = '/Users/olegnarushevich/QA_32_automation/webinars/Trello/src/test/resources/images.jpeg'

    @allure.step("Fill onboarding form")
    def fillOnboardingForm(self, storeName, city, street, phoneNumber):
        index = self.generate_random_index()
        store_name = self.wait.until(EC.element_to_be_clickable(self.STORE_NAME))
        store_name.clear()
        store_name.send_keys(storeName + f"{index}")
        self.wait.until(EC.element_to_be_clickable(self.CITY_FIELD)).send_keys(city)
        self.wait.until(EC.element_to_be_clickable(self.STREET_FIELD)).send_keys(street)
        self.wait.until(EC.element_to_be_clickable(self.STREET_NUMBER_FIELD)).send_keys(index)
        self.wait.until(EC.element_to_be_clickable(self.PHONE_NUMBER_FIELD)).send_keys(phoneNumber + f"{index}")
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Add banner and avatar images")
    def addBannerAndAvatarImages(self):
        js_script = "arguments[0].style='display: block;';"
        banner_input = self.wait.until(EC.presence_of_element_located(self.BANNER_INPUT))
        self.driver.execute_script(js_script, banner_input)
        banner_input.send_keys(self.banner_image_path)
        time.sleep(3)
        js_script = "arguments[0].style='';"
        self.driver.execute_script(js_script, banner_input)

        js_script = "arguments[0].style='display: block;';"
        avatar_input = self.wait.until(EC.presence_of_element_located(self.AVATAR_INPUT))
        self.driver.execute_script(js_script, avatar_input)
        avatar_input.send_keys(self.avatar_image_path)
        time.sleep(3)
        js_script = "arguments[0].style='';"
        self.driver.execute_script(js_script, avatar_input)

    @allure.step("Add default banner and avatar images")
    def addDefaultBannerAndAvatarImages(self):
        self.wait.until(EC.element_to_be_clickable(self.DEFAULT_BANNER_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.DEFAULT_AVATAR_BUTTON)).click()

    @allure.step("Add description")
    def addDescription(self, ):
        text = self.generate_random_word_list()
        self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION_FIELD)).send_keys(text)

    @allure.step("Submit onboarding form")
    def submitOnboardingForm(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.SUCCESSFULL_CREATE_BUTTON)).click()
