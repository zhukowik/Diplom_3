from selenium.webdriver.common.by import By


class MainPageLocators:
    OVERLAY = [By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"]
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH, ".//p[text()='Личный Кабинет']"]
    BUTTON_LOG_MAIN = [By.XPATH, ".//button[text()='Войти в аккаунт']"]
    HEADER_LOGO = [By.CLASS_NAME, "AppHeader_header__logo__2D0X2"]
    BUTTON_CONSTRUCTOR = [By.XPATH, ".//p[text()='Конструктор']"]
    BUTTON_ORDER_FEED = [By.XPATH, ".//p[text()='Лента Заказов']"]
    INGREDIENT = [By.XPATH, ".//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']"]
    LABEL_DETAIL = [By.XPATH, ".//h2[text()='Детали ингредиента']"]
    BUTTON_CLOSE_POPUP_INGREDIENT = [By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']/button"]
    LABEL_COLLECT_BURGER = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    POPUP = [By.XPATH, ".//div[@class='App_App__aOmNj']/section"]
    BASKET_BURGER = [By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']"]
    CAUNTER = [By.XPATH, ".//div[@class='counter_counter__ZNLkj counter_default__28sqi']"]
    BUTTON_PLACE_AN_ORDER = [By.XPATH, ".//button[text()='Оформить заказ']"]
    LABEL_STARTED_COOKING = [By.XPATH, ".//p[@class='undefined text text_type_main-small mb-2']"]
    POPUP_ORDER_DETAIL = [By.XPATH, ".//p[@class='text text_type_main-medium mb-8']"]

    ORDER_NUMBER = [By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]']
