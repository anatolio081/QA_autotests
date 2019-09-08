import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators.AdmMainPage import AdmMainPage
from locators.AdmProductPage import AdmProductPage
from locators.AdminLoginPage import AdminLoginPage
from Data.StaticTestData import TestData
from utils.generator import get_test_data

import pytest


@pytest.fixture
def browser_adm(request, browser):
    '''
     Фикстура для авторизации в админскую панель.
     :param request:
     :return wd: возвращает страницу админки
     '''
    #добавить к текущему урл admin
    browser.get(browser.current_url + "admin")
    #Ввести логин
    user_name_input = browser.find_element_by_id(AdminLoginPage.user_name_id['id'])
    user_name_input.send_keys(TestData.login)
    # Ввести пароль
    user_pass_input = browser.find_element_by_id(AdminLoginPage.password_id['id'])
    user_pass_input.send_keys(TestData.password)
    # Авторизоваться
    browser.find_element_by_xpath(AdminLoginPage.login_button_xpath['xpath']).click()
    return browser


def test_add_product(browser_adm):
    """
    Тест на добавление нового товара
    Предусловия:Товар из Data/StaticTestData.py отсутствует в каталоге
    Шаги:
    1.Раскрыть левое меню 'Catalog'
    2.Нажать на кнопку 'Products'
    3 Получить колличество товаров из сноски в правом-нижнем углу
    4.Нажать на кнопку добавления нового товара
    5.Ввести данные в Product Name
    6.Ввести данные в Meta Tag Title
    7.Перейти на вкладку Data
    8.Ввести данные в Model
    9.Нажать на кнопку сохранения товара
    10 Получить новое колличество товаров из сноски в правом-нижнем углу
    Ожидаемый результат:кол-во товаров до добавления меньше кол-ва товаров после
    :param browser_adm:
    :return:
    """
    # получить тестовые данные
    data = get_test_data()
    #клик по кнопке Каталог
    try:
        catalog = WebDriverWait(browser_adm, 5).until(
            EC.presence_of_element_located((By.ID, AdmMainPage.Navigation.Catalog.it['id'])))# ожидаю открытие после логина
        catalog.click()
    except (TimeoutException, EC.NoSuchElementException):
        assert "element is not found"
    #Клик по кнопке с продуктами
    try:
        product = WebDriverWait(browser_adm, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, AdmMainPage.Navigation.Catalog.products_text_link['text_link'])))# ожидаю раскрытия дроп-бокса для клика
        product.click()
    except ElementNotInteractableException:
        assert "element is not iteractable"
    #Посчитать кол-во товаров из сноски в правом верхнем углу
    table_statistic = browser_adm.find_element_by_xpath(AdmProductPage.ProductList.product_statistic_xpath['xpath'])
    count_text = table_statistic.text.split()
    count_before = int(count_text[5])
    # Нажать на кнопку добавления нового товара
    browser_adm.find_element_by_xpath(AdmProductPage.TopRightButtons.add_button_xpath['xpath']).click()
    # Ввести Product Name
    product_name = browser_adm.find_element_by_id(AdmProductPage.ProductPage.product_name_id['id'])
    product_name.send_keys(data.product_name)
    #Ввести данные в Meta Tag Title
    product_meta = browser_adm.find_element_by_id(AdmProductPage.ProductPage.product_meta_id['id'])
    product_meta.send_keys(data.meta)
    #Перейти на вкладку Data
    browser_adm.find_element_by_link_text(AdmProductPage.ProductPage.data_link_text['link_text']).click()
    #Ввести данные в Model
    input_model = browser_adm.find_element_by_id(AdmProductPage.ProductPage.data_input_model_id['id'])
    input_model.send_keys(data.model)
    #Нажать на кнопку сохранения товара
    browser_adm.find_element_by_xpath(AdmProductPage.TopRightButtons.save_button_xpath['xpath']).click()
    # Посчитать кол-во товаров из сноски в правом верхнем углу
    table_statistic = browser_adm.find_element_by_xpath(AdmProductPage.ProductList.product_statistic_xpath['xpath'])
    count_text = table_statistic.text.split()
    count_after = int(count_text[5])
    assert count_after > count_before


def test_edit_product(browser_adm):
    """
    Тест на редактирование товара
    Предусловия:Товар есть в таблице Products
    Шаги:
    1.Раскрыть левое меню 'Catalog'
    2.Нажать на кнопку 'Products'
    3.Сохранить в переменные изначальные наименования модели и имени первого товара
    4.Открыть на редактирование первый товар
    5.Изменить поле текста 'product name',добавив к ним TestData.data_edit_postfix
    6.Изменить поле текста 'model name', добавив к ним TestData.data_edit_postfix
    7.применить изменения
    8.Получить измененные значения в имени и модели товара.
    Ожидаемый результат:'product name','model' имеют в полях измененные значения с добавленным TestData.data_edit_postfix
    :param browser_adm:
    :return:
    """
    #Раскрыть левое меню 'Catalog'
    try:
        catalog = WebDriverWait(browser_adm, 5).until(
            EC.presence_of_element_located((By.ID, AdmMainPage.Navigation.Catalog.it['id'])))# ожидаю открытие после логина
        catalog.click()
    except (TimeoutException, EC.NoSuchElementException):
        assert "element is not found"
    # 2.Нажать на кнопку 'Products'
    try:
        product = WebDriverWait(browser_adm, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, AdmMainPage.Navigation.Catalog.products_text_link['text_link'])))# ожидаю раскрытия дроп-бокса для клика
        product.click()
    except ElementNotInteractableException:
        assert "element is not iteractable"
    # 3.Сохранить в переменные изначальные наименования модели и имени первого товара
    tbl = browser_adm.find_element_by_xpath(AdmProductPage.ProductList.it['xpath'])
    rows = tbl.find_elements_by_tag_name(AdmProductPage.ProductList.row_tag['tag'])
    cells = rows[0].find_elements_by_tag_name(AdmProductPage.ProductList.cell_tag['tag'])
    legacy_name = cells[2].text
    legacy_model = cells[3].text
    #4.Открыть на редактирование первый товар
    cells[7].find_element_by_xpath(AdmProductPage.ProductList.edit_button_xpath['xpath']).click()
    # 5.Изменить поле текста 'product name',добавив к ним TestData.data_edit_postfix
    product_name = browser_adm.find_element_by_id(AdmProductPage.ProductPage.product_name_id['id'])
    product_name.send_keys(Keys.CONTROL + "a")
    product_name.send_keys(Keys.BACKSPACE)
    product_name.send_keys(legacy_name + TestData.data_edit_postfix)
    # 6.Изменить поле текста 'model name', добавив к ним TestData.data_edit_postfix
    browser_adm.find_element_by_link_text(AdmProductPage.ProductPage.data_link_text['link_text']).click()
    model_name = browser_adm.find_element_by_id(AdmProductPage.ProductPage.data_input_model_id['id'])
    model_name.send_keys(Keys.CONTROL + "a")
    model_name.send_keys(Keys.BACKSPACE)
    model_name.send_keys(legacy_model + TestData.data_edit_postfix)
    # 7.применить изменения
    browser_adm.find_element_by_xpath(AdmProductPage.TopRightButtons.save_button_xpath['xpath']).click()
    ActionChains(browser_adm).pause(1).perform()  # жду алерт
    # 8.Получить измененные значения в имени и модели товара.
    tbl = browser_adm.find_element_by_xpath(AdmProductPage.ProductList.it['xpath'])
    rows = tbl.find_elements_by_tag_name(AdmProductPage.ProductList.row_tag['tag'])
    cells = rows[0].find_elements_by_tag_name(AdmProductPage.ProductList.cell_tag['tag'])
    assert cells[2].text == legacy_name + TestData.data_edit_postfix
    assert cells[3].text == legacy_model + TestData.data_edit_postfix


def test_del_product(browser_adm):
    """
    Тест на удаление нового товара
    Предусловия:Есть минимум 2 товара в таблице products
    Шаги:
    1.Раскрыть левое меню 'Catalog'
    2.Нажать на кнопку 'Products'
    3.Получить колличество товаров из сноски в правом-нижнем углу
    4.Выделить первый товар для удаление
    5.Нажать на кнопку Удалить
    6.В всплывшем алерте подтвердить удаление товара
    7.Раскрыть левое меню 'Catalog'
    8.Нажать на кнопку 'Products'
    9.Получить измененное колличество товаров из сноски в правом-нижнем углу
    Ожидаемый результат: Колличество товаров после удаления меньше колличества товаров до удаления
    :param browser_adm:
    :return:
    """
    #    1.Раскрыть левое меню 'Catalog'
    try:
        catalog = WebDriverWait(browser_adm, 5).until(
            EC.presence_of_element_located((By.ID, AdmMainPage.Navigation.Catalog.it['id'])))  # ожидаю открытие после логина
        catalog.click()
    except (TimeoutException, EC.NoSuchElementException):
        assert "element is not found"
    #    2.Нажать на кнопку 'Products'
    try:
        product = WebDriverWait(browser_adm, 2).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, AdmMainPage.Navigation.Catalog.products_text_link['text_link'])))  # ожидаю раскрытия дроп-бокса для клика
        product.click()
    except ElementNotInteractableException:
        assert "element is not iteractable"
    #   3.Получить колличество товаров из сноски в правом-нижнем углу
    table_statistic = browser_adm.find_element_by_xpath(AdmProductPage.ProductList.product_statistic_xpath['xpath'])
    count_text = table_statistic.text.split()
    count_before = int(count_text[5])
    #    4.Выделить первый товар для удаление
    tbl = browser_adm.find_element_by_xpath(AdmProductPage.ProductList.it['xpath'])
    time.sleep(2)
    rows = tbl.find_elements_by_tag_name(AdmProductPage.ProductList.row_tag['tag'])
    time.sleep(2)
    cells = rows[0].find_elements_by_tag_name(AdmProductPage.ProductList.cell_tag['tag'])
    time.sleep(2)
    cells[0].click()
    time.sleep(2)
    #5.Нажать на кнопку Удалить
    browser_adm.find_element_by_xpath(AdmProductPage.TopRightButtons.delete_button_xpath['xpath']).click()
    #    6.В всплывшем алерте подтвердить удаление товара
    try:
        alert = browser_adm.switch_to.alert #появление алерта
        alert.accept()
    except:
        assert "alert is not appeared"
    #7.Раскрыть каталог
    try:
        catalog = WebDriverWait(browser_adm, 2).until(
            EC.element_to_be_clickable((By.ID,
                                        AdmMainPage.Navigation.Catalog.it['id'])))  # ожидаю возможность взаимодействия с кнопкой каталога, после алерта
        catalog.click()
    except (TimeoutException, EC.NoSuchElementException):
        assert "element is not iteractable"
    #7.Раскрыть Продукты
    try:
        product = WebDriverWait(browser_adm, 2).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, AdmMainPage.Navigation.Catalog.products_text_link['text_link'])))  # ожидаю раскрытия дроп-бокса для клика
        product.click()
    except ElementNotInteractableException:
        assert "element is not iteractable"
    #Посчитать колличество товаров
    table_statistic = browser_adm.find_element_by_xpath(AdmProductPage.ProductList.product_statistic_xpath['xpath'])
    count_text = table_statistic.text.split()
    count_after = int(count_text[5])
    assert count_after < count_before
