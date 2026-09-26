import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@allure.feature("Личный кабинет пользователя")
class TestAccount:
    TEST_EMAIL = "test@stellarburgers.com"
    TEST_PASSWORD = "testpass123"

    @allure.story("Авторизация")
    @allure.title("Проверка перехода на страницу логина по кнопке")
    def test_login_page_click(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open("/")

        with allure.step("Нажимаем Личный Кабинет"):
            main_page.click_account_link()

        login_page = LoginPage(driver)
        with allure.step("Проверяем, что текущий URL соответствует странице логина"):
            assert login_page.is_login_page(), f"Не попали на логин. URL: {driver.current_url}"

    @allure.story("История заказов")
    @allure.title("Проверка навигации в историю заказов из аккаунта")
    def test_order_history_navigation(self, driver):
        with allure.step("Выполняем вход в систему"):
            login_page = LoginPage(driver)
            login_page.open_login_page()
            login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)

        with allure.step("Переходим в личный кабинет"):
            main_page = MainPage(driver)
            main_page.click_account_link()

        with allure.step("Нажимаем на ссылку 'История заказов'"):
            account_page = AccountPage(driver)
            account_page.click_order_history()

        with allure.step("Проверяем, что мы на странице истории заказов"):
            assert account_page.is_on_order_history_page(), f"Не попали в историю. URL: {driver.current_url}"

    @allure.story("Выход из системы")
    @allure.title("Проверка корректного выхода из личного кабинета")
    def test_logout(self, driver):
        with allure.step("Выполняем вход в систему"):
            login_page = LoginPage(driver)
            login_page.open_login_page()
            login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)

        with allure.step("Переходим в личный кабинет и нажимаем 'Выход'"):
            main_page = MainPage(driver)
            main_page.click_account_link()
            account_page = AccountPage(driver)
            account_page.click_logout()

        with allure.step("Проверяем, что URL больше не содержит /profile"):
            assert "/profile" not in driver.current_url, f"Мы всё еще в профиле после выхода! URL: {driver.current_url}"