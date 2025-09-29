import time
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Make_My_Labs.Configration.configpath import UploadFile
from Make_My_Labs.Configration.csvdatareader import Csvdatareader


class TenantCatalogPage(Basepage, metaclass=Logmethodmeta):
    def __init__(self, driver):
        super().__init__(driver)

    tenant_dropdown_xpath = "//input[@id='rc_select_2']"
    tenant_dropdown_list_xpath = ("//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder']//div["
                                  "@class='rc-virtual-list-holder-inner']//div//div")
    search_box_xpath = "//input[@placeholder='Search']"
    standalone_radio_xpath = "//input[@value='1']"
    guided_lab_radio_xpath = "//input[@value='0']"
    export_button_xpath = "//button[@class='ant-btn ant-btn-secondary btn-small']//span"
    vm_preparing_text_xpath = "// span[contains(text(), 'Preparing your VM')]"
    # Login end user
    email_id_field = "//div[@class='placeholderContainer']//input[@type='email']"
    password_field = "//div[@class='placeholderContainer']//input[@name='passwd']"
    next_button = "//div[@class='inline-block button-item ext-button-item']//input[@type='submit']"
    signin_button = "//div[@class='inline-block button-item ext-button-item']//input[@type='submit']"
    vm_prepare_dialog_box = "//span[contains(text(),'Preparing your VM')]"
    extend_vm_text_xpath = "//span[@class='ant-typography label-graph mt4']"
    # Super admin logout
    logout_symbol = "//header[@class='ant-layout-header header']//div[5]//*[name()='svg']"
    logout_button = "//button[@type='submit']"
    logout_account = "//div[normalize-space()='gslabadmin']"
    use_another_account = "//div[@id='otherTileText']"

    def select_tenant(self, tenant_name):
        self.wait_for_element(self.tenant_dropdown_xpath, locator_type="xpath")
        self.select_dropdown_by_name(
            tenant_name, self.tenant_dropdown_xpath, self.tenant_dropdown_list_xpath)

    def click_export(self):
        self.wait_for_element(self.export_button_xpath, locator_type="xpath")

        self.download_file(UploadFile.file_download_location(), self.export_button_xpath,
                           locator_type="xpath", file_name="\\tenant-catalog.csv")

    def logout_super_admin(self):
        self.wait_for_element(self.logout_symbol, locator_type="xpath")
        self.element_click(self.logout_symbol, locator_type="xpath")
        self.wait_for_element(self.logout_button, locator_type="xpath")
        self.element_click(self.logout_button, locator_type="xpath")
        self.wait_for_element(self.logout_account, locator_type="xpath")
        self.element_click(self.logout_account, locator_type="xpath")
        time.sleep(2)

    def enter_email(self, email):
        self.send_keys(email, self.email_id_field, locator_type="xpath")

    def click_next_button(self):
        self.element_click_js(self.next_button, locator_type="xpath")

    def enter_password(self, password):
        self.send_keys(password, self.password_field, locator_type="xpath")

    def click_signin_button(self):
        self.element_click_js(self.signin_button, locator_type="xpath")

    def login_end_user(self, email, password):
        self.wait_for_element(self.email_id_field, locator_type="xpath")
        self.enter_email(email)
        self.wait_for_element(self.next_button, locator_type="xpath")
        self.click_next_button()
        self.wait_for_element(self.password_field, locator_type="xpath")
        self.enter_password(password)
        self.wait_for_element(self.password_field, locator_type="xpath")
        self.click_signin_button()

    def download_csv_file(self, tenant_name):
        self.select_tenant(tenant_name)
        time.sleep(2)
        self.click_export()
        self.logout_super_admin()

    def login_pooled_vm(self):
        odl_url = Csvdatareader.get_data_from_csv(UploadFile.csv_data_file("\\tenant-catalog.csv"),
                                                  "D0010_AutomationTest_Template_displayname_pooled", "ODL URL")
        self.visit_url(odl_url)
        self.log.info("Going to ODL URL " + odl_url)
        self.wait_for_element(self.use_another_account, locator_type="xpath")
        self.element_click(self.use_another_account, locator_type="xpath")
        time.sleep(1)

    def verify_pooled_vm_page(self):
        self.wait_till_element_invisibility(self.vm_preparing_text_xpath, locator_type="xpath", timeout=180)
        self.wait_for_element(self.extend_vm_text_xpath, locator_type="xpath")
        time.sleep(30)
        return self.get_text(self.extend_vm_text_xpath, locator_type="xpath")

