from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    ORDER_FEED_LINK = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    CONSTRUCT_BURGER_HEADER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    ACCOUNT_HEADER_LINK = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

    BUN_INGREDIENT = (By.CSS_SELECTOR, "a[class*='BurgerIngredient_ingredient__'][draggable='true']")
    CONSTRUCTOR_TOP_ZONE = (By.CSS_SELECTOR, "[class*='constructor-element_pos_top']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_ID_MODAL_TEXT = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")

    INGREDIENT_SECTION = (By.CLASS_NAME, "BurgerIngredients_ingredients__")
    BUN_ITEMS = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')]")
    SAUCE_ITEMS = (By.XPATH,
                   "//p[text()='Соусы']/following::li[contains(@class, 'BurgerIngredients_ingredients__item')]")
    FILLING_ITEMS = (By.XPATH,
                     "//p[text()='Начинки']/following::li[contains(@class, 'BurgerIngredients_ingredients__item')]")

    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class*='counter_counter__']")

    INGREDIENT_MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal__contentBox_']")
    INGREDIENT_MODAL_HEADING = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    INGREDIENT_MODAL_CLOSE = (By.CSS_SELECTOR, "[class*='Modal_modal__close_']")

    ORDER_LIST = (By.CLASS_NAME, "OrderList_list__")
    ORDER_ITEM = (By.CLASS_NAME, "OrderList_item__")

    ORDER_MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal__contentBox_']")
    ORDER_MODAL_CLOSE = (By.CLASS_NAME, "OrderModal_close__")

    ORDERS_IN_PROGRESS = (By.XPATH,
                          "//p[text()='В работе:']/following-sibling::div[contains(@class, 'OrderFeedList_ready')]//span")
    TOTAL_ORDERS_DONE = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::span")
    TODAY_ORDERS_DONE = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::span")


class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    EMAIL_INPUT_ALT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT_ALT = (By.XPATH, "//input[@type='password']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' or @type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль' or @type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_close__")
    SHOW_PASSWORD_ICON = (By.XPATH, "//input[@name='Пароль']/following-sibling::div[contains(@class, 'icon')]")
    ACCOUNT_LINK = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    LABEL = (By.XPATH, "//label[contains(text(), 'Пароль')]")


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    EMAIL_INPUT_ALT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    SHOW_PASSWORD_ICON = (By.XPATH, "//input[@name='Пароль']/following-sibling::div")
    INPUT_FIELDS = (By.CSS_SELECTOR, "input")
    BUTTONS = (By.CSS_SELECTOR, "button")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Мы отправили инструкцию по восстановлению пароля')]")
    PASSWORD_PARENT = (By.XPATH, "ancestor::div[contains(@class, 'input')]")


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//*[contains(text(), 'Профиль')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//*[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(), 'Выход')]")
    LOGIN_LINK = (By.XPATH, "//*[contains(text(), 'Войти')]")
    ORDER_HISTORY_ITEMS = (By.CSS_SELECTOR, "[class*='OrderHistory_item']")


class OrderFeedPageLocators:
    ORDER_MODAL = (By.CLASS_NAME, "OrderModal_modal__")
    ORDER_MODAL_CLOSE = (By.CLASS_NAME, "OrderModal_close__")
    ORDER_MODAL_HEADER = (By.CLASS_NAME, "OrderModal_header__")
    ORDER_ITEMS = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__')]")
    ORDER_MODAL_CONTAINER = (By.CSS_SELECTOR, "div[class*='Modal_orderBox__']")
    ORDER_LINKS = (By.CSS_SELECTOR, "a[class*='OrderHistory_link__'][href^='/feed/']")
    FEED_HEADER = (By.XPATH,
                   "//h1[contains(text(), 'Лента заказов')] | //h2[contains(text(), 'Лента заказов')] | //p[contains(text(), 'В работе')]")

    TOTAL_DONE_COUNTER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__')]")
    TODAY_DONE_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за сегодня:')]//following-sibling::p[contains(@class, 'OrderFeed_number__')][1]"
    )
    FIRST_IN_PROGRESS_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady_')]")

    ORDERS_READY = (By.CLASS_NAME, "OrderFeedList_ready__")
    ORDERS_DONE = (By.CLASS_NAME, "OrderFeedList_done__")


class ConstructorPageLocators:
    INGREDIENT_ITEMS = (By.CSS_SELECTOR, "li[class*='BurgerIngredients_ingredients__item']")
    INGREDIENT_MODAL = (By.CLASS_NAME, "IngredientModal_modal__")
    INGREDIENT_MODAL_CLOSE = (By.CLASS_NAME, "IngredientModal_close__")