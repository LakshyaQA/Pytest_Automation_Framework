

from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
from Techademy_Campus.Configuration.readProperties import ReadConfig


class FacultyTimeTable(Basepage):

    log = cl.custom_logger()

    """
       This Faculty TimeTable class is for viewing the faculty timetable in registrar flow  and viewing
        My timetable in Faculty ,Student ,HOD Role.

        Author : Meghana Avinash Kadam

    """


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    _timetable_tab = "//span[text()='Time Table']"
    _Program_name = "//div[@name='program_name']"
    _select_program = "//li[text()='BTech in Marine Engineering']"
    _subject_name = "//div[@name='subject_name']"
    _select_subject = "//li[text()='Mathematics – I (ME1-01)']"
    _faculty_name = "//div[@name='faculty_name']"
    _select_faculty = "//li[text()='Faculty one']"
    _start_date = "(//input[@placeholder='mm/dd/yyyy'])[1]"
    _end_date = "(//input[@placeholder='mm/dd/yyyy'])[2]"
    _session_name = "//span[text()='Online session']"

    def click_on_time_table(self):
        self.wait_for_element(self._timetable_tab, locator_type="xpath")
        self.element_click_js(self._timetable_tab, "xpath")

    def click_on_program_name(self):
        self.element_click(self._Program_name, "xpath")
        #  self.waitForElement(self._Program_name, locator_type="xpath")

    def click_on_program(self):
        self.element_click(self._select_program, "xpath")
        # self.waitForElement(self._select_program, locator_type="xpath")

    def navigate_to_program_name(self):
        self.click_on_program_name()
        self.click_on_program()

    def click_on_subject_name(self):
        self.element_click(self._subject_name, "xpath")
        # self.waitForElement(self._subject_name, locator_type="xpath")

    def click_on_subject(self):
        self.element_click(self._select_subject, "xpath")
        # self.waitForElement(self._select_subject, locator_type="xpath")


    def navigate_to_subject_name(self):
        self.click_on_subject_name()
        self.click_on_subject()

    def click_on_faculty_name(self):
        self.element_click(self._faculty_name, "xpath")
        # self.waitForElement(self._faculty_name, locator_type="xpath")

    def click_on_faculty(self):
        self.element_click(self._select_faculty, "xpath")
        # self.waitForElement(self._select_faculty, locator_type="xpath")


    def navigate_to_faculty_name(self):
        self.click_on_faculty_name()
        self.click_on_faculty()

    def enter_start_date(self):
        self.wait_for_element(self._start_date, locator_type="xpath")
        date = self.get_current_date(0-2)
        string_date = str(date)
        self.send_keys(string_date, self._start_date, locator_type="xpath")

    def enter_end_date(self):
        self.wait_for_element(self._end_date, locator_type="xpath")
        end_date = self.get_current_date(0+4)
        date_string = str(end_date)
        self.send_keys(date_string, self._end_date, locator_type="xpath")

    def click_on_session_name(self):
        self.element_click(self. _session_name, "xpath")
        self.wait_for_element(self. _session_name, locator_type="xpath")

    def enter_faculty_time_table(self):
        self.click_on_time_table()
        self.navigate_to_program_name()
        self.navigate_to_subject_name()
        self.navigate_to_faculty_name()
        self.enter_start_date()
        self.enter_end_date()

    def my_time_table(self):     # In Faculty flow/HOD Flow/Student Flow  - My Time Table
        self.click_on_time_table()
        self.navigate_to_program_name()
        self.navigate_to_subject_name()
        self.enter_start_date()
        self.enter_end_date()
        # self.click_on_session_name()
