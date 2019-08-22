import pytest


def test_is_it_opencart(driver_headlessed, url_f):
    """
    из фикстуры драйвер получаем сам драйвер
    из фикстуры url_f получаем урл, что задается в опциях запуска теста
    :param driver:
    :param url_f:
    :return:
    """
    driver_headlessed.get(url_f)
    assert "OpenCart" in driver_headlessed.page_source
