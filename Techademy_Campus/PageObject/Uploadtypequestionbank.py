from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
from Common_Packages.resources.ConfigPath import UploadFile
from Techademy_Campus.Configuration.readProperties import ReadConfig

'''

This page includes locators and functions of upload type question bank creation under assessment repository for HOD and
faculty role 

    author : Vidyashri

'''


class Assessment(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'question_bank_creation')
    expected_result_delete = ReadConfig.get_expected_result('Expected Results', 'delete_question_bank')
    path = UploadFile.file_upload_path('question_bank_bulk_upload.xlsx')

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # _dashboard_tab = "//span[text()='Dashboard']"
    _manage_tab = "//button[text()='Manage']"
    _programs_tab = "//span[text()='Programs']"
    _assessment_repository = "//span[text()='Assessment Repository']"
    _question_bank_name = "//input[@name='question_bank_name']"
    _enter_version = "//input[@name='version']"
    _course_name = "//input[@id='free-solo-2-demo']"
    _option_maths = "//li[text()='Mathematics – I  (ME1-01)']"
    _option_marine_boilers = "//li[text()='Marine Boilers  (ME4-15)']"
    _course_code = "//input[@name='course_code']"
    _drag_drop_image = "//div[@class='MuiStack-root w-100 mt2 css-1mzerio']//p[1]"
    _click_upload = "//button[text()='Upload']"
    _question_bank_list = "//button[text()='Question Bank List']"
    _actual_result = "//div[text()='Question bank created successfully.']"

    # delete created question bank
    _3dots = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium qa-student-elipses "
              "css-1rtdwbw'])[2]")
    _delete = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-17vjt6s']"
    _submit = "//button[text()='Submit']"
    _actual_result_delete = "//div[text()='Question bank deleted successfully.']"

    def click_on_manage(self):
        self.element_click(self._manage_tab, "xpath")

    def click_on_programs(self):
        self.element_click(self._programs_tab, "xpath")

    def click_on_assessment_repository(self):
        self.element_click_js(self._assessment_repository, "xpath")

    def enter_question_bank_name(self, question_bank_name):
        self.send_keys(question_bank_name, self._question_bank_name, "xpath")

    def enter_version(self, version):
        self.send_keys(version, self._enter_version, "xpath")

    def select_course_name(self):
        self.send_keys("Mathematics – I  (ME1-01)", self._course_name, "xpath")
        self.element_click_js(self._option_maths, "xpath")

    def select_course_name_boilers(self):
        self.send_keys("Marine Boilers  (ME4-15)", self._course_name, "xpath")
        self.element_click_js(self._option_marine_boilers, "xpath")

    def enter_course_code(self, course_code):
        self.send_keys(course_code, self._course_code, "xpath")

    def click_on_drag_drop(self, path):
        self.element_click(self._drag_drop_image, "xpath")
        self.upload_file(path, self._drag_drop_image, "xpath")

    def click_on_upload_button(self):
        self.element_click_js(self._click_upload, "xpath")

    def click_on_question_bank_list(self):
        self.element_click_js(self._question_bank_list, "xpath")

        # delete created question bank

    def click_on_3dots(self):
        self.element_click_js(self._3dots, "xpath")

    def click_on_delete(self):
        self.element_click_js(self._delete, "xpath")

    def click_on_submit(self):
        self.element_click_js(self._submit, "xpath")

    def navigate_to_manage_tab(self):
        self.click_on_manage()

    def create_question_bank_fac(self, question_bank_name, version, course_code):
        self.click_on_assessment_repository()
        self.enter_question_bank_name(question_bank_name)
        self.enter_version(version)
        self.select_course_name()
        self.enter_course_code(course_code)
        self.click_on_drag_drop(self.path)
        self.click_on_upload_button()

    def create_question_bank_hod(self, question_bank_name, version, course_code):
        self.click_on_assessment_repository()
        self.enter_question_bank_name(question_bank_name)
        self.enter_version(version)
        self.select_course_name_boilers()
        self.enter_course_code(course_code)
        self.click_on_drag_drop(self.path)
        self.click_on_upload_button()

    def delete_question_bank(self):
        self.click_on_question_bank_list()
        self.click_on_3dots()
        self.click_on_delete()
        self.click_on_submit()

    def verify_question_bank_creation(self):
        self.verify_by_comparing_text(locator=self._actual_result, locator_type="xpath",
                                      expected_result=self.expected_result,
                                      result_msg="Question bank created successfully.")

    def verify_delete_question_bank(self):
        self.verify_by_comparing_text(locator=self._actual_result_delete, locator_type="xpath",
                                      expected_result=self.expected_result_delete,
                                      result_msg="Question bank deleted successfully.")
