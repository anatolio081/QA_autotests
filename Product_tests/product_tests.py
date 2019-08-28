from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators.AdmMainPage import AdmMainPage
from locators.AdmProductPage import AdmProductPage
from locators.AdminLoginPage import AdminLoginPage
from Data.TestData import TestData
import pytest


@pytest.fixture
def browser_adm(request, browser):
    '''
     Фикстура для авторизации в админскую панель.
     :param request:
     :return wd: возвращает страницу админки
     '''
    browser.get(browser.current_url + "admin")
    user_name_input = browser.find_element_by_id(AdminLoginPage.user_name_id)
    user_name_input.send_keys(TestData.login)
    user_pass_input = browser.find_element_by_id(AdminLoginPage.password_id)
    user_pass_input.send_keys(TestData.password)
    browser.find_element_by_tag_name(AdminLoginPage.login_button_tag).click()
    return browser


def test_add_product(browser_adm):
    """
    Тест на добавление нового товара
    Предусловия:Товар из Data/TestData.py отсутствует в каталоге
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
    Ожидаемый результат:кол-во товаров до меньше кол-ва товаров после
    :param browser_adm:
    :return:
    """
    ActionChains(browser_adm).pause(3).perform()  # жду Загрузку страницы
    browser_adm.find_element_by_id(AdmMainPage.menu_catalog_id).click()
    ActionChains(browser_adm).pause(0.5).perform()  # жду Раскрытие меню каталога
    product = browser_adm.find_element_by_link_text("Products")
    product.click()
    table_statistic = browser_adm.find_element_by_xpath(AdmProductPage.table_statistic_xpath)
    count_text = table_statistic.text.split()
    count_before = int(count_text[5])
    browser_adm.find_element_by_xpath(AdmProductPage.add_button_xpath).click()
    product_name = browser_adm.find_element_by_id(AdmProductPage.product_name_id)
    product_name.send_keys(TestData.data_product_name)
    product_meta = browser_adm.find_element_by_id(AdmProductPage.product_meta_id)
    product_meta.send_keys(TestData.data_meta_name)
    browser_adm.find_element_by_link_text(AdmProductPage.data_link_text).click()
    input_model = browser_adm.find_element_by_id(AdmProductPage.data_input_model_id)
    input_model.send_keys(TestData.data_model_name)
    browser_adm.find_element_by_xpath(AdmProductPage.save_button_xpath).click()
    table_statistic = browser_adm.find_element_by_xpath(AdmProductPage.table_statistic_xpath)
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
    6.Изменить поле текста 'product name',добавив к ним TestData.data_edit_postfix
    6.Изменить поле текста 'model name', добавив к ним TestData.data_edit_postfix
    7.применить изменения
    Ожидаемый результат:'product name','model' имеют в полях измененные значения с добавленным TestData.data_edit_postfix
    :param browser_adm:
    :return:
    """
    ActionChains(browser_adm).pause(3).perform()  # жду Загрузку страницы
    browser_adm.find_element_by_id(AdmMainPage.menu_catalog_id).click()
    ActionChains(browser_adm).pause(0.5).perform()  # жду Раскрытие меню каталога
    browser_adm.find_element_by_link_text(AdmMainPage.products_text_link).click()
    tbl = browser_adm.find_element_by_xpath(AdmProductPage.product_table_xpath)
    rows = tbl.find_elements_by_tag_name(AdmProductPage.row_tag)
    cells = rows[0].find_elements_by_tag_name(AdmProductPage.cell_tag)
    legacy_name = cells[2].text
    legacy_model = cells[3].text
    cells[7].find_element_by_xpath(AdmProductPage.edit_button_xpath).click()
    product_name = browser_adm.find_element_by_id(AdmProductPage.product_name_id)
    product_name.send_keys(Keys.CONTROL + "a")
    product_name.send_keys(Keys.BACKSPACE)
    product_name.send_keys(legacy_name + TestData.data_edit_postfix)
    browser_adm.find_element_by_link_text(AdmProductPage.data_link_text).click()
    model_name = browser_adm.find_element_by_id(AdmProductPage.data_input_model_id)
    model_name.send_keys(Keys.CONTROL + "a")
    model_name.send_keys(Keys.BACKSPACE)
    model_name.send_keys(legacy_model + TestData.data_edit_postfix)
    browser_adm.find_element_by_xpath(AdmProductPage.save_button_xpath).click()
    ActionChains(browser_adm).pause(1).perform()  # жду алерт
    tbl = browser_adm.find_element_by_xpath(AdmProductPage.product_table_xpath)
    rows = tbl.find_elements_by_tag_name(AdmProductPage.row_tag)
    cells = rows[0].find_elements_by_tag_name(AdmProductPage.cell_tag)
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
    6.Нажать на кнопку Удалить
    6.В всплывшем алерте подтвердить удаление товара
    7.Получить измененное колличество товаров из сноски в правом-нижнем углу
    Ожидаемый результат:счетчик товаров уменьшился на 1
    :param browser_adm:
    :return:
    """
    ActionChains(browser_adm).pause(3).perform()  # жду Загрузку страницы
    browser_adm.find_element_by_id(AdmMainPage.menu_catalog_id).click()
    ActionChains(browser_adm).pause(0.5).perform()  # жду Раскрытие меню каталога
    browser_adm.find_element_by_link_text(AdmMainPage.products_text_link).click()
    table_statistic = browser_adm.find_element_by_xpath(AdmProductPage.table_statistic_xpath)
    count_text = table_statistic.text.split()
    count_before = int(count_text[5])
    tbl = browser_adm.find_element_by_xpath(AdmProductPage.product_table_xpath)
    rows = tbl.find_elements_by_tag_name(AdmProductPage.row_tag)
    cells = rows[0].find_elements_by_tag_name(AdmProductPage.cell_tag)
    cells[0].click()
    ActionChains(browser_adm).pause(3).perform()
    browser_adm.find_element_by_xpath(AdmProductPage.delete_button_xpath).click()
    try:
        alert = browser_adm.switch_to_alert()
        alert.accept()
    except:
        assert "alert is failed"
    ActionChains(browser_adm).pause(0.5).perform()  # жду Закрытие алерта
    browser_adm.find_element_by_id(AdmMainPage.menu_catalog_id).click()
    browser_adm.find_element_by_link_text(AdmMainPage.products_text_link).click()
    table_statistic = browser_adm.find_element_by_xpath(AdmProductPage.table_statistic_xpath)
    count_text = table_statistic.text.split()
    count_after = int(count_text[5])
    assert count_after < count_before
