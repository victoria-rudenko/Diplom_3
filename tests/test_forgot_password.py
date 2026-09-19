import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


class TestForgotPassword:
    """Тесты восстановления пароля"""

    def test_forgot_password_link_click(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_forgot_password()
        forgot_page = ForgotPasswordPage(driver)
        assert forgot_page.is_on_forgot_password_page(), "Не удалось перейти на страницу восстановления пароля"

    def test_enter_email_and_click_restore(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_forgot_password_page()
        test_email = "test@example.com"
        forgot_page.enter_email(test_email)
        forgot_page.click_restore()
        login_page = LoginPage(driver)
        assert login_page.is_reset_password_page(), "Не произошел редирект на страницу подтверждения после восстановления пароля"

    def test_show_hide_password_makes_field_active(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_show_password()
        is_active = login_page.is_password_field_active()
        assert is_active, "Поле пароля не стало активным после клика по иконке глаза"