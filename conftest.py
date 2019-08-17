import os
import sys
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.opera import options
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
def driver_fix(request):
    '''
    фикстура для запуска браузера в режиме --headless
    :param request:
    :return wd:
    '''
    print("im in fixture")
    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        firefox_opts = webdriver.FirefoxOptions()
        firefox_opts.add_argument("--headless")#работает
        wd = webdriver.Firefox(options=firefox_opts)
    elif browser == 'chrome':
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_argument("--headless")#не работает
        #chrome_opts.headless=True#не работает
        #chrome_opts.set_headless(True)#так же не работает
        wd = webdriver.Chrome(options=chrome_opts)
    elif browser == 'opera':
        opera_driver_loc = os.path.abspath('/usr/bin/operadriver')
        opera_exe_loc = os.path.abspath('/usr/bin/opera')
        opera_caps = desired_capabilities.DesiredCapabilities.OPERA.copy()
        opera_opts = options.ChromeOptions()
        opera_opts.add_argument("--headless")#не работает
        opera_opts._binary_location = opera_exe_loc
        wd = webdriver.Chrome(executable_path=opera_driver_loc, options=opera_opts,
                              desired_capabilities=opera_caps)
    else:
        print('Unsupported browser!')
        sys.exit(1)
    request.addfinalizer(wd.close)
    return wd.get(url)
