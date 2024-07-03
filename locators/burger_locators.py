from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, "//a[.='Конструктор']"  # кнопка "Конструктор"
    ORDER_FEED_BUTTON = By.XPATH, "//a[.='Лента Заказов']"  # кнопка "Лента заказов"
    BURGER_INGREDIENT_BUTTON = By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']"  # кнопка "Флюоресцентная булка"
    BURGER_INGREDIENT_DETAILS = By.XPATH, ".//h2[text()='Детали ингредиента']"  # строка "Детали ингредиента"
    CLOSE_MODAL_BUTTON = By.XPATH, "//*[@id='root']/div/section[1]/div[1]/button"  # кнопка закрытия модального окна
    BURGER_CONSTRUCTOR_BASKET = By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]"  # область корзины
    ORDER_CREATE_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')  # Идентификатор заказа
    BURGER_INGREDIENT_COUNTER = By.XPATH, ".//p[contains(@class, 'num')]"  # Счетчик ингредиента
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"  # кнопка "Оформить заказ"
    ORDER_STATUS_INFO = By.XPATH, ".//p[contains (text(),  'Ваш заказ начали готовить')]"  # строка "Ваш заказ начали готовить"
    PROFILE_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    LK_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    MAIN_PAGE_HEADER = By.XPATH, "//h1[text()='Соберите бургер']"
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")


class LoginLocators:
    EMAIL_FIELD = By.XPATH, ".//label[text()='Email']//parent::*/input"
    PASSWORD_FIELD = By.XPATH, ".//input[@type='password']"
    LOGIN_BUTTON_ANY_FORMS = By.XPATH, ".//button[text()='Войти']"
    FORGOT_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"  # ссылка "Восстановить пароль"
    LOGIN_FORM_HEADER = By.XPATH, ".//h2[text()='Вход']"


class ForgotPasswordlocators:
    INPUT_EMAIL_FORGOT_PAGE = By.XPATH, "//label[text()='Email']/following-sibling::input"  # поле ввода почты
    RESET_BUTTON_FORGOT_PAGE = By.XPATH, "//button[text()='Восстановить']"  # кнопка "Восстановить"

    PASSWORD_INPUT_ACTIVE = By.CSS_SELECTOR, ".input.input_status_active"  # поле пароль активно
    PASSWORD_BUTTON_SHOW = By.XPATH, "//div[contains(@class,'icon-action')]"  # кнопка "Показать пароль"
    SAVE_BUTTON = By.XPATH, "//button[text()='Сохранить']"  # кнопка "Сохранить"


class OrdersLocators:
    ORDERS_LIST_HEADER = By.XPATH, "//h1[text()='Лента заказов']"  # Заголовок "Лента заказов"
    ORDER_ELEMENTS = By.XPATH, "//p[text()='Cостав']"
    ORDER_HISTORY_LINK = By.XPATH, "//*[contains(@class, 'OrderHistory_link')]"
    ALL_ORDERS_IN_HISTORY = By.XPATH, ("//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]")
    ALL_ORDERS_IN_FEED = By.XPATH, (".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                    "text_type_digits-default']")
    TOTAL_ORDER_COUNT = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    DAILY_ORDER_COUNT = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    NUMBER_IN_PROGRESS_CSS = By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li"  # Номер в разделе "В работе"
    NUMBER_IN_PROGRESS = By.XPATH, (".//ul[@class='OrderFeed_orderListReady__1YFem "
                                    "OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")


class ProfileLocators:
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')  # Кнопка "Профиль"
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')  # Кнопка "История заказов"
    ENABLED_ORDER_HISTORY_BUTTON = (
    By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]')  # Включенная кнопка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    LK_INFO_MESSAGE = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
