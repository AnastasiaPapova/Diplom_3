import allure
from conftest import driver
from pages.login_user_page import LoginUserPage
from pages.main_page import MainPage
from pages.user_profile_page import UserProfilePage

from main_data.urls import Urls


class TestLKProfile:
    @allure.title('Переход в ЛК по клику на кнопку «Личный кабинет»')
    def test_go_to_account_from_header(self, driver):
        login_user = LoginUserPage(driver)
        login_user.login()
        main_page = MainPage(driver)
        main_page.click_on_account()
        user_profile_page = UserProfilePage(driver)
        current_url = user_profile_page.check_switch_on_profile()
        assert current_url == Urls.profile_page_url

    @allure.title('Переход в раздел История заказов по кнопке "История заказов"')
    def test_go_to_order_history(self, driver):
        login_user = LoginUserPage(driver)
        login_user.login()
        main_page = MainPage(driver)
        main_page.click_on_account()
        user_profile_page = UserProfilePage(driver)
        user_profile_page.click_order_history_button()
        current_url = user_profile_page.check_switch_to_order_history()
        assert current_url == Urls.account_order_history_page_url

    @allure.title('Переход на старницу авторизации при нажатии кнопки "Выход"')
    def test_logout(self, driver):
        login_user = LoginUserPage(driver)
        login_user.login()
        main_page = MainPage(driver)
        main_page.click_on_account()
        user_profile_page = UserProfilePage(driver)
        user_profile_page.click_log_out_button()
        current_url = login_user.check_switch_to_login_page()
        assert current_url == Urls.login_page_url
