import allure
from conftest import pages
from main_data.urls import Urls
from main_data.personal_data import PersonalData


class TestRecoveryPassword:

    @allure.title('Проверка на переход по клику на Восстановить пароль на странице логина')
    def test_click_password_reset_button(self, pages):
        pages.click_on_account()
        pages.click_password_reset_link()
        current_url = pages.get_current_url()
        assert current_url == Urls.forgot_password_page_url

    @allure.title('Проверка на ввод почты и переход после клика по кнопке "Восстановить"')
    def test_enter_email_and_click_reset(self, pages):
        pages.open_link(Urls.forgot_password_page_url)
        pages.set_email_for_reset_password(PersonalData.user_login)
        pages.click_reset_button()
        pages.find_save_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.reset_password_page_url

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_make_field_active(self, pages):
        pages.open_link(Urls.forgot_password_page_url)
        pages.set_email_for_reset_password(PersonalData.user_login)
        pages.click_reset_button()
        pages.find_save_button()
        pages.click_on_show_password_button()
        assert pages.find_input_active()