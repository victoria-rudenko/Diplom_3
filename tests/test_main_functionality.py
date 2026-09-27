import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.feature("Основной функционал приложения")
class TestMainFunctionality:
    """Проверка основного функционала"""

    TEST_EMAIL = "test@stellarburgers.com"
    TEST_PASSWORD = "testpass123"

    @allure.story("Навигация")
    @allure.title("Проверка перехода на страницу Конструктора")
    def test_constructor_link_click(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем на ссылку 'Конструктор'"):
            main_page.click_constructor()

        with allure.step("Проверяем, что открылась страница Конструктора (виден заголовок)"):
            assert main_page.is_constructor_header_visible(), \
                "Не открылась страница Конструктор по клику на Конструктор"

    @allure.story("Навигация")
    @allure.title("Проверка перехода в Ленту заказов")
    def test_order_feed_link_click(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем на ссылку 'Лента заказов'"):
            main_page.click_order_feed()

        with allure.step("Проверяем, что URL содержит '/feed'"):
            current_url = main_page.get_current_url()
            assert "/feed" in current_url, "Не удалось перейти в Ленту заказов"

    @allure.story("Модальные окна ингредиентов")
    @allure.title("Проверка открытия модального окна ингредиента при клике")
    def test_ingredient_click_opens_modal(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Кликаем на карточку ингредиента"):
            main_page.click_ingredient()

        with allure.step("Проверяем, что модальное окно ингредиента отображается"):
            assert main_page.is_ingredient_modal_visible(), "Модальное окно ингредиента не появилось"

    @allure.story("Модальные окна ингредиентов")
    @allure.title("Проверка закрытия модального окна ингредиента по клику на крестик")
    def test_ingredient_modal_close(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Открываем модальное окно ингредиента"):
            main_page.click_ingredient()

        with allure.step("Закрываем модальное окно кликом по крестику"):
            main_page.close_ingredient_modal()

        with allure.step("Проверяем, что модальное окно больше не видимо"):
            assert not main_page.is_ingredient_modal_visible(), \
                "Модальное окно не закрылось после клика по крестику"

    @allure.story("Работа с конструктором")
    @allure.title("Проверка увеличения счетчика ингредиентов при добавлении булочки")
    def test_ingredient_counter_increases(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Фиксируем начальное значение счетчика"):
            counter_before = 0

        with allure.step("Добавляем булочку в конструктор"):
            main_page.add_bun_to_constructor()

        with allure.step("Получаем новое значение счетчика"):
            counter_after = main_page.get_ingredient_counter()

        with allure.step("Проверяем, что счетчик увеличился на 2 (верхняя и нижняя часть булки)"):
            assert counter_after == counter_before + 2, \
                f"Счётчик не увеличился. Было: {counter_before}, стало: {counter_after}"

    @allure.story("Оформление заказа")
    @allure.title("Проверка успешного создания заказа авторизованным пользователем")
    def test_logged_in_user_can_create_order(self, driver):
        with allure.step(f"Авторизуемся с email: {self.TEST_EMAIL}"):
            login_page = LoginPage(driver)
            login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)

        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("Добавляем булочку в конструктор"):
            main_page.add_bun_to_constructor()

        with allure.step("Нажимаем кнопку 'Оформить заказ'"):
            main_page.click_order_button()

        with allure.step("Проверяем, что заказ успешно создан (появилось модальное окно успеха)"):
            assert main_page.is_order_created(), "Заказ не создан"