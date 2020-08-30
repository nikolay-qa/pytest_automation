import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


lg = """["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", 
"ro", "ru", "sk", "uk", "zh-hans"]"""  # define all the available languages in list, triple quotes for wrapping


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")      # adding option for different internet browsers
    parser.addoption('--language', action='store', default="en",
                     help=f"Choose language:{lg}")      # adding option for choosing necessary language


@pytest.fixture(scope="function")
def browser(request):       # return variable with requested browser and language
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

