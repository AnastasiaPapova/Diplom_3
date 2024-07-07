import allure
from locators.burger_locators import ForgotPasswordlocators, LoginUserPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_on_element(LoginUserPageLocators.FORGOT_PASSWORD)

    @allure.step('Заполнение поля емейл для восстановления пароля')
    def set_email_for_reset_password(self, email):
        self.set_text(ForgotPasswordlocators.INPUT_EMAIL_FORGOT_PAGE, email)

    @allure.step('Найти активное поле Пароль')
    def find_input_active(self):
        return self.wait_until_element_visibility(ForgotPasswordlocators.PASSWORD_INPUT_ACTIVE)

    @allure.step('Нажать на кнопку Восстановить')
    def click_reset_button(self):
        self.move_to_element_and_click(ForgotPasswordlocators.RESET_BUTTON_FORGOT_PAGE)

    @allure.step('Клик на кнопку Показать/скрыть пароль')
    def click_on_show_password_button(self):
        self.click_on_element(ForgotPasswordlocators.PASSWORD_BUTTON_SHOW)

    @allure.step('Найти кнопку Сохранить')
    def find_save_button(self):
        self.wait_until_element_visibility(ForgotPasswordlocators.SAVE_BUTTON)
