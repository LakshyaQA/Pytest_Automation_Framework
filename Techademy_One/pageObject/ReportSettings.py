"""
    This page includes locators and functions of Reports Settings page

    """

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig


class ReportSettingsTests(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'Report_Settings_Success')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _LXP_Course_CheckBox1 = "(//input[@type='checkbox'])[1]"
    _LXP_Course_CheckBox2 = "(//input[@type='checkbox'])[2]"
    _LXP_Course_CheckBox3 = "(//input[@type='checkbox'])[3]"
    _LXP_Course_CheckBox4 = "(//input[@type='checkbox'])[4]"
    _Usage_Report1 = "(//input[@type='checkbox'])[5]"
    _Usage_Report2 = "(//input[@type='checkbox'])[6]"
    _Usage_Report3 = "(//input[@type='checkbox'])[7]"
    _Usage_Report4 = "(//input[@type='checkbox'])[8]"
    _Adaptive1 = "(//input[@type='checkbox'])[9]"
    _Adaptive2 = "(//input[@type='checkbox'])[10]"
    _Adaptive3 = "(//input[@type='checkbox'])[11]"
    _Adaptive4 = "(//input[@type='checkbox'])[12]"
    _MCQ1 = "(//input[@type='checkbox'])[13]"
    _MCQ2 = "(//input[@type='checkbox'])[14]"
    _MCQ3 = "(//input[@type='checkbox'])[15]"
    _MCQ4 = "(//input[@type='checkbox'])[16]"
    _Coding1 = "(//input[@type='checkbox'])[17]"
    _Coding2 = "(//input[@type='checkbox'])[18]"
    _Coding3 = "(//input[@type='checkbox'])[19]"
    _Coding4 = "(//input[@type='checkbox'])[20]"
    _Cloud1 = "(//input[@type='checkbox'])[21]"
    _Cloud2 = "(//input[@type='checkbox'])[22]"
    _Cloud3 = "(//input[@type='checkbox'])[23]"
    _Cloud4 = "(//input[@type='checkbox'])[24]"
    _Candidates1 = "(//input[@type='checkbox'])[25]"
    _Candidates2 = "(//input[@type='checkbox'])[26]"
    _Candidates3 = "(//input[@type='checkbox'])[27]"
    _Candidates4 = "(//input[@type='checkbox'])[28]"
    _Job_Postings1 = "(//input[@type='checkbox'])[29]"
    _Job_Postings2 = "(//input[@type='checkbox'])[30]"
    _Job_Postings3 = "(//input[@type='checkbox'])[31]"
    _Job_Postings4 = "(//input[@type='checkbox'])[32]"
    _Employees1 = "(//input[@type='checkbox'])[33]"
    _Employees2 = "(//input[@type='checkbox'])[34]"
    _Employees3 = "(//input[@type='checkbox'])[35]"
    _Employees4 = "(//input[@type='checkbox'])[36]"
    _Save_Settings = "//button[normalize-space()='Save Settings']"
    _Report_Settings_Success = "//div[@id='notistack-snackbar']"

    def selectCheckbox1(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._LXP_Course_CheckBox1, locator_type="xpath")

    def selectCheckbox2(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._LXP_Course_CheckBox2, locator_type="xpath")

    def selectCheckbox3(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._LXP_Course_CheckBox3, locator_type="xpath")

    def selectCheckbox4(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._LXP_Course_CheckBox4, locator_type="xpath")

    def selectCheckbox5(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Usage_Report1, locator_type="xpath")

    def selectCheckbox6(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Usage_Report2, locator_type="xpath")

    def selectCheckbox7(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Usage_Report3, locator_type="xpath")

    def selectCheckbox8(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Usage_Report4, locator_type="xpath")

    def selectCheckbox9(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Adaptive1, locator_type="xpath")

    def selectCheckbox10(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Adaptive2, locator_type="xpath")

    def selectCheckbox11(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Adaptive3, locator_type="xpath")

    def selectCheckbox12(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Adaptive4, locator_type="xpath")

    def selectCheckbox13(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._MCQ1, locator_type="xpath")

    def selectCheckbox14(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._MCQ2, locator_type="xpath")

    def selectCheckbox15(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._MCQ3, locator_type="xpath")

    def selectCheckbox16(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._MCQ4, locator_type="xpath")

    def selectCheckbox17(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Coding1, locator_type="xpath")

    def selectCheckbox18(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Coding2, locator_type="xpath")

    def selectCheckbox19(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Coding3, locator_type="xpath")

    def selectCheckbox20(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Coding4, locator_type="xpath")

    def selectCheckbox21(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Cloud1, locator_type="xpath")

    def selectCheckbox22(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Cloud2, locator_type="xpath")

    def selectCheckbox23(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Cloud3, locator_type="xpath")

    def selectCheckbox24(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Cloud4, locator_type="xpath")

    def selectCheckbox25(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Candidates1, locator_type="xpath")

    def selectCheckbox26(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Candidates2, locator_type="xpath")

    def selectCheckbox27(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Candidates3, locator_type="xpath")

    def selectCheckbox28(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Candidates4, locator_type="xpath")

    def selectCheckbox29(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Job_Postings1, locator_type="xpath")

    def selectCheckbox30(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Job_Postings2, locator_type="xpath")

    def selectCheckbox31(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Job_Postings3, locator_type="xpath")

    def selectCheckbox32(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Job_Postings4, locator_type="xpath")

    def selectCheckbox33(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Employees1, locator_type="xpath")

    def selectCheckbox34(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Employees2, locator_type="xpath")

    def selectCheckbox35(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Employees3, locator_type="xpath")

    def selectCheckbox36(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Employees4, locator_type="xpath")

    def ClickOnSaveSettings(self):
        self.element_click(self._Save_Settings, locator_type="xpath")

    def ReportSettings(self):
        self.selectCheckbox1()
        self.selectCheckbox2()
        self.selectCheckbox3()
        self.selectCheckbox4()
        self.selectCheckbox5()
        self.selectCheckbox6()
        self.selectCheckbox7()
        self.selectCheckbox8()
        self.selectCheckbox9()
        self.selectCheckbox10()
        self.selectCheckbox11()
        self.selectCheckbox12()
        self.selectCheckbox13()
        self.selectCheckbox14()
        self.selectCheckbox15()
        self.selectCheckbox16()
        self.selectCheckbox17()
        self.selectCheckbox18()
        self.selectCheckbox19()
        self.selectCheckbox20()
        self.selectCheckbox21()
        self.selectCheckbox22()
        self.selectCheckbox23()
        self.selectCheckbox24()
        self.selectCheckbox25()
        self.selectCheckbox26()
        self.selectCheckbox27()
        self.selectCheckbox28()
        self.selectCheckbox29()
        self.selectCheckbox30()
        self.selectCheckbox31()
        self.selectCheckbox32()
        self.selectCheckbox33()
        self.selectCheckbox34()
        self.selectCheckbox35()
        self.selectCheckbox36()
        self.ClickOnSaveSettings()

    def VerifyReportSettings(self):
        self.verify_by_comparing_text(locator=self._Report_Settings_Success, locator_type="xpath", expected_result=self.expected_result,
                                      result_msg="ReportSettingsTest")

















