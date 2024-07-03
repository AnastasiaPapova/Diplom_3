import allure
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver

from main_data.urls import Urls
from locators import WebUILocators
from pages import WebUIHandler


@allure.step('Открытие браузера')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Urls.main_page_url)
    elif request.param == 'firefox':
        # firefox_options = webdriver.FirefoxOptions()
        # firefox_options.add_argument('--headless')
        # driver = webdriver.Firefox(options=firefox_options)
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(Urls.main_page_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def pages(driver):
    driver = driver
    pages = WebUIHandler(driver, WebUILocators())
    return pages


@pytest.fixture(scope='function')
def login(pages):
    pages.login()
