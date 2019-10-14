from locators.user import CatalogPage

class CatalogPage:
    def __init__(self, browser):
        self.browser = browser

    def get_catalog_header_text(self):
        header = self.browser.find_element_by_tag_name(CatalogPage.Content.headet_tag['tag'])
        return header