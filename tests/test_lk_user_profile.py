import allure
from conftest import pages, login

from main_data.urls import Urls


class TestLKProfile:
    @allure.title('Переход в ЛК по клику на кнопку «Личный кабинет»')
    def test_go_to_account_from_header(self, pages, login):
        pages.click_on_account()
        current_url = pages.check_switch_on_profile()
        assert current_url == Urls.profile_page_url

    @allure.title('Переход в раздел История заказов по кнопке "История заказов"')
    def test_go_to_order_history(self, pages, login):
        pages.click_on_account()
        pages.click_order_history_button()
        current_url = pages.check_switch_to_order_history()
        assert current_url == Urls.account_order_history_page_url

    @allure.title('Переход на старницу авторизации при нажатии кнопки "Выход"')
    def test_logout(self, pages, login):
        pages.click_on_account()
        pages.click_log_out_button()
        current_url = pages.check_switch_to_login_page()
        assert current_url == Urls.login_page_url
