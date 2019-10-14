from locators.user import ProductPage


class ProductPage:
    def __init__(self, browser):
        self.browser = browser

    def get_content(self):
        content = self.browser.find_element_by_id(ProductPage.Content.it['id'])
        return content