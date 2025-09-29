import time

from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl


class EmployeeTab(Basepage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _interviewer = "//h4[contains(text(), 'Raj Malhotra')]"
    _edit = ("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary "
             "MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-text "
             "MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary css-1jvgoqt']")
    _location = "//input[@name='location']"
    _select_online = "//li[contains(text(), 'Online')]"
    _designation = "//input[@name='designation']"
    _click_edit = "//button[contains(text(), 'Edit')]"
    _actual_result = "//h6[contains(text(), 'On-Site')]"

    def select_interviewer(self):
        self.wait_for_element(self._interviewer, locator_type="xpath")
        self.element_click_js(self._interviewer, locator_type="xpath")

    def click_on_edit(self):
        self.wait_for_element(self._edit, locator_type="xpath")
        self.element_click_js(self._edit, locator_type="xpath")

    def edit_location(self, location):
        self.wait_for_element(self._location, locator_type="xpath")
        self.element_click(self._location, locator_type="xpath")
        self.clear_input_field(self._location, locator_type="xpath")
        self.send_keys(location, self._location, locator_type="xpath")

    def edit_designation(self, designation):
        self.wait_for_element(self._designation, locator_type="xpath")
        self.clear_input_field(self._designation, locator_type="xpath")
        self.send_keys(designation, self._designation, locator_type="xpath")

    def edit_button(self):
        self.wait_for_element(self._click_edit, locator_type="xpath")
        self.element_click_js(self._click_edit, locator_type="xpath")

    def edit_interviewer_details(self, location, designation):
        self.click_on_edit()
        time.sleep(2)
        self.edit_location(location)
        time.sleep(2)
        self.edit_designation(designation)
        time.sleep(2)
        self.edit_button()
        self.wait_for_element(self._actual_result, locator_type="xpath")
        return self.get_text(self._actual_result, locator_type="xpath")
