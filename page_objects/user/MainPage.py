from page_objects import BasePage
from locators.user import MainPage, Common


class MainPage(BasePage):

    def __init__(self, browser):
        self.driver = browser

    def enter_search_data(self, data):
        input_box = self.browser.find_element_by_class_name(MainPage.SearchBlock.search_input_class_name['class_name'])
        input_box.send_keys(data)

    def use_search_(self):
        self.browser.find_element_by_class_name(MainPage.SearchBlock.search_button_class_name['class_name']).click()

    def click_first_featured_product(self):
        featured = self.browser.find_element_by_xpath(MainPage.Featured.it['xpath'])
        featured.find_element_by_class_name(MainPage.Featured.add_wishlist_class_name['class_name']).click()

    def check_alert_appear(self):
        self.browser.find_element_by_css_selector(Common.alert.success.it['css'])

    def click_ALL_Phones_and_PDA_Link(self):
        menu = self.browser.find_element_by_id(MainPage.Menu.it['id'])
        menu.find_element_by_link_text(MainPage.Menu.phones_pdas_txt_link['text_link']).click()

    def click_ALL_Laptops_and_notebook_Link(self):
        menu = self.browser.find_element_by_id(MainPage.Menu.it['id'])
        laptop_link = menu.find_element_by_link_text(MainPage.Menu.LaptopsAndNotebooks.it['text_link']).click
        self.browser.find_element_by_link_text(MainPage.Menu.LaptopsAndNotebooks.all_txt_link['text_link']).click()

    def get_text_Laptop_and_notebook_text(self):
        menu = self.browser.find_element_by_id(MainPage.Menu.it['id'])
        laptop_notebook_link = menu.find_element_by_link_text(MainPage.Menu.LaptopsAndNotebooks.it['text_link'])
        return laptop_notebook_link

