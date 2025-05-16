
import allure
import curl
from data import DataPersonalAccount
from pages.personal_account_page import PersonalAccountPage



class TestLoginPage:

    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_going_personal_account_when_click(self, login):
        personal_account_page = PersonalAccountPage(login)
        personal_account_page.click_button_personal_account()
        personal_account_page.find_label_profile()
        assert personal_account_page.get_url_personal_account() == curl.PERSONAL_ACCOUNT

    @allure.title("Проверка перехода в раздел «История заказов»")
    def test_going_history_order(self,login):
        personal_account_page = PersonalAccountPage(login)
        personal_account_page.main_page_loading_wait()
        personal_account_page.click_button_personal_account()
        personal_account_page.find_label_profile()
        personal_account_page.click_history_order()
        assert personal_account_page.get_class_button_history() == DataPersonalAccount.CLASS_ACTIVE_HISTORY

    @allure.title("Проверка выхода из аккаунта")
    def test_exit_account(self, login):
        personal_account_page = PersonalAccountPage(login)
        personal_account_page.main_page_loading_wait()
        personal_account_page.click_button_personal_account()
        personal_account_page.find_label_profile()
        personal_account_page.click_button_exit_account()
        personal_account_page.find_label_login()
        assert personal_account_page.get_url_page() == curl.LOGIN_PAGE