import allure
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver

from main_data.urls import Urls


@allure.step('Открытие браузера')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Urls.main_page_url)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(Urls.main_page_url)
    yield driver
    driver.quit()
