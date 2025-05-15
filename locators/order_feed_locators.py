from selenium.webdriver.common.by import By


class OrderFeedLocators:
    POPUP_ORDER_DETAIL = [By.XPATH, ".//p[@class='text text_type_main-medium mb-8']"]
    ORDER = [By.XPATH, ".//li[@class='OrderHistory_listItem__2x95r mb-6']"]
    ORDER_FROM_HISTORY = [By.XPATH, ".//p[@class='text text_type_digits-default']"]
    BUTTON_CLOSE_SUCCESSFUL_WINDOW = [By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]']
    ALL_ORDERS = [By.XPATH, './/div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    FOR_TODAY_ORDERS = [By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "digits-large")]']
    WORK_ORDER = [By.XPATH, './/*[contains(@class, "orderListReady")]//li[contains(@class,"digits-default")]']

    @staticmethod
    def locator_order(number):
        return [By.XPATH, f".//p[text()='{number}']"]