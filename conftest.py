import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

chrome_options = ChromeOptions()
firefox_options = webdriver.FirefoxOptions()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store',  default='en',
                     help="Choose language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == 'en':
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
        firefox_options.set_preference('intl.accept_languages', 'en')
    elif language == 'ru':
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        firefox_options.set_preference('intl.accept_languages', 'ru')
    else:
        raise pytest.UsageError("--language should be en or ru")

    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        print("\n[+] Start Chrome browser for test...")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\n[+] Start Firefox browser for test...")
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\n[+] Quit browser")
    browser.quit()
