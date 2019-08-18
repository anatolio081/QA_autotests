import os
import sys
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.opera import options as options_oper
import pytest


def pytest_addoption(parser):
    """parser add Option"""
    parser.addoption(
        "--url",
        action="store",
        default="http://127.0.0.1",
        help="Opencart web address"
    )

    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser name"
    )

@pytest.fixture(scope="session")
def url_f(request):
    """
    Фикстура для получения url для из опций запуска
    :param request:
    :return:
    """
    url = request.config.getoption("--url")
    return url



@pytest.fixture(scope="session")
def driver(request):
    '''
    фикстура для запуска браузера
    :param request:
    :return wd:
    '''
    print("im in fixture")
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        firefox_opts = webdriver.FirefoxOptions()
        firefox_opts.add_argument("--headless")
        wd = webdriver.Firefox(options=firefox_opts)
    elif browser == 'chrome':
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_argument("--headless")
        chrome_opts.add_argument("--disable-gpu")
        chrome_opts.add_argument("--start-fullscreen")
        wd = webdriver.Chrome(options=chrome_opts)
    elif browser == 'opera':
        opera_driver_loc = os.path.abspath('/usr/bin/operadriver')
        opera_exe_loc = os.path.abspath('/usr/bin/opera')
        opera_caps = desired_capabilities.DesiredCapabilities.OPERA.copy()
        opera_opts = options_oper.ChromeOptions()
        opera_opts.add_argument("--headless")
        opera_opts._binary_location = opera_exe_loc
        wd = webdriver.Chrome(executable_path=opera_driver_loc, options=opera_opts,
                              desired_capabilities=opera_caps)
    else:
        print('Unsupported browser!')
        sys.exit(1)
    request.addfinalizer(wd.close)
    return wd
