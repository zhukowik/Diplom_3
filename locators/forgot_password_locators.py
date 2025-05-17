from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_FORGOT_PASSWORD = [By.XPATH, ".//input"]
    BUTTON_RECOVER = [By.XPATH, ".//button[text()='Восстановить']"]
    BUTTON_SHOW_PASSWORD = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]
    FIELD_PASSWORD = [By.XPATH, ".//div[@class='input__container']/div"]