import os
import sys
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.opera import options as options_oper
from selenium.webdriver.chrome.options import Options as options_chr
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


@pytest.fixture(params=["chrome", "safari", "firefox"])
def parametrized_browser(request):
    """
    Фикстура автоматом подхватывающая УРЛ из парсера.. и позволяющая одним тестом запускать 3 браузера
    :param request:
    :return:
    """
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    elif browser_param == "opera":
        opera_driver_loc = os.path.abspath('/usr/bin/operadriver')
        opera_exe_loc = os.path.abspath('/usr/bin/opera')
        opera_caps = desired_capabilities.DesiredCapabilities.OPERA.copy()
        opera_opts = options_oper.ChromeOptions()
        opera_opts._binary_location = opera_exe_loc
        wd = webdriver.Chrome(executable_path=opera_driver_loc, options=opera_opts,
                              desired_capabilities=opera_caps)
    else:
        raise Exception(f"{request.param} is not supported!")

    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))
    return driver


@pytest.fixture
def browser(request):
    '''
     фикстура для запуска браузера
     для домашки по поиску элементов
     :param request:
     :return wd: возвращает вебдрайвер
     '''
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        chrome_driver_loc = os.path.abspath('/usr/bin/chromedriver')
        chrome_exe_loc = os.path.abspath('/usr/bin/google-chrome-stable')
        chrome_caps = desired_capabilities.DesiredCapabilities.CHROME.copy()
        chrome_opts = options_oper.ChromeOptions()
        chrome_opts._binary_location = chrome_exe_loc
        driver = webdriver.Chrome(executable_path=chrome_driver_loc, options=chrome_opts,
                                  desired_capabilities=chrome_caps)
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    elif browser_param == "opera":
        opera_driver_loc = os.path.abspath('/usr/bin/operadriver')
        opera_exe_loc = os.path.abspath('/usr/bin/opera')
        opera_caps = desired_capabilities.DesiredCapabilities.OPERA.copy()
        opera_opts = options_oper.ChromeOptions()
        opera_opts._binary_location = opera_exe_loc
        driver = webdriver.Chrome(executable_path=opera_driver_loc, options=opera_opts,
                              desired_capabilities=opera_caps)
    else:
        raise Exception(f"{request.param} is not supported!")

    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))
    return driver


@pytest.fixture(scope="session")
def driver_headlessed(request):
    '''
    фикстура для запуска браузера в режиме headless
    для домашки по запуску браузеров
    :param request:
    :return wd: возвращает вебдрайвер
    '''
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        firefox_opts = webdriver.FirefoxOptions()
        firefox_opts.add_argument("--headless")
        wd = webdriver.Firefox()
    elif browser == 'chrome':
        chrome_opts = options_chr()
        chrome_opts.add_argument("--headless")
        chrome_opts.add_argument("--disable-gpu")
        chrome_opts.add_argument("--no-sandbox")
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
