import time
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Make_My_Labs.Configration.configpath import UploadFile


class Createtemplatepage(Basepage, metaclass=Logmethodmeta):

    def __init__(self, driver):
        super().__init__(driver)

    # Create Template page objects

    add_category_xpath = "//div[@id='categoryInfiniteScroll']//span/input"
    add_category_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder']//div[@class='rc-virtual-list-holder-inner']//div//div"
    os_platform_id = "os_platform"
    os_platform_xpath = "//input[@id='os_platform']"
    os_platform_list_xpath = "//div[@class='ant-select-item-option-content' and contains(text(),'Windows') or contains(text(),'Linux')]"
    pooled_template_tab = "//h1[normalize-space()='Pooled Templates']"
    display_name_xpath = "//div[@class='ant-form-item-control-input-content']//input[@id='display_name']"
    description_xpath = "//textarea[@placeholder='Description']"
    naming_prefix_id = "naming_prefix"
    naming_prefix_xpath = "//input[@id='naming_prefix']"
    admin_user_id = "admin_user_name"
    admin_user_xpath = "//input[@id='admin_user_name']"
    admin_password_id = "admin_password"
    admin_password_xpath = "//input[@id='admin_password']"
    enable_linked_clone_id = "is_linked_clone_enabled"
    enable_linked_clone_xpath = "//button[@id='is_linked_clone_enabled']"
    vt_enable_id = "is_vt_enabled"
    vt_enable_xpath = "//button[@id='is_vt_enabled']"
    base_vm_folder_name_id = "base_vm_folder_name"
    base_vm_folder_name_xpath = "//input[@id='base_vm_folder_name']"
    base_vm_folder_name_list_xpath = "//div[@class='rc-virtual-list-holder-inner']//div[@class='ant-select-item-option-content']"
    base_vm_name_id = "base_vm_name"
    base_vm_name_xpath = "//input[@id='base_vm_name']"
    base_vm_name_list_xpath = "//div[@class='rc-virtual-list-holder-inner']//div[@class='ant-select-item-option-content']"

    base_vm_snapshots_name_id = "base_vm_snapshot_name"
    base_vm_snapshots_name_xpath = "//input[@id='base_vm_snapshot_name']"

    base_vm_snapshots_name_list_xpath = "//div[@class='rc-virtual-list-holder-inner']//div[@class='ant-select-item-option-content']"
    instance_size_xpath = "//div[@id='instanceInfiniteScroll']//span/input"
    instance_size_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div//div[@class='ant-select-item-option-content' and contains(text(),'CPU')]"
    is_enable_for_provisioning_id = "is_provisioning_enabled"
    is_enable_for_provisioning_xpath = "//button[@id='is_provisioning_enabled']"
    create_template_button_xpath = "//button[@class='ant-btn ant-btn-primary qa-createTemplate-btn']"
    cancel_button_xpath = "//*[contains(@class,'qa-cancel')]"
    row_data = "//tbody/tr[7]"
    standard_network_xpath = "//span[@class='ant-typography body-short-text'][normalize-space()='Standard Network']"
    network_name_xpath = "//input[@id='network_name']"
    resource_xpath = "//div[@class='ant-typography ant-typography-ellipsis ant-typography-single-line tooltip-text undefined']"
    create_template_option_xpath = "//button[@type='submit']"
    search_placeholder_xpath = "//input[@placeholder='Search']"
    delete_template_xpath = "//*[contains(@class,'qa-delete')]"
    edit_template_xpath = "//*[contains(@class,'qa-editUserDetails')]"
    edit_button_xpath = "//*[contains(@class,'qa-add')]"
    delete_button_xpath = "//span[normalize-space()='Delete']"
    publish_button_xpath = "//*[contains(@class,'qa-publish')]"
    sku_name_input_xpath = "//input[@name='role']"
    description_box_xpath = "//*[@placeholder='Enter Description']"
    inner_publish_button_xpath = "//*[contains(@class,'qa-action')]"
    machine_catalog_menu_option_xpath = "//span[contains(text(),'Machine Catalog')]"
    search_bar_xpath = "//input[@placeholder='Search']"
    option_xpath = "//*[@class='ant-btn ant-btn-default ant-btn-icon-only ant-dropdown-trigger']"
    edit_option_xpath = "//span[normalize-space()='Edit']"
    sku_list_xpath = '//*[@class="ant-table-row ant-table-row-level-0"]'
    sku_menu_xpath = "//button[@class='ant-btn ant-btn-default ant-btn-icon-only ant-dropdown-trigger']"
    remove_sku_option_xpath = "//span[contains(text(),'Remove')]"
    remove_sku_button_xpath = "//button[@type='submit']/span[contains(text(),'Remove')]"
    sku_save_changes_button_xpath = "//button[@type='submit']/span[contains(text(),'Save Changes')]"
    discard_button_xpath = "//span[normalize-space()='Discard']"
    cloud_display_name_id = "template_name"
    validity_day_id = "validity"
    programmatic_access_id = "programmatic_access"
    self_enroll_id = "self_enroll"
    is_duration_based_id = "is_duration"
    credit_based_id = "credit"
    browse_file_button_xpath = "//*[contains(@class,'small qa-browse-btn')]"
    upload_xpath = "//span[@class='ant-upload ant-upload-btn']/input[@type='file']"
    public_cloud_xpath = "//h1[normalize-space()='Public Cloud']"
    view_template_xpath = "//span[normalize-space()='View Template']"
    standalone_xpath = "//p[contains(text(),'Create a regular template')]"
    next_button_xpath = "//button[contains(@type,'submit')]"
    select_resource_provider_dropdown_xpath = "//input[@id='provider_name']"
    select_resource_provider_dropdown_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder']//div[@class='rc-virtual-list-holder-inner']//div//div"
    searchbox_xpath = "//span[@class='ant-input-affix-wrapper my1']"
    create_template_button = "//div[@class='sub-header-right']//button[@class='ant-btn ant-btn-primary qa-createTemplate-btn']"
    connection_name = "//table//th//div//span[contains(text(),'Connection Name')]"
    guided_lab_xpath = "//span[normalize-space()='Guided Lab']"
    standalone_lab_xpath = "//span[normalize-space()='Standalone']"
    pooled_template_checkbox_xpath = "//input[@id='is_pooled_template']"
    no_of_VM_xpath = "//input[@id='no_of_vms']"
    lab_type_xpath = "//input[@id='pooled_lab_type']"
    lab_type_list_xpath = "//div[@class='ant-select-item-option-content' and contains(text(),'Persistent') or contains(text(),'Non Persistent')]"
    dvs_network_xpath = "//span[contains(text(),'DVS Network')]"
    created_template_success_message = "//div[@class='ant-notification-notice-message' and contains(text(),'Template created successfully.')]"
    publish_checkbox_xpath = "//tbody/tr[contains(@data-row-key,'')][2]//input[@type='checkbox']"
    republish_text_xpath = "//div[@class='republish-btn']"

    def select_resource_provider_dropdown(self, resource_provider_name):
        self.wait_for_element(
            self.select_resource_provider_dropdown_xpath, locator_type="xpath")
        self.select_dropdown_by_name(resource_provider_name, self.select_resource_provider_dropdown_xpath,
                                     self.select_resource_provider_dropdown_list_xpath)

    def search_private_resource_provider_input(self, connection_name):
        self.send_keys(connection_name, self.searchbox_xpath, locator_type="xpath")

    def click_connection_name(self, connection_name):
        connection_list_name_to_click = f"//u//div[contains(text(),'{connection_name}')]"
        self.wait_for_element(connection_list_name_to_click,
                              locator_type="xpath")
        self.element_click_js(
            connection_list_name_to_click, locator_type="xpath")

    def reach_template_page(self, resource_provider_name, connection_name, type_of_template):
        self.select_resource_provider_dropdown(resource_provider_name)
        time.sleep(1)
        self.click_connection_name(connection_name)
        time.sleep(1)
        self.click_create_template_buttons()
        self.select_template_type(type_of_template)
        self.click_next_button()

    def click_create_template_button(self):
        self.element_click(self.create_template_button, locator_type="xpath")

    def select_template_type(self, type):
        if type == "Guided Lab":
            self.wait_for_element(self.guided_lab_xpath, locator_type="xpath")
            self.element_click(self.guided_lab_xpath, locator_type="xpath")
        if type == "Standalone":
            self.wait_for_element(self.standalone_lab_xpath,
                                  locator_type="xpath")
            self.element_click(self.standalone_lab_xpath, locator_type="xpath")

    def click_next_button(self):
        self.wait_for_element(self.next_button_xpath, locator_type="xpath")
        self.element_click(self.next_button_xpath, locator_type="xpath")

    def click_create_template_buttons(self):
        self.wait_for_element(
            self.create_template_button_xpath, locator_type="xpath")
        self.element_click_js(
            self.create_template_button_xpath, locator_type="xpath")

    def click_create_template_option(self):
        self.element_click_js(
            self.create_template_option_xpath, locator_type="xpath")

    def click_add_category_dropdown(self, add_category):
        self.send_keys(add_category, self.add_category_xpath, locator_type="xpath")
        time.sleep(2)
        self.select_element_keyboard(add_category, self.add_category_xpath, locator_type="xpath")

    def click_os_platform_dropdown(self, platform_type):
        self.select_dropdown_by_name(
            platform_type, self.os_platform_xpath, self.os_platform_list_xpath)

    def enter_display_name(self, display_name):
        self.send_keys(display_name, self.display_name_xpath, locator_type="xpath")

    def enter_description(self, description):
        self.send_keys(description, self.description_xpath, locator_type="xpath")

    def click_pooled_template_checkbox(self, status, no_of_vm, lab_type):
        if status == "Yes":
            self.element_click(
                self.pooled_template_checkbox_xpath, locator_type="xpath")
            self.send_keys(no_of_vm, self.no_of_VM_xpath, locator_type="xpath")
            self.select_dropdown_by_name(
                lab_type, self.lab_type_xpath, self.lab_type_list_xpath)

    def enter_naming_prefix_option(self, naming_prefix):
        self.send_keys(naming_prefix, self.naming_prefix_xpath, locator_type="xpath")

    def enter_admin_username(self, username):
        self.send_keys(username, self.admin_user_xpath, locator_type="xpath")

    def enter_admin_password(self, password):
        self.send_keys(password, self.admin_password_xpath, locator_type="xpath")

    def click_enable_linked_clone_button(self, status):
        if status == "Yes":
            self.element_click(
                self.enable_linked_clone_xpath, locator_type="xpath")

    def select_network_type(self, type_of_network, standard_type_of_network):
        if type_of_network == "DVS Network":
            self.wait_for_element(self.dvs_network_xpath, locator_type="xpath")
            self.element_click(self.dvs_network_xpath, locator_type="xpath")
        if type_of_network == "Standard Network":
            self.wait_for_element(self.standard_network_xpath,
                                  locator_type="xpath")
            self.element_click(self.standard_network_xpath,
                               locator_type="xpath")
            self.wait_for_element(self.network_name_xpath, locator_type="xpath")
            network_name_list_xpath = f"//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder']//div[@class='rc-virtual-list-holder-inner']//div//div[contains(text(),'{standard_type_of_network}')]"
            self.select_dropdown_by_name(
                standard_type_of_network, self.network_name_xpath, network_name_list_xpath)

    def click_vt_enable_button(self, status):
        if status == "Yes":
            self.element_click(self.vt_enable_xpath, locator_type="xpath")

    def click_base_vm_folder_name_dropdown(self, base_vm_folder_name):
        self.wait_for_element(self.base_vm_folder_name_xpath,
                              locator_type="xpath")
        self.select_dropdown_by_name(base_vm_folder_name, self.base_vm_folder_name_xpath,
                                     self.base_vm_folder_name_list_xpath)

    def click_base_vm_name_dropdown(self, base_vm_name):
        self.select_dropdown_by_name(
            base_vm_name, self.base_vm_name_xpath, self.base_vm_name_list_xpath)
        base_vm_name_list_first_dropdown_xpath = (f"//div[@class='rc-virtual-list']//div["
                                                  f"@class='rc-virtual-list-holder-inner']//div[contains(@label,"
                                                  f"'{base_vm_name}')]")
        self.wait_for_element(
            base_vm_name_list_first_dropdown_xpath, locator_type="xpath", timeout=120)
        self.element_click(
            base_vm_name_list_first_dropdown_xpath, locator_type="xpath")

    def click_base_vm_snapshots_name_dropdown(self, base_vm_snapshots_name):
        self.select_dropdown_by_name(base_vm_snapshots_name, self.base_vm_snapshots_name_xpath,
                                     self.base_vm_snapshots_name_list_xpath)
        base_vm_snapshots_name_list_first_dropdown_xpath = (f"//div[@class='rc-virtual-list']//div["
                                                            f"@class='rc-virtual-list-holder-inner']//div[contains("
                                                            f"@label,'{base_vm_snapshots_name}')]")
        self.wait_for_element(
            base_vm_snapshots_name_list_first_dropdown_xpath, locator_type="xpath", timeout=120)
        self.element_click(
            base_vm_snapshots_name_list_first_dropdown_xpath, locator_type="xpath")

    def click_instance_size_dropdown(self, instance_size):
        self.wait_for_element(self.instance_size_xpath, locator_type="xpath")
        # self.select_dropdown_by_name(
        #     instance_size, self.instance_size_xpath, self.instance_size_list_xpath)
        self.send_keys(instance_size, self.instance_size_xpath, locator_type="xpath")
        time.sleep(2)
        self.select_element_keyboard(instance_size, self.instance_size_xpath, locator_type="xpath")

    def click_is_enable_for_provisioning_button(self, status):
        if status == "Yes":
            self.element_click(
                self.is_enable_for_provisioning_xpath, locator_type="xpath")

    def upload_guided_lab_instructions(self):
        self.upload_file(UploadFile.json_data_file(
            "\\guided_lab_instructions.json"), self.browse_file_button_xpath, locator_type="xpath")

    def click_pooled_template_tab(self):
        self.wait_for_element(self.pooled_template_tab, locator_type="xpath")
        self.element_click(self.pooled_template_tab, locator_type="xpath")

    def search_template(self, templatename):
        self.send_keys(templatename, self.search_placeholder_xpath, locator_type="xpath")

    def verify_created_template(self):
        return self.get_text(self.created_template_success_message, locator_type="xpath")

    def creating_template_and_publish(self, add_category, platform_type, display_name, description,
                                      pooled_template_status,
                                      no_of_vm, lab_type, naming_prefix, admin_username, admin_password,
                                      enable_linked_clone_status,
                                      vt_enable_status, is_enable_for_provisioning_status, base_vm_folder_name,
                                      base_vm_name,
                                      base_vm_snapshots_name, instance_size, type_of_network, standard_type_of_network,
                                      template_name_search):
        self.click_add_category_dropdown(add_category)
        self.click_os_platform_dropdown(platform_type)
        self.enter_display_name(display_name)
        self.enter_description(description)
        self.click_pooled_template_checkbox(
            pooled_template_status, no_of_vm, lab_type)
        self.enter_naming_prefix_option(naming_prefix)
        self.enter_admin_username(admin_username)
        self.enter_admin_password(admin_password)
        self.click_enable_linked_clone_button(enable_linked_clone_status)
        self.click_vt_enable_button(vt_enable_status)
        self.click_is_enable_for_provisioning_button(
            is_enable_for_provisioning_status)
        time.sleep(1)
        self.click_base_vm_folder_name_dropdown(base_vm_folder_name)
        time.sleep(1)
        self.click_base_vm_name_dropdown(base_vm_name)
        time.sleep(1)
        self.click_base_vm_snapshots_name_dropdown(base_vm_snapshots_name)
        time.sleep(1)
        self.click_instance_size_dropdown(instance_size)
        time.sleep(1)
        self.select_network_type(type_of_network, standard_type_of_network)
        time.sleep(1)
        self.click_create_template_option()
        time.sleep(1)
        self.search_template(template_name_search)
        time.sleep(1)
        self.click_publish_button()
        time.sleep(1)
        self.click_inner_publish_button()
        time.sleep(1)

    def creating_pooled_template_and_publish(self, add_category, platform_type, display_name, description,
                                             pooled_template_status,
                                             no_of_vm, lab_type, naming_prefix, admin_username, admin_password,
                                             enable_linked_clone_status,
                                             vt_enable_status, is_enable_for_provisioning_status, base_vm_folder_name,
                                             base_vm_name,
                                             base_vm_snapshots_name, instance_size, type_of_network,
                                             standard_type_of_network,
                                             template_name_search):
        self.click_add_category_dropdown(add_category)
        self.click_os_platform_dropdown(platform_type)
        self.enter_display_name(display_name)
        self.enter_description(description)
        self.click_pooled_template_checkbox(
            pooled_template_status, no_of_vm, lab_type)
        self.enter_naming_prefix_option(naming_prefix)
        self.enter_admin_username(admin_username)
        self.enter_admin_password(admin_password)
        self.click_enable_linked_clone_button(enable_linked_clone_status)
        self.click_vt_enable_button(vt_enable_status)
        self.click_is_enable_for_provisioning_button(
            is_enable_for_provisioning_status)
        time.sleep(1)
        self.click_base_vm_folder_name_dropdown(base_vm_folder_name)
        time.sleep(1)
        self.click_base_vm_name_dropdown(base_vm_name)
        time.sleep(1)
        self.click_base_vm_snapshots_name_dropdown(base_vm_snapshots_name)
        time.sleep(1)
        self.click_instance_size_dropdown(instance_size)
        time.sleep(1)
        self.select_network_type(type_of_network, standard_type_of_network)
        time.sleep(1)
        self.click_create_template_option()
        time.sleep(1)
        self.click_pooled_template_tab()
        time.sleep(1)
        self.search_template(template_name_search)
        time.sleep(1)
        self.click_publish_button()
        time.sleep(1)
        self.click_inner_publish_button()
        time.sleep(1)

    def creating_guided_lab_template_and_publish(self, add_category, platform_type, display_name, description,
                                                 pooled_template_status,
                                                 no_of_vm, lab_type, naming_prefix, admin_username, admin_password,
                                                 enable_linked_clone_status,
                                                 vt_enable_status, is_enable_for_provisioning_status,
                                                 base_vm_folder_name,
                                                 base_vm_name,
                                                 base_vm_snapshots_name, instance_size, type_of_network,
                                                 standard_type_of_network,
                                                 template_name_search):
        self.click_add_category_dropdown(add_category)
        self.click_os_platform_dropdown(platform_type)
        self.enter_display_name(display_name)
        self.enter_description(description)
        self.click_pooled_template_checkbox(
            pooled_template_status, no_of_vm, lab_type)
        self.enter_naming_prefix_option(naming_prefix)
        self.enter_admin_username(admin_username)
        self.enter_admin_password(admin_password)
        self.click_enable_linked_clone_button(enable_linked_clone_status)
        self.click_vt_enable_button(vt_enable_status)
        self.click_is_enable_for_provisioning_button(
            is_enable_for_provisioning_status)
        time.sleep(1)
        self.click_base_vm_folder_name_dropdown(base_vm_folder_name)
        time.sleep(1)
        self.click_base_vm_name_dropdown(base_vm_name)
        time.sleep(1)
        self.click_base_vm_snapshots_name_dropdown(base_vm_snapshots_name)
        time.sleep(1)
        self.click_instance_size_dropdown(instance_size)
        time.sleep(1)
        self.select_network_type(type_of_network, standard_type_of_network)
        time.sleep(1)
        self.upload_guided_lab_instructions()
        time.sleep(1)
        self.click_create_template_option()
        time.sleep(1)
        self.search_template(template_name_search)
        time.sleep(1)
        self.click_publish_button()
        time.sleep(1)
        self.click_inner_publish_button()
        time.sleep(1)

    def click_publish_button(self):
        self.element_click_js(self.publish_checkbox_xpath,
                              locator_type="xpath")
        self.element_click_js(self.publish_button_xpath, locator_type="xpath")

    def click_inner_publish_button(self):
        self.element_click_js(
            self.inner_publish_button_xpath, locator_type="xpath")

    def verify_created_published_template(self):
        return self.get_text(self.republish_text_xpath, locator_type="xpath")
