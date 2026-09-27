from pages.base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


class MainPage(BasePage):
    def open_main_page(self):
        self.open("/")

    def click_account_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ACCOUNT_HEADER_LINK)
        )
        element.click()

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_LINK)

    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)

    def is_constructor_header_visible(self):
        element = self.find_element(MainPageLocators.CONSTRUCT_BURGER_HEADER)
        if element:
            return True
        else:
            return False

    def click_ingredient(self, ingredient_type="bun", index=0):
        if ingredient_type == "bun":
            elements = self.find_elements(MainPageLocators.BUN_ITEMS)
        elif ingredient_type == "sauce":
            elements = self.find_elements(MainPageLocators.SAUCE_ITEMS)
        elif ingredient_type == "filling":
            elements = self.find_elements(MainPageLocators.FILLING_ITEMS)
        else:
            elements = self.find_elements(MainPageLocators.BUN_ITEMS)

        if elements and len(elements) > index:
            elements[index].click()

    def is_ingredient_modal_visible(self):
        if self.find_element(MainPageLocators.INGREDIENT_MODAL_HEADING, timeout=5).is_displayed():
            return True
        else:
            return False

    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.INGREDIENT_MODAL_CLOSE)

    def get_ingredient_counter(self, ingredient_type="bun", index=0):
        if ingredient_type == "bun":
            elements = self.find_elements(MainPageLocators.BUN_ITEMS)
        elif ingredient_type == "sauce":
            elements = self.find_elements(MainPageLocators.SAUCE_ITEMS)
        elif ingredient_type == "filling":
            elements = self.find_elements(MainPageLocators.FILLING_ITEMS)
        else:
            elements = self.find_elements(MainPageLocators.BUN_ITEMS)

        if elements and len(elements) > index:
            counter = elements[index].find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        return 0

    def add_ingredient_to_order(self, ingredient_type="bun", index=0):
        self.click_ingredient(ingredient_type, index)

    def get_orders_in_progress_count(self):
        try:
            element = self.find_element(MainPageLocators.ORDERS_IN_PROGRESS)
            return int(element.text)
        except:
            return 0

    def get_total_done_count(self):
        try:
            element = self.find_element(MainPageLocators.TOTAL_ORDERS_DONE)
            return int(element.text)
        except:
            return 0

    def get_today_done_count(self):
        try:
            element = self.find_element(MainPageLocators.TODAY_ORDERS_DONE)
            return int(element.text)
        except:
            return 0

    def add_bun_to_constructor(self):
        source = self.wait_for_element_present(MainPageLocators.BUN_INGREDIENT)
        target = self.wait_for_element_present(MainPageLocators.CONSTRUCTOR_TOP_ZONE)

        self.scroll_into_view(target)

        js_dnd = """
        function simulateDragDrop(sourceNode, destinationNode) {
            var event = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer: new DataTransfer() });
            sourceNode.dispatchEvent(event);
            var dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer: event.dataTransfer });
            destinationNode.dispatchEvent(dropEvent);
            var dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer: event.dataTransfer });
            sourceNode.dispatchEvent(dragEndEvent);
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.execute_js(js_dnd, source, target)

    def click_order_button(self):
        order_button = self.wait_for_element_clickable(MainPageLocators.ORDER_BUTTON)
        order_button.click()

    def get_order_id(self):
        modal_element = self.wait_for_element_present(MainPageLocators.ORDER_ID_MODAL_TEXT)
        parent_text = modal_element.find_element(By.XPATH, "..").text
        match = re.search(r'(\d+)', parent_text)
        order_id = match.group(1) if match else None

        assert order_id is not None, "Не удалось извлечь номер заказа из модального окна"
        return int(order_id)

    def is_order_created(self):
        try:
            self.find_element(MainPageLocators.ORDER_MODAL, timeout=5)
            return True
        except:
            return False

    def close_modal(self):
        self.close_modal_by_esc()