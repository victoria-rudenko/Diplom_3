from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url=""):
        self.driver.get(f"{self.BASE_URL}{url}")

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_change(self, expected_url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(expected_url_part)
        )

    def wait_for_element_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

    def execute_js(self, script, *args):
        self.driver.execute_script(script, *args)

    def close_modal_by_esc(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)