import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def sent_keys_to_input(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Найти элемент на странице и получить его класс")
    def find_the_item_on_the_page(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute("class")

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView;", element)


