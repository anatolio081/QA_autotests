from locators.user import SearchPage

class SearchPage:

    def __init__(self,browser):
        self.browser = browser

    def get_search_result_captions(self):
        captions = []
        found_elms = (self.browser.find_elements_by_class_name(SearchPage.Content.found_products['class_name']))
        for elm in found_elms:
            caption = elm.find_element_by_class_name(SearchPage.Content.product_caption['class_name'])
            captions.append(caption.find_element_by_tag_name(SearchPage.Content.product_link['tag']).text)
        return captions

    def check_result(self):
        pass