class AdmProductPage:
    class TopRightButtons:
        it = {'class': 'pull-right'}
        add_button_xpath = {"xpath": "//a[@data-original-title='Add New']"}
        delete_button_xpath = {"xpath": "//button[@data-original-title='Delete']"}
        save_button_xpath = {"xpath": "//button[@data-original-title='Save']"}

    class ProductList:
        it = {"xpath": "//table[@class='table table-bordered table-hover']//tbody"}
        edit_button_xpath = {"xpath": "//a[@data-original-title='Edit']"}
        row_tag = {"tag": "tr"}
        cell_tag = {"tag": "td"}
        product_statistic_xpath = {"xpath": "//div[@class='col-sm-6 text-right']"}

    class Filter:
        filter_input_id = {"id": "input-name"}
        filter_button_id = {"id": "button-filter"}

    class ProductPage:
        product_name_id = {"id": "input-name1"}
        product_meta_id = {"id": "input-meta-title1"}
        data_input_model_id = {"id": "input-model"}
        data_link_text = {"link_text": "Data"}