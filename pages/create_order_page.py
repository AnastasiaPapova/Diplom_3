import allure

from locators.burger_locators import OrdersLocators
from pages.base_page import BasePage


class CreateOrderPage(BasePage):
    @allure.step('Нажатие на заказ в списке Лента заказов')
    def click_order(self):
        self.click_on_element(OrdersLocators.ORDER_HISTORY_LINK)

    @allure.step('Проверка отображения состава')
    def check_order_structure(self):
        return self.check_presence(OrdersLocators.ORDER_ELEMENTS).is_displayed()

    @allure.step("Проверка совпадения заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Проверка идентификатора заказа в ленте")
    def is_order_id_found_at_feed(self, order_number):
        return self.check_order_id(order_number, OrdersLocators.ALL_ORDERS_IN_FEED)

    @allure.step("Проверка идентификатора заказа в истории")
    def is_order_id_found_at_history(self, order_number):
        return self.check_order_id(order_number, OrdersLocators.ALL_ORDERS_IN_HISTORY)

    @allure.step('Переход на страницу Лента заказов')
    def click_orders_list(self):
        self.move_to_element_and_click(OrdersLocators.ORDER_FEED_BUTTON)
        self.wait_until_element_visibility(OrdersLocators.ORDERS_LIST_HEADER)

    @allure.step("Получение количества заказов")
    def get_total_order_count_daily(self, locator):
        BasePage.wait_for_element_to_be_clickable(locator)
        return self.get_actually_text(locator)

    @allure.step('Получение номер заказа')
    def get_user_order(self, orders_numbers):
        order_refactor = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(OrdersLocators.NUMBER_IN_PROGRESS, order_refactor)
        return order_refactor

    @allure.step('Получение номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_actually_text(OrdersLocators.NUMBER_IN_PROGRESS)