import allure

import curl
from data import DataUser, DataResetPassword
from pages.forgot_password_page import ForgotPasswordPage
from tests.conftest import driver


class TestForgotPassword:
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_going_to_page_forgot_password_when_click_text(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.main_page_loading_wait()
        forgot_password.click_button_personal_account()
        forgot_password.click_on_text_forgot_password()
        assert forgot_password.get_url_forgot_password() == curl.FORGOT_PASSWORD_PAGE

    @allure.title("Проверка ввода почты и клик по кнопке «Восстановить»")
    def test_send_keys_field_email_and_click_button_recover(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.main_page_loading_wait()
        forgot_password.click_button_personal_account()
        forgot_password.click_on_text_forgot_password()
        forgot_password.send_keys_in_email_field(DataUser.EMAIL)
        forgot_password.click_button_recover()
        forgot_password.wait_for_field_password()
        assert forgot_password.get_url_forgot_password() == curl.RESET_PASSWORD

    @allure.title("Проверка клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_show_field_active(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.main_page_loading_wait()
        forgot_password.click_button_personal_account()
        forgot_password.click_on_text_forgot_password()
        forgot_password.send_keys_in_email_field(DataUser.EMAIL)
        forgot_password.click_button_recover()
        forgot_password.click_button_show_password()
        assert forgot_password.get_class_field_password() == DataResetPassword.CLASS_RESET_PASSWORD_FOCUSED


