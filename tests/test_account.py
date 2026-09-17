import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TestAccount:
    TEST_EMAIL = "test@stellarburgers.com"
    TEST_PASSWORD = "testpass123"

    def test_login_page_click(self, driver):
        main_page = MainPage(driver)
        main_page.open("/")
        main_page.click_login_button()

        login_page = LoginPage(driver)
        assert login_page.is_login_page(), f"Не попали на логин. URL: {driver.current_url}"

    def test_order_history_navigation(self, driver):
        # Логинимся
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)

        # Кликаем "Личный Кабинет"
        main_page = MainPage(driver)
        main_page.click_account_link()

        # Кликаем "История заказов"
        account_page = AccountPage(driver)
        account_page.click_order_history()

        assert account_page.is_on_order_history_page(), f"Не попали в историю. URL: {driver.current_url}"

    def test_logout(self, driver):
        # Логинимся
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)

        # Идем в Личный Кабинет
        main_page = MainPage(driver)
        main_page.click_account_link()

        # Нажимаем Выход
        account_page = AccountPage(driver)
        account_page.click_logout()

        assert "/profile" not in driver.current_url, f"Мы всё еще в профиле после выхода! URL: {driver.current_url}"