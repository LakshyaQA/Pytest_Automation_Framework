import Common_Packages.Utility.custom_logger as cl

from Common_Packages.Base.basepage import Basepage
from Techademy_Campus.Configuration.readProperties import ReadConfig

'''

This page includes locators and functions of internal evaluation for HOD and faculty role

    author : Vidyashri

'''


class Evaluation(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'Internal_Evaluation')

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    _manage_tab = "//button[text()='Manage']"
    _evaluation = "//span[text()='Evaluation']"
    _internal_evaluation = "//button[text()='Internal Evaluation']"
    _program_name = "//input[@name='program_name']"
    _tech_in_marine_engineering = "//li[text()='BTech in Marine Engineering']"
    _select_year = "//input[@name='program_year']"
    _first_year = "//li[text()='First Year']"
    _second_year = "//li[text()='Second Year']"
    _semester = "//input[@name='semester']"
    _semester1 = "//li[text()='Semester 2']"
    _semester4 = "//li[text()='Semester 4']"
    _Subject = "//input[@name='subject']"
    _materials = "//li[text()='Strength of Materials (ME2-05)']"
    _boilers = "//li[text()='Marine Boilers (ME4-15)']"
    _show_details = "//button[text()='Show Details']"
    _select_assignment = "//p[text()='Assignment-23-may']"
    _evaluate = "//a[contains(text(), 'Evaluate')]"
    _feedback_textbox = "//textarea[@name='feedback']"
    _points = "//input[@name='points']"
    _submit = "//button[text()='Submit']"
    _actual_result = "//div[text()='The operation completed successfully']"

    def click_on_manage(self):
        self.element_click(self._manage_tab, "xpath")

    def click_on_evaluation(self):
        self.element_click(self._evaluation, "xpath")

    def select_program_name(self):
        self.element_click_js(self._program_name, "xpath")
        self.element_click_js(self._tech_in_marine_engineering, "xpath")

    def select_year(self, name):
        name_select = f"//li[normalize-space()='{name}']"
        self.element_click_js(self._select_year, "xpath")
        self.element_click_js(name_select, "xpath")

    def select_semester(self, name):
        name_select = f"//li[normalize-space()='{name}']"
        self.element_click_js(self._semester, "xpath")
        self.element_click_js(name_select, "xpath")

    def select_subject(self, name):
        name_select = f"//li[normalize-space()='{name}']"
        self.element_click_js(self._Subject, "xpath")
        self.element_click_js(name_select, "xpath")

    def click_on_show_details(self):
        self.element_click_js(self._show_details, "xpath")

    def click_on_select_assignment(self):
        self.wait_for_element(self._select_assignment, "xpath")
        self.element_click_js(self._select_assignment, "xpath")

    def click_on_evaluate(self):
        self.element_click_js(self._evaluate, "xpath")

    def enter_feedback(self, feedback):
        self.element_click_js(self._feedback_textbox, locator_type="xpath")
        self.send_keys(feedback, self._feedback_textbox, "xpath")

    def enter_points(self, points):
        self.element_click_js(self._points, locator_type="xpath")
        self.send_keys(points, self._points, "xpath")

    def click_on_submit(self):
        self.element_click_js(self._submit, "xpath")

    def navigate_to_manage_tab(self):
        self.click_on_manage()
        self.click_on_evaluation()

    def int_evaluation_fac(self, feedback, points):
        self.select_program_name()
        self.select_year("First Year")
        self.select_semester("Semester 2")
        self.select_subject("Strength of Materials (ME2-05)")
        self.click_on_show_details()
        self.click_on_select_assignment()
        self.click_on_evaluate()
        self.enter_feedback(feedback)
        self.enter_points(points)
        self.click_on_submit()

    def int_evaluation_hod(self, feedback, points):
        self.select_program_name()
        self.select_year("Second Year")
        self.select_semester("Semester 4")
        self.select_subject("Marine Boilers (ME4-15)")
        self.click_on_show_details()
        self.click_on_select_assignment()
        self.click_on_evaluate()
        self.enter_feedback(feedback)
        self.enter_points(points)
        self.click_on_submit()

    def verify_internal_evaluation(self):
        self.verify_by_comparing_text(locator=self._actual_result, locator_type="xpath",
                                      expected_result=self.expected_result,
                                      result_msg="The operation completed successfully.")
