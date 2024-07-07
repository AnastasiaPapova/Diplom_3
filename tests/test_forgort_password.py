import allure
from pages.main_page import MainPage
from conftest import driver
from pages.forgot_password_page import PasswordRecoveryPage
from main_data.urls import Urls
from main_data.personal_data import PersonalData


class TestRecoveryPassword:

    @allure.title('Проверка на переход по клику на Восстановить пароль на странице логина')
    def test_click_password_reset_button(self, driver):
        main_page = MainPage(driver)
        forgot_pass_page = PasswordRecoveryPage(driver)
        main_page.click_on_account()
        forgot_pass_page.click_password_reset_link()
        current_url = main_page.get_current_url()
        assert current_url == Urls.forgot_password_page_url

    @allure.title('Проверка на ввод почты и переход после клика по кнопке "Восстановить"')
    def test_enter_email_and_click_reset(self, driver):
        forgot_pass_page = PasswordRecoveryPage(driver)
        forgot_pass_page.open_link(Urls.forgot_password_page_url)
        forgot_pass_page.set_email_for_reset_password(PersonalData.user_login)
        forgot_pass_page.click_reset_button()
        forgot_pass_page.find_save_button()
        current_url = forgot_pass_page.get_current_url()
        assert current_url == Urls.reset_password_page_url

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_make_field_active(self, driver):
        forgot_pass_page = PasswordRecoveryPage(driver)
        forgot_pass_page.open_link(Urls.forgot_password_page_url)
        forgot_pass_page.set_email_for_reset_password(PersonalData.user_login)
        forgot_pass_page.click_reset_button()
        forgot_pass_page.find_save_button()
        forgot_pass_page.click_on_show_password_button()
        assert forgot_pass_page.find_input_active()