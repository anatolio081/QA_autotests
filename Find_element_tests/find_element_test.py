from selenium.webdriver.common.action_chains import ActionChains
from locators.MainPage import MainPage
from locators.SearchPage import SearchPage
from locators.ProductPage import ProductPage
from locators.RegisterPage import RegisterPage



def test_search(browser):
    """
    проверка тестовой выборки в поиске
    шаги:
    1.Найти поле для ввода данных поиска
    2.Нажать кнопку поиска
    3.Проверить заголовки элементов на наличие введенных в поиск данных
    Ожидаемый результат:В заголовках присутствует часть поискового запроса
    :param browser:
    :return:
    """
    test_data = "БАГЕТ"
    input_box = browser.find_element_by_class_name(MainPage.search_input_class_name)
    input_box.send_keys(test_data)
    browser.find_element_by_class_name(MainPage.search_button_class_name).click()
    found_search_elms = browser.find_elements_by_class_name(SearchPage.search_div_elems_class_name)
    for elm in found_search_elms:
        caption = elm.find_element_by_class_name("caption")
        assert test_data in caption.find_element_by_tag_name("a").text


def test_alert_wishlist(browser):
    """
    Проверка появления алерт-div блока при добавлении в желаемое
    шаги:
    1.Нажать на первое изображение товара
    2.Нажать на кнопку 'добавить в favorites'
    3.Проверить появление алерта
    Ожидаемый результат:Алерт появился
    :param browser:
    :return:
    """
    browser.find_element_by_xpath(MainPage.promo_element_xpath).click()
    browser.find_element_by_xpath(ProductPage.add_wishlist_xpath).click()
    ActionChains(browser).pause(0.5).perform()#хром слишком быстро пытался найти алерт..заставил подождать
    browser.find_element_by_class_name(ProductPage.alert_success_class_name)


def test_catalog_items(browser):
    """
    Проверка наличия Div блоков с товарами в разделе, в который они добавлены
    Предусловия:в каталог добавлены товары типа Phones & PDAs
    шаги:
    1.Найти меню
    2.Нажать на элемент по текстовому линку Phones & PDAs
    3.Проверить наличие DIV блоков с товарами и возможность наведения на них
    Ожидаемый результат:Присутствуют Div блоки с товарами, и курсор на них наводится
    :param browser:
    :return:
    """
    menu = browser.find_element_by_id(MainPage.menu_id)
    menu.find_element_by_link_text("Phones & PDAs").click()
    products = browser.find_elements_by_class_name(CatalogPage.product_class_name)
    for product in products:
        ActionChains(browser).move_to_element(product).pause(2).perform()


def test_laptop_link(browser):
    """
    шаги:
    1.Найти раздел с Laptops & Notebooks
    2.Раскрыть выпадающий список с ссылками
    3.Зайти на страницу каталога
    4.Сверить то, что мы попали действительно на нужную страницу каталога по её заголовку
    Ожидаемый результат:Переход на страницу с каталогом ноутбуков произведен успешно
    :param browser:
    :return:
    """
    laptop_link = browser.find_element_by_link_text("Laptops & Notebooks")
    ActionChains(browser).move_to_element(laptop_link).pause(2).perform()
    browser.find_element_by_link_text("Show All Laptops & Notebooks").click()
    h2 = browser.find_element_by_tag_name("h2")
    assert h2.text == "Laptops & Notebooks"


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
    top_right_links = browser.find_element_by_css_selector(MainPage.topright_menu_cssSel)
    top_right_links.find_element_by_xpath("//a[@title='My Account']").click()
    browser.find_element_by_link_text("Register").click()
    content = browser.find_element_by_id(RegisterPage.content_id)
    first_name_input = content.find_element_by_id(RegisterPage.firstname_input_id)
    first_name_input.send_keys("vasya")
    last_name_input = content.find_element_by_id(RegisterPage.lastname_input_id)
    last_name_input.send_keys("bzdonsky")
    email_input = content.find_element_by_id(RegisterPage.email_input_id)
    email_input.send_keys("bzdon@gmail.com")
    telephone_input = content.find_element_by_id(RegisterPage.telephone_input_id)
    telephone_input.send_keys("+71112221122")
    password_input = content.find_element_by_id(RegisterPage.pass_input_id)
    password_input.send_keys("12345678")
    confirm_input = content.find_element_by_id(RegisterPage.confirm_input_id)
    confirm_input.send_keys("12345678")
