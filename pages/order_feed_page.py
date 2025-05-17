import allure

from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Кликнуть на заказ')
    def click_order(self):
        self.click_on_element(OrderFeedLocators.ORDER)

    @allure.step("Сравни текст в деталях заказа")
    def check_text_popup_order(self, text):
        actual_text = self.get_text_on_element(OrderFeedLocators.POPUP_ORDER_DETAIL)
        return actual_text == text

    @allure.step("Кликнуть на кнопку 'Лента Заказов'")
    def click_button_order_feed(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Найти заказ в ленте заказов')
    def find_order_in_feed(self, number):
        self.scroll_to_element(OrderFeedLocators.locator_order(number))
        self.find_the_item_on_the_page(OrderFeedLocators.locator_order(number))

    @allure.step("Получить номер заказа из истории")
    def get_number_order(self):
        return self.get_text_on_element(OrderFeedLocators.ORDER_FROM_HISTORY)

    @allure.step("Клик на История заказов")
    def click_history_order(self):
        self.click_on_element(PersonalAccountLocators.HISTORY_ORDER)

    @allure.step("Клик по кнопке 'личный кабинет'")
    def click_button_personal_account(self):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Получить количество заказов за все время')
    def get_count_all_orders(self):
        return self.get_text_on_element(OrderFeedLocators.ALL_ORDERS)

    @allure.step('Получить количество за сегодня')
    def get_count_today_orders(self):
        return self.get_text_on_element(OrderFeedLocators.FOR_TODAY_ORDERS)

    @allure.step('Получить номер заказа В работе')
    def get_order_in_work(self):
        return self.get_text_on_element(OrderFeedLocators.WORK_ORDER)

    @allure.step("Клик на кнопку Оформить заказ")
    def click_button_place_order(self):
        self.click_on_element(MainPageLocators.BUTTON_PLACE_AN_ORDER)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_for_element(MainPageLocators.INGREDIENT)
        basket = self.wait_for_element(MainPageLocators.BASKET_BURGER)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step("Закрыть окна успешного заказа")
    def click_button_close_window_successful(self):
        self.click_on_element(OrderFeedLocators.BUTTON_CLOSE_SUCCESSFUL_WINDOW)

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_button_constructor(self):
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)


    @allure.step('Дождаться загрузки страницы')
    def order_loading_wait(self):
        self.get_order_in_work()
        self.wait_for_element_hide(OrderFeedLocators.WORK_ORDER)