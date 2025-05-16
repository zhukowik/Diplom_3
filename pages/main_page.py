import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_button_personal_account(self):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_button_constructor(self):
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Кликнуть на кнопку 'Лента Заказов'")
    def click_button_order_feed(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step("Кликнуть на иконку закрытия попапа ингредиенты")
    def click_icon_close_popup_ingredient(self):
        self.wait_for_element(MainPageLocators.BUTTON_CLOSE_POPUP_INGREDIENT)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_POPUP_INGREDIENT)

    @allure.step("Найти label 'Соберите бургер'")
    def find_label_collect_burger(self):
        self.find_the_item_on_the_page(MainPageLocators.LABEL_COLLECT_BURGER)

    @allure.step("Получить класс попапа")
    def get_class_popup(self):
        actual_class = self.find_the_item_on_the_page(MainPageLocators.POPUP)
        return actual_class

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_for_element(MainPageLocators.INGREDIENT)
        basket = self.wait_for_element(MainPageLocators.BASKET_BURGER)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step("Сравни число каунтера")
    def check_caunter(self, quantity):
        actual_text = self.get_text_on_element(MainPageLocators.CAUNTER)
        return actual_text == quantity

    @allure.step("Клик на кнопку Оформить заказ")
    def click_button_place_order(self):
        self.click_on_element(MainPageLocators.BUTTON_PLACE_AN_ORDER)

    @allure.step("Сравни текст в окне ")
    def check_text_popup_order(self, text):
        actual_text = self.get_text_on_element(MainPageLocators.LABEL_STARTED_COOKING)
        return actual_text == text

    @allure.step("Получить url страницы")
    def get_url_main(self):
        url = self.get_url_page()
        return url