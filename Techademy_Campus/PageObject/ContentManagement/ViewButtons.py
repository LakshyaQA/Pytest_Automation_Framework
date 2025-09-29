import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class ViewButtons(Basepage):
    log = cl.custom_logger()

    '''
        This class includes viewing of the CO PO Mapping, viewing of Course Outcome and View as a Student. 

        author: Abhilash

        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for viewing CO PO Mapping, Course Outcomes & As a Student

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    ViewAsAStudent_button = "//button[text()='View As a Student']"
    Close_symbol = "//button[contains(@aria-label, 'close')]"
    ViewCourseOutcome_button = "//button[text()='View Course Outcome']"
    Close_button = "//button[text()='Close']"
    COPOMapping_button = "//button[text()='CO PO Mapping']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnDepartment(self):
        self.wait_for_element(self.Department_option, locator_type="xpath")
        self.element_click_js(self.Department_option, "xpath")

    def clickOnViewDetails(self):
        self.wait_for_element(self.ViewDetails_button, locator_type="xpath")
        self.element_click_js(self.ViewDetails_button, "xpath")

    def clickOnViewAsAStudent(self):
        self.wait_for_element(self.ViewAsAStudent_button, locator_type="xpath")
        self.element_click_js(self.ViewAsAStudent_button, "xpath")
        self.web_scroll("Down")
        time.sleep(2)

    def clickOnCloseSymbol(self):
        self.wait_for_element(self.Close_symbol, locator_type="xpath")
        self.element_click_js(self.Close_symbol, "xpath")
        time.sleep(2)

    def clickOnViewCourseOutcomes(self):
        self.wait_for_element(self.ViewCourseOutcome_button, locator_type="xpath")
        self.element_click_js(self.ViewCourseOutcome_button, "xpath")
        time.sleep(1)

    def clickOnCloseButton(self):
        self.wait_for_element(self.Close_button, locator_type="xpath")
        self.element_click_js(self.Close_button, "xpath")
        time.sleep(2)

    def clickOnCOPOMapping(self):
        self.wait_for_element(self.COPOMapping_button, locator_type="xpath")
        self.element_click_js(self.COPOMapping_button, "xpath")
        time.sleep(2)

    def ViewingButtons(self):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnViewAsAStudent()
        self.clickOnCloseSymbol()
        self.clickOnViewCourseOutcomes()
        self.clickOnCloseButton()
        self.clickOnCOPOMapping()
