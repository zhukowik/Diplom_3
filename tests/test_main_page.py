
import allure

import curl
from data import DataMainPage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title("Проверка перехода в конструтор")
    def test_going_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_button_personal_account()
        main_page.click_button_constructor()
        assert main_page.get_url_page() == curl.main_site

    @allure.title("Проверка перехода в ленту заказов")
    def test_going_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_button_personal_account()
        main_page.click_button_order_feed()
        assert main_page.get_url_page() == curl.ORDER_FEED

    @allure.title("Проверка всплывающего окна при клике на ингредиент")
    def test_pop_up_window_when_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_ingredient()
        assert curl.INGREDIENT in main_page.get_url_main()

    @allure.title("Проверка закрытия попапа при клике на иконку крестика")
    def test_close_popup_when_click_icon(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_ingredient()
        main_page.click_icon_close_popup_ingredient()
        assert main_page.get_class_popup() == DataMainPage.CLASS_POPUP_CLOSE

    @allure.title("Проверка изменения  каунтера при добавлении ингредиента в заказ")
    def test_change_caunter_when_add_ingredient_order(self,login):
        main_page = MainPage(login)
        main_page.main_page_loading_wait()
        main_page.put_ingredient_into_basket()
        assert main_page.check_caunter("2")

    @allure.title("Проверка оформления заказа")
    def test_place_order(self, login):
        main_page = MainPage(login)
        main_page.main_page_loading_wait()
        main_page.put_ingredient_into_basket()
        main_page.click_button_place_order()
        assert main_page.check_text_popup_order(DataMainPage.TEXT_POPUP_ORDER)


