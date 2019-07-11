import pytest
from fixture.applications import Applications
from selenium import webdriver

fixture = None


@pytest.yield_fixture(scope='session')
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope='session', autouse=True)
def app(driver):
    global fixture
    if fixture is None:
        fixture = Applications(driver)
    return fixture

