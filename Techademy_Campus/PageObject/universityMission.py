from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
import time
from Techademy_Campus.Configuration.readProperties import ReadConfig


class UniversityMission(Basepage):
    log = cl.custom_logger()

    '''
         This Create University Mission class is for creating a university mission and preview it  in registrar role 

              author : Meghana Avinash Kadam 

        '''
    mission_name_value = ReadConfig.get_university_mission('University Mission', 'mission_name')
    mission_description_value = ReadConfig.get_university_mission('University Mission', 'mission_description')
    expected_result_save = ReadConfig.get_expected_result('Expected Results', 'save_university_mission')
    expected_result_submit = ReadConfig.get_expected_result('Expected Results', 'submit_university_mission')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _manage_tab = "//button[text()='Manage']"
    _programs_tab = "//span[text()='Programs']"
    _university_mission = "//button[text()='UNIVERSITY MISSION']"
    _mission_tab = "//input[@class='MuiInputBase-input MuiOutlinedInput-input css-1ebbnfp']"
    _description_tab = "//div[@class='ql-editor ql-blank']"
    _add_icon = "//div[@class='MuiGrid-root css-1ntbpe1']"
    _save_icon = "(//div[@class='MuiGrid-root css-1m41dy5'])[1]"
    _preview_button = "//button[text()='Preview']"
    _close_button = "//button[text()='Close']"
    _submit_button = "//button[text()='Submit']"
    _download_button = "//button[text()='Download']"
    _printer_option = "//button[@id='selecttrigger-1']//div[text()='Microsoft Print to PDF']"
    _save_pdf = "//span[text()='Save']"
    _cancel_button = "//span[text()='Cancel']"
    _actual_university_mission_save = "//div[text()='mission-1 saved']"
    _actual_university_mission_submit = "//div[text()='Mission Created Successfully']"

    def click_on_manage(self):
        self.wait_for_element(self._manage_tab, locator_type="xpath")
        self.element_click(self._manage_tab, "xpath")

    def click_on_programs(self):
        self.wait_for_element(self._programs_tab, locator_type="xpath")
        self.element_click(self._programs_tab, "xpath")

    def click_on_university_mission(self):
        self.wait_for_element(self. _university_mission, locator_type="xpath")
        self.element_click(self. _university_mission, "xpath")

    def enter_mission(self, mission_name):
        self.wait_for_element(self._mission_tab, locator_type="xpath")
        self.element_click(self._mission_tab, "xpath")
        self.send_keys(mission_name, self._mission_tab, "xpath")

    def enter_mission_description(self, mission_description):
        self.wait_for_element(self._description_tab, locator_type="xpath")
        self.element_click(self._description_tab, "xpath")
        self.send_keys(mission_description, self._description_tab, "xpath")

    def click_on_add(self):
        self.wait_for_element(self._add_icon, locator_type="xpath")
        self.element_click(self._add_icon, "xpath")

    def click_on_save(self):
        self.wait_for_element(self. _save_icon, locator_type="xpath")
        self.element_click(self. _save_icon, "xpath")

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


    def create_university_mission(self):
        self.click_on_manage()
        self.click_on_programs()
        self.click_on_university_mission()
        self.enter_mission(self.mission_name_value)
        time.sleep(2)
        self.enter_mission_description(self.mission_description_value)
        time.sleep(2)
        self.click_on_save()
        self.verify_university_mission_save()
        time.sleep(2)

    def preview_university_mission(self):
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
        self.verify_university_mission_submit()
        time.sleep(2)


    def verify_university_mission_save(self):
        self.verify_by_comparing_text(locator=self._actual_university_mission_save, locator_type="xpath",
                                      expected_result=self.expected_result_save,
                                      result_msg="University Mission Not saved")

    def verify_university_mission_submit(self):
        self.verify_by_comparing_text(locator=self._actual_university_mission_submit, locator_type="xpath",
                                      expected_result=self.expected_result_submit,
                                      result_msg="University Mission Not Created")


