import time

import allure

from data import DataOrderFeed
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:

    @allure.title("Проверка клика на заказ, откроется всплывающее окно с деталями")
    def test_click_order_open_window_detail(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.main_page_loading_wait()
        order_feed.click_button_order_feed()
        order_feed.click_order()
        assert order_feed.check_text_popup_order(DataOrderFeed.TEXT_POPUP_ORDER_DETAIL)

    @allure.title("Проверка отображения заказа из истории заказов, в ленте заказов")
    def test_display_order_from_history_in_feed(self,login):
        order_feed = OrderFeedPage(login)
        order_feed.main_page_loading_wait()
        order_feed.click_button_personal_account()
        order_feed.click_history_order()
        order = order_feed.get_number_order()
        order_feed.click_button_order_feed()
        assert order_feed.find_order_in_feed(order)

    @allure.title('Проверка при создании нового заказа счетчик Выполнено за все время увеличивается')
    def test_count_all_orders(self, login):
        order_feed = OrderFeedPage(login)
        order_feed.main_page_loading_wait()
        order_feed.click_button_order_feed()
        order_all = order_feed.get_count_all_orders()
        order_feed.click_button_constructor()
        order_feed.put_ingredient_into_basket()
        order_feed.click_button_place_order()
        order_feed.main_page_loading_wait()
        order_feed.click_button_close_window_successful()
        order_feed.click_button_order_feed()
        order_feed.order_loading_wait()
        assert int(order_all) + 1 == order_feed.get_count_all_orders()

    @allure.title('Проверка при создании нового заказа счетчик Выполнено за все время увеличивается')
    def test_count_all_orders(self, login):
        order_feed = OrderFeedPage(login)
        order_feed.main_page_loading_wait()
        order_feed.click_button_order_feed()
        order_today = order_feed.get_count_today_orders()
        order_feed.click_button_constructor()
        order_feed.put_ingredient_into_basket()
        order_feed.click_button_place_order()
        order_feed.main_page_loading_wait()
        order_feed.click_button_close_window_successful()
        order_feed.click_button_order_feed()
        order_feed.order_loading_wait()
        assert int(order_today) + 1 == order_feed.get_count_today_orders()

    @allure.title('Проверка после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, login):
        order_feed = OrderFeedPage(login)
        order_feed.main_page_loading_wait()
        order_feed.put_ingredient_into_basket()
        order_feed.click_button_place_order()
        order_feed.main_page_loading_wait()
        order_number = order_feed.get_order_number()
        order_feed.click_button_close_window_successful()
        order_feed.click_button_order_feed()
        assert order_number == order_feed.get_order_in_work()


