from pages.auth_user_page import AuthUserPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.forgot_password_page import PasswordRecoveryPage
from pages.create_order_page import CreateOrderPage
from pages.user_profile_page import UserProfilePage


class WebUIHandler(MainPage, AuthUserPage, PasswordRecoveryPage, UserProfilePage, CreateOrderPage):
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators
