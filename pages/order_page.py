import re

import allure
from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class OrderDetailsPage(BasePage):
    PAGE_URL = Links.ORDERS_PAGE_STG
    ORDERS_ICON = ("xpath", "//li[@class='ant-menu-item toolbar-item']")
    ORDER_PAYMENT_STATUS = ("xpath", "//span[@style='display: flex; width: 50px;']")
    STORE_PAYMENT_STATUS_MAP = {
        "https://seller-app-stg.web.app/40/": ["Paid"],
        "https://seller-app-stg.web.app/152/": ["Unpaid"],
        # Add more stores as needed
    }
    ORDER_TOTAL_QUANTITY_ITEMS = ("xpath", "//div[@style='display: flex; align-content: flex-start; width: 50px;']")
    ORDER_LINKS = ("xpath", "//div[@class='ant-collapse-item']")
    ORDER_ITEMS = ("xpath", "//li[@class='ant-list-item']")
    ITEM_QUANTITY = ("xpath", "//div[@class='item-quantity']")
    NEW_ORDER_SATUS = ("xpath", "//span[.=' New']")
    READY_FOR_PICKUP_ORDER_STATUS = ("xpath", "//span[.=' Ready']")
    DONE_ORDER_STATUS = ("xpath", "//span[.=' Done']")
    CANCELLED_ORDER_STATUS = ("xpath", "//span[.=' Canceled']")
    EDIT_ORDER = ("xpath", "//button[contains(.,'Edit')]")
    DELETE_ITEM_BUTTON = ("xpath", "//button[@class='ant-btn ant-btn-circle ant-btn-icon-only']")
    CONFIRM_ITEM_DELETION = ("xpath", "//button[.='Yes']")
    RESTORE_ORDER_BUTTON = ("xpath", "//button[contains(.,'Restore')]")

    @allure.step("Open orders page")
    def open_orders_page(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDERS_ICON)).click()

    @allure.step("Get payment status of order by index")
    def get_order_payment_status_by_index(self, index):
        payment_status_elements = self.wait.until(EC.presence_of_all_elements_located(self.ORDER_PAYMENT_STATUS))
        payment_status = payment_status_elements[index].text
        allure.attach(payment_status, name="Order Payment Status", attachment_type=allure.attachment_type.TEXT)
        return payment_status

    @allure.step("Get current store URL")
    def get_current_url(self):
        current_url = self.driver.current_url
        allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
        return current_url

    @allure.step("Get expected payment statuses based on the store URL")
    def get_expected_payment_statuses(self, current_url):
        for store_identifier, statuses in self.STORE_PAYMENT_STATUS_MAP.items():
            if store_identifier in current_url:
                return statuses
        # Default to both statuses if the store is not specifically listed
        return ["Paid", "Unpaid"]

    @allure.step("Get total number of items from order header")
    def get_total_items_from_header(self):
        total_items_element = self.wait.until(EC.presence_of_element_located(self.ORDER_TOTAL_QUANTITY_ITEMS))
        total_items_text = total_items_element.text.strip()
        allure.attach(total_items_text, name="Total Items Header Text", attachment_type=allure.attachment_type.TEXT)
        if not total_items_text:
            raise ValueError("The total items header text is empty.")
        match = re.search(r'\d+', total_items_text)
        if match:
            total_items = int(match.group())
        else:
            raise ValueError(f"Could not find a number in the header text: {total_items_text}")
        allure.attach(str(total_items), name="Total Items in Header", attachment_type=allure.attachment_type.TEXT)
        print(f"Total items from header: {total_items}")
        return total_items

    @allure.step("Select order by index")
    def select_order_by_index(self, index):
        order_links = self.wait.until(EC.presence_of_all_elements_located(self.ORDER_LINKS))
        order_links[index].click()

    @allure.step("Count the total quantity of items in the order")
    def count_order_items_quantity(self):
        order_items_elements = self.wait.until(EC.presence_of_all_elements_located(self.ORDER_ITEMS))
        total_quantity = 0
        for item in order_items_elements:
            try:
                quantity_text = item.find_element(By.XPATH, ".//div[@class='item-quantity']").text.strip()
                if not quantity_text:
                    allure.attach(item.get_attribute('outerHTML'), name="Item HTML with Empty Quantity",
                                  attachment_type=allure.attachment_type.HTML)
                    continue  # Skip items with empty quantity text
                match = re.search(r'\d+', quantity_text)
                if match:
                    quantity = int(match.group())
                else:
                    allure.attach(quantity_text, name="Unmatched Quantity Text",
                                  attachment_type=allure.attachment_type.TEXT)
                    continue  # Skip items where quantity text does not contain a number
                total_quantity += quantity
            except Exception as e:
                allure.attach(item.get_attribute('outerHTML'), name="Item HTML on Exception",
                              attachment_type=allure.attachment_type.HTML)
                allure.attach(str(e), name="Exception Message", attachment_type=allure.attachment_type.TEXT)
                continue  # Skip items where an exception occurred
        allure.attach(str(total_quantity), name="Total Quantity of Items in Order",
                      attachment_type=allure.attachment_type.TEXT)
        print(f"Total quantity of items in order: {total_quantity}")
        return total_quantity

    @allure.step("Get order status")
    def get_order_status(self):
        try:
            if self.wait.until(EC.presence_of_element_located(self.NEW_ORDER_SATUS)):
                return "New"
        except:
            pass
        try:
            if self.wait.until(EC.presence_of_element_located(self.READY_FOR_PICKUP_ORDER_STATUS)):
                return "Ready for Pickup"
        except:
            pass
        try:
            if self.wait.until(EC.presence_of_element_located(self.DONE_ORDER_STATUS)):
                return "Done"
        except:
            pass
        try:
            if self.wait.until(EC.presence_of_element_located(self.CANCELLED_ORDER_STATUS)):
                return "Cancelled"
        except:
            pass
        return None

    @allure.step("Click edit button if present")
    def click_edit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_ORDER)).click()

    @allure.step("Delete item by index {index}")
    def delete_item_by_index(self, index):
        delete_buttons = self.wait.until(EC.presence_of_all_elements_located(self.DELETE_ITEM_BUTTON))
        delete_buttons[index].click()

    @allure.step("Confirm item deletion")
    def confirm_item_deletion(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_ITEM_DELETION)).click()

