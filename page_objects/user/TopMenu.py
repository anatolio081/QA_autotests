from page_objects.user.MainPage import MainPage

class TopMenu(MainPage):

    def __init__(self, browser):
        self.browser = browser


    def open_register_form(self):
        self.browser.find_element_by_xpath(MainPage.TopLinks.MyAccount.it['xpath']).click()
        self.browser.find_element_by_link_text("Register").click()

