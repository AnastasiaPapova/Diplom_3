import allure

from main_data.personal_data import PersonalData
from locators.burger_locators import LoginUserPageLocators
from pages.base_page import BasePage


class LoginUserPage(BasePage):

    @allure.step('Перейти на страницу авторизации по кнопке "Войти в аккаунт"')
    def click_lk_button(self):
        self.move_to_element_and_click(LoginUserPageLocators.LK_BUTTON)

    @allure.step('Авторизация')
    def login(self):
        self.click_lk_button()
        self.set_email(PersonalData.user_login)
        self.set_password(PersonalData.user_password)
        self.click_login_button()

    @allure.step('Заполняем поле "email"')
    def set_email(self, user_email):
        self.wait_for_element_to_be_clickable(LoginUserPageLocators.EMAIL_FIELD)
        self.click_on_element(LoginUserPageLocators.EMAIL_FIELD)
        self.set_text(LoginUserPageLocators.EMAIL_FIELD, user_email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password(self, user_password):
        self.click_on_element(LoginUserPageLocators.PASSWORD_FIELD)
        self.set_text(LoginUserPageLocators.PASSWORD_FIELD, user_password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.click_on_element(LoginUserPageLocators.LOGIN_BUTTON_ANY_FORMS)
        self.wait_for_element_to_be_clickable(LoginUserPageLocators.PROFILE_BUTTON)

    @allure.step('Проверяем переход на страницу Авторизации')
    def check_switch_to_login_page(self):
        self.wait_until_element_visibility(LoginUserPageLocators.LOGIN_FORM_HEADER)
        return self.get_current_url()
