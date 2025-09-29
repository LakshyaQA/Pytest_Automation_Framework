import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class PublishCourses(Basepage):
    logg = cl.custom_logger()

    '''
            This class includes the publishing of the MOOC Courses by the MOOC Admin
            
            author: Abhilash

            '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for publishing courses

    Mooc_tab = "//button[text() = 'MOOC']"
    PublishCourse_option = "//span[text()='Publish Courses']"
    PublishForStudents_line = "(//span[text()='Publish For Students'])[1]"
    PublishCourse_button = "//button[text()='Publish Course']"
    PublishCourse_SuccessMessage = "//div[text()='Course Published Successfully!']"

    def clickOnMOOCTab(self):
        self.wait_for_element(self.Mooc_tab, locator_type="xpath")
        self.element_click_js(self.Mooc_tab, "xpath")

    def clickOnPublishCoursesOption(self):
        self.wait_for_element(self.PublishCourse_option, locator_type="xpath")
        self.element_click_js(self.PublishCourse_option, "xpath")

    def clickOnPublishForStudents(self):
        self.wait_for_element(self.PublishForStudents_line, locator_type="xpath")
        self.element_click_js(self.PublishForStudents_line, "xpath")

    def clickOnPublishCourseButton(self):
        self.element_click_js(self.PublishCourse_button, "xpath")

    def gotoMoocCoursesScreen(self):
        self.clickOnMOOCTab()
        self.clickOnPublishCoursesOption()

    def PublishTheCourse(self):
        self.clickOnPublishForStudents()
        self.clickOnPublishCourseButton()

    def verifying_PublishCourses(self):
        self.verify_by_element_presence(self.PublishCourse_SuccessMessage, "xpath", "Course "
                                                                                    "Published Successfully!")


