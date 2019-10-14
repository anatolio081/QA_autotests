from typing import Dict


class MainPage:
    """
    Класс для локаторов основной страницы
    """

    class Menu:
        it = {"id": "menu"}
        phones_pdas_txt_link = {'text_link': 'Phones & PDAs'}
        class LaptopsAndNotebooks:
            it = {'text_link': 'Laptops & Notebooks'}
            all_txt_link = {'text_link': 'Show All Laptops & Notebooks'}

    class SearchBlock:
        search_input_class_name = {'class_name': 'input-lg'}
        search_button_class_name = {'class_name': 'btn-lg'}

    class Content:
        it = {'id': 'content'}
        promo_element_xpath = {'xpath': '//div[@class="swiper-viewport"]'}

    class TopLinks:
        it = {'id': 'top-links'}
        class MyAccount:
            it = {'xpath': '//a[@title="My Account"]'}
            register_text_link = {'text_link': 'Register'}


    class Featured:
        it = {'xpath': '//*[@id="content"]/div[2]'}
        add_wishlist_class_name = {'class_name': 'fa-heart'}
