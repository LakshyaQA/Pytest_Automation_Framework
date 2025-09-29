# import time
from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
from Techademy_Campus.Configuration.readProperties import ReadConfig





class AssignBadge(Basepage):
    log = cl.custom_logger()

    """
        This Assign Badge class is for assigning a badge to a particular student in registrar role.
         
         author : Meghana Avinash Kadam
      
      
    """


    expected_result = ReadConfig.get_expected_result('Expected Results', 'assign_badge')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _manage_tab = "//button[text()='Manage']"
    _badge_creation_tab = "//span[text()='Badge-Creation']"
    _assign_badge_button = "//button[text()='Assign Badge']"
    _select_department = "//input[@name='dept_id']"
    _select_department_name = "//li[text()='Marine Engineering']"
    _select_program = "//input[@name='program_id']"
    _select_program_name = "//li[contains(text() ,'BTech in Marine Engineering')]"
    _select_student = "//input[@name='stud_badge_data.stud_id']"
    _select_student_name = "//li[text()='student@campusqa.in']"
    _select_badge = "//input[@name='badge_id']"
    _select_badge_name = "//li[text()='Academic Excellence']"
    _assign_button = "//button[text()='Assign']"
    _cancel_button = "//button[text()='Cancel']"
    _actual_element = "//div[text()='Badge assigned succesfully']"

    def click_on_manage(self):
        self.wait_for_element(self._manage_tab, locator_type="xpath")
        self.element_click(self._manage_tab, "xpath")

    def click_on_badge_creation(self):
        self.wait_for_element(self._badge_creation_tab, locator_type="xpath")
        self.element_click(self._badge_creation_tab, "xpath")

    def click_on_assign_badge_button(self):
        self.wait_for_element(self._assign_badge_button, locator_type="xpath")
        self.element_click_js(self._assign_badge_button, "xpath")

    def click_on_select_department(self):
        # self.waitForElement(self._select_department, locator_type="xpath")
        self.element_click_js(self._select_department, "xpath")
        self.wait_for_element(self. _select_department_name, locator_type="xpath")
        self.element_click_js(self. _select_department_name, "xpath")

    def click_on_select_program(self):
        # self.waitForElement(self.  _select_program, locator_type="xpath")
        self.element_click_js(self.  _select_program, "xpath")
        self.wait_for_element(self._select_program_name, locator_type="xpath")
        self.element_click_js(self._select_program_name, "xpath")

    def click_on_select_student(self):
        # self.waitForElement(self. _select_student, locator_type="xpath")
        self.element_click_js(self. _select_student, "xpath")
        self.wait_for_element(self._select_student_name, locator_type="xpath")
        self.element_click_js(self._select_student_name, "xpath")

    def click_on_select_badge(self):
        # self.waitForElement(self. _select_badge, locator_type="xpath")
        self.element_click_js(self. _select_badge, "xpath")
        self.wait_for_element(self._select_badge_name, locator_type="xpath")
        self.element_click_js(self._select_badge_name, "xpath")

    def click_on_assign_button(self):
        self.wait_for_element(self._assign_button, locator_type="xpath")
        self.element_click_js(self._assign_button, "xpath")

    def click_on_cancel_button(self):
        self.wait_for_element(self._cancel_button, locator_type="xpath")
        self.element_click(self._cancel_button, "xpath")



    def navigate_to_manage_tab(self):
        self.click_on_manage()
        self.click_on_badge_creation()
        self.click_on_assign_badge_button()
        self.click_on_select_department()
        self.click_on_select_program()
        self.click_on_select_student()
        self.click_on_select_badge()
        # time.sleep(3)
        self.click_on_assign_button()
        # self.click_on_cancel_button()

    def verify_assigning_badge(self):
        self.verify_by_comparing_text(locator=self. _actual_element, locator_type="xpath", expected_result=self.
                                      expected_result, result_msg="Assigning a badge failed")


