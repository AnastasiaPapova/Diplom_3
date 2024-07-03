import allure
import pytest

import conftest
from conftest import pages, login, driver
from locators.burger_locators import OrdersLocators


class TestCreateOrder:
    @allure.title('Проверка появления всплывающего окна с деталями при клике на заказ')
    def test_get_order_popup(self, pages):
        pages.click_orders_list()
        pages.click_order()
        assert pages.check_order_structure() == True

    @allure.title('Проверка отображения заказа')
    def test_find_order_in_list(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.check_show_window_with_order_id()
        order_number = pages.get_with_order_id()
        pages.click_close_modal_order()
        pages.click_on_account()
        pages.click_order_history_button()
        is_order_id_found_at_history = pages.is_order_id_found_at_history(order_number)
        pages.click_orders_list()
        is_order_id_found_at_feed = pages.is_order_id_found_at_feed(order_number)
        assert is_order_id_found_at_history and is_order_id_found_at_feed, "Заказы в истории и в ленте не совпадают"

    @allure.title('Проверка отображения номера заказа в разделе "В работе')
    def test_new_order_appears_in_work_list(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        order_number = pages.get_with_order_id()
        pages.click_close_modal_order()
        pages.click_orders_list()
        order_number_refactor = pages.get_user_order(order_number)
        order_in_progress = pages.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress

    @allure.title('При создании заказа, происходит изменение значения счетчиков заказов')
    @pytest.mark.parametrize('counter', [OrdersLocators.TOTAL_ORDER_COUNT, OrdersLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, pages, login, counter):
        pages.click_orders_list()
        prev_counter_value = pages.get_total_order_count_daily(counter)
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_modal_order()
        pages.click_orders_list()
        current_counter_value = pages.get_total_order_count_daily(counter)
        assert current_counter_value > prev_counter_value, "Заказ не создался, counter не сработал"


