import allure
from conftest import driver
from pages.create_order_page import CreateOrderPage
from pages.main_page import MainPage
from pages.login_user_page import LoginUserPage
from main_data.urls import Urls


class TestMainPage:

    @allure.title('Переход на страницу заказов при нажатии в header «Лента заказов»')
    def test_redirection_to_order_list(self, driver):
        order_page = CreateOrderPage(driver)
        order_page.click_orders_list()
        current_url = order_page.get_current_url()
        assert current_url == Urls.feed_page_url

    @allure.title('Переход на страницу сбора бургера при нажатии кнопки "Конструктор"')
    def test_go_to_constructor(self, driver):
        order_page = CreateOrderPage(driver)
        main_page = MainPage(driver)
        order_page.click_orders_list()
        main_page.click_constructor_button()
        current_url = order_page.get_current_url()
        assert current_url == Urls.main_page_url

    @allure.title('При нажатии на ингридиент всплывает окно с информаций')
    def test_popup_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        actually_text = main_page.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    @allure.title('Закрытие окна при нажатии крестика в модальном окне')
    def test_close_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.click_cross_button()
        main_page.invisibility_ingredient_details()
        assert main_page.check_displayed_ingredient_details() == False

    @allure.title('После добавления ингридиента счетчик ингридента сменился')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        prev_counter_value = main_page.get_count_value()
        main_page.add_filling_to_order()
        actual_value = main_page.get_count_value()
        assert actual_value > prev_counter_value

    @allure.title('Проверка возможности оформления заказ авторизованным пользователем')
    def test_successful_order(self, driver):
        login_user = LoginUserPage(driver)
        login_user.login()
        main_page = MainPage(driver)
        main_page.add_filling_to_order()
        main_page.click_order_button()
        actually_text = main_page.check_show_window_with_order_id()
        assert actually_text == "идентификатор заказа" and main_page.check_displayed_order_status_text() == True