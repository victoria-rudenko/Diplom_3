import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestMainFunctionality:
    """Проверка основного функционала"""

    TEST_EMAIL = "test@stellarburgers.com"
    TEST_PASSWORD = "testpass123"

    def test_constructor_link_click(self, driver):
        # Проверка перехода по клику на Конструктор
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_constructor()

        assert main_page.is_constructor_header_visible(), \
            "Не открылась страница Конструктор по клику на Конструктор"

    def test_order_feed_link_click(self, driver):
        # Проверка перехода по клику на Лента заказов
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed()

        assert "/feed" in driver.current_url, "Не удалось перейти в Ленту заказов"

    def test_ingredient_click_opens_modal(self, driver):
        # Проверка что при клике на ингредиент появляется всплывающее окно
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_visible(), "Модальное окно ингредиента не появилось"


    def test_ingredient_modal_close(self, driver):
        # Проверка что всплывающее окно закрывается кликом по крестику
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()
        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_visible(), \
            "Модальное окно не закрылось после клика по крестику"

    def test_ingredient_counter_increases(self, driver):
        # Проверка что при добавлении ингредиента увеличивается счётчик
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = 0
        main_page.add_bun_to_constructor()
        counter_after = main_page.get_ingredient_counter()

        # счётчик должен увеличиться на 2, т.к. булочек добавляется сразу 2
        assert counter_after == counter_before + 2, \
            f"Счётчик не увеличился. Было: {counter_before}, стало: {counter_after}"

    def test_logged_in_user_can_create_order(self, driver):
        # Проверка что залогиненный пользователь может оформить заказ
        login_page = LoginPage(driver)
        login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_bun_to_constructor()
        main_page.click_order_button()

        assert main_page.is_order_created(), "Заказ не создан"