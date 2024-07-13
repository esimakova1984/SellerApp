import requests
import unittest
from requests.auth import HTTPBasicAuth

class TestAPIRequest(unittest.TestCase):

    def setUp(self):
        self.url = "https://shopperstgenv.wpengine.com/wp-json/wc/v3/products"
        self.consumer_key = "ck_51f6246e062c0a24f4c1e0b08432914b6b6b115c"
        self.consumer_secret = "cs_61c766a4bf7f58551ced3e4ceacd41eb524b2bee"
        self.params = {
            'sku': '6912301014638',
            'per_page': 100
        }

    def test_api_request(self):
        response = requests.get(self.url, params=self.params, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))

        # Логирование запроса и ответа
        print("Request URL:", response.url)
        print("Request Headers:", response.request.headers)
        print("Response Code:", response.status_code)
        print("Response Text:", response.text)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200, f"API request failed with status code: {response.status_code}")

        # Проверка наличия продуктов в ответе
        products = response.json()
        self.assertTrue(products, "No products found with the specified SKU")

if __name__ == "__main__":
    unittest.main()