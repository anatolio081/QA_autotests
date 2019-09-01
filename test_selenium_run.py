import pytest


def test_is_it_opencart(driver_headlessed, url_f):
    """
    из фикстуры драйвер получаем сам драйвер
    из фикстуры url_f получаем урл, что задается в опциях запуска теста
    :param driver:
    :param url_f:
    :return:
    """
    print("my URL is: "+url_f)
    driver_headlessed.get(url_f)
    powered_by = driver_headlessed.find_element_by_xpath("/html/body/footer/div/p/a")
    assert "OpenCart" in powered_by.text
