import pytest

def test_neverssl_online():
    pytest._driver.get("http://neverssl.com/online/?proxeditor_pytest")
    assert "43b045" in pytest._driver.page_source

def test_neverssl_online_create():
    pytest._driver.get("http://neverssl.com/online/create?proxeditor_pytest")
    assert "Proxy Works" in pytest._driver.page_source

def test_neverssl_redirect():
    pytest._driver.get("http://neverssl.com/redirect?proxeditor_pytest")
    assert "https://neverssl.com/online/" in pytest._driver.current_url

def test_neverssl_online():
    pytest._driver.get("http://neverssl.com/online/?proxeditor_pytest")
    assert "43b045" in pytest._driver.page_source

def test_github_thomasync():
    pytest._driver.get("https://github.com/thomasync?proxeditor_pytest")
    assert "Proxy Works" in pytest._driver.title