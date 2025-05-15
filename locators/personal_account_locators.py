from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    FORGOT_PASSWORD = [By.XPATH, ".//a[text()='Восстановить пароль']"]
    LOG_EMAIL = [By.XPATH, ".//label[text()='Email']/following-sibling::input"]
    PASSWORD = [By.XPATH, ".//input[@type='password']"]
    BUTTON_LOGIN = [By.XPATH, ".//button[text()='Войти']"]
    LABEL_PROFILE = [By.XPATH, ".//a[text()='Профиль']"]
    HISTORY_ORDER = [By.XPATH, ".//a[text()='История заказов']"]
    BUTTON_EXIT_ACCOUNT = [By.XPATH, ".//button[text()='Выход']"]
    LABEL_LOGIN = [By.XPATH, ".//h2[text()='Вход']"]