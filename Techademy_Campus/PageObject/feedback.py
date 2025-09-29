import time

from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl


from Techademy_Campus.Configuration.readProperties import (ReadConfig)

class Feedback(Basepage):

    log = cl.custom_logger()
    """

        This feedback class is for searching the feedback with name for (Registrar ,HOD, Faculty,Student Role)
        and providing feedback to course ,feedback for faculty ,feedback for others in Student role.

        Author : Meghana Avinash Kadam
    """

    search_textbox_value = ReadConfig.get_feedback('FeedBack', 'search_textbox')
    description_textbox_value = ReadConfig.get_feedback('FeedBack', 'description_textbox')
    expected_result = ReadConfig.get_expected_result('Expected Results', 'feedback')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _profile_tab = "//p[@class='designation-title']"
    _feedback_tab = "//span[text()='Feedback']"
    _search_textbox = "//input[@placeholder='Search...']"
    _provide_a_feedback_button = "//button[text()='Provide a feedback']"
    _course = ("//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputTypeSearch "
               "MuiInputBase-inputSizeSmall MuiAutocomplete-input MuiAutocomplete-inputFocused css-1g6d2zd']")
    _faculty = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[2]"
    _select_faculty = "//div[@name='facultyDrop']"
    _select_faculty_name = "//li[@data-option-index='6']"
    _other = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[3]"
    _select_course = "//li[@data-option-index='1']"
    _your_feedback = "//textarea[@name='feedback_desc']"
    _submit_button = "//button[text()='Submit']"
    _cancel_button = "//button[text()='Cancel']"
    _actual_element = "//div[text()='Feedback Submitted Successfully']"
    _logout_tab = "//span[text()='Logout']"

    def click_on_profile(self):
        self.element_click_js(self._profile_tab, "xpath")

    def click_on_feedback(self):
        self.wait_for_element(self._feedback_tab, locator_type="xpath")
        self.element_click(self._feedback_tab, "xpath")

    def enter_feedback_by(self, search_textbox):
        self.element_click_js(self._search_textbox, "xpath")
        self.send_keys(search_textbox, self._search_textbox, locator_type="xpath")

    def click_on_provide_a_feedback_button(self):
        self.wait_for_element(self._provide_a_feedback_button, locator_type="xpath")
        self.element_click_js(self._provide_a_feedback_button, "xpath")

    def click_on_course(self):
        # self.waitForElement(self._course, locator_type="xpath")
        self.element_click(self._course, "xpath")
        self.element_click(self. _select_course, "xpath")

    def enter_description(self, description_textbox):
        self.element_click(self._your_feedback, "xpath")
        self.send_keys(description_textbox, self._your_feedback, locator_type="xpath")

    def click_on_faculty_radio_button(self):
        self.element_click(self. _faculty, "xpath")
        self.element_click_js(self. _select_faculty, "xpath")
        self.element_click(self. _select_faculty, "xpath")
        self.element_click_js(self._select_faculty_name, locator_type="xpath")


    def click_on_other_radio_button(self):
        self.element_click(self._other, "xpath")

    def click_on_logout(self):
        self.wait_for_element(self._logout_tab, locator_type="xpath")
        self.element_click(self._logout_tab, "xpath")

    def click_on_submit_button(self):
        self.element_click(self. _submit_button, "xpath")

    def click_on_cancel_button(self):
        self.element_click(self. _cancel_button, "xpath")

    def search_feedback(self):
        self.click_on_profile()
        self.click_on_feedback()
        time.sleep(1)
        self.enter_feedback_by(self.search_textbox_value)
        time.sleep(2)
        self.web_scroll("down")
        time.sleep(1)


    def feedback_for_course(self):
        # self.click_on_profile()
        # self.click_on_feedback()
        # time.sleep(1)
        self.click_on_provide_a_feedback_button()
        self.click_on_course()
        self.enter_description(self.description_textbox_value)
        time.sleep(1)
        self.click_on_submit_button()
        time.sleep(1)
        # self.click_on_cancel_button()

    def feedback_for_faculty(self):
        # self.click_on_profile()
        # self.click_on_feedback()
        self.click_on_provide_a_feedback_button()
        self.click_on_faculty_radio_button()
        self.enter_description(self.description_textbox_value)
        self.click_on_submit_button()
        time.sleep(1)

    def feedback_for_other(self):
        # self.click_on_profile()
        # self.click_on_feedback()
        # time.sleep(1)
        self.click_on_provide_a_feedback_button()
        self.click_on_other_radio_button()
        self.enter_description(self.description_textbox_value)
        time.sleep(1)
        self.click_on_submit_button()
        time.sleep(1)


    def verify_feedback_output(self):
        self.verify_by_comparing_text(locator=self._actual_element, locator_type="xpath", expected_result=self.
                                      expected_result, result_msg="Feedback not submitted")
