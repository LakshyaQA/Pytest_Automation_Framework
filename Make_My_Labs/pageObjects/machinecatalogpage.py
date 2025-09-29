import time
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Common_Packages.Utility.custom_logger import custom_logger


class Machinecatalogpage(Basepage, metaclass=Logmethodmeta):
    def __init__(self, driver):
        super().__init__(driver)

    # locator
    search_xpath = "//input[@placeholder='Search']"
    machine_catalog_option_xpath = "//span[contains(text(),'Machine Catalog')]"
    create_catalog_button_xpath = "//button[@class='ant-btn ant-btn-primary create-catalog-btn qa-createCatalog-btn']"
    machine_menu_option_xpath = ("//*[@id='app-content-id']/section/section/section/main/div[3]/div/div/div["
                                 "4]/div/div[1]/button[2]")
    machin_edit_option_xpath = "//span[normalize-space()='Edit']"
    name_id = 'display_name'
    catalog_name = "//input[@id='display_name']"
    input_lab_type_xpath = "//input[@id='template_type']"
    input_lab_type_list_xpath = ("//div[@class='ant-select-item-option-content' and contains(text(),'Guided Lab') or "
                                 "contains(text(),'Standalone')]")
    publisher_id = "publisher_name"
    sku_checkbox = "//tbody[@class='ant-table-tbody']//tr//td//input[@type='checkbox']"
    sku1_xpath = "(//input[@type='checkbox'])[2]"
    sku2_xpath = "(//input[@type='checkbox'])[3]"
    sku3_xpath = "(//input[@type='checkbox'])[4]"
    create_button_xpath = "//button[@type='submit']"
    back_button_xpath = "//*[contains(@class,'qa-cancel-btn')]"
    verify_catalog_xpath = "//span[normalize-space()='shab']"
    add_more_sku_xpath = "//*[contains(@class,'qa-add-more-sku')]"
    threedot_action_xpath = "//*[@class='ant-btn ant-btn-default ant-btn-icon-only ant-dropdown-trigger']"
    edit_cancel_xpath = '//button/span[text()="Cancel"]'
    edit_save_xpath = '//button/span[text()="Save Changes"]'
    add_more_in_add_more_sku_xpath = "//*[contains(@class,'qa-add-sku')]"
    close_logo_in_add_more_xpath = '//span[@aria-label="close"]'
    edit_retire_xpath = '//button/span[text()="Retire"]'
    retire_cancel_xpath = '//button/span[text()="Cancel"]'
    retire_retire_xpath = '//button/span[text()="Retire"]'
    calender_retire_xpath = 'skulist_category_data'
    sku_table_headers_xpath = '//*[@id="app-content-id"]//table/thead/tr'
    sku_head_item = ['Title', 'Category', 'SKU Description', 'Retiring Date']
    first_row_Sku_xpath = '//*[@id="app-content-id"]//table/tbody/tr[2]/td[1]'
    threeDot_option_retire_date_xpath = '//span[text()="Retiring Date"]'
    threeDot_option_remove_xpath = '//span[text()="Remove"]'
    SKU_table_rows_xpath = '//*[@id="app-content-id"]//table/tbody/tr'
    edit_name_variable = "Automation Testing"
    catalog_list_xpath = '//div[@class="card-body-container"]/div/div[2]/div'
    decommisioned_option_xpath = "//input[@value='6']"
    publish_option_xpath = "//input[@value='4']"
    publish_button_xpath = "//button[@type='submit']/span[contains(text(),'Publish')]"
    delete_option_xpath = "//span[normalize-space()='Delete']"
    delete_button_xpath = "//button[@type='submit']/span[contains(text(),'Delete')]"
    delete_template_xpath = "//*[contains(@class,'qa-public-details-delete pointer-cursor')]"
    delete_under_template_xpath = "//*[contains(@class,'qa-delete-vm-proceed')]"
    delete_batch_xpath = "//*[contains(@class,'qa-tenant-delete')]"
    private_cloud_xpath = "//h1[normalize-space()='Private Cloud']"
    public_cloud_xpath = "//h1[normalize-space()='Public Cloud']"
    view_template_xpath = "//span[normalize-space()='View Template']"
    add_batch_from_template_xpath = "//button[normalize-space()='Add Batch']"
    batch_name_xpath = "//input[@id='batch_name']"
    tenant_xpath = "//input[@id='tenantInfiniteScroll12e']"
    description_xpath = "//*[@placeholder='Description']"
    start_date_placeholder_id = "start_date"
    start_date_xpath = ("//*[@class='ant-picker-cell ant-picker-cell-disabled ant-picker-cell-in-view "
                        "ant-picker-cell-today']/./following-sibling::*[@class='ant-picker-cell "
                        "ant-picker-cell-in-view'][1]")
    end_date_xpath = "//input[@id='end_date']"
    enter_date_xpath = ("//td[contains(@title,'2024-11-30')]//div[contains(@class,'ant-picker-cell-inner')]["         
                        "normalize-space()='30']")
    user_dropdown_xpath = "//input[@id='users']"
    add_batch_btn_xpath = "//button[@type='submit']"
    add_lab_xpath = "//span[normalize-space()='Add Labs']"
    iiht_Admin_xpath = "//div[text()='IIHT Admin']"
    back_batch_button_xpath = "//h1[@class='ant-typography sub-heading mouse-pointer']"
    batch_publish_xpath = "//*[contains(@class,'qa-publish-btn')]"
    cancel_button_xpath = "//span[normalize-space()='Cancel']"
    cancel_inner_xpath = "//span[normalize-space()='Discard']"
    machine_catalog_menu_xpath = "//*[contains(@class,'qa-catalogues')]//a[@href='/machineCatalogue']"
    standalone_xpath = "//div[contains(@class,'ant-select-item-option-content')][normalize-space()='Standalone']"
    verification_element_xpath = "//div[text()='Automation Edited Catalog']"
    pooled_template_checkbox = "//input[@id='is_pooled_template']"
    my_labs_button_xpath = "//button[@class='ant-btn ant-btn-primary qa-vm-approval-proceed']"
    enroll_button_xpath = "//button[@class='ant-btn ant-btn-primary btn-small qa-enroll-btn']"

    def click_create_catalog_button(self):
        self.wait_for_element(self.create_catalog_button_xpath, locator_type="xpath")
        self.element_click(self.create_catalog_button_xpath,
                           locator_type="xpath")

    def search_catalog(self, catalog_name):
        self.wait_for_element(self.search_xpath, locator_type="xpath")
        self.send_keys(catalog_name, self.search_xpath, locator_type="xpath")
        time.sleep(2)

    def click_publish_option(self, catalog_name):
        catalog_xpath = (f"//span[@class='ant-typography qa-class-machinecatalog-{catalog_name}']//parent::*["
                         f"span]//parent::*["
                         "@class='ant-card-meta-title']//parent::*[@class='ant-card-meta-detail']//parent::*["
                         "@class='ant-card-meta']//parent::*[@class='card-body-container']//parent::*["
                         "@class='ant-ribbon-wrapper']//span//input[@value='4']")
        self.wait_for_element(catalog_xpath, locator_type="xpath")
        self.element_click(catalog_xpath, locator_type="xpath")

    def click_publish_button(self):
        self.wait_for_element(self.publish_button_xpath, locator_type="xpath")
        self.element_click_js(self.publish_button_xpath, locator_type="xpath")

    def publish_catalog(self, catalog_name):
        time.sleep(1)
        self.click_publish_option(catalog_name)
        time.sleep(1)
        self.click_publish_button()
        time.sleep(2)

    def publish_selected(self, catalog_name):
        catalog_xpath = (f"//span[@class='ant-typography qa-class-machinecatalog-{catalog_name}']//parent::*["
                         f"span]//parent::*["
                         "@class='ant-card-meta-title']//parent::*[@class='ant-card-meta-detail']//parent::*["
                         "@class='ant-card-meta']//parent::*[@class='card-body-container']//parent::*["
                         "@class='ant-ribbon-wrapper']//span//input[@value='4']")
        return self.is_radio_button_checked(catalog_xpath, locator_type="xpath")

    def enter_name(self, catalogname):
        self.wait_for_element(self.catalog_name, locator_type="xpath")
        self.send_keys(catalogname, self.catalog_name, locator_type="xpath")

    def select_lab_type(self, labtype):
        self.wait_for_element(self.input_lab_type_xpath, locator_type="xpath")
        self.select_dropdown_by_name(labtype, self.input_lab_type_xpath, self.input_lab_type_list_xpath)

    def click_pooled_template_checkbox(self):
        self.wait_for_element(self.pooled_template_checkbox, locator_type="xpath")
        self.element_click(self.pooled_template_checkbox, locator_type="xpath")

    def published_sku_search_box(self, template_name):
        self.wait_for_element(self.search_xpath, locator_type="xpath")
        self.send_keys(template_name, self.search_xpath, locator_type="xpath")

    def select_sku1(self):
        self.wait_for_element(self.sku_checkbox, locator_type="xpath")
        self.element_click(self.sku_checkbox, locator_type="xpath")

    def click_create_button(self):
        self.wait_for_element(self.create_button_xpath, locator_type="xpath")
        self.element_click(self.create_button_xpath, locator_type="xpath")

    def machine_catalog_verify(self, catalog_name):
        catalog_xpath = (f"//span[contains(@class,'{catalog_name}')]//parent::span//parent"
                         "::div//parent::div//parent::div//parent::div//following-sibling::div["
                         "contains(@class,'card-description')]//span[contains(text(), 'Published')]")
        self.wait_for_element(catalog_xpath, locator_type="xpath", timeout=60)
        return self.get_page_source()

    def create_catalog(self, catalogname, labtype, template_name):
        time.sleep(2)
        self.click_create_catalog_button()
        self.enter_name(catalogname)
        self.select_lab_type(labtype)
        self.published_sku_search_box(template_name)
        self.select_sku1()
        self.click_create_button()
        time.sleep(2)

    def create_catalog_pooled(self, catalogname, labtype, template_name):
        time.sleep(2)
        self.click_create_catalog_button()
        self.enter_name(catalogname)
        self.select_lab_type(labtype)
        self.click_pooled_template_checkbox()
        self.published_sku_search_box(template_name)
        self.select_sku1()
        self.click_create_button()
        time.sleep(2)

    def create_catalog_guided(self, catalogname, labtype, template_name):
        time.sleep(2)
        self.click_create_catalog_button()
        self.enter_name(catalogname)
        self.select_lab_type(labtype)
        self.published_sku_search_box(template_name)
        self.select_sku1()
        self.click_create_button()
        time.sleep(2)

    def click_my_labs_button(self):
        self.wait_for_element(self.my_labs_button_xpath, locator_type="xpath")
        self.element_click(self.my_labs_button_xpath, locator_type="xpath")

    def click_enroll_button(self):
        time.sleep(1)
        self.wait_for_element(self.enroll_button_xpath, locator_type="xpath")
        self.element_click_js(self.enroll_button_xpath, locator_type="xpath")

    def select_private_lab_type(self, labtype):
        checkbox = f"//span[contains(text(),'{labtype}')]"
        self.wait_for_element(checkbox, locator_type="xpath")
        time.sleep(2)
        self.element_click(checkbox, locator_type="xpath")
        time.sleep(1)
