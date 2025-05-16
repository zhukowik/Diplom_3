from data import DataUser
from locators.personal_account_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class PersonalAccountPage(BasePage):
    @allure.step("Нажать на текст 'Восстановить пароль'")
    def click_on_text_forgot_password(self):
        self.click_on_element(PersonalAccountLocators.FORGOT_PASSWORD)

    @allure.step("Ввести текст в поле email")
    def send_keys_text_in_email_field(self, email):
        self.sent_keys_to_input(PersonalAccountLocators.LOG_EMAIL, email)

    @allure.step("Ввести текст в поле пароль")
    def send_keys_text_in_password_field(self, password):
        self.sent_keys_to_input(PersonalAccountLocators.PASSWORD, password)

    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_on_button_login(self):
        self.click_on_element(PersonalAccountLocators.BUTTON_LOGIN)

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.send_keys_text_in_email_field(email)
        self.send_keys_text_in_password_field(password)
        self.click_on_button_login()

    @allure.step("Клик по кнопке 'личный кабинет'")
    def click_button_personal_account(self):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step("Клик на История заказов")
    def click_history_order(self):
        self.click_on_element(PersonalAccountLocators.HISTORY_ORDER)

    @allure.step("Клик по логотипу для перехода на главную страницу")
    def click_logo(self):
        self.click_on_element(MainPageLocators.HEADER_LOGO)

    @allure.step("Найти label 'Профиль'")
    def find_label_profile(self):
        self.wait_for_element(PersonalAccountLocators.LABEL_PROFILE)

    @allure.step("Получить класс кнопки История заказов")
    def get_class_button_history(self):
        actual_class = self.find_the_item_on_the_page(PersonalAccountLocators.HISTORY_ORDER)
        return actual_class

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть на кнопку выхода из аккаунта')
    def click_button_exit_account(self):
        self.click_on_element(PersonalAccountLocators.BUTTON_EXIT_ACCOUNT)

    @allure.step("Найти label Вход")
    def find_label_login(self):
        self.wait_for_element(PersonalAccountLocators.LABEL_LOGIN)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_for_element(MainPageLocators.INGREDIENT)
        basket = self.wait_for_element(MainPageLocators.BASKET_BURGER)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step("Клик на кнопку Оформить заказ")
    def click_button_place_order(self):
        self.click_on_element(MainPageLocators.BUTTON_PLACE_AN_ORDER)

    @allure.step("Получить url страницы")
    def get_url_personal_account(self):
        url = self.get_url_page()
        return url