class AdmProductPage:
    add_button_xpath = "//a[@data-original-title='Add New']"
    save_button_xpath = "//button[@data-original-title='Save']"
    delete_button_xpath = "//button[@data-original-title='Delete']"
    edit_button_xpath = "//a[@data-original-title='Edit']"
    product_table_xpath = "//table[@class='table table-bordered table-hover']//tbody"
    table_statistic_xpath = "//div[@class='col-sm-6 text-right']"

    product_name_id = "input-name1"
    product_meta_id = "input-meta-title1"
    filter_input_id = "input-name"
    filter_button_id = "button-filter"
    data_input_model_id = "input-model"

    data_link_text = "Data"

    row_tag = "tr"
    cell_tag = "td"
