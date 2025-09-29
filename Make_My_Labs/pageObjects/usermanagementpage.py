from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta


class Usermanagementpage(Basepage, metaclass=Logmethodmeta):

    def __init__(self, driver):
        super().__init__(driver)

    create_new_user_xpath = "//button[@class='ant-btn ant-btn-primary qa-addUser-btn']"
    select_tenant_xpath = "//input[@id='tenant']"
    select_tenant_dropdown_xpath = "//div[@class='rc-virtual-list-holder-inner']//div//div"
    first_name_xpath = "//input[@id='first_name']"
    middle_name_xpath = "//input[@id='middle_name']"
    last_name_xpath = "//input[@id='last_name']"
    email_xpath = "//input[@id='email']"
    mobile_number_xpath = "//input[@id='phone_number']"
    activate_user_account_xpath = "//*[@id='user_activation_by']/label[1]/span[2]/span/strong"
    default_role_dropdown_xpath = "//*[@id='role']"
    default_role_value_xpath = "//div[contains(text(),'Tenant User')]"
    assign_role_xpath = "//input[@id='role_details']"
    assign_role_list_xpath = "//div[@class='rc-virtual-list-holder-inner']//div//div"
    business_unit_xpath = "//*[@id='business_unit']"
    business_unit_value_xpath = "//div[@label='FINANCE']"
    create_user_button_xpath = "//button[@type='submit']//span[contains(text(),'Create New User')]"
    ok_button_xpath = "//button[@class='ant-btn ant-btn-primary qa-create-edit-user-proceed']"
    success_msg_xpath = "//span[@class='ant-typography text-center base undefined']"
    edit_user_option_xpath = "//*[contains(@class,'qa-user-edit')]"
    update_profile_xpath = "//*[contains(@class,'qa-submit-btn')]"
    edit_success_msg_xpath = "//*[contains(@class,'qa-create-edit-user-proceed')]"
    search_bar_xpath = "//input[@type='text']"
    delete_user_option_xpath = "//*[contains(@class,'qa-user-delete')]"
    confirm_delete_button_xpath = "//*[contains(@class,'qa-delete-user-proceed')]"

    def click_create_new_user_button(self):
        self.wait_for_element(self.create_new_user_xpath, locator_type="xpath")
        self.element_click_js(self.create_new_user_xpath, locator_type="xpath")

    def select_tenant(self, tenant_name):
        self.wait_for_element(self.select_tenant_xpath, locator_type="xpath")
        self.select_dropdown_by_name(tenant_name, self.select_tenant_xpath, self.select_tenant_dropdown_xpath)

    def enter_firstname(self, first_name):
        self.wait_for_element(self.first_name_xpath, locator_type="xpath")
        self.send_keys(first_name, self.first_name_xpath, locator_type="xpath")

    def enter_middlename(self, middle_name):
        self.wait_for_element(self.middle_name_xpath, locator_type="xpath")
        self.send_keys(middle_name, self.middle_name_xpath, locator_type="xpath")

    def enter_lastname(self, last_name):
        self.wait_for_element(self.last_name_xpath, locator_type="xpath")
        self.send_keys(last_name, self.last_name_xpath, locator_type="xpath")

    def enter_email_id(self, email_id):
        self.wait_for_element(self.email_xpath, locator_type="xpath")
        self.send_keys(email_id, self.email_xpath, locator_type="xpath")

    def enter_mobile_number(self, mobile_num):
        if mobile_num is not None:
            self.wait_for_element(self.mobile_number_xpath, locator_type="xpath")
            self.send_keys(mobile_num, self.mobile_number_xpath, locator_type="xpath")

    def click_assign_role_dropdown(self, role_name):
        if role_name is not None:
            self.wait_for_element(self.assign_role_xpath, locator_type="xpath")
            self.select_dropdown_by_name(role_name, self.assign_role_xpath, self.assign_role_list_xpath)

    def click_create_new_user(self):
        self.wait_for_element(self.create_user_button_xpath, locator_type="xpath")
        self.element_click(self.create_user_button_xpath, locator_type="xpath")

    def click_success_msg_box(self):
        self.wait_for_element(self.ok_button_xpath, locator_type="xpath")
        self.element_click_js(self.ok_button_xpath, locator_type="xpath")

    def create_new_user(self, tenant_name, first_name, middle_name, last_name, email_id, mobile_num, role_name):
        self.click_create_new_user_button()
        self.select_tenant(tenant_name)
        self.enter_firstname(first_name)
        self.enter_middlename(middle_name)
        self.enter_lastname(last_name)
        self.enter_email_id(email_id)
        self.enter_mobile_number(mobile_num)
        self.click_assign_role_dropdown(role_name)
        self.click_create_new_user()

    def verify_new_user(self):
        self.wait_for_element(self.success_msg_xpath, locator_type="xpath")
        return self.get_text(self.success_msg_xpath, locator_type="xpath")






