import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:
    """Тесты раздела Лента заказов"""

    TEST_EMAIL = "test@stellarburgers.com"
    TEST_PASSWORD = "testpass123"


    def test_order_click_opens_modal(self, driver):
        # Проверка что при клике на заказ открывается всплывающее окно
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed()
        feed_page.click_first_order()

        assert feed_page.is_order_modal_opened(), "Модальное окно заказа не открылось"


    def test_user_orders_in_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_bun_to_constructor()
        main_page.click_order_button()
        order_id = main_page.get_order_id()
        main_page.close_modal()
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed()
        feed_page.wait_for_feed_loaded()
        is_order_displayed = feed_page.is_order_present_in_feed(order_id)

        assert is_order_displayed, f"Заказ с номером {order_id} не отображается на экране ленты заказов"


    def test_total_done_counter_increases(self, driver):
        #Проверка что при создании нового заказа счётчик 'Выполнено за всё время' увеличивается
        login_page = LoginPage(driver)
        login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed()
        total_before = feed_page.get_total_done_count()
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_bun_to_constructor()
        main_page.click_order_button()
        feed_page.open_order_feed()
        feed_page.wait_for_feed_loaded()
        total_after = feed_page.get_total_done_count()

        assert total_after > total_before, \
            f"Счётчик 'Выполнено за всё время' не увеличился. Было: {total_before}, стало: {total_after}"



    def test_today_done_counter_increases(self, driver):
        # Проверка что при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается
        login_page = LoginPage(driver)
        login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed()
        today_before = feed_page.get_today_done_count()
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_bun_to_constructor()
        main_page.click_order_button()
        feed_page.open_order_feed()
        feed_page.wait_for_feed_loaded()
        today_after = feed_page.get_today_done_count()

        assert today_after > today_before, \
            f"Счётчик 'Выполнено за сегодня' не увеличился. Было: {today_before}, стало: {today_after}"


    def test_new_order_in_progress(self, driver):
        # Проверка что после оформления заказа его номер появляется в разделе 'В работе'
        login_page = LoginPage(driver)
        login_page.login(self.TEST_EMAIL, self.TEST_PASSWORD)
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.add_bun_to_constructor()
        main_page.click_order_button()
        order_id = main_page.get_order_id()
        main_page.close_modal()
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed()
        feed_page.wait_for_feed_loaded()
        in_progress_order = feed_page.get_in_progress_order()

        assert in_progress_order == order_id, f"Заказ {order_id} не найден в разделе 'В работе'"