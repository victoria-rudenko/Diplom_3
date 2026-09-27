from pages.base_page import BasePage
from locators import ForgotPasswordPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ForgotPasswordPage(BasePage):
    def open_forgot_password_page(self):
        self.open("/forgot-password")

    def enter_email(self, email):
        email_input = self.find_element(ForgotPasswordPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def click_restore(self):
        self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)

    def click_login_link(self):
        self.click_element(ForgotPasswordPageLocators.LOGIN_LINK)

    def enter_password(self, password):
        password_input = self.find_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_show_password(self):
        password_input = self.find_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
        try:
            show_password = password_input.find_element(ForgotPasswordPageLocators.SHOW_PASSWORD_ICON)
            show_password.click()
        except:
            password_container = self.find_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
            password_container.click()

    def is_password_field_active(self):
        try:
            password_input = self.find_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
            parent = password_input.find_element(ForgotPasswordPageLocators.PASSWORD_PARENT)
            class_name = parent.get_attribute("class")
            return "active" in class_name
        except:
            return False

    def is_on_forgot_password_page(self, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains("/forgot-password")
            )
            return True
        except TimeoutException:
            return False

    def is_on_login_page(self):
        return "/login" in self.get_current_url()

    def is_success_message_displayed(self):
        try:
            self.find_element(ForgotPasswordPageLocators.SUCCESS_MESSAGE)
            return True
        except:
            return False