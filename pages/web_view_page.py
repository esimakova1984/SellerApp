from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC



class WebViewPage(BasePage):
    PAGE_URL = Links.WEB_VIEW_PAGE_STG
    BADGE = ("xpath", "//span[contains(@class, 'badge') and contains(@class, 'type-4')]")
    CLOSE_COOKIES_BUTTON = ("xpath", "//a[@class='button']")

    def is_badge_present(self, text):
        try:
            badge_element = self.wait.until(EC.presence_of_element_located(self.BADGE))
            badge_text = badge_element.text
            print(f"Badge found: {badge_text}")  # Debugging statement
            print(f"Expected badge text: {text}")
            return text in badge_text
        except Exception as e:
            print(f"Badge with text '{text}' not found: {e}")
            return False

    def go_to_product_page(self, product_name):
        base_url = self.PAGE_URL
        unique_product_path = f"{base_url}/{product_name}"
        self.driver.get(unique_product_path)

    def close_cookies(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_COOKIES_BUTTON)).click()
