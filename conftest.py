import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", 'en')


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        print("\n[+] Start Chrome browser for test...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\n[+] Start Firefox browser for test...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n[+] Quit browser")
    browser.quit()
