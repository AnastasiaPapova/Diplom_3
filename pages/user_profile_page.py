import allure

from locators.burger_locators import ProfileLocators
from pages.base_page import BasePage


class UserProfilePage(BasePage):

    @allure.step('Проверка перехода на страницу профиля')
    def check_switch_on_profile(self):
        self.wait_until_element_visibility(ProfileLocators.PROFILE_BUTTON)
        return self.get_current_url()

    @allure.step('Клик по кнопке «История заказов»')
    def click_order_history_button(self):
        self.wait_for_element_to_be_clickable(ProfileLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element(ProfileLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверка перехода на страницу История заказов')
    def check_switch_to_order_history(self):
        self.wait_until_element_visibility(ProfileLocators.ENABLED_ORDER_HISTORY_BUTTON)
        return self.get_current_url()

    @allure.step('Клик по кнопке «Выход»')
    def click_log_out_button(self):
        self.wait_for_element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON)
        self.click_on_element(ProfileLocators.LOGOUT_BUTTON)