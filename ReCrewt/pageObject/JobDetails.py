from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl


class JobDetails(Basepage):
    log = cl.custom_logger()



    def __init__(self, driver):
       super().__init__(driver)
       self.driver = driver


    #Locators
    _edit = "//button[contains(text(), 'Edit')]"





    def click_edit(self):
        self.wait_for_element(self._edit, locator_type="xpath")
        self.element_click_js(self._edit, locator_type="xpath")

