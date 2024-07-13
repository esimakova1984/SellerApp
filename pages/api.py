import allure
import requests

from base.base_page import BasePage


class Api(BasePage):

    @allure.step("Get product by SKU from API")
    def get_product_by_sku(self, sku):
        url = "https://shopperstgenv.wpengine.com/wp-json/wc/v3/products"
        consumer_key = "ck_51f6246e062c0a24f4c1e0b08432914b6b6b115c"
        consumer_secret = "cs_61c766a4bf7f58551ced3e4ceacd41eb524b2bee"
        sku = "6912301014638"

        params = {
            'consumer_key': consumer_key,
            'consumer_secret': consumer_secret,
            'sku': sku
        }

        response = requests.get(url, params=params)
        allure.attach(response.text, name="API Response", attachment_type=allure.attachment_type.JSON)

        if response.status_code == 200:
            products = response.json()
            if products:
                product = products[0]
                allure.attach(str(product), name="Found Product", attachment_type=allure.attachment_type.JSON)
                return product
            else:
                allure.attach(f"No product found with SKU: {sku}", name="Product Not Found", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(f"Failed to fetch products, status code: {response.status_code}", name="API Error", attachment_type=allure.attachment_type.TEXT)

        return None