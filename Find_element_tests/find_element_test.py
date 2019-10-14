from selenium.webdriver.common.action_chains import ActionChains
from Data.StaticTestData import TestData
from page_objects.user import CartPage, SearchPage, MainPage, CatalogPage, ProductPage
import time


def test_search(browser):
    """
    проверка тестовой выборки в поиске
    шаги:
    1.Найти поле для ввода данных поиска и ввести данные в нее
    2.Нажать кнопку поиска
    3.Проверить заголовки элементов на наличие введенных в поиск данных
    Ожидаемый результат:В заголовках присутствует часть поискового запроса
    :param browser:
    :return:
    """
    # 1.Найти поле для ввода данных поиска и ввести данные в нее
    MainPage.enter_search_data(TestData.search_data)
    # 2.Нажать кнопку поиска
    MainPage.use_search_()
    # 3.Получить заголовки элементов на наличие введенных и проверить
    captions = SearchPage.get_search_result_captions()
    for cpt in captions:
        assert TestData.search_data in captions


def test_alert_wishlist(browser):
    """
    Проверка появления алерт-div блока при добавлении в желаемое
    шаги:
    1.Нажать на кнопку 'добавить в favorites'
    2.Проверить появление алерта
    Ожидаемый результат:Алерт появился
    :param browser:
    :return:
    """
    #1.Нажать на кнопку 'добавить в favorites'
    MainPage.click_first_featured_product()
    #2.Проверить появление алерта
    MainPage.check_alert_appear()


def test_no_product_items(browser):
    """
    Проверка отсутствия товаров в категории, где их нет
    Предусловия:в каталог Phones & PDAs не добавлены товары
    шаги:
    1.Нажать на элемент по текстовому линку Phones & PDAs
    2.Проверить наличие надписи об отсутствии элементов.
    Ожидаемый результат:наличие надписи There are no products to list in this category.
    :param browser:
    :return:
    """
    #нажать ссылку all Phones and pdas
    MainPage.click_ALL_Phones_and_PDA_Link()
    content = ProductPage.get_content()
    assert "There are no products to list in this category" in content.text


def test_laptop_link(browser):
    """
    шаги:
    1.Кликнуть на линк с разделом каталога Laptops & Notebooks
    2.Сверить то, что мы попали действительно на нужную страницу каталога по её заголовку
    Ожидаемый результат:Переход на страницу с каталогом ноутбуков произведен успешно
    :param browser:
    :return:
    """
    # 1..Раскрыть выпадающий список Laptops & Notebooks
    MainPage.click_ALL_Laptops_and_notebook_Link()
    # 3 .Зайти на страницу каталога
    header = CatalogPage.get_catalog_header_text()
    assert MainPage.get_text_Laptop_and_notebook_text() == header.text


def test_register_form(browser):
    """Проверка возможности ввода данных в форму регистрации
       шаги:
       1.На главной странице в правом верхнем углу экрана найти кнопку "My Account" и кликнуть на неё
       2.В выпавшем списке нажать на кнопку Register
       3.Ввести валидные данные для регистрации
       Ожидаемый результат:Данные введены
       :param browser:
       :return:
       """
    # 1.На главной странице в правом верхнем углу экрана найти кнопку "My Account" и кликнуть на неё
    browser.find_element_by_xpath(MainPage.TopLinks.MyAccount.it['xpath']).click()
    browser.find_element_by_link_text("Register").click()
    # 3.Ввести валидные данные для регистрации firstname
    content = browser.find_element_by_id(RegisterPage.Content.it['id'])
    first_name_input = content.find_element_by_id(RegisterPage.Content.firstname_input_id['id'])
    first_name_input.send_keys("vasya")
    # 3.Ввести валидные данные для регистрации lastName
    last_name_input = content.find_element_by_id(RegisterPage.Content.lastname_input_id['id'])
    last_name_input.send_keys("bzdonsky")
    # 3.Ввести валидные данные для регистрации email
    email_input = content.find_element_by_id(RegisterPage.Content.email_input_id['id'])
    email_input.send_keys("bzdon@gmail.com")
    # 3.Ввести валидные данные для регистрации telephone
    telephone_input = content.find_element_by_id(RegisterPage.Content.telephone_input_id['id'])
    telephone_input.send_keys("+71112221122")
    # 3.Ввести валидные данные для регистрации password
    password_input = content.find_element_by_id(RegisterPage.Content.pass_input_id['id'])
    password_input.send_keys("12345678")
    # 3.Ввести валидные данные для регистрации password_confirm
    confirm_input = content.find_element_by_id(RegisterPage.Content.confirm_pass_input_id['id'])
    confirm_input.send_keys("12345678")
