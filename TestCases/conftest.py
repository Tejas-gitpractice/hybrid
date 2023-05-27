from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("launching Chrome browser.............")
    elif browser=="firefox":
        driver = webdriver.Firefox()
        print("launching Firefox browser...........")
    else:
        driver = webdriver.Ie
    return driver





def pytest_addoption(parser):                  # this will get the value from cli/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):                                    # this will return the browser value to setup method
    return request.config.getoption("--browser")



