import allure

from locators.forgot_password_locators import ForgotPasswordLocators
from locators.personal_account_locators import PersonalAccountLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step("Ввести текст в поле Email")
    def send_keys_in_email_field(self, email):
        self.sent_keys_to_input(ForgotPasswordLocators.EMAIL_FORGOT_PASSWORD, email)

    @allure.step("Кликнуть на кнопку восстановить")
    def click_button_recover(self):
        self.click_on_element(ForgotPasswordLocators.BUTTON_RECOVER)

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_button_personal_account(self):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step("Нажать на текст 'Восстановить пароль'")
    def click_on_text_forgot_password(self):
        self.click_on_element(PersonalAccountLocators.FORGOT_PASSWORD)

    @allure.step("Найти поле пароль на странице восстановления пароля")
    def wait_for_field_password(self):
        self.wait_for_element(ForgotPasswordLocators.FIELD_PASSWORD)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_button_show_password(self):
        self.click_on_element(ForgotPasswordLocators.BUTTON_SHOW_PASSWORD)

    @allure.step("Получить класс поля пароль")
    def get_class_field_password(self):
        actual_class = self.find_the_item_on_the_page(ForgotPasswordLocators.FIELD_PASSWORD)
        return actual_class

    @allure.step("Получить url страницы")
    def get_url_forgot_password(self):
        url = self.get_url_page()
        return url