import pytest
from selenium import webdriver

from curl import main_site
from data import DataUser

from pages.personal_account_page import PersonalAccountPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    login = PersonalAccountPage(driver)
    login.login(DataUser.EMAIL, DataUser.PASSWORD)
    return driver

