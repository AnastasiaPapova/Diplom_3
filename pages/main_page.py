import allure
import time

from locators.burger_locators import MainPageLocators, LoginLocators, OrdersLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Перейти в "ЛК" по кнопке "Личный кабинет"')
    def click_on_account(self):
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Переход на страницу Лента заказов')
    def click_orders_list(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_until_element_visibility(OrdersLocators.ORDERS_LIST_HEADER)

    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_until_element_visibility(MainPageLocators.MAIN_PAGE_HEADER)

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BURGER_INGREDIENT_BUTTON)
        self.click_on_element(MainPageLocators.BURGER_INGREDIENT_BUTTON)

    @allure.step('Проверка наличия деталей ингредиентов на экране')
    def check_displayed_ingredient_details(self) -> bool:
        return self.check_presence(MainPageLocators.BURGER_INGREDIENT_DETAILS).is_displayed()

    @allure.step('Проверка всплывающего окна с деталями игридиента')
    def check_show_window_with_details(self):
        self.wait_until_element_visibility(MainPageLocators.BURGER_INGREDIENT_DETAILS)
        return self.get_actually_text(MainPageLocators.BURGER_INGREDIENT_DETAILS)

    @allure.step('Закрытие попапа')
    def click_cross_button(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step('Проверка скрытости деталей ингредиентов')
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.BURGER_INGREDIENT_DETAILS)

    @allure.step('Получение значения счетчика ингредиента')
    def get_count_value(self):
        return self.get_actually_text(MainPageLocators.BURGER_INGREDIENT_COUNTER)

    @allure.step('Добавить ингридиент в заказ')
    def add_filling_to_order(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BURGER_INGREDIENT_BUTTON)
        self.drag_and_drop_element(MainPageLocators.BURGER_INGREDIENT_BUTTON,
                                   MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверка оформления заказа и его идентификатора')
    def check_show_window_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_CREATE_IDENTIFICATE)
        return self.get_actually_text(MainPageLocators.ORDER_CREATE_IDENTIFICATE)

    @allure.step('Проверка начала готовности заказа')
    def check_displayed_order_status_text(self) -> bool:
        return self.check_presence(MainPageLocators.ORDER_STATUS_INFO).is_displayed()

    @allure.step('Получение ORDER_ID')
    def get_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_CREATE_IDENTIFICATE)
        # self.wait_until_element_visibility(MainPageLocators.ORDER_ID)
        order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        return f"{order_id}"

    @allure.step("Проверка открытия модального окна")
    def modal_box_is_open(self):
        if self.wait_until_element_visibility(MainPageLocators.BURGER_INGREDIENT_DETAILS):
            return True

    @allure.step("Закрыть модальное окно после создания заказа")
    def click_close_modal_order(self):
        self.wait_until_element_visibility(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_BUTTON)
