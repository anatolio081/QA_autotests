import pytest


def test_is_it_opencart(driver, url_f):
    """
    из фикстуры драйвер получаем сам драйвер
    из фикстуры url_f получаем урл, что задается в опциях запуска теста
    :param driver:
    :param url_f:
    :return:
    """
    driver.get(url_f)
    assert "OpenCart" in driver.page_source
