import time
from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Common_Packages.Base.basepage import Basepage


class Createtenantpage(Basepage, metaclass=Logmethodmeta):

    def __init__(self, driver):
        super().__init__(driver)

    # Create Tenant
    create_tenant_button = "//span[normalize-space()='Create Tenant']"
    tenant_name_field = "tenantName"
    tenant_email_id_field = "tenantEmailId"
    tenant_table_xpath = "//*[@class='ant-table-row ant-table-row-level-0']"
    tenant_management_option_xpath = "//span[contains(text(),'Tenant Management')]"
    tenant_option_xpath = "//span[contains(text(),'Tenants')]"
    tenant_address_1_id = "tenantAddress_1"
    tenant_address_2_id = "tenantAddress_2"
    tenant_country_xpath = "//input[@id='country']"
    tenant_state_xpath = "//input[@id='state']"
    tenant_city_xpath = "//input[@id='city']"
    zip_code_xpath = "//input[@placeholder='Zip/Postal code']"
    add_csm_user_xpath = "//input[@id='csmUsers']"
    add_csm_user_listbox_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div[@class='ant-select-item-option-content']"
    add_csm_user_text = "//label[@for='csmUsers']"
    service_xpath = "//input[@id='tenant_services']"
    service_listbox_xpath = "//div[@class='ant-select-dropdown iiht-ant-select-dropdown ant-select-dropdown-placement-bottomLeft ']"
    services_text = "//label[@for='tenant_services']"

    service_xpath_allow_portal_login = "//div[@class='ant-select-selector']//span[@class='ant-select-selection-item']//span[@class='ant-select-selection-item-content' and contains(text(),'Allow Portal Login')]"
    account_manager_xpath = "//input[@id='accountManagers']"
    account_manager_xpath_listbox_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div[@class='ant-select-item-option-content']"
    machine_catalog_xpath = "//input[@id='machineCatalog']"
    machine_catalog_listxpath = "//body[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]//div[contains(@id,'')]//div"
    approval_email_xpath = "//input[@id='approverEmail']"
    auth_config_xpath = "//div[@class='ant-select-selector']//span[@class='ant-select-selection-search']//input[@id='authConfig_1']"
    auth_config_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder']//div[@class='rc-virtual-list-holder-inner']//div//div"
    tenant_url_xpath = "//input[@id='tenantUrl']"
    auto_onboarding_xpath = "//*[contains(@class,'qa-auto-board')]"
    enter_vm_xpath = "//*[contains(@class,'qa-vm-name')]"
    create_tenant_button_xpath = "//button[@type='submit']/span[contains(text(),'Create Tenant')]"
    saveAccount_and_next_xpath = "//button[@type='submit']/span[contains(text(),'Save Account & Next >')]"
    tenant_proceed_xpath = "//button[contains(@class,'ant-btn ant-btn-primary qa-create-tenant-proceed')]"
    tenant_success_xpath = "//span[@class='ant-typography text-center sub-heading-text-two headingColor']"
    edit_tenant_xpath = "//*[contains(@class,'qa-tenant-edit')]"
    delete_tenant_xpath = "//*[contains(@class,'qa-tenant-delete')]"
    delete_button_xpath = "//*[contains(@class,'qa-delete-tenantUser-proceed')]"
    pause_text_xpath = "//div[contains(text(),'Paused')]"
    Active_pause_button_xpath = "//div[@class='play-pause']//*[name()='svg']"
    Active_button_xpath = "//span[normalize-space()='Active']"

    # pricing Profile
    pricing_profile_xpath = "//input[contains(@id, 'profile_type')]"
    pricing_profile_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div//div[@class='ant-select-item-option-content' and contains(text(),'Fixed') or contains(text(),'Pay') ]"
    one_time_onboarding_xpath = "//input[contains(@name, 'onboard_fee')]"
    billing_cycle_xpath = "//input[contains(@id,'billing_cycle')]"
    billing_cycle_list_xpath = "//div[@class='ant-select-item-option-content' and contains(text(),'Weekly') or contains(text(),'Monthly') or contains(text(),'Yearly') or contains(text(),'Quarterly')]"
    calender_xpath = "//span[@class='ant-picker-suffix']"
    calender_input_xpath = "//input[@id='1#end_date_agreement#489488c2-04e1-429b-8729-12980d1c864f' or placeholder='Select Date']"
    delete_size_xpath = "//*[@class='qa-delInstance-btn']"
    end_date_agreement_xpath = "//input[@placeholder='Select Date']"
    OTOB_toggle_xpath = "//button[contains(@id, 'is_onboard_fee')]"
    OTOB_input_xpath = "//input[@placeholder='One Time Onboarding Fee']"
    currency_xpath = "//div[contains(@name,'currency')]//input[contains(@id,'currency')]"
    currency_list_xpath = "//div[@class='ant-select-item-option-content' and contains(text(),'INR') or contains(text(),'USD')]"
    instance_size_input_xpath = "//input[contains(@id,'instance_size')]"
    instance_size_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div//div[@class='ant-select-item-option-content' and contains(text(),'CPU')]"
    cost_against_xpath = "//input[@placeholder='Cost against instance']"
    # cost_against_2_xpath = "//*[@id='app-content-id']//div[2]/form/div[4]/div[2]/div/div[2]/div/div/span"
    add_more_xpath = "//span[contains(text(),'+ Add More')]"
    save_and_next_xpath = "//form[contains(@data-testid,'group-select-component')]//div[contains(@class,'ant-col ant-form-item-control')]//button[contains(@type,'submit')]"
    no_of_hours_xpath = "//input[@placeholder='Enter No. of Hours']"
    billing_visible_xpath_toggle = "//*[contains(@id,'is_billing_visible_to_tenant_user')]"
    budget_alloted_xpath = "//input[contains(@name,'max_cost_allowed')]"
    pay_per_user_xpath_toggle = "//button[contains(@id, 'pay_per_user')]"
    pricing_profile_success_message = "//div[@class='ant-notification-notice-message'and contains(text(),'Pricing Profile Created Successfully')]"

    # SetQouta
    set_qouta_text_xpath = "//h1[normalize-space()='Set Quota']"
    core_text_xpath = "//input[@id='cores']"
    core_textbox_id = "cores"
    core_checkbox_xpath = "//input[@id='is_cores_unlimited']"
    max_vms_auto_approve_Per_User_checkbox_xpath = "//input[@id='is_max_vm_auto_approve_per_user_unlimited']"
    input_max_vm_auto_approve_per_user_xpath = "//input[@id='is_max_vm_auto_approve_per_user_unlimited']"
    # core_checkbox_id = "is_cores_unlimited"
    memory_text_xpath = "//label[@for='memory']"
    memory_checkbox_xpath = "//input[@id='is_memory_unlimited']"
    storage_text_xpath = "//label[@for='storage']"
    storage_input_xpath = "//input[@id='storage']"
    storage_checkbox_xpath = "//input[@id='is_storage_unlimited']"
    total_vm_count_text_xpath = "//label[@for='total_vm_count']"
    total_vm_count_checkbox_xpath = "//input[@id='is_total_vm_unlimited']"
    monthly_vm_quata_text_xpath = "//label[@for='monthly_quota_vms']"
    monthly_vm_quata_checkbox_xpath = "//input[@id='is_monthly_quota_vms_unlimited']"
    duration_for_suspend_user_vm_in_idle_state_text_xpath = "//label[@for='vm_idle_state_suspend_duration']"
    duration_for_suspend_user_vm_in_idle_state_placeholder_id = "vm_idle_state_suspend_duration"
    duration_for_suspend_user_vm_in_idle_state_placeholder_xpath = "//input[@id='vm_idle_state_suspend_duration']"
    quota_reset_for_user_text_xpath = "//label[@for='quota_reset_for_user']"
    quota_reset_for_user_placeholder_xpath = "//input[@id='quota_reset_for_user']"
    quota_reset_for_user_placeholder_list_xpath = "//div[@class='ant-select-item-option-content' and contains(text(),'Weekly') or contains(text(),'Monthly') or contains(text(),'Yearly') or contains(text(),'Quarterly')]"
    No_concurrent_connection_text = "//label[@for='no_concurrent_connect']"
    No_concurrent_connection_checkbox_xpath = "//input[@id='is_no_concurrent_connect_unlimited']"
    input_no_of_concurrent_connections_xpath = "//input[@id='no_concurrent_connect']"
    No_of_max_user_text = "//label[@for='number_of_max_user']"
    No_of_max_user_placeholder_xpath = "//input[@id='number_of_max_user']"
    max_vm_per_user_text = "//label[@for='max_vm_per_user']"
    max_vm_per_user_checkbox_xpath = "//input[@id='is_max_vm_per_user_unlimited']"
    input_max_vm_per_user_xpath = "//input[@id='max_vm_per_user']"
    max_vm_auto_approve_per_user_text = "//label[@for='max_vm_auto_approve_per_user']"
    max_vm_auto_approve_per_user_placeholder_id = "max_vm_auto_approve_per_user"
    vm_max_extention_count_text = "//label[@for='vm_max_extension_count']"
    vm_max_extention_count_placeholder_xpath = "//input[@id='vm_max_extension_count']"
    include_deleted_vm_for_max_vms_count_text = "//label[@for='is_include_deleted_vms_for_max_vms_count']"
    extention_approval_text = "//label[@for='is_extension_approval']"
    save_and_next_button = "//*[contains(@class,'qa-submitUserForm-btn')]"
    core_xpath = "//input[@id='is_cores_unlimited']"
    core_input_xpath = "//input[@id='cores']"
    memory_xpath = "//div[@class='ant-row']//input[@id='memory']"
    total_vmcount_input_xpath = "//input[@id='total_vm_count']"
    monthly_vm_quota_xpath = "//input[@id='is_total_vm_unlimited']"
    include_deleted_VMs_for_Max_VMs_Count_toggle_xpath = "//button[@id='is_include_deleted_vms_for_max_vms_count']"
    extension_approval_toggle_xpath = "//button[@id='is_extension_approval']"
    set_quota_success_message = "//div[@class='ant-notification-notice-message'and contains(text(),'Set Quota created Successfully')]"

    # Extention And Expiry
    extention_and_expiry_text_xpath = "//h1[normalize-space()='Extension & Expiry']"
    base_pack_text_xpath = "//span[normalize-space()='Base Pack']"
    base_pack_name_input_xpath = "//input[contains(@name,'basebase')]"
    validity_days_text_xpath = "//label[@for='validity_days']"
    # validity_days_placeholder_id = "validity_days"
    validity_days_input_xpath = "//input[contains(@name,'validity_days')]"
    duration_minutes_text_xpath = "//label[@for='duration_minutes']"
    duration_minutes_placeholder_xpath = "//input[contains(@class,'qa-basepack-duration')]"
    mark_as_default_checkbox_xpath = "//input[@id='is_default']"
    auto_delete_vm_post_expiry_text_id = "//label[@for='auto_delete_vm_post_expiry']"
    auto_delete_toogle_xpath = "//button[@name='auto_delete_vm_post_expiry']"
    add_more_extension_xpath = "//*[contains(@class,'qa-ext-form-addMore')]"
    delete_extension_xpath = "//div[@class='ant-form-item-control-input-content']//*[contains(@id, 'delete')]"
    # adding Extension pack
    add_extension_pack_text_xpath = "//span[normalize-space()='Add Extension Pack']"
    name_text_xpath = "//label[contains(@for,'name#0ce33425-0646-4311-8329-c19d1ec4b0a9')]"
    name_extension_input_xpath = "//input[contains(@class,'ant-input qa-machineCatname-0 iiht-ant-input')]"
    validity_days_textaddpack_xpath = "//input[contains(@class,'ant-input qa-validity-0 iiht-ant-input')]"
    duration_extension_pack_xpath = "//input[contains(@class,'ant-input qa-duration-0 iiht-ant-input')]"
    validity_days_addpack_placeholder_xpath = "//input[contains(@class,'ant-input qa-validity-0 iiht-ant-input')]"
    duration_minutes_textaddpack_xpath = "//label[@for='duration_minutes#0ce33425-0646-4311-8329-c19d1ec4b0a9']"
    duration_minutes_placeholder_addpack_xpath = "//input[contains(@class,'ant-input qa-duration-0 iiht-ant-input')]"
    add_more_button_xpath = "//button[@class='ant-btn ant-btn-primary qa-ext-form-nextBtn']"
    use_only_for_workspace_checkbox_xpath = "//input[@id='use_only_for_workspace']"
    save_next_button_extention_expirypage_xpath = "//*[contains(@class,'qa-ext-form-nextBtn')]"
    extension_and_expiry_success_message = "//div[@class='ant-notification-notice-message'and contains(text(),'Extension & Expiry details created successfully.')]"

    # notification settings
    vm_expiry_warning_notification_1_xpath = "// input[ @ id = 'vm_expiry_warning_notification_1']"
    vm_expiry_warning_notification_2_xpath = "// input[ @ id = 'vm_expiry_warning_notification_2']"
    vm_expiry_warning_notification_3_xpath = "// input[ @ id = 'vm_expiry_warning_notification_3']"
    vm_expiry_remaining_hours_notification_1_xpath = "// input[ @ id = 'vm_expiry_remaining_hours_notification_1']"
    vm_expiry_remaining_hours_notification_2_xpath = "// input[ @ id = 'vm_expiry_remaining_hours_notification_2']"
    vm_expiry_remaining_hours_notification_3_xpath = "// input[ @ id = 'vm_expiry_remaining_hours_notification_3']"
    vm_unutilized_warning_notification_days_xpath = "// input[ @ id = 'vm_unutilized_warning_notification_days']"
    vm_decomission_after_expiry_xpath = "//input[@id='vm_decomission_after_expiry']"
    vm_decomission_warning_notification_xpath = "//input[@id='vm_decomission_warning_notification']"
    notify_when_resource_is_available_toggle_xpath = "//button[@id='notify_when_resource_available']"
    Next_summary_button = "//button[@type='submit']/span[contains(text(),'Next: Summary >')]"
    Notification_Settings_success_message = ("//div[@class='ant-notification-notice-message'and contains(text(),"
                                             "'Notification Settings updated Successfully')]")

    # summary Page
    Submit_button = "//button[@type='button']/span[contains(text(),'Submit')]"
    # verifying tenant
    search_tenant_xpath = "//input[@placeholder='Search']"
    # country
    country_dropdownxpath = "//input[@id='country']"
    country_listxpath = (
        "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div["
        "@class='ant-select-item-option-content']")

    state_dropdownxpath = "//div[@class='ant-select-selector']//input[@aria-owns='state_list']"
    state_listxpath = ("//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div["
                       "@class='ant-select-item-option-content']")

    city_dropdownxpath = "//input[@id='city']"
    city_listxpath = ("//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div["
                      "@class='ant-select-item-option-content']")

    # Search Tenant
    tenant_url_1_xpath = "//div[contains(text(),'.makemylabs.in/')]"
    tooltip_link_xpath = "//div[@role='tooltip' and contains(text(),'makemylabs.in')]"
    # Logout_Super Admin
    logout_symbol = "//header[@class='ant-layout-header header']//div[5]//*[name()='svg']"
    logout_button = "//button[@type='submit']"
    logout_account = "//div[normalize-space()='gslabadmin']"

    #Login_Tenant_User
    use_another_account = "//div[@id='otherTileText']"
    login_button = "//button[@type='button' and @class='ant-btn ant-btn-primary qa-login-btn']"
    email_id_field = "//div[@class='placeholderContainer']//input[@type='email']"
    password_field = "//div[@class='placeholderContainer']//input[@name='passwd']"
    next_button = "//div[@class='inline-block button-item ext-button-item']//input[@type='submit']"
    signin_button = "//div[@class='inline-block button-item ext-button-item']//input[@type='submit']"
    donot_show_again_xpath = "//h1[contains(text(),'Show Again')]"

    def click_create_tenant_button(self):
        self.wait_for_element(self.create_tenant_button, locator_type="xpath")
        self.element_click(self.create_tenant_button, locator_type="xpath")

    def enter_tenant_name(self, tenant_name):
        self.send_keys(tenant_name, self.tenant_name_field, locator_type="id")

    def enter_email_id(self, email_id):
        self.send_keys(email_id, self.tenant_email_id_field, locator_type="id")

    def enter_tenant_address1(self, address):
        self.send_keys(address, self.tenant_address_1_id, locator_type="id")

    def enter_tenant_address2(self, address):
        self.send_keys(address, self.tenant_address_2_id, locator_type="id")

    def enter_tenant_zip_code(self, zipcode):
        self.send_keys(zipcode, self.zip_code_xpath, locator_type="xpath")

    def enter_approval_email(self, email):
        self.send_keys(email, self.approval_email_xpath, locator_type="xpath")

    def click_auto_onboarding(self, status):
        if status == "Yes":
            self.element_click(self.auto_onboarding_xpath, locator_type="xpath")

    def click_enter_vm_name(self, status):
        if status == "Yes":
            self.element_click(self.auto_onboarding_xpath, locator_type="xpath")

    def click_tenant_proceed(self):

        self.wait_for_element(self.tenant_proceed_xpath, locator_type="xpath")
        self.element_click_js(self.tenant_proceed_xpath, locator_type="xpath")

    def click_add_more(self):
        self.element_click_js(self.add_more_xpath)

    def click_save_and_next(self):
        self.wait_for_element(self.save_and_next_xpath, locator_type="xpath")
        self.element_click_js(self.save_and_next_xpath, locator_type="xpath")

    def select_tenant_country(self, name):
        self.select_dropdown_by_name(name, self.country_dropdownxpath, self.country_listxpath)

    def select_tenant_state(self, state):
        self.select_dropdown_by_name(state, self.state_dropdownxpath, self.state_listxpath)

    def select_tenant_city(self, tenantcity):
        self.select_dropdown_by_name(tenantcity, self.city_dropdownxpath, self.city_listxpath)

    def select_services(self, service):
        self.wait_for_element(self.state_listxpath, locator_type="xpath")
        self.select_dropdown_by_name(service, self.service_xpath, self.service_listbox_xpath)

    def select_account_manager(self, account_manager):
        self.scroll_by_visible_element(self.account_manager_xpath, locator_type="xpath")
        self.select_dropdown_by_name(account_manager, self.account_manager_xpath,
                                     self.account_manager_xpath_listbox_xpath)

    def select_csm_user(self, csm_user):
        self.select_dropdown_by_name(csm_user, self.add_csm_user_xpath, self.add_csm_user_listbox_xpath)
        self.element_click_js(self.add_csm_user_text, locator_type="xpath")

    def select_machine_catalog_1(self, machine_catalog_1):
        self.select_dropdown_by_name(machine_catalog_1, self.machine_catalog_xpath, self.machine_catalog_listxpath)

    def select_machine_catalog_2(self, machine_catalog_2):
        self.select_dropdown_by_name(machine_catalog_2, self.machine_catalog_xpath, self.machine_catalog_listxpath)

    def select_auth_config(self, auth_config):
        self.select_dropdown_by_name(auth_config, self.auth_config_xpath, self.auth_config_list_xpath)

    def enter_tenant_url(self, tenant_url):
        self.send_keys(tenant_url, self.tenant_url_xpath, locator_type="xpath")

    def click_create_tenant(self):
        self.element_click(self.create_tenant_button_xpath, locator_type="xpath")

    def verify_tenant_created(self):
        success_message = self.get_text(self.tenant_success_xpath, locator_type="xpath")
        return success_message

    def verify_pricing_profile_created(self):
        return self.get_text(self.pricing_profile_success_message, locator_type="xpath")

    def select_pricing_profile(self, pricing_profile):
        self.wait_for_element(self.pricing_profile_xpath, locator_type="xpath")
        self.select_dropdown_by_name(pricing_profile, self.pricing_profile_xpath, self.pricing_profile_list_xpath)

    def select_billing_cycle(self, cycle):
        self.wait_for_element(self.billing_cycle_xpath, locator_type="xpath")
        self.select_dropdown_by_name(cycle, self.billing_cycle_xpath, self.billing_cycle_list_xpath)

    def select_currency(self, currency):
        self.wait_for_element(self.currency_xpath, locator_type="xpath")
        self.select_dropdown_by_name(currency, self.currency_xpath, self.currency_list_xpath)

    def select_instance(self, instancesize):
        self.wait_for_element(self.instance_size_input_xpath, locator_type="xpath")
        self.select_dropdown_by_name(instancesize, self.instance_size_input_xpath, self.instance_size_list_xpath)

    def enter_cost_against_instance(self, cost):
        self.send_keys(cost, self.cost_against_xpath, locator_type="xpath")

    def click_billing_visible_toggle(self, status):
        if status == "Yes":
            self.wait_for_element(self.billing_visible_xpath_toggle, locator_type="xpath")
            self.element_click(self.billing_visible_xpath_toggle, locator_type="xpath")
        else:
            self.cl.info("Toggle not selected")

    def select_end_date_agreement(self, date):
        self.wait_for_element(self.end_date_agreement_xpath, locator_type="xpath")
        self.select_element_keyboard(date, self.end_date_agreement_xpath, locator_type="xpath")

    def enter_one_time_onboarding_fee(self, status, onboardingfee):
        if status == "Yes":
            self.wait_for_element(self.OTOB_toggle_xpath, locator_type="xpath")
            self.element_click(self.OTOB_toggle_xpath, locator_type="xpath")
            self.send_keys(onboardingfee, self.OTOB_input_xpath, locator_type="xpath")
        else:
            self.cl.info("One Time Onboarding Fee toggle is OFF")

    def click_pay_per_user_toggle(self, status):
        if status == "Yes":
            self.element_click(self.pay_per_user_xpath_toggle, locator_type="xpath")

    def enter_no_of_hours(self, hours):
        self.element_click(self.no_of_hours_xpath, locator_type="xpath")

    def enter_budget_alloted(self, budget):
        self.send_keys(budget, self.budget_alloted_xpath, locator_type="xpath")

    def click_core_checkbox(self, status, noofcore):
        if status == "Yes":
            self.element_click(self.core_xpath, locator_type="xpath")
        else:
            self.enter_core(noofcore)

    def enter_core(self, noofcore):
        self.send_keys(noofcore, self.core_input_xpath, locator_type="xpath")

    def enter_memory(self, memoryquantity):
        self.send_keys(memoryquantity, self.memory_xpath, locator_type="xpath")

    def click_memory_checkbox(self, status, memoryquantity):
        if status == "Yes":
            self.element_click(self.memory_checkbox_xpath, locator_type="xpath")
        else:
            self.enter_memory(memoryquantity)

    def click_storage_checkbox(self, status, storagequantity):
        if status == "Yes":
            self.element_click(self.storage_checkbox_xpath, locator_type="xpath")
        else:
            self.enter_storage(storagequantity)

    def enter_storage(self, storagequantity):
        self.send_keys(storagequantity, self.storage_input_xpath, locator_type="xpath")

    def click_total_vm_count_checkbox(self, status, totalvmcount):
        if status == "Yes":
            self.element_click(self.total_vm_count_checkbox_xpath, locator_type="xpath")
        else:
            self.enter_total_vmcount(totalvmcount)

    def enter_total_vmcount(self, totalvmcount):
        self.send_keys(totalvmcount, self.total_vmcount_input_xpath, locator_type="xpath")

    def click_monthly_vm_quota_checkbox(self, status, monthlyvmquota):
        if status == "Yes":
            self.element_click(self.monthly_vm_quata_checkbox_xpath, locator_type="xpath")
        else:
            self.enter_monthly_vm_quota(monthlyvmquota)

    def enter_monthly_vm_quota(self, monthlyvmquota):
        self.send_keys(monthlyvmquota, self.monthly_vm_quota_xpath, locator_type="xpath")

    def enter_duration_for_suspend_user_vm_in_idle_state(self, suspendvm):
        self.send_keys(suspendvm, self.duration_for_suspend_user_vm_in_idle_state_placeholder_xpath,
                       locator_type="xpath")

    def enter_quota_reset_for_user(self, quota):
        self.select_dropdown_by_name(quota, self.quota_reset_for_user_placeholder_xpath,
                                     self.quota_reset_for_user_placeholder_list_xpath)

    def click_no_concurrent_connection_checkbox(self, status, concurrentconnections):
        if status == "Yes":
            self.element_click(self.No_concurrent_connection_checkbox_xpath, locator_type="xpath")
        else:
            self.enter_no_of_concurrent_connections(concurrentconnections)

    def enter_no_of_concurrent_connections(self, concurrentconnections):
        self.send_keys(concurrentconnections, self.input_no_of_concurrent_connections_xpath, locator_type="xpath")

    def enter_no_of_max_user(self, status, noofmaxusers):
        if status == "Yes":
            self.send_keys(noofmaxusers, self.No_of_max_user_placeholder_xpath, locator_type="xpath")

    def enter_max_vm_per_user_checkbox(self, status, maxvmperuser):
        if status == "Yes":
            self.element_click(self.max_vm_per_user_checkbox_xpath, locator_type="xpath")
        else:
            self.enter_max_vm_per_user(maxvmperuser)

    def enter_max_vm_per_user(self, maxvmperuser):
        self.send_keys(maxvmperuser, self.input_max_vm_per_user_xpath, locator_type="xpath")

    def enter_max_vm_auto_approve_per_user(self, maxvmautoapproveperuser):
        self.send_keys(maxvmautoapproveperuser, self.input_max_vm_auto_approve_per_user_xpath, locator_type="xpath")

    def click_max_vm_auto_approve_per_user(self, status, maxvmautoapproveperuser):
        if status == "Yes":
            self.element_click(self.max_vms_auto_approve_Per_User_checkbox_xpath, locator_type="xpath")
        else:
            self.enter_max_vm_auto_approve_per_user(maxvmautoapproveperuser)

    def enter_vm_max_extension_count(self, status, vmmaxextensioncount, extensionapproval_status):
        if status == "Yes":
            self.send_keys(vmmaxextensioncount, self.vm_max_extention_count_placeholder_xpath, locator_type="xpath")
            if extensionapproval_status == "Yes":
                self.element_click(self.extension_approval_toggle_xpath, locator_type="xpath")

    def click_include_deleted_v_ms_for_max_v_ms_count(self, status):
        if status == "Yes":
            self.element_click(self.include_deleted_VMs_for_Max_VMs_Count_toggle_xpath, locator_type="xpath")

    def click_save_and_next_button(self):
        self.element_click(self.save_and_next_button, locator_type="xpath")

    def enter_base_pack_name(self, basepackname):
        self.send_keys(basepackname, self.base_pack_name_input_xpath, locator_type="xpath")

    def enter_validity_in_days(self, validity):
        self.send_keys(validity, self.validity_days_input_xpath, locator_type="xpath")

    def enter_duration_in_minutes(self, duration):
        self.send_keys(duration, self.duration_minutes_placeholder_xpath, locator_type="xpath")

    def mark_as_default_basepack(self, status):
        if status == "Yes":
            self.element_click(self.mark_as_default_checkbox_xpath, locator_type="xpath")

    def click_auto_delete_toggle(self, status):
        if status == "Yes":
            self.element_click(self.auto_delete_toogle_xpath, locator_type="xpath")

    def enter_name_addpack(self, addpackname):
        self.send_keys(addpackname, self.name_extension_input_xpath, locator_type="xpath")

    def enter_validity_in_days_for_addpack(self, days):
        self.send_keys(days, self.validity_days_addpack_placeholder_xpath, locator_type="xpath")

    def enter_duration_in_minutes_for_addpack(self, minutes):
        self.send_keys(minutes, self.duration_minutes_placeholder_addpack_xpath, locator_type="xpath")

    def click_use_only_for_worksapce_checkbox(self, status):
        if status == "Yes":
            self.element_click(self.use_only_for_workspace_checkbox_xpath, locator_type="xpath")

    def click_on_save_next_button_extention_expirypage(self):
        self.element_click(self.save_next_button_extention_expirypage_xpath, locator_type="xpath")

    def enter_vm_expiry_warning_notification_1(self, status, days):
        if status == "Yes":
            self.send_keys(days, self.vm_expiry_warning_notification_1_xpath, locator_type="xpath")

    def enter_vm_expiry_warning_notification_2(self, status, days):
        if status == "Yes":
            self.send_keys(days, self.vm_expiry_warning_notification_2_xpath, locator_type="xpath")

    def enter_vm_expiry_warning_notification_3(self, status, days):
        if status == "Yes":
            self.send_keys(days, self.vm_expiry_warning_notification_3_xpath, locator_type="xpath")

    def enter_vm_expiry_remaining_hours_notification_1(self, status, hours):
        if status == "Yes":
            self.send_keys(hours, self.vm_expiry_remaining_hours_notification_1_xpath, locator_type="xpath")

    def enter_vm_expiry_remaining_hours_notification_2(self, status, hours):
        if status == "Yes":
            self.send_keys(hours, self.vm_expiry_remaining_hours_notification_2_xpath, locator_type="xpath")

    def enter_vm_expiry_remaining_hours_notification_3(self, status, hours):
        if status == "Yes":
            self.send_keys(hours, self.vm_expiry_remaining_hours_notification_3_xpath, locator_type="xpath")

    def enter_vm_unutilized_warning_notification_days(self, status, days):
        if status == "Yes":
            self.send_keys(days, self.vm_unutilized_warning_notification_days_xpath, locator_type="xpath")

    def enter_vm_decomission_after_expiry(self, status, days):
        if status == "Yes":
            self.send_keys(days, self.vm_decomission_after_expiry_xpath, locator_type="xpath")

    def vm_decomission_warning_notification(self, status, days):
        if status == "Yes":
            self.send_keys(days, self.vm_decomission_warning_notification_xpath, locator_type="xpath")

    def click_when_resource_is_availabe_toggle(self, status):
        if status == "Yes":
            self.element_click(self.notify_when_resource_is_available_toggle_xpath, locator_type="xpath")

    def click_next_summary_button(self):
        self.element_click(self.Next_summary_button, locator_type="xpath")

    def click_submit_button(self):
        self.element_click(self.Submit_button, locator_type="xpath")

    def verify_extension_and_expiry(self):
        return self.get_text(self.extension_and_expiry_success_message, locator_type="xpath")

    def verify_notification_setting(self):
        return self.get_text(self.Notification_Settings_success_message, locator_type="xpath")

    def create_tenant(self, tenant_name, email_id, address1, address2, country_name, state_name, city_name, zipcode,
                      service, account_manager, csm_user, machine_catalog_1, machine_catalog_2, machine_catalog_3,
                      auth_config, tenant_url,
                      auto_onboarding_status):
        self.enter_tenant_name(tenant_name)
        self.enter_email_id(email_id)
        self.enter_tenant_address1(address1)
        self.enter_tenant_address2(address2)
        self.select_tenant_country(country_name)
        self.select_tenant_state(state_name)
        self.select_tenant_city(city_name)
        self.enter_tenant_zip_code(zipcode)
        self.select_services(service)
        self.select_account_manager(account_manager)
        self.select_csm_user(csm_user)
        self.select_machine_catalog_1(machine_catalog_1)
        self.select_machine_catalog_2(machine_catalog_2)
        self.select_machine_catalog_2(machine_catalog_3)
        self.select_auth_config(auth_config)
        self.enter_tenant_url(tenant_url)
        self.click_auto_onboarding(auto_onboarding_status)
        self.click_create_tenant()

    def fixed_cost_per_vm(self, pricing_profile, billingcycle, aggrementenddate, ontimeonboardingstatus,
                          ontimeonboardingfee, currency, billing_visible_to_tenant_user_status, instancesize,
                          costagainstinstance):
        self.select_pricing_profile(pricing_profile)
        time.sleep(1)
        self.select_billing_cycle(billingcycle)
        self.select_end_date_agreement(aggrementenddate)
        self.enter_one_time_onboarding_fee(ontimeonboardingstatus, ontimeonboardingfee)
        self.select_currency(currency)
        self.click_billing_visible_toggle(billing_visible_to_tenant_user_status)
        self.select_instance(instancesize)
        self.enter_cost_against_instance(costagainstinstance)
        self.click_save_and_next()
        time.sleep(2)

    def pay_per_use(self, pricing_profile, billingcycle, aggrementenddate, ontimeonboardingstatus, ontimeonboardingfee,
                    currency, billing_visible_to_tenant_user_status, instancesize, costagainstinstance):
        self.select_pricing_profile(pricing_profile)
        time.sleep(1)
        self.select_billing_cycle(billingcycle)
        self.select_end_date_agreement(aggrementenddate)
        self.enter_one_time_onboarding_fee(ontimeonboardingstatus, ontimeonboardingfee)
        self.select_currency(currency)
        self.click_billing_visible_toggle(billing_visible_to_tenant_user_status)
        self.select_instance(instancesize)
        self.enter_cost_against_instance(costagainstinstance)
        self.click_save_and_next()
        time.sleep(2)

    def fixed_hrs_at_company(self, pricing_profile, billingcycle, noofhours, aggrementenddate, ontimeonboardingstatus,
                             ontimeonboardingfee, currency, payperusestatus, billing_visible_to_tenant_user_status,
                             instancesize, costagainstinstance):
        self.select_pricing_profile(pricing_profile)
        time.sleep(1)
        self.select_billing_cycle(billingcycle)
        self.enter_no_of_hours(noofhours)
        self.select_end_date_agreement(aggrementenddate)
        self.enter_one_time_onboarding_fee(ontimeonboardingstatus, ontimeonboardingfee)
        self.select_currency(currency)
        self.click_pay_per_user_toggle(payperusestatus)
        self.click_billing_visible_toggle(billing_visible_to_tenant_user_status)
        self.select_instance(instancesize)
        self.enter_cost_against_instance(costagainstinstance)
        self.click_save_and_next()
        time.sleep(2)

    def fixed_cost_at_company(self, pricing_profile, billingcycle, budgetallocated, aggrementenddate,
                              ontimeonboardingstatus, ontimeonboardingfee, currency, payperusestatus,
                              billing_visible_to_tenant_user_status, instancesize, costagainstinstance):
        self.select_pricing_profile(pricing_profile)
        time.sleep(1)
        self.select_billing_cycle(billingcycle)
        self.enter_budget_alloted(budgetallocated)
        self.select_end_date_agreement(aggrementenddate)
        self.enter_one_time_onboarding_fee(ontimeonboardingstatus, ontimeonboardingfee)
        self.select_currency(currency)
        self.click_pay_per_user_toggle(payperusestatus)
        self.click_billing_visible_toggle(billing_visible_to_tenant_user_status)
        self.select_instance(instancesize)
        self.enter_cost_against_instance(costagainstinstance)
        self.click_save_and_next()
        time.sleep(2)

    def set_quota_page(self, corestatus, noofcore, memorystatus, memoryquantity, storagestatus, storagequantity,
                       totalvmcountstatus, totalvmcount, monthlyvmquotastatus, monthlyvmquota, suspendvm,
                       quotaresetforuser, concurrentconnectionsstatus, concurrentconnections, noofmaxusersstatus,
                       noofmaxusers, maxvmperuserstatus, maxvmperuser, maxvmautoapproveperuserstatus,
                       maxvmautoapproveperuser, vmmaxextensioncountstatus, vmmaxextensioncount,
                       extensionapproval_status, includedeleted_v_msfor_max_v_ms_count_status):
        self.click_core_checkbox(corestatus, noofcore)
        self.click_memory_checkbox(memorystatus, memoryquantity)
        self.click_storage_checkbox(storagestatus, storagequantity)
        self.click_total_vm_count_checkbox(totalvmcountstatus, totalvmcount)
        self.click_monthly_vm_quota_checkbox(monthlyvmquotastatus, monthlyvmquota)
        self.enter_duration_for_suspend_user_vm_in_idle_state(suspendvm)
        self.enter_quota_reset_for_user(quotaresetforuser)
        self.click_no_concurrent_connection_checkbox(concurrentconnectionsstatus, concurrentconnections)
        self.enter_no_of_max_user(noofmaxusersstatus, noofmaxusers)
        self.enter_max_vm_per_user_checkbox(maxvmperuserstatus, maxvmperuser)
        self.click_max_vm_auto_approve_per_user(maxvmautoapproveperuserstatus, maxvmautoapproveperuser)
        self.enter_vm_max_extension_count(vmmaxextensioncountstatus, vmmaxextensioncount, extensionapproval_status)
        self.click_include_deleted_v_ms_for_max_v_ms_count(includedeleted_v_msfor_max_v_ms_count_status)
        self.click_save_and_next_button()
        time.sleep(2)

    def extention_and_expiry_page(self, basepackname, basepackdays, basepackmins, defaultbasepackstatus,
                                  autodeletestatus, addpackname, addpackdays, addpackminutes, workspacecheckboxstatus):
        self.enter_base_pack_name(basepackname)
        self.enter_validity_in_days(basepackdays)
        self.enter_duration_in_minutes(basepackmins)
        self.mark_as_default_basepack(defaultbasepackstatus)
        self.click_auto_delete_toggle(autodeletestatus)
        self.enter_name_addpack(addpackname)
        self.enter_validity_in_days_for_addpack(addpackdays)
        self.enter_duration_in_minutes_for_addpack(addpackminutes)
        self.click_use_only_for_worksapce_checkbox(workspacecheckboxstatus)
        self.click_on_save_next_button_extention_expirypage()

    def notification_setting_page(self, vm_expiry_warning_notification_1_status, vm_expiry_warning_notification_1_days,
                                  vm_expiry_warning_notification_2_status, vm_expiry_warning_notification_2_days,
                                  vm_expiry_warning_notification_3_status, vm_expiry_warning_notification_3_days,
                                  vm_expiry_remaining_hours_notification_1_status,
                                  vm_expiry_remaining_hours_notification_1_hours,
                                  vm_expiry_remaining_hours_notification_2_status,
                                  vm_expiry_remaining_hours_notification_2_hours,
                                  vm_expiry_remaining_hours_notification_3_status,
                                  vm_expiry_remaining_hours_notification_3_hours,
                                  vm_unutilized_warning_notification_days_status,
                                  vm_unutilized_warning_notification_days_days,
                                  enter_vm_decomission_after_expiry_status, enter_vm_decomission_after_expiry_days,
                                  vm_decomission_warning_notification_status, vm_decomission_warning_notification_days,
                                  togglestatus):
        self.enter_vm_expiry_warning_notification_1(vm_expiry_warning_notification_1_status,
                                                    vm_expiry_warning_notification_1_days)
        self.enter_vm_expiry_warning_notification_2(vm_expiry_warning_notification_2_status,
                                                    vm_expiry_warning_notification_2_days)
        self.enter_vm_expiry_warning_notification_3(vm_expiry_warning_notification_3_status,
                                                    vm_expiry_warning_notification_3_days)
        self.enter_vm_expiry_remaining_hours_notification_1(vm_expiry_remaining_hours_notification_1_status,
                                                            vm_expiry_remaining_hours_notification_1_hours)
        self.enter_vm_expiry_remaining_hours_notification_2(vm_expiry_remaining_hours_notification_2_status,
                                                            vm_expiry_remaining_hours_notification_2_hours)
        self.enter_vm_expiry_remaining_hours_notification_3(vm_expiry_remaining_hours_notification_3_status,
                                                            vm_expiry_remaining_hours_notification_3_hours)
        self.enter_vm_unutilized_warning_notification_days(vm_unutilized_warning_notification_days_status,
                                                           vm_unutilized_warning_notification_days_days)
        self.enter_vm_decomission_after_expiry(enter_vm_decomission_after_expiry_status,
                                               enter_vm_decomission_after_expiry_days)
        self.vm_decomission_warning_notification(vm_decomission_warning_notification_status,
                                                 vm_decomission_warning_notification_days)
        self.click_when_resource_is_availabe_toggle(togglestatus)
        self.click_next_summary_button()

    def summary_page(self):
        self.click_submit_button()

    def verity_set_quota(self):
        return self.get_text(self.set_quota_success_message, locator_type="xpath")

    def copy_tenant_url(self):
        self.wait_for_element(self.tenant_url_1_xpath, locator_type="xpath")
        self.mouse_hover_on_element(self.tenant_url_1_xpath, locator_type="xpath", hover_time="2")
        self.wait_for_element(self.tooltip_link_xpath, locator_type="xpath")
        self.copy_invite(self.tooltip_link_xpath, locator_type="xpath")

    def visit_tenant_url(self):
        self.open_invite_link()

    def logout_super_admin(self):
        self.wait_for_element(self.logout_symbol, locator_type="xpath")
        self.element_click(self.logout_symbol, locator_type="xpath")
        self.wait_for_element(self.logout_button, locator_type="xpath")
        self.element_click(self.logout_button, locator_type="xpath")
        self.wait_for_element(self.logout_account, locator_type="xpath")
        self.element_click(self.logout_account, locator_type="xpath")
        time.sleep(2)

    def search_tenant(self, tenant_name):
        self.wait_for_element(self.search_tenant_xpath, locator_type="xpath")
        self.send_keys(tenant_name, self.search_tenant_xpath, locator_type="xpath")

    def click_searched_tenant(self, tenant_name):
        search_result = f"//div[normalize-space()='{tenant_name}']"
        self.wait_for_element(search_result, locator_type="xpath")
        self.element_click_js(search_result, locator_type="xpath")

    def login(self, email, password):
        self.wait_for_element(self.login_button, locator_type="xpath")
        self.element_click_js(self.login_button, locator_type="xpath")
        self.wait_for_element(self.use_another_account, locator_type="xpath")
        self.element_click_js(self.use_another_account, locator_type="xpath")
        self.wait_for_element(self.email_id_field, locator_type="xpath")
        self.send_keys(email, self.email_id_field, locator_type="xpath")
        self.wait_for_element(self.next_button, locator_type="xpath")
        self.element_click_js(self.next_button, locator_type="xpath")
        self.wait_for_element(self.password_field, locator_type="xpath")
        self.send_keys(password, self.password_field, locator_type="xpath")
        self.wait_for_element(self.signin_button, locator_type="xpath")
        self.element_click_js(self.signin_button, locator_type="xpath")
