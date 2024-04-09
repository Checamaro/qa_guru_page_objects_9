import pytest
from selene import browser
from selene.support.shared import browser
from selene.support.shared import browser as shared_browser



"""Открываем браузер Chrome и страницу с формой"""


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_name = 'chrome'
    shared_browser.driver.maximize_window()
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'