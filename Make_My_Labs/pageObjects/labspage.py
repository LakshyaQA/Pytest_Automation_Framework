import time

from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta


class Labspage(Basepage, metaclass=Logmethodmeta):

    def __init__(self, driver):
        super().__init__(driver)

    provision_success_message_xpath = "//span[contains(text(),'Provisioning Success')]"
    start_button_xpath = "//*[name()='svg' and @class='pointer-cursor qa-start-btn ']"
    submit_button_xpath = "//button[@type='submit']"
    running_xpath = "//span[contains(text(),'Running')]"
    connect_button_xpath = "//*[name()='svg' and @class='qa-connect-btn pointer-cursor']"
    stop_button_xpath = "//button[@type='button']//span[contains(text(),'Stop')]"

    def click_start_button(self):
        self.wait_for_element(self.start_button_xpath, locator_type="xpath")
        self.element_click(self.start_button_xpath, locator_type="xpath")

    def click_submit_button(self):
        self.wait_for_element(self.submit_button_xpath, locator_type="xpath")
        self.element_click(self.submit_button_xpath, locator_type="xpath")

    def click_connect_button(self):
        self.wait_for_element(self.connect_button_xpath, locator_type="xpath")
        self.element_click(self.connect_button_xpath, locator_type="xpath")

    def click_stop_button(self):
        self.wait_for_element(self.stop_button_xpath, locator_type="xpath")
        self.element_click(self.stop_button_xpath, locator_type="xpath")

    def visit_guidedlab_vm(self):
        self.wait_for_element(self.provision_success_message_xpath, locator_type="xpath", timeout=600)
        time.sleep(2)
        self.click_start_button()
        self.click_submit_button()
        self.wait_for_element(self.running_xpath, locator_type="xpath")
        self.click_connect_button()
        self.click_submit_button()

    def verify_guidedlab_vm(self):
        time.sleep(60)
        return self.get_text(self.stop_button_xpath, locator_type="xpath")
