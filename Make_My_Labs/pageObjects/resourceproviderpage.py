import time
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta


class ResourceProvider(Basepage, metaclass=Logmethodmeta):

    def __init__(self, driver):
        super().__init__(driver)

    private_resource_provider = "//h1[normalize-space()='Private Resource Provider']"
    public_resource_provider = "//h1[normalize-space()='Public Resource Provider']"
    select_resource_provider_dropdown_xpath = "//input[@id='provider_name']"
    select_resource_provider_dropdown_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder']//div[@class='rc-virtual-list-holder-inner']//div//div"
    searchbox_xpath = "//input[@placeholder='Search']"
    connection_list_name_to_click = "//tbody[@class='ant-table-tbody']//tr[2]//td//u//div"
    create_template_button = "//button[@class='ant-btn ant-btn-primary qa-createTemplate-btn']"
    connection_name = "//table//th//div//span[contains(text(),'Connection Name')]"
    username = "//table//th//div//span[contains(text(),'Username')]"
    vmware_datacenter = "//table//th//div//span[contains(text(),'VMWare Datacenter')]"
    vmware_cluster = "//table//th//div//span[contains(text(),'VMWare Cluster')]"
    add_resource_provider_button1 = "//button[@class='ant-btn ant-btn-primary addAccount-btn qa-addAccount-btn']"
    add_resource_provider_button2 = "//button[@class='ant-btn ant-btn-primary qa-add-btn']"
    connection_name_text = "//input[@id='connection_name']"
    server_url_text = "//input[@id='server_url']"
    username_text = "//input[@id='username']"
    password_text = "//input[@id='password']"
    host_enable_checkbox = "//span[@class='ant-typography body-long-text']"
    connect_button = "//button[@type='submit']"
    connection_name_searchbox = "//input[@placeholder='Search']"
    vmware_data_center_input_xpath = "//input[@id='vmware_datacenter']"
    vmware_data_center_input_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div//div"
    vmware_cluster_input_xpath = "//input[@id='vmware_cluster']"
    vmware_cluster_list_input_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div//div"
    datastore_cluster_input_xpath = "//input[@id='datastore_cluster']"
    datastore_cluster_list_xpath = "//div[@class='rc-virtual-list']//div[@class='rc-virtual-list-holder-inner']//div//div"
    resoucre_provider_created_success_message = "//div[@class='ant-notification-notice-message' and contains(text(),'Created')]"

    def click_add_resource_provider_button1(self):
        self.wait_for_element(self.add_resource_provider_button1, locator_type="xpath")
        self.element_click(self.add_resource_provider_button1, locator_type="xpath")

    def click_add_resource_provider_button2(self):
        self.wait_for_element(self.add_resource_provider_button2, locator_type="xpath")
        self.element_click(self.add_resource_provider_button2, locator_type="xpath")

    def input_connection_name(self, connectionname):
        self.wait_for_element(self.connection_name_text, locator_type="xpath")
        self.send_keys(connectionname, self.connection_name_text, locator_type="xpath")

    def input_server_url(self, serverurl):
        self.wait_for_element(self.server_url_text, locator_type="xpath")
        self.send_keys(serverurl, self.server_url_text, locator_type="xpath")

    def input_username(self, username):
        self.wait_for_element(self.username_text, locator_type="xpath")
        self.send_keys(username, self.username_text, locator_type="xpath")

    def input_password(self, password):
        self.wait_for_element(self.password_text, locator_type="xpath")
        self.send_keys(password, self.password_text, locator_type="xpath")

    def click_host_enable_checkbox(self, check_box):
        self.wait_for_element(self.host_enable_checkbox, locator_type="xpath")
        if check_box == "Yes":
            self.element_click(self.host_enable_checkbox, locator_type="xpath")

    def click_connect_button(self):
        self.wait_for_element(self.connect_button, locator_type="xpath")
        self.element_click(self.connect_button, locator_type="xpath")

    def enter_vm_ware_data_center(self, name):
        self.wait_for_element(self.vmware_data_center_input_xpath, locator_type="xpath")
        self.select_dropdown_by_name(name, self.vmware_data_center_input_xpath, self.vmware_data_center_input_list_xpath)

    def enter_vm_ware_cluster(self, name):
        self.wait_for_element(self.vmware_cluster_input_xpath, locator_type="xpath")
        self.select_dropdown_by_name(name, self.vmware_cluster_input_xpath, self.vmware_cluster_list_input_xpath)

    def enter_datastore_cluster(self, name):
        self.wait_for_element(self.datastore_cluster_input_xpath, locator_type="xpath")
        self.select_dropdown_by_name(name, self.datastore_cluster_input_xpath, self.datastore_cluster_list_xpath)

    def select_resource_provider_dropdown(self, resource_provider_name):
        self.select_dropdown_by_name(resource_provider_name, self.select_resource_provider_dropdown_xpath,
                                     self.select_resource_provider_dropdown_xpath)

    def search_private_resource_provider_input(self, connection_name):
        self.send_keys(connection_name, self.searchbox_xpath, locator_type="xpath")
        time.sleep(2)

    def click_connection_name(self):
        self.element_click(self.connection_list_name_to_click, locator_type="xpath")

    def send_resourceprovider_data(self, connectionname, serverurl, username, password, check_box, vm_ware_data_center,
                                   vm_ware_cluster, datastore_cluster):
        self.input_connection_name(connectionname)
        self.input_server_url(serverurl)
        self.input_username(username)
        self.input_password(password)
        self.click_host_enable_checkbox(check_box)
        self.click_connect_button()
        self.enter_vm_ware_data_center(vm_ware_data_center)
        self.enter_vm_ware_cluster(vm_ware_cluster)
        self.enter_datastore_cluster(datastore_cluster)
        self.click_add_resource_provider_button2()

    def reach_template_page(self, resource_provider_name, connection_name):
        self.select_resource_provider_dropdown(resource_provider_name)
        self.search_private_resource_provider_input(connection_name)
        self.click_connection_name()

    def resource_provided_created_verify(self):
        return self.get_text(self.resoucre_provider_created_success_message, locator_type="xpath")
