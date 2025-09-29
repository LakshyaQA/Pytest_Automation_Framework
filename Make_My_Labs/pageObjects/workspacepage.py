import time
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Make_My_Labs.Configration.configpath import UploadFile


class Workspacepage(Basepage, metaclass=Logmethodmeta):
    def __init__(self, driver):
        super().__init__(driver)

    # workspace_manager_xpath = "//span[contains(text(),'Workspace Manager')]"
    create_workspace_xpath = "//button[@type='button']/span[contains(text(),'Create Workspace')]"
    workspace_name_xpath = "//input[@id='workspace_name']"
    tenant_list_path = "//*[@class='ant-select-item-option-content']"
    tenant_xpath = "//div[text()='tenant workspace']"
    tenant_input_xpath = "//input[@id='tenant_id']"
    tenant_input_list_xpath = ("//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div["
                               "@class='ant-select-item-option-content']")
    lab_type_input_xpath = "//input[@id='lab_type']"
    lab_type_input_list_xpath = ("//div[@class='ant-select-item-option-content' and contains(text(),'Persistent') or "
                                 "contains(text(),'Non Persistent')]")
    lab_drop_down_xpath = "//div[text()='Persistent']"
    schedule_radio_button_xpath = "//div[@data-test='radio-component']//label//span[2]//span"
    all_day_xpath = "//input[@id='is_all_day']"
    extra_schedule_xpath = "//input[@id='is_extra_schedule']"
    all_day_start_timing_xpath = "//input[@id='datetime_start']"
    all_day_end_timing_xpath = "//input[@id='datetime_end']"
    extra_schedule_start_timing_xpath = "//input[@id='extra_datetime_start']"
    extra_schedule_end_timing_xpath = "//input[@id='extra_datetime_end']"
    start_date_placeholder_id = "datetime_start"
    next_icon_xpath = "//*[@class='ant-picker-next-icon']"
    start_date_xpath = "//input[@id='datetime_start']"
    end_date_placeholder_id = "datetime_end"
    end_date_xpath = "//input[@id='datetime_end']"
    aad_xpath = "//div[text()='AAD']"
    resource_template_input_xpath = "//input[@id='sku_id']"
    resource_template_input_xpath_list_xpath = ("//div[@class='rc-virtual-list']//div["
                                                "@class='rc-virtual-list-holder-inner']//div["
                                                "@class='ant-select-item-option-content']")
    instance_size_input_xpath = ("//div[@class='ant-select-selector']//span["
                                 "@class='ant-select-selection-search']//input[@id='instance_size']")
    instance_size_input_list_xpath = ("//div[@class='rc-virtual-list']//div["
                                      "@class='rc-virtual-list-holder-inner']//div//div["
                                      "@class='ant-select-item-option-content' and contains(text(),'CPU')]")
    min_vmcount_xpath = "//input[@placeholder='Min VM Count']"
    max_vmcount_xpath = "//input[@placeholder='Max Allowed VM Count']"
    override_cost_xpath = "//input[@id='override_pricing']"
    cost_per_hour_xpath = "//input[@id='cost_per_hour']"
    override_cost_per_hour_checkbox_xpath = "//input[@id='override_cost_per_hour']"
    resource_usage_xpath = "//input[@placeholder='Resource Usage Duration Per User (Hours)']"
    resource_exp_duration = "//input[@placeholder='Resource Expiry Duration (Days)']"
    vm_decom_days_id = "decommission_days"
    leading_time_provisioning_xpath = "//input[@id='leading_time']"
    post_provision_login_checkbox = "//input[@id='provision_post_login']"
    no_of_extension_xpath = "//input[@placeholder='No. Of Extensions']"
    select_extension_pack_xpath = "//input[@id='extension-section']"
    select_extension_pack_list_xpath = ("//div[@class='rc-virtual-list']//div["
                                        "@class='rc-virtual-list-holder-inner']//div["
                                        "@class='ant-select-item-option-content']")
    extension_resource_usage_xpath = "//input[@id='threshold_percentage']"
    extension_resource_duration_checkbox_xpath = "//input[@id='override_extension']"
    auth_name_id = "auth_name"
    auth_name_xpath = "//input[@id='auth_name']"
    auth_config_id = "auth_type"
    auth_config_xpath = "//input[@id='auth_type']"
    auth_config_list_xpath = ("//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder']//div["
                              "@class='rc-virtual-list-holder-inner']//div//div")
    sso_xpath = "//div[contains(text(),'SSO')]"
    local_user_xpath = "//div[contains(text(),'Local User')]"
    aadconfig_xpath = "//div[contains(text(),'AAD')]"
    issue_url_id = "issuer_url"
    addb2c_xpath = "//input[@placeholder='Enter Domain Name']"
    application_id_xpath = "//input[@placeholder='Enter Application ID']"
    clientSecret_xpath = "//input[@placeholder='Enter Callback Path']"
    signup_xpath = "//input[@placeholder='Enter SignIn or SignUp Policy']"
    reset_password_xpath = "//input[@placeholder='Enter Reset password Policy']"
    edit_policy_xpath = "//input[@placeholder='Enter Edit Profile Policy']"
    support_xpath = "//input[@placeholder='Enter Supported Domains']"
    manual_Registration_xpath = "//span[contains(text(),'Manual Registration')][1]"
    create_invitation_link_xpath = "//span[contains(text(),'Create Invitation Link')]"
    copy_link_xpath = "//span[@aria-label='copy']//*[name()='svg']"
    addMore_xpath = "//span[normalize-space()='+ Add More']"
    username_xpath = "//input[@placeholder='Enter User Name']"
    submit_xpath = "//div[@class='ant-form-item-control-input-content']//button[@type='submit']"
    edit_button_xpath = "(//*[name()='svg'][@class='pointer-cursor qa-workspace-edit-icon'])[1]"  # "//*[contains(@class,'qa-workspace-edit')]"
    save_and_next_xpath = "//*[contains(@class,'qa-workspace-save-and-next')]"
    inner_save_next_button = "//button[contains(@type,'submit')]"  # "//*[contains(@class,'qa-save-next']"
    delete_button_xpath = "//*[contains(@class,'qa-workspace-delete')]"
    inner_delete_button_xpath = "//*[contains(@class,'qa-remove-sku-proceed')]"
    prising_id = "pricing_id"
    select_prising_profile_xpath = "//div[contains(text(),'Pay per use')]"
    publish_button = "//tbody//tr[2]//td[9]//button"
    max_redemption_count_id = "max_redemption_count"
    provision_post_login_id = "leading_time"
    link_text = "//*[contains(@class,'qa-ws-invitation normal-text workspace-issuerUrl')]"
    user_login_button_xpath = "//span[contains(text(),'Login')]"
    user_login_button_xpath1 = "//*[contains(@class,'autoOnboard-button')]"
    username_textbox_id = "i0116"
    password_textbox_id = "i0118"
    next_button_id = "idSIButton9"
    stay_signin_yes_button_id = "idSIButton9"
    duration_no_of_days_input_xpath = "//input[@id='duration_days']"
    duration_start_date_and_time_xpath = "//input[@id='datetime3']"
    pricing_profile_input_xpath = "//input[@id='pricing_id']"
    pricing_profile_input_list_xpath = ("//div[@class='rc-virtual-list']//div["
                                        "@class='rc-virtual-list-holder-inner']//div["
                                        "@class='ant-select-item-option-content']")
    search_box_xpath = "//input[@placeholder='Search']"
    published_success_text_xpath = "//tbody//tr[2]//td[8]//span//div"
    bulk_upload_local_user_xpath = "(//div[@class='ant-upload-drag-container']//button)[2]"
    users_xpath = "//div[@role='tab']//h1[contains(text(),'Users')]"
    invitation_link = "//td[@class='ant-table-cell']//div[contains(text(),'https://uat.makemylabs.in/wsm/')]"
    invitation_link_tooltip = "//div[@class='ant-tooltip-inner' and contains(text(),'invitation_id')]"
    # Workspace VM AAD
    ws_username_xpath = "//input[@name='username']"
    ws_login_button = "//button[@type='button' and @class='ant-btn ant-btn-primary qa-login-btn']"
    ws_password_field = "//div[@class='placeholderContainer']//input[@name='passwd']"
    ws_signin_button = "//div[@class='inline-block button-item ext-button-item']//input[@type='submit']"
    ws_power_status_text_xpath = "//span[contains(text(),'Power Status')]"
    ws_dots_xpath = "//*[name()='svg']//*[name()='g' and @data-name='Group 11076']"
    ws_power_on = "(//div[@class='flexElements'])[1]"
    ws_running_text_xpath = "//span[normalize-space()='Running']"
    ws_connect_button_xpath = "//div[@class='workspace-lab-card-bottom']//span//button"
    ws_stop_text = "//span[contains(text(),'Stop')]"

    # Workspace VM LocalUser
    ws_username_xpath_l = "//input[@name='username']"
    ws_password_field_l = "//input[@name='password']"
    ws_login_button_l = "//button[@type='button' and @class='ant-btn ant-btn-primary qa-login-btn']"

    # Super admin logout
    logout_symbol = "//header[@class='ant-layout-header header']//div[5]//*[name()='svg']"
    logout_button = "//button[@type='submit']"
    logout_account = "//div[normalize-space()='gslabadmin']"
    use_another_account = "//div[@id='otherTileText']"

    def search_workspace(self, workspace_name):
        self.send_keys(workspace_name, self.search_box_xpath, locator_type="xpath")

    def click_create_workspace_button(self):

        self.element_click_js(self.create_workspace_xpath, locator_type="xpath")

    def search_and_publish_option(self, search_workspace):
        self.send_keys(search_workspace, self.search_box_xpath, locator_type="xpath")
        self.element_click(self.publish_button, locator_type="xpath")

    def click_on_workspace_name(self, workspace_name):
        workspace_name_xpath = f"//td[@class='ant-table-cell']//u//div[contains(text(),'D0010')]"
        self.element_click(workspace_name_xpath, locator_type="xpath")

    def click_on_users_tab(self):
        self.wait_for_element(self.users_xpath, locator_type="xpath")
        self.element_click(self.users_xpath, locator_type="xpath")

    def logout_super_admin(self):
        self.wait_for_element(self.logout_symbol, locator_type="xpath")
        self.element_click(self.logout_symbol, locator_type="xpath")
        self.wait_for_element(self.logout_button, locator_type="xpath")
        self.element_click(self.logout_button, locator_type="xpath")
        self.wait_for_element(self.logout_account, locator_type="xpath")
        self.element_click(self.logout_account, locator_type="xpath")
        time.sleep(2)

    def login_workspace_local_user(self, username, password):
        self.wait_for_element(self.ws_username_xpath_l, locator_type="xpath")
        self.send_keys(username, self.ws_username_xpath, locator_type="xpath")
        self.wait_for_element(self.ws_password_field_l, locator_type="xpath")
        self.send_keys(password, self.ws_password_field_l, locator_type="xpath")
        self.wait_for_element(self.ws_login_button_l, locator_type="xpath")
        self.element_click(self.ws_login_button_l, locator_type="xpath")

    def login_workspace_aad(self, username, password):
        # self.waitForElement(self.ws_username_xpath, locator_type="xpath")
        # self.sendKeys(username, self.ws_username_xpath, locator_type="xpath")
        # self.waitForElement(self.ws_login_button, locator_type="xpath")
        # self.element_click(self.ws_login_button, locator_type="xpath")
        self.wait_for_element(self.ws_password_field, locator_type="xpath")
        self.send_keys(password, self.ws_password_field, locator_type="xpath")
        self.wait_for_element(self.ws_signin_button, locator_type="xpath")
        self.element_click(self.ws_signin_button, locator_type="xpath")

    def ws_connect(self):
        self.wait_for_element(self.ws_power_status_text_xpath, locator_type="xpath", timeout=2000)
        self.wait_for_element(self.ws_power_status_text_xpath, locator_type="xpath")
        self.wait_for_element(self.ws_dots_xpath, locator_type="xpath")
        self.mouse_hover_on_element(self.ws_dots_xpath, locator_type="xpath", hover_time="2")
        self.wait_for_element(self.ws_power_on, locator_type="xpath")
        self.element_click_js(self.ws_power_on, locator_type="xpath")
        self.wait_for_element(self.ws_running_text_xpath, locator_type="xpath", timeout=600)
        self.wait_for_element(self.ws_connect_button_xpath, locator_type="xpath")
        self.element_click_js(self.ws_connect_button_xpath, locator_type="xpath")
        self.wait_for_element(self.ws_stop_text, locator_type="xpath", timeout=600)
        time.sleep(30)

    def get_invitation_link_and_visit_ws(self, workspace_name):
        self.click_on_workspace_name(workspace_name)
        self.click_on_users_tab()
        self.wait_for_element(self.invitation_link, locator_type="xpath")
        self.mouse_hover_on_element(self.invitation_link, locator_type="xpath", hover_time="2")
        self.copy_invite(self.invitation_link_tooltip, locator_type="xpath")
        self.logout_super_admin()
        self.open_invite_link()

    def enter_workspace_name(self, workspacename):
        self.send_keys(workspacename, self.workspace_name_xpath, locator_type="xpath")

    def select_tenant(self, tenant_name):
        self.select_dropdown_by_name(tenant_name, self.tenant_input_xpath, self.tenant_input_list_xpath)

    def select_lab_type(self, labtype):
        self.select_dropdown_by_name(labtype, self.lab_type_input_xpath, self.lab_type_input_list_xpath)

    def input_select_duration_no_of_days(self, duration_no_of_days):
        self.send_keys(duration_no_of_days, self.duration_no_of_days_input_xpath, locator_type="xpath")

    def input_select_duration_start_date_and_time(self, duration_start_date_and_time_count):
        date = self.get_current_date_and_time(duration_start_date_and_time_count)
        self.send_keys(date, self.duration_start_date_and_time_xpath, locator_type="xpath")

    def select_schedule(self, scheduletype, all_day_checkbox, start_date_count, end_date_count,
                        allday_start_date_and_time,
                        allday_end_date_and_time, extra_schedule_checkbox, extra_schedule_start_date_and_time,
                        extra_schedule_end_date_and_time, duration_no_of_days, duration_start_date_and_time_count):
        if scheduletype == "Date Range":
            if all_day_checkbox == "Yes":
                self.click_on_all_day()
                self.input_start_date(start_date_count)
                self.input_end_date(end_date_count)
            else:
                self.allday_start_date_and_time(allday_start_date_and_time)
                self.allday_end_date_and_time(allday_end_date_and_time)
                if extra_schedule_checkbox == "Yes":
                    self.extra_schedule_start_date_and_time(extra_schedule_start_date_and_time)
                    self.extra_schedule_end_date_and_time(extra_schedule_end_date_and_time)
        if scheduletype == "Duration":
            self.input_select_duration_no_of_days(duration_no_of_days)
            self.input_select_duration_start_date_and_time(duration_start_date_and_time_count)

    def click_on_all_day(self):
        self.element_click_js(self.all_day_xpath, locator_type="xpath")

    def click_on_extra_schedule(self):
        self.element_click_js(self.extra_schedule_xpath, locator_type="xpath")

    def input_start_date(self, excel_date_count):
        int_excel_date_count = int(excel_date_count)
        date = self.get_current_date(int_excel_date_count)
        string_date = str(date)
        self.select_element_keyboard(string_date, self.start_date_xpath, locator_type="xpath")
        time.sleep(1)

    def input_end_date(self, excel_date_count):
        int_excel_date_count = int(excel_date_count)
        date = self.get_current_date(int_excel_date_count)
        string_date = str(date)
        self.select_element_keyboard(string_date, self.end_date_xpath, locator_type="xpath")
        time.sleep(1)

    def allday_start_date_and_time(self, excel_hours):
        start_date_time = self.get_current_date_and_time(excel_hours)
        self.send_keys(start_date_time, self.all_day_start_timing_xpath, locator_type="xpath")

    def allday_end_date_and_time(self, excel_hours):
        end_date_time = self.get_current_date_and_time(excel_hours)
        self.send_keys(end_date_time, self.all_day_start_timing_xpath, locator_type="xpath")

    def extra_schedule_start_date_and_time(self, excel_hours):
        start_date_time = self.get_current_date_and_time(excel_hours)
        self.send_keys(start_date_time, self.extra_schedule_start_timing_xpath, locator_type="xpath")

    def extra_schedule_end_date_and_time(self, excel_hours):
        end_date_time = self.get_current_date_and_time(excel_hours)
        self.send_keys(end_date_time, self.all_day_start_timing_xpath, locator_type="xpath")

    def click_save_and_next(self):
        self.element_click_js(self.inner_save_next_button, locator_type="xpath")

    def create_workspace(self, workspacename, tenant_name, labtype, scheduletype, all_day_checkbox, start_date,
                         end_date, allday_start_date_and_time, allday_end_date_and_time, extra_schedule_checkbox,
                         extra_schedule_start_date_and_time, extra_schedule_end_date_and_time, duration_no_of_days,
                         duration_start_date_and_time_count):
        self.click_create_workspace_button()
        time.sleep(1)
        self.enter_workspace_name(workspacename)
        time.sleep(0.5)
        self.select_tenant(tenant_name)
        time.sleep(0.5)
        self.select_lab_type(labtype)
        time.sleep(0.5)
        self.select_schedule(scheduletype, all_day_checkbox, start_date, end_date, allday_start_date_and_time,
                             allday_end_date_and_time, extra_schedule_checkbox, extra_schedule_start_date_and_time,
                             extra_schedule_end_date_and_time, duration_no_of_days, duration_start_date_and_time_count)
        time.sleep(2)
        self.element_click(self.submit_xpath, locator_type="xpath")

    def add_resource(self, resource_template_name, instance_size, min_vm_count, max_vm_count, over_ride_cost_status,
                     pricing_profile_name, over_ride_cost_per_hour_status, cost_per_hour,
                     resource_usage_duration_per_user, vm_decommision_after_expiry, post_provision_login_status,
                     post_provision_login, extend_duration_status, no_of_extensions, select_pack, threshhold_value,
                     auth_name, auth_config):
        self.select_resource_template(resource_template_name)
        time.sleep(0.5)
        self.select_instance_size(instance_size)
        time.sleep(0.5)
        self.enter_min_vm_count(min_vm_count)
        time.sleep(0.5)
        self.enter_max_vm_count(max_vm_count)
        time.sleep(0.5)
        self.click_override_cost(over_ride_cost_status, pricing_profile_name)
        time.sleep(0.5)
        self.enter_cost_per_hour(over_ride_cost_per_hour_status, cost_per_hour)
        time.sleep(0.5)
        self.enter_resource_usage_duration(resource_usage_duration_per_user)
        time.sleep(0.5)
        self.enter_vm_decommissioned_days(vm_decommision_after_expiry)
        time.sleep(0.5)
        self.enter_leading_time_provisioning(post_provision_login_status, post_provision_login)
        time.sleep(0.5)
        self.enter_no_extension(extend_duration_status, no_of_extensions, select_pack, threshhold_value)
        time.sleep(0.5)
        self.click_submit()
        time.sleep(1)
        self.enter_auth_name(auth_name)
        time.sleep(0.5)
        self.select_auth_config(auth_config)

    def select_resource_template(self, resource_template_name):
        self.select_dropdown_by_name(resource_template_name, self.resource_template_input_xpath,
                                     self.resource_template_input_xpath_list_xpath)

    def select_instance_size(self, instance_size):
        self.select_dropdown_by_name(instance_size, self.instance_size_input_xpath, self.instance_size_input_list_xpath)
        self.wait_for_element(self.instance_size_input_list_xpath, locator_type="xpath")

    def enter_min_vm_count(self, min_vm_count):
        time.sleep(1)
        self.send_keys(min_vm_count, self.min_vmcount_xpath, locator_type="xpath")

    def enter_max_vm_count(self, max_vm_count):
        self.send_keys(max_vm_count, self.max_vmcount_xpath, locator_type="xpath")

    def click_override_cost(self, over_ride_cost_status, pricing_profile_name):

        if over_ride_cost_status == "Yes":
            self.element_click(self.override_cost_xpath, locator_type="xpath")
            self.select_dropdown_by_name(pricing_profile_name, self.pricing_profile_input_xpath,
                                         self.pricing_profile_input_list_xpath)

    def enter_cost_per_hour(self, over_ride_cost_per_hour_status, cost_per_hour):
        if over_ride_cost_per_hour_status == "Yes":
            self.element_click(self.override_cost_per_hour_checkbox_xpath, locator_type="xpath")
            self.send_keys(cost_per_hour, self.cost_per_hour_xpath, locator_type="xpath")

    def enter_resource_usage_duration(self, resource_usage_duration_per_user):
        self.send_keys(resource_usage_duration_per_user, self.resource_usage_xpath, locator_type="xpath")

    def enter_vm_decommissioned_days(self, vm_decommision_after_expiry):
        self.send_keys(vm_decommision_after_expiry, self.vm_decom_days_id, locator_type="id")

    def enter_leading_time_provisioning(self, post_provision_login_status, post_provision_login):
        if post_provision_login_status == "Yes":
            self.element_click(self.post_provision_login_checkbox, locator_type="xpath")
        else:
            self.send_keys(post_provision_login, self.provision_post_login_id)

    def enter_no_extension(self, extend_duration_status, no_of_extensions, select_pack, threshhold_value):
        if extend_duration_status == "Yes":
            self.element_click(self.extension_resource_duration_checkbox_xpath, locator_type="xpath")

            self.send_keys(no_of_extensions, self.no_of_extension_xpath, locator_type="xpath")

            self.select_dropdown_by_name(select_pack, self.select_extension_pack_xpath,
                                         self.select_extension_pack_list_xpath)

            self.send_keys(threshhold_value, self.extension_resource_usage_xpath, locator_type="xpath")

    def enter_auth_name(self, auth_name):
        self.send_keys(auth_name, self.auth_name_xpath, locator_type="xpath")

    def enter_issuer_url(self, issuer_url):
        self.wait_for_element(self.issue_url_id, locator_type="id")
        self.send_keys(issuer_url, self.issue_url_id, locator_type="id")

    def bulk_upload_local_user(self):
        self.wait_for_element(self.bulk_upload_local_user_xpath, locator_type="xpath")
        self.upload_file(UploadFile.csv_data_file("\\WorkSpace_LocalUser.csv"), self.bulk_upload_local_user_xpath,
                         locator_type="xpath")

    def click_submit(self):
        self.element_click(self.submit_xpath, locator_type="xpath")

    def select_auth_config(self, auth_config):
        self.select_dropdown_by_name(auth_config, self.auth_config_xpath, self.auth_config_list_xpath)

    def click_manual_registration(self, user_name):
        self.wait_for_element(self.manual_Registration_xpath, locator_type="xpath")
        self.element_click(self.manual_Registration_xpath, locator_type="xpath")
        self.wait_for_element(self.addMore_xpath, locator_type="xpath")
        self.element_click(self.addMore_xpath, locator_type="xpath")
        self.wait_for_element(self.username_xpath, locator_type="xpath")
        self.send_keys(user_name, self.username_xpath, locator_type="xpath")
        time.sleep(1)
        self.wait_for_element(self.submit_xpath, locator_type="xpath")
        self.element_click(self.submit_xpath, locator_type="xpath")
        time.sleep(1)

    def auth_config_local_user_registration(self, issuer_url):
        self.enter_issuer_url(issuer_url)
        self.bulk_upload_local_user()
        self.click_submit()

    def verify_published_workspace_name(self):
        return self.get_text(self.published_success_text_xpath, locator_type="xpath")

    def verify_ws_vm_page(self):
        return self.get_text(self.ws_stop_text, locator_type="xpath")
