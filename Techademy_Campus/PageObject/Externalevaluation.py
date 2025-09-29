import Common_Packages.Utility.custom_logger as cl

from Common_Packages.Base.basepage import Basepage
from Techademy_Campus.Configuration.readProperties import ReadConfig

'''

This page includes locators and functions of external evaluation for HOD and faculty role

    author : Vidyashri

'''


class EXTEvaluation(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'External_Evaluation')

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # MID/END EXAM Evaluation
    _manage_tab = "//button[text()='Manage']"
    _evaluation = "//span[text()='Evaluation']"
    _mid_end_exam_evaluation = "//button[text()='MID/END EXAM EVALUATION']"
    _program_name = "//input[@name='program_name']"
    _marine_engineering = "//li[text()='BTech in Marine Engineering']"
    _year = "//input[@name='program_year']"
    _first_year1 = "//li[text()='First Year']"
    _second_year = "//li[text()='Second Year']"
    _select_semester = "//input[@name='semester']"
    _semester_2 = "//li[text()='Semester 1']"
    _semester_4 = "//li[text()='Semester 4']"
    _show_details = "//button[text()='Show Details']"
    _view = "(//span[text()='VIEW'])[1]"
    _start_evaluation = "//p[contains(text(), 'Start Evaluation')]"
    _evaluate_exam = "//a[contains(text(), 'Evaluate')]"
    _points_given1 = "//input[@name='points']"
    _submit = "//button[text()='Submit']"
    _feedback_textbox = "//textarea[@name='feedback']"
    _actual_result = "//div[text()='Operation successful']"

    def click_on_manage(self):
        self.element_click(self._manage_tab, "xpath")

    def click_on_evaluation(self):
        self.element_click(self._evaluation, "xpath")

    # mid/end exam evaluation

    def click_on_mid_or_end_exam_evaluation(self):
        self.element_click(self._mid_end_exam_evaluation, "xpath")

    def select_program(self):
        self.element_click_js(self._program_name, "xpath")
        self.element_click_js(self._marine_engineering, "xpath")

    def select_year(self, name):
        name_select = f"//li[normalize-space()='{name}']"
        self.element_click_js(self._year, "xpath")
        self.element_click_js(name_select, "xpath")

    def select_semester(self, name):
        name_select = f"//li[normalize-space()='{name}']"
        self.element_click_js(self._select_semester, "xpath")
        self.element_click_js(name_select, "xpath")

    def click_on_show_details(self):
        self.element_click_js(self._show_details, "xpath")

    def click_on_view(self):
        self.element_click(self._view, "xpath")

    def click_on_start_evaluation(self):
        self.element_click_js(self._start_evaluation, "xpath")

    def click_on_evaluate(self):
        self.element_click_js(self._evaluate_exam, "xpath")

    def enter_points1(self, points):
        self.element_click_js(self._points_given1, locator_type="xpath")
        self.send_keys(points, self._points_given1, "xpath")

    def enter_feedback(self, feedback):
        self.element_click_js(self._feedback_textbox, locator_type="xpath")
        self.send_keys(feedback, self._feedback_textbox, "xpath")

    def click_on_submit(self):
        self.element_click_js(self._submit, "xpath")

    def navigate_to_manage_tab(self):
        self.click_on_manage()
        self.click_on_evaluation()

    def ext_evaluation_fac(self, feedback, points):
        self.click_on_mid_or_end_exam_evaluation()
        self.select_program()
        self.select_year("First Year")
        self.select_semester("Semester 1")
        self.click_on_show_details()
        self.click_on_view()
        self.click_on_start_evaluation()
        self.click_on_evaluate()
        self.enter_feedback(feedback)
        self.enter_points1(points)
        self.click_on_submit()

    def ext_evaluation_hod(self, feedback, points):
        self.click_on_mid_or_end_exam_evaluation()
        self.select_program()
        self.select_year("Second Year")
        self.select_semester("Semester 4")
        self.click_on_show_details()
        self.click_on_view()
        self.click_on_start_evaluation()
        self.click_on_evaluate()
        self.enter_feedback(feedback)
        self.enter_points1(points)
        self.click_on_submit()

    def verify_external_evaluation(self):
        self.verify_by_comparing_text(locator=self._actual_result, locator_type="xpath",
                                      expected_result=self.expected_result,
                                      result_msg="Operation successful")
