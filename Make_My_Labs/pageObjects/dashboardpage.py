import time
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta


class Dashboardpage(Basepage, metaclass=Logmethodmeta):

    def __init__(self, driver):
        super().__init__(driver)

    dashboard = "//a[@href='/dashboard']"
    machine_catalog_0 = ("//div[@role='menuitem']//span[@class='ant-typography label-regular'][normalize-space("
                         ")='Machine Catalog']")
    machine_catalog_1 = "//a[@href='/machineCatalogue']"
    machine_catalog_2 = "//span[@class='ant-menu-title-content']//a[@href='/userMachineCatalog']"
    tenant_catalog = "//a[@href='/tenantCatalogue']"
    b2c = "//span[@class='ant-typography label-regular'][normalize-space()='B2C']"
    b2c_labs = ("//li[@class='ant-menu-item ant-menu-item-only-child vertical-line border-less border-top "
                "submenu-border-left qa-catalogue-sku-b2c-item sider-items-sub']//a")
    plans = ("//li[@class='ant-menu-item ant-menu-item-only-child vertical-line border-less border-top "
             "submenu-border-left qa-plan-item sider-items-sub']//a")
    request_manager = "//a[@href='/requestManager']"
    resource_manager = "//span[contains(text(),'Resource Manager')]"
    resource_provider = "//span[@class='ant-menu-title-content']//a[@href='/resourceManager/resourceProvider']"
    manage_vm = "//a[@href='/manageVm']"
    manage_instance_size = "//a[@href='/resourceManager/manageInstanceSize']"
    tenant_management = "//span[contains(text(),'Tenant Management')]"
    tenants = "//a[@href='/tenantManagement']"
    user_management = "//a[@href='/tenantManagement/userManagement']"
    workspace_manager = "//a[@href='/workspace']"
    usage = "//a[@href='/usage']"
    notification_manager = "//span[contains(text(),'Notification Manager')]"
    manage_notifications = "//a[@href='/notificationManagement']"
    notifications = "//a[@href='/notifications']"
    settings = "//span[@class='ant-typography label-regular'][normalize-space()='Settings']"
    action_logs = "//a[@href='/actionLog']"
    rbac_management = "//a[@href='/tenantManagement/rbacManagement']"
    notification_settings = "//a[@href='/notificationSettings']"
    reports = "//a[@href='/report/customReport']"
    vm_insights = "//a[@href='/vm-insight']"
    invoices = "//a[@href='/invoices']"
    reseller_license = "//a[@href='/LicenceList']"
    welcome_text = "//span[@class='ant-typography label-regular welcome-title']"
    donot_show_again_xpath = "//h1[contains(text(),'Show Again')]"
    logout_symbol = "(//*[name()='svg']//*[@id='Shape'])[2]"
    logout_button = "//button[@type='submit']"
    account_button = "//small[@data-bind='text: session.unsafe_displayName']"
    loader_xpath = "//div[@class='loader-text']"

    def click_dashboard(self):
        self.wait_for_element(self.dashboard, locator_type="xpath")
        self.element_click_js(self.dashboard, locator_type="xpath")

    def click_resource_manager(self):
        self.wait_for_element(self.resource_manager, locator_type="xpath")
        self.element_click_js(self.resource_manager, locator_type="xpath")

    def click_resource_provider(self):
        self.click_resource_manager()
        self.wait_for_element(self.resource_provider, locator_type="xpath")
        self.element_click_js(self.resource_provider, locator_type="xpath")

    def click_tenant_management(self):
        self.wait_for_element(self.tenant_management, locator_type="xpath")
        self.element_click_js(self.tenant_management, locator_type="xpath")

    def click_tenants(self):
        self.wait_for_element(self.tenants, locator_type="xpath")
        self.element_click_js(self.tenants, locator_type="xpath")

    def click_user_management(self):
        self.wait_for_element(self.user_management, locator_type="xpath")
        self.element_click_js(self.user_management, locator_type="xpath")

    def click_workspace_manager(self):
        self.element_click_js(self.workspace_manager, locator_type="xpath")

    def click_machine_catalog0(self):
        self.element_click_js(self.machine_catalog_0, locator_type="xpath")

    def click_machine_catalog(self):
        self.click_machine_catalog0()
        self.element_click_js(self.machine_catalog_1, locator_type="xpath")

    def click_machine_catalog2(self):
        self.wait_for_element(self.machine_catalog_2, locator_type="xpath")
        self.element_click_js(self.machine_catalog_2, locator_type="xpath")

    def click_tenant_catalog(self):
        self.click_machine_catalog0()
        time.sleep(1)
        self.element_click_js(self.tenant_catalog, locator_type="xpath")
        time.sleep(1)

    def get_welcome_text_dashboard(self):
        return self.get_text(self.welcome_text, locator_type="xpath")

    def click_do_not_show_again(self):
        self.wait_for_element(self.donot_show_again_xpath, locator_type="xpath")
        self.element_click_js(self.donot_show_again_xpath, locator_type="xpath")

    def logout(self):
        self.wait_till_element_invisibility(self.loader_xpath, locator_type="xpath", timeout=5)
        self.wait_for_element(self.logout_symbol, locator_type="xpath")
        self.element_click(self.logout_symbol, locator_type="xpath")
        self.wait_for_element(self.logout_button, locator_type="xpath")
        self.element_click_js(self.logout_button, locator_type="xpath")
        self.wait_for_element(self.account_button, locator_type="xpath")
        self.element_click_js(self.account_button, locator_type="xpath")
        time.sleep(3)
