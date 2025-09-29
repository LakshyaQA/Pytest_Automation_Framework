import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class AffiliateCourses(Basepage):
    log = cl.custom_logger()

    '''
            This class includes the affiliating of the MOOCCourse by the MOOC Admin

            author: Abhilash

            '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for affiliating courses

    Mooc_tab = "//button[text() = 'MOOC']"
    AffiliateCourses_option = "//span[text() = 'Affiliate Courses']"
    CourseTobeAffiliated = ("(//span[@class='qa-visibility-icon mouse-pointer w-100 display-flex justify-flex-end "
                            "items-center'])[9]")
    AffiliateCourse_button = "(//button[text()='Affiliate Course'])[1]"
    CostOfCourse_textfield = "//input[@name='courseCost']"
    CreditPointsOfCourse_textfield = "//input[@name='creditPoints']"
    AffiliateTheCourse_button = "(//button[text()='Affiliate Course'])[3]"
    AffiliateCourse_SuccessMessage = "//div[text()='Affiliation Successfully Completed!']"

    def clickOnMOOCTab(self):
        self.wait_for_element(self.Mooc_tab, locator_type="xpath")
        self.element_click_js(self.Mooc_tab, "xpath")

    def clickOnAffiliateCoursesOption(self):
        self.wait_for_element(self.AffiliateCourses_option, locator_type="xpath")
        self.element_click_js(self.AffiliateCourses_option, "xpath")

    def clickOnCourse_tobeAffiliated(self):
        self.wait_for_element(self.CourseTobeAffiliated, locator_type="xpath")
        self.element_click_js(self.CourseTobeAffiliated, "xpath")

    def clickOnAffiliateCourseButton(self):
        self.wait_for_element(self.AffiliateCourse_button, locator_type="xpath")
        self.element_click_js(self.AffiliateCourse_button, "xpath")

    def clickOnCostOfCourseTextfield(self):
        self.wait_for_element(self.CostOfCourse_textfield, locator_type="xpath")
        self.element_click_js(self.CostOfCourse_textfield, "xpath")

    def clickOnCreditsOfCourseTextfield(self):
        self.wait_for_element(self.CreditPointsOfCourse_textfield, locator_type="xpath")
        self.element_click_js(self.CreditPointsOfCourse_textfield, "xpath")

    def enterCostOfCourse(self, cost):
        self.send_keys(cost, self.CostOfCourse_textfield, "xpath")

    def enterCreditsOfCourse(self, credit_points):
        self.send_keys(credit_points, self.CreditPointsOfCourse_textfield, "xpath")

    def clickOnAffiliateTheCourseButton(self):
        self.element_click_js(self.AffiliateTheCourse_button, "xpath")

    def gotoMoocCoursesScreen(self):
        self.clickOnMOOCTab()
        self.clickOnAffiliateCoursesOption()

    def AffiliateTheCourse(self, cost, credit_points):
        self.clickOnCourse_tobeAffiliated()
        self.clickOnAffiliateCourseButton()
        self.clickOnCostOfCourseTextfield()
        self.enterCostOfCourse(cost)
        self.clickOnCreditsOfCourseTextfield()
        self.enterCreditsOfCourse(credit_points)
        self.clickOnAffiliateTheCourseButton()

    def verifying_AffiliateCourse(self):
        self.verify_by_element_presence(self.AffiliateCourse_SuccessMessage, "xpath", "Affiliation "
                                                                                      "Successfully Completed!")
