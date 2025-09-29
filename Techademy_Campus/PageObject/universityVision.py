from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
import time
from Techademy_Campus.Configuration.readProperties import ReadConfig


class UniversityVision(Basepage):
    log = cl.custom_logger()


    """
        This Create University vision class is for creating an university vision and preview the vision 
         in registrar role.
        
          Author: Meghana Aviansh Kadam
        
    """


    vision_name_value = ReadConfig.get_university_vision('University Vision', 'vision_name')
    vision_description_value = ReadConfig.get_university_vision('University Vision', 'vision_description')
    expected_result_save = ReadConfig.get_expected_result('Expected Results', 'save_university_vision')
    expected_result_create = ReadConfig.get_expected_result('Expected Results', 'create_university_vision')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _manage_tab = "//button[text()='Manage']"
    _programs_tab = "//span[text()='Programs']"
    _university_vision = "//button[text()='UNIVERSITY VISION']"
    _vision_tab = "//input[@class='MuiInputBase-input MuiOutlinedInput-input css-1ebbnfp']"
    _description_tab = "//div[@class='ql-editor ql-blank']"
    _save_button = "//button[text()='Save']"
    _preview_button = "//button[text()='Preview']"
    _close_button = "//button[text()='Close']"
    _submit_button = "//button[text()='Submit']"
    _download_button = "//button[text()='Download']"
    _printer_option = "//button[@id='selecttrigger-1']//div[text()='Microsoft Print to PDF']"
    _save_pdf = "//span[text()='Save']"
    _cancel_button = "//span[text()='Cancel']"
    _actual_result_save = "//div[text()='Vision saved']"
    _actual_result_submit = "//div[text()='Vision Created Successfully']"



    def click_on_manage(self):
        self.wait_for_element(self._manage_tab, locator_type="xpath")
        self.element_click(self._manage_tab, "xpath")

    def click_on_programs(self):
        self.wait_for_element(self._programs_tab, locator_type="xpath")
        self.element_click(self._programs_tab, "xpath")

    def click_on_university_vision(self):
        self.wait_for_element(self. _university_vision, locator_type="xpath")
        self.element_click(self. _university_vision, "xpath")

    def enter_vision(self, vision_name):
        self.wait_for_element(self._vision_tab, locator_type="xpath")
        self.element_click(self._vision_tab, "xpath")
        self.send_keys(vision_name, self._vision_tab, "xpath")

    def enter_vision_description(self, vision_description):
        self.wait_for_element(self._description_tab, locator_type="xpath")
        self.element_click(self._description_tab, "xpath")
        self.send_keys(vision_description, self._description_tab, "xpath")

    def click_on_save(self):
        self.wait_for_element(self. _save_button, locator_type="xpath")
        self.element_click(self. _save_button, "xpath")

    def click_on_preview(self):
        self.wait_for_element(self._preview_button, locator_type="xpath")
        self.element_click(self. _preview_button, "xpath")

    def click_on_close(self):
        self.wait_for_element(self._close_button, locator_type="xpath")
        self.element_click(self._close_button, "xpath")

    def click_on_download(self):
        self.wait_for_element(self. _download_button, locator_type="xpath")
        self.element_click(self. _download_button, "xpath")

    def click_on_printer(self):
        self.wait_for_element(self.  _printer_option, locator_type="xpath")
        self.element_click(self.  _printer_option, "xpath")

    def click_on_save_pdf(self):
        self.wait_for_element(self._save_pdf, locator_type="xpath")
        self.element_click(self._save_pdf, "xpath")

    def click_on_submit(self):
        self.wait_for_element(self._submit_button, locator_type="xpath")
        self.element_click(self._submit_button, "xpath")


    def create_university_vision(self):
        self.click_on_manage()
        self.click_on_programs()
        self.click_on_university_vision()
        self.enter_vision(self.vision_name_value)
        time.sleep(2)
        self.enter_vision_description(self.vision_description_value)
        time.sleep(2)
        self.click_on_save()
        self.verify_save_university_vision()
        time.sleep(2)


    def preview_university_vision(self):
        self.click_on_preview()
        time.sleep(2)
        self.click_on_close()
        time.sleep(2)
        # self.click_on_download()
        # time.sleep(2)
        # self.click_on_printer()
        # time.sleep(2)
        # self.click_on_save_pdf()
        # time.sleep(2)
        self.click_on_submit()
        self.verify_create_university_vision()
        time.sleep(2)


    def verify_save_university_vision(self):
        self.verify_by_comparing_text(locator=self._actual_result_save,locator_type="xpath",
                                      expected_result=self.expected_result_save, result_msg="Vision Not Saved")


    def verify_create_university_vision(self):
        self.verify_by_comparing_text(locator=self._actual_result_submit,locator_type="xpath",
                                      expected_result=self.expected_result_create, result_msg="Vision Not Created")


