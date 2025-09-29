import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class CreateExam(Basepage):
    log = cl.custom_logger()

    '''
            This class includes the creation of exam schedule by the Registrar role

            author: Abhilash

            '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating the exam schedule

    manage_tab = "//button[@id='basic-button']"
    exam_option = "(//span[@class='MuiTypography-root MuiTypography-link basic-menu-item-icon css-2rvg0p'])[5]"
    cluster_dropdown = "//div[@name='cluster_name']"
    cluster_option = "//li[contains(text(), 'Engineering')]"
    department_dropdown = "//div[@name='department_name']"
    department_option = "//li[contains(text(), 'Marine Engineering')]"
    program_dropdown = "//div[@name='program_name']"
    program_option = "//li[contains(text(), 'BTech in Marine Engineering')]"
    ShowDetails_button = "//button[text()='Show Details']"
    AddExam_button = "(//button[text()='Add Exam'])[1]"
    semester_dropdown = "//input[@name='semester_id']"
    semester_option = "//li[text()='Semester1']"
    ExamTitle_field = "//input[@name='exam_title']"
    ExamStartDate_field = "(//input[@type='tel'])[1]"
    ExamEndDate_field = "(//input[@type='tel'])[2]"
    ResultPublishOn_field = "(//input[@type='tel'])[3]"
    CreateExam_button = "//button[text()='create exam']"
    success_message = "//div[contains(text(), 'Exam creation successful')]"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnExamOption(self):
        self.wait_for_element(self.exam_option, locator_type="xpath")
        self.element_click_js(self.exam_option, "xpath")

    def clickOnCluster(self):
        self.element_click_js(self.cluster_dropdown, locator_type="xpath")
        self.wait_for_element(self.cluster_dropdown, locator_type="xpath")

    def clickOnDepartment(self):
        self.element_click_js(self.department_dropdown, locator_type="xpath")
        self.wait_for_element(self.department_dropdown, locator_type="xpath")

    def clickOnProgram(self):
        self.element_click_js(self.program_dropdown, locator_type="xpath")
        self.wait_for_element(self.program_dropdown, locator_type="xpath")

    def selectClusterOption(self):
        self.element_click(self.cluster_dropdown, locator_type="xpath")
        self.element_click(self.cluster_option, locator_type="xpath")

    def selectDepartmentOption(self):
        self.element_click(self.department_dropdown, "xpath")
        self.element_click(self.department_option, "xpath")

    def selectProgramOption(self):
        self.element_click(self.program_dropdown, "xpath")
        self.element_click(self.program_option, "xpath")

    def clickOnShowDetails(self):
        self.element_click_js(self.ShowDetails_button, locator_type="xpath")

    def clickOnAddExam(self):
        self.element_click_js(self.AddExam_button, locator_type="xpath")

    def selectSemesterOption(self):
        self.wait_till_element_invisibility(self.semester_dropdown, locator_type="xpath")
        self.element_click_js(self.semester_dropdown, "xpath")
        self.wait_for_element(self.semester_option, "xpath")
        self.element_click_js(self.semester_option, "xpath")

    def clickOnExamTitle(self):
        self.element_click_js(self.ExamTitle_field, locator_type="xpath")

    def clickOnExamStartDate(self):
        self.element_click_js(self.ExamStartDate_field, locator_type="xpath")

    def clickOnExamEndDate(self):
        self.element_click(self.ExamEndDate_field, locator_type="xpath")

    def clickOnResultPublishOn(self):
        self.element_click_js(self.ResultPublishOn_field, locator_type="xpath")

    def enterExamTitle(self, title):
        self.send_keys(title, self.ExamTitle_field, locator_type="xpath")

    def enterExamStartDate(self, s_date):
        self.send_keys(s_date, self.ExamStartDate_field, locator_type="xpath")

    def enterExamEndDate(self, e_date):
        self.send_keys(e_date, self.ExamEndDate_field, locator_type="xpath")

    def enterResultPublishOn(self, result):
        self.send_keys(result, self.ResultPublishOn_field, locator_type="xpath")

    def clickOnCreateExam(self):
        self.element_click_js(self.CreateExam_button, locator_type="xpath")

    def clickOn_Exam(self):
        self.clickOnManageTab()
        self.clickOnExamOption()

    def select_exam_details(self):
        self.clickOnCluster()
        self.selectClusterOption()
        self.clickOnDepartment()
        self.selectDepartmentOption()
        self.clickOnProgram()
        self.selectProgramOption()
        self.clickOnShowDetails()
        self.clickOnAddExam()

    def create_exam(self, title, s_date, e_date, result):
        self.selectSemesterOption()
        self.enterExamTitle(title)
        self.enterExamStartDate(s_date)
        self.enterExamEndDate(e_date)
        self.enterResultPublishOn(result)
        self.clickOnCreateExam()
