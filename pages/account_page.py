import re
from pages.base_page import BasePage
from locators import AccountPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AccountPage(BasePage):
    def click_profile(self):
        self.click_element(AccountPageLocators.PROFILE_LINK)

    def click_order_history(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY_LINK)

    def click_logout(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        WebDriverWait(self.driver, 10).until(
            lambda driver: "/profile" not in driver.current_url,
            message="После нажатия 'Выход' не произошел редирект со страницы профиля"
        )

    def click_login(self):
        self.click_element(AccountPageLocators.LOGIN_LINK)

    def is_on_account_page(self):
        url = self.get_current_url()
        return "/account" in url and "/order-history" not in url and "/orders" not in url

    def is_on_order_history_page(self):
        url = self.get_current_url()
        return "/account/order-history" in url

    def get_order_history_items(self):
        try:
            return self.find_elements(AccountPageLocators.ORDER_HISTORY_ITEMS)
        except Exception:
            return []

    def get_first_order_number(self):
        items = self.get_order_history_items()
        if items:
            text = items[0].text
            match = re.search(r'#(\d+)', text)
            if match:
                return match.group(1)
        return None

    def wait_for_redirect_to_login(self, timeout=10):
        self.wait_for_url_change("/login", timeout)