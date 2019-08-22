from selenium.webdriver.common.action_chains import ActionChains
from locators.MainPage import MainPage
from locators.SearchPage import SearchPage
from locators.ProductPage import ProductPage
import time

def wait():
    time.sleep(1)

def test_element_by_class_name_selector(browser):
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
    test_data = "MacBook"
    input_box = browser.find_element_by_class_name(MainPage.search_input_class_name)
    input_box.send_keys(test_data)
    browser.find_element_by_class_name(MainPage.search_button_class_name).click()
    found_search_elms = browser.find_elements_by_class_name(SearchPage.search_div_elems_class_name)
    for elm in found_search_elms:
        caption = elm.find_element_by_class_name("caption")
        assert test_data in caption.find_element_by_tag_name("a").text


def test_element_by_xpath(browser):
    """
    Проверка появления алерт-div блока при добавлении в желаемое
    шаги:
    1.Нажать на первое изображение товара
    2.Нажать на кнопку 'добавить в favorites'
    3.Проверить появление алерта
    :param browser:
    :return:
    """
    browser.find_element_by_xpath(MainPage.promo_element_xpath).click()
    browser.find_element_by_xpath(ProductPage.add_wishlist_xpath).click()
    browser.find_element_by_xpath("//div[@class='alert,alert alert-success alert-dismissible']")#непонятно почему нельзя обратиться по классу через xpath
    #Ведь в нем появляется такой блок <div class="alert alert-success alert-dismissible">
    browser.find_element_by_class_name("alert-success")#но таким способом получается нормально


def test_element_by_id(browser):
    """
    Проверка наличия Div блоков с товарами в разделе, в который они добавлены
    Предусловия:в каталог добавлены товары типа Phones & PDAs
    шаги:
    1.Найти меню
    2.Нажать на элемент по текстовому линку Phones & PDAs
    3.Проверить наличие DIV блоков с товарами и возможность наведения на них
    :param browser:
    :return:
    """
    menu = browser.find_element_by_id(MainPage.menu_id)
    menu.find_element_by_link_text("Phones & PDAs").click()
    products = browser.find_elements_by_class_name("product-thumb")
    for product in products:
        ActionChains(browser).move_to_element(product).pause(2).perform()




def test_element_by_link_text(browser):
    """
    шаги:
    1.Найти раздел с Laptops & Notebooks
    2.Раскрыть выпадающий список с ссылками
    3.Зайти на страницу каталога
    4.Сверить то, что мы попали действительно на нужную страницу каталога по её заголовку
    :param browser:
    :return:
    """
    laptop_link = browser.find_element_by_link_text("Laptops & Notebooks")
    ActionChains(browser).move_to_element(laptop_link).pause(2).perform()
    browser.find_element_by_link_text("Show All Laptops & Notebooks").click()
    h2 = browser.find_element_by_tag_name("h2")
    assert h2.text == "Laptops & Notebooks"



def test_elements_by_css_selector(browser):
    top_right_links = browser.find_element_by_css_selector("ul.pull-right")
    top_right_links.find_element_by_xpath("//a[@title='My Account']").click()
    browser.find_element_by_link_text("Register").click()
    content = browser.find_element_by_id("content")
    a = content.find_element_by_id("account")
    inputs = a.find_element_by_tag_name("input")
    inputs.click()
    #inputs.send_keys("111")
    print(inputs.tag_name)






    #content = browser.find_element_by_css_selector(SearchPage.content_css_class)
    #h1 = content.find_element_by_tag_name("h1")
    #assert h1.text == "Search"