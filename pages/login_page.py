from pages.base_page import BasePage
from locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    def open_login_page(self):
        self.open("/login")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        self._close_modal_if_exists()

    def is_login_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/login")
            )
            return True
        except TimeoutException:
            return False

    def _close_modal_if_exists(self):
        try:
            close_btn = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(LoginPageLocators.MODAL_CLOSE_BUTTON)
            )
            close_btn.click()
        except:
            try:
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            except:
                pass

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(email_field).click().perform()
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(password_field).click().perform()

        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(login_btn).click().perform()

    def login(self, email, password):
        self.open_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        WebDriverWait(self.driver, 15).until(
            lambda driver: "/login" not in driver.current_url,
            message="Не удалось уйти со страницы /login после нажатия 'Войти'"
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.ACCOUNT_LINK),
            message="После логина не появилась ссылка 'Личный Кабинет'"
        )


    def is_reset_password_page(self, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains("/reset-password")
            )
            return True
        except TimeoutException:
            return False

    def click_show_password(self):
        show_password_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.SHOW_PASSWORD_ICON)
        )
        show_password_icon.click()

    def is_password_field_active(self) -> bool:
        try:
            label_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(LoginPageLocators.LABEL)
            )
            class_name = label_element.get_attribute("class")
            return "input__placeholder-focused" in class_name
        except Exception:
            return False

    def click_forgot_password(self):
        forgot_password_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)
        )
        forgot_password_link.click()