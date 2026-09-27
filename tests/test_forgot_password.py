import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.feature("Восстановление доступа")
class TestForgotPassword:
    """Тесты восстановления пароля"""

    @allure.story("Навигация")
    @allure.title("Проверка перехода на страницу восстановления пароля по ссылке")
    def test_forgot_password_link_click(self, driver):
        with allure.step("Открываем страницу логина"):
            login_page = LoginPage(driver)
            login_page.open_login_page()

        with allure.step("Нажимаем ссылку 'Забыли пароль'"):
            login_page.click_forgot_password()

        with allure.step("Проверяем, что открылась страница восстановления пароля"):
            forgot_page = ForgotPasswordPage(driver)
            assert forgot_page.is_on_forgot_password_page(), "Не удалось перейти на страницу восстановления пароля"

    @allure.story("Процесс восстановления")
    @allure.title("Проверка ввода email и редиректа после нажатия кнопки восстановления")
    def test_enter_email_and_click_restore(self, driver):
        test_email = "test@example.com"

        with allure.step("Открываем страницу восстановления пароля"):
            forgot_page = ForgotPasswordPage(driver)
            forgot_page.open_forgot_password_page()

        with allure.step(f"Вводим тестовый email: {test_email}"):
            forgot_page.enter_email(test_email)

        with allure.step("Нажимаем кнопку восстановления"):
            forgot_page.click_restore()

        with allure.step("Проверяем редирект на страницу подтверждения сброса пароля"):
            login_page = LoginPage(driver)
            assert login_page.is_reset_password_page(), "Не произошел редирект на страницу подтверждения после восстановления пароля"

    @allure.story("Интерфейс поля пароля")
    @allure.title("Проверка активации поля пароля при клике на иконку глаза")
    def test_show_hide_password_makes_field_active(self, driver):
        with allure.step("Открываем страницу логина"):
            login_page = LoginPage(driver)
            login_page.open_login_page()

        with allure.step("Нажимаем иконку показа пароля"):
            login_page.click_show_password()

        with allure.step("Проверяем, что поле пароля стало активным"):
            is_active = login_page.is_password_field_active()
            assert is_active, "Поле пароля не стало активным после клика по иконке глаза"