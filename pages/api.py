# import allure
# import requests
# from base.base_page import BasePage
#
# class Api(BasePage):
#
#     base_url = "https://shopperstgenv.wpengine.com/wp-json/wc/v3/products"
#     consumer_key = "ck_51f6246e062c0a24f4c1e0b08432914b6b6b115c"
#     consumer_secret = "cs_61c766a4bf7f58551ced3e4ceacd41eb524b2bee"
#
#     @allure.step("Get product by SKU from API")
#     def get_product_id_by_sku(self, sku):
#         params = {
#             'consumer_key': self.consumer_key,
#             'consumer_secret': self.consumer_secret,
#             'sku': sku
#         }
#
#         response = requests.get(self.base_url, params=params)
#         allure.attach(response.text, name="API Response for SKU", attachment_type=allure.attachment_type.JSON)
#
#         if response.status_code == 200:
#             products = response.json()
#             if products:
#                 product = products[0]
#                 allure.attach(str(product), name="Found Product", attachment_type=allure.attachment_type.JSON)
#                 return product.get('id')
#             else:
#                 allure.attach(f"No product found with SKU: {sku}", name="Product Not Found", attachment_type=allure.attachment_type.TEXT)
#         else:
#             allure.attach(f"Failed to fetch products, status code: {response.status_code}", name="API Error", attachment_type=allure.attachment_type.TEXT)
#             if response.status_code == 403:
#                 allure.attach("Access forbidden. Please check your API keys and permissions.", name="403 Forbidden", attachment_type=allure.attachment_type.TEXT)
#
#         return None
#
#     @allure.step("Get product by ID from API")
#     def get_product_by_id(self, product_id):
#         url = f"{self.base_url}/{product_id}"
#         params = {
#             'consumer_key': self.consumer_key,
#             'consumer_secret': self.consumer_secret
#         }
#
#         response = requests.get(url, params=params)
#         allure.attach(response.text, name="API Response for ID", attachment_type=allure.attachment_type.JSON)
#
#         if response.status_code == 200:
#             product = response.json()
#             allure.attach(str(product), name="Product Details", attachment_type=allure.attachment_type.JSON)
#             return product
#         else:
#             allure.attach(f"Failed to fetch product, status code: {response.status_code}", name="API Error", attachment_type=allure.attachment_type.TEXT)
#             if response.status_code == 403:
#                 allure.attach("Access forbidden. Please check your API keys and permissions.", name="403 Forbidden", attachment_type=allure.attachment_type.TEXT)
#
#         return None

import allure
import requests
from requests.auth import HTTPBasicAuth
from base.base_page import BasePage

class Api(BasePage):

    base_url = "https://shopperstgenv.wpengine.com/wp-json/wc/v2/products"
    consumer_key = "ck_51f6246e062c0a24f4c1e0b08432914b6b6b115c"
    consumer_secret = "cs_61c766a4bf7f58551ced3e4ceacd41eb524b2bee"

    @allure.step("Get product by SKU from API")
    def get_product_by_sku(self, sku):
        params = {
            'sku': sku,
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret
        }

        headers = {
            'User-Agent': 'PostmanRuntime/7.40.0',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'PHPSESSID=7393c6fe878d3b4eaaefe21b11c2c9bf; tinvwl_wishlists_data_counter=1; '
                      'wpe-auth=071d5985dd99d9f852a3c06a67dc1f00d359a42b0ee2b15925787a71416d1180',
        }

        response = requests.get(self.base_url, params=params, headers=headers)
        allure.attach(response.url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="API Response for SKU", attachment_type=allure.attachment_type.HTML)

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
            if response.status_code == 403:
                allure.attach("Access forbidden. Please check your API keys and permissions.", name="403 Forbidden", attachment_type=allure.attachment_type.TEXT)
            if response.status_code == 401:
                allure.attach("Authorization error. Please check your API keys and permissions.", name="401 Unauthorized", attachment_type=allure.attachment_type.TEXT)

        return None