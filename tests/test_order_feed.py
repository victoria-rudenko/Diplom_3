import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    """Тесты раздела Лента заказов"""

    TEST_EMAIL = "test@stellarburgers.com"
    TEST_PASSWORD = "testpass123"

    @allure.story("Просмотр деталей заказа")
    @allure.title("Проверка открытия модального окна заказа при клике на него в ленте")
    def test_order_click_opens_modal(self, driver):
        with allure.step("Открываем страницу Ленты заказов"):
            feed_page = OrderFeedPage(driver)
            feed_page.open_order_feed()

        with allure.step("Кликаем на первый заказ в ленте"):
            feed_page.click_first_order()

        with allure.step("Проверяем, что модальное окно заказа открылось"):
            assert feed_page.is_order_modal_opened(), "Модальное окно заказа не открылось"

    @allure.story("Отображение заказов пользователя")
    @allure.title("Проверка отображения только что созданного заказа в общей ленте")
    def test_user_orders_in_feed(self, driver):
        with allure.step(f"Авторизуемся под тестовым пользователем ({self.TEST_EMAIL})"):
            login_page = LoginPage(driver)
            login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)

        with allure.step("Создаем новый заказ на главной странице"):
            main_page = MainPage(driver)
            main_page.open_main_page()
            main_page.add_bun_to_constructor()
            main_page.click_order_button()
            order_id = main_page.get_order_id()
            main_page.close_modal()

        with allure.step("Переходим в Ленту заказов и ожидаем её загрузки"):
            feed_page = OrderFeedPage(driver)
            feed_page.open_order_feed()
            feed_page.wait_for_feed_loaded()

        with allure.step(f"Проверяем, что заказ с номером {order_id} присутствует в ленте"):
            is_order_displayed = feed_page.is_order_present_in_feed(order_id)
            assert is_order_displayed, f"Заказ с номером {order_id} не отображается на экране ленты заказов"

    @allure.story("Статистика заказов")
    @allure.title("Проверка увеличения счетчика 'Выполнено за всё время' при создании заказа")
    def test_total_done_counter_increases(self, driver):
        with allure.step("Авторизуемся и переходим в Ленту заказов"):
            login_page = LoginPage(driver)
            login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)
            feed_page = OrderFeedPage(driver)
            feed_page.open_order_feed()

        with allure.step("Фиксируем начальное значение счетчика 'Выполнено за всё время'"):
            total_before = feed_page.get_total_done_count()

        with allure.step("Создаем новый заказ"):
            main_page = MainPage(driver)
            main_page.open_main_page()
            main_page.add_bun_to_constructor()
            main_page.click_order_button()

        with allure.step("Возвращаемся в Ленту заказов и ожидаем обновления"):
            feed_page.open_order_feed()
            feed_page.wait_for_feed_loaded()

        with allure.step("Проверяем, что счетчик 'Выполнено за всё время' увеличился"):
            total_after = feed_page.get_total_done_count()
            assert total_after > total_before, \
                f"Счётчик 'Выполнено за всё время' не увеличился. Было: {total_before}, стало: {total_after}"

    @allure.story("Статистика заказов")
    @allure.title("Проверка увеличения счетчика 'Выполнено за сегодня' при создании заказа")
    def test_today_done_counter_increases(self, driver):
        with allure.step("Авторизуемся и переходим в Ленту заказов"):
            login_page = LoginPage(driver)
            login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)
            feed_page = OrderFeedPage(driver)
            feed_page.open_order_feed()

        with allure.step("Фиксируем начальное значение счетчика 'Выполнено за сегодня'"):
            today_before = feed_page.get_today_done_count()

        with allure.step("Создаем новый заказ"):
            main_page = MainPage(driver)
            main_page.open_main_page()
            main_page.add_bun_to_constructor()
            main_page.click_order_button()

        with allure.step("Возвращаемся в Ленту заказов и ожидаем обновления"):
            feed_page.open_order_feed()
            feed_page.wait_for_feed_loaded()

        with allure.step("Проверяем, что счетчик 'Выполнено за сегодня' увеличился"):
            today_after = feed_page.get_today_done_count()
            assert today_after > today_before, \
                f"Счётчик 'Выполнено за сегодня' не увеличился. Было: {today_before}, стало: {today_after}"

    @allure.story("Статусы заказов")
    @allure.title("Проверка появления нового заказа в разделе 'В работе'")
    def test_new_order_in_progress(self, driver):
        with allure.step("Авторизуемся и создаем новый заказ"):
            login_page = LoginPage(driver)
            login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)
            main_page = MainPage(driver)
            main_page.open_main_page()
            main_page.add_bun_to_constructor()
            main_page.click_order_button()
            order_id = main_page.get_order_id()
            main_page.close_modal()

        with allure.step("Переходим в Ленту заказов и ожидаем её загрузки"):
            feed_page = OrderFeedPage(driver)
            feed_page.open_order_feed()
            feed_page.wait_for_feed_loaded()

        with allure.step("Проверяем, что номер созданного заказа отображается в разделе 'В работе'"):
            in_progress_order = feed_page.get_in_progress_order()
            assert in_progress_order == order_id, f"Заказ {order_id} не найден в разделе 'В работе'"