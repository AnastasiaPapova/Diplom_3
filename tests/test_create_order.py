import allure
import pytest
from pages.create_order_page import CreateOrderPage
from pages.user_profile_page import UserProfilePage
from pages.login_user_page import LoginUserPage
from pages.main_page import MainPage
from conftest import driver
from locators.burger_locators import OrdersLocators


class TestCreateOrder:
    @allure.title('Проверка появления всплывающего окна с деталями при клике на заказ')
    def test_get_order_popup(self, driver):
        order_page = CreateOrderPage(driver)
        order_page.click_orders_list()
        order_page.click_order()
        assert order_page.check_order_structure() == True

    @allure.title('Проверка отображения заказа')
    def test_find_order_in_list(self, driver):
        login_user = LoginUserPage(driver)
        login_user.login()
        order_page = CreateOrderPage(driver)
        user_page = UserProfilePage(driver)
        main_page = MainPage(driver)
        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.check_show_window_with_order_id()
        order_number = main_page.get_with_order_id()
        main_page.click_close_modal_order()
        main_page.click_on_account()
        user_page.click_order_history_button()
        is_order_id_found_at_history = order_page.is_order_id_found_at_history(order_number)
        order_page.click_orders_list()
        is_order_id_found_at_feed = order_page.is_order_id_found_at_feed(order_number)
        assert is_order_id_found_at_history and is_order_id_found_at_feed, "Заказы в истории и в ленте не совпадают"

    @allure.title('Проверка отображения номера заказа в разделе "В работе')
    def test_new_order_appears_in_work_list(self, driver):
        login_user = LoginUserPage(driver)
        login_user.login()
        main_page = MainPage(driver)
        main_page.add_filling_to_order()
        main_page.click_order_button()
        order_number = main_page.get_with_order_id()
        main_page.click_close_modal_order()
        order_page = CreateOrderPage(driver)
        order_page.click_orders_list()
        order_number_refactor = order_page.get_user_order(order_number)
        order_in_progress = order_page.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress

    @allure.title('При создании заказа, происходит изменение значения счетчиков заказов')
    @pytest.mark.parametrize('counter', [OrdersLocators.TOTAL_ORDER_COUNT, OrdersLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, driver, counter):
        login_user = LoginUserPage(driver)
        login_user.login()
        order_page = CreateOrderPage(driver)
        main_page = MainPage(driver)
        order_page.click_orders_list()
        prev_counter_value = order_page.get_total_order_count_daily(counter)
        main_page.click_constructor_button()
        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.click_close_modal_order()
        order_page.click_orders_list()
        current_counter_value = order_page.get_total_order_count_daily(counter)
        assert current_counter_value > prev_counter_value, "Заказ не создался, counter не сработал"


