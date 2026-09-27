from pages.base_page import BasePage
from locators import OrderFeedPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re


class OrderFeedPage(BasePage):
    def open_order_feed(self):
        self.open("/feed")

    def wait_for_feed_loaded(self):
        self.wait_for_element_present(OrderFeedPageLocators.FEED_HEADER)

    def click_first_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderFeedPageLocators.ORDER_LINKS)
        )
        order_links = self.driver.find_elements(*OrderFeedPageLocators.ORDER_LINKS)

        assert len(order_links) > 0, "Список заказов пуст, нечего кликать!"

        first_order_link = order_links[0]
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(first_order_link)
        )
        first_order_link.click()

    def click_order(self, index=0):
        orders = self.find_elements(OrderFeedPageLocators.ORDER_ITEMS)
        if orders and len(orders) > index:
            orders[index].click()

    def is_order_modal_opened(self, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_MODAL_CONTAINER)
            )
            return True
        except TimeoutException:
            return False

    def is_order_modal_visible(self):
        try:
            self.find_element(OrderFeedPageLocators.ORDER_MODAL, timeout=5)
            return True
        except:
            return False

    def close_order_modal(self):
        self.click_element(OrderFeedPageLocators.ORDER_MODAL_CLOSE)

    def get_in_progress_order(self):
        try:
            element = self.find_element(OrderFeedPageLocators.FIRST_IN_PROGRESS_ORDER)
            return int(element.text)
        except:
            return 0

    def get_total_done_count(self):
        element = self.find_element(OrderFeedPageLocators.TOTAL_DONE_COUNTER)
        return int(element.text)

    def get_today_done_count(self):
        try:
            element = self.find_element(OrderFeedPageLocators.TODAY_DONE_COUNTER)
            return int(element.text)
        except:
            return 0

    def is_order_present_in_feed(self, order_id: str) -> bool:
        locator = (By.XPATH, f"//*[contains(., '#{order_id}')] | //*[contains(., '{order_id}')]")
        order_element = self.wait_for_element_present(locator)
        return order_element.is_displayed()

    def get_order_numbers_in_feed(self):
        orders = self.find_elements(OrderFeedPageLocators.ORDER_ITEMS)
        numbers = []
        for order in orders:
            text = order.text
            match = re.search(r'#(\d+)', text)
            if match:
                numbers.append(match.group(1))
        return numbers

    def wait_for_new_order(self, old_count, timeout=30):
        import time
        start = time.time()
        while time.time() - start < timeout:
            current_count = len(self.find_elements(OrderFeedPageLocators.ORDER_ITEMS))
            if current_count > old_count:
                return True
        return False