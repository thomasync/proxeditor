import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Before all tests
@pytest.fixture(autouse=True)
def pytest_constructor():
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=127.0.0.1:8302')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    pytest._driver = driver

# Verify that the proxy does not require authentication
def test_authentification():
    pytest._driver.get("http://mitm.it")
    assert "Proxy Authentication Required" not in pytest._driver.title