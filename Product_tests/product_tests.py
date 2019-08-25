from selenium.webdriver.common.action_chains import ActionChains
from locators.AdmMainPage import AdmMainPage
from locators.AdmProductPage import AdmProductPage
from Data.TestData import TestData
import time
import pytest


@pytest.fixture
def browser_adm(request, browser):
    '''
     Фикстура для авторизации в админскую панель.
     :param request:
     :return wd: возвращает страницу админки
     '''
    login = "user"
    password = "bitnami1"
    browser.get(browser.current_url + "admin")
    user_name_input = browser.find_element_by_id("input-username")
    user_name_input.send_keys(login)
    user_pass_input = browser.find_element_by_id("input-password")
    user_pass_input.send_keys(password)
    browser.find_element_by_tag_name("button").submit()
    return browser


def test_add_product(browser_adm):
    """
    Тест на добавление нового товара
    Шаги.
    1.Раскрыть левое меню 'Catalog'
    2.Нажать на кнопку 'Products'
    3.Нажать на кнопку добавления нового товара
    4.Ввести данные в Product Name
    5.Ввести данные в Meta Tag Title
    6.Перейти на вкладку Data
    7.Ввести данные в Model
    8.Нажать на кнопку сохранения товара
    9.На появившейся странице с товаром в фильтр ввести наименование товара
    10.Применить фильр по имени товара
    11.В отфильтрованной выгрузке найти имя найденного товара
    Ожидаемый результат:Имя добавленного товара найдено
    :param browser_adm:
    :return:
    """
    ActionChains(browser_adm).pause(3).perform()
    menu_catalog = browser_adm.find_element_by_id(AdmMainPage.menu_catalog_id)
    menu_catalog.click()
    browser_adm.find_element_by_link_text(AdmMainPage.products_text_link).click()
    browser_adm.find_element_by_xpath(AdmProductPage.add_button_xpath).click()
    product_name = browser_adm.find_element_by_id(AdmProductPage.product_name_id)
    product_name.send_keys(TestData.data_product_name)
    product_meta = browser_adm.find_element_by_id(AdmProductPage.product_meta_id)
    product_meta.send_keys(TestData.data_meta_name)
    browser_adm.find_element_by_link_text(AdmProductPage.data_link_text).click()
    input_model = browser_adm.find_element_by_id(AdmProductPage.data_input_model)
    input_model.send_keys(TestData.data_model_name)
    browser_adm.find_element_by_xpath(AdmProductPage.save_button_xpath).click()
    filter_input = browser_adm.find_element_by_id(AdmProductPage.filter_input_id)
    filter_input.send_keys(TestData.data_product_name)
    filter_button = browser_adm.find_element_by_id(AdmProductPage.filter_button_id)
    filter_button.click()
    body_of_selected = browser_adm.find_element_by_tag_name(AdmProductPage.body_of_selected_tag)
    cells = body_of_selected.find_elements_by_tag_name(AdmProductPage.result_cells_tag)
    result = False
    for cell in cells:
        if cell.text == TestData.data_product_name:
            result = True
            break
    assert result

def test_del_product(browser_adm):
    """
    Тест на удаление нового товара
    Шаги.
    1.Раскрыть левое меню 'Catalog'
    2.Нажать на кнопку 'Products'
    3.Применить фильр по имени товара
    4.В отфильтрованной выгрузке найти имя найденного товара
    5.Нажать на чекбокс для найденного товара
    6.Нажать кнопку delete
    7.Применить повторно фильр относительно имени товара
    8.В отфильтрованной выгрузке найти имя найденного товара
    Ожидаемый результат:Имя добавленного товара не найдено
    :param browser_adm:
    :return:
    """
    pass