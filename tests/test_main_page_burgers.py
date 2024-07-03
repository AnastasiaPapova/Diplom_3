import allure
from conftest import pages, login
from main_data.urls import Urls


class TestMainPage:

    @allure.title('Переход на страницу заказов при нажатии в header «Лента заказов»')
    def test_redirection_to_order_list(self, pages):
        pages.click_orders_list()
        current_url = pages.get_current_url()
        assert current_url == Urls.feed_page_url

    @allure.title('Переход на страницу сбора бургера при нажатии кнопки "Конструктор"')
    def test_go_to_constructor(self, pages):
        pages.click_orders_list()
        pages.click_constructor_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.main_page_url

    @allure.title('При нажатии на ингридиент всплывает окно с информаций')
    def test_popup_of_ingredient(self, pages):
        pages.click_on_ingredient()
        actually_text = pages.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    @allure.title('Закрытие окна при нажатии крестика в модальном окне')
    def test_close_ingredient_details_window(self, pages):
        pages.click_on_ingredient()
        pages.click_cross_button()
        pages.invisibility_ingredient_details()
        assert pages.check_displayed_ingredient_details() == False

    @allure.title('После добавления ингридиента счетчик ингридента сменился')
    def test_ingredient_counter(self, pages):
        prev_counter_value = pages.get_count_value()
        pages.add_filling_to_order()
        actual_value = pages.get_count_value()
        assert actual_value > prev_counter_value

    @allure.title('Проверка возможности оформления заказ авторизованным пользователем')
    def test_successful_order(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        actually_text = pages.check_show_window_with_order_id()
        assert actually_text == "идентификатор заказа" and pages.check_displayed_order_status_text() == True