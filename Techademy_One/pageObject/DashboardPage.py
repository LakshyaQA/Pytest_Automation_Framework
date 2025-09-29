"""
    This page includes locators and functions of dashboard page

    """

import time

import allure

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class Dashboard(Basepage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # _select_tenant = "//*[@id=':r0:']"
    _select_tenant_dropdown_option = "//li[contains(@id,'option-1')]"
    _select_tenant_dropdown = "//*[@name='tenant_id']"
    _trending_Labs = "//button[normalize-space()='Labs']"
    _trending_lxp = "//button[normalize-space()='Lxp']"
    _trending_Assessments = "//button[normalize-space()='Assessments']"
    _user_trending_All_apps = "(//div[@class='MuiStack-root css-j7qwjs'])[1]"
    _user_trending_labs = "(//div[@class='MuiStack-root css-j7qwjs'])[3]"
    _user_trending_lxp = "(//div[@class='MuiStack-root css-j7qwjs'])[2]"
    _user_trending_assessments = "(//div[@class='MuiStack-root css-j7qwjs'])[4]"
    _continue_learning_All_apps = "(//button[normalize-space()='All Apps'])[2]"
    _continue_learning_labs = ("(//div[@class='MuiButton-icon MuiButton-startIcon "
                               "MuiButton-iconSizeMedium css-1l6c7y9'])[2]")
    _continue_learning_lxp = ("(//div[@class='MuiButton-icon MuiButton-startIcon "
                              "MuiButton-iconSizeMedium css-1l6c7y9'])[3]")
    _continue_learning_assessments = ("(//div[@class='MuiButton-icon "
                                      "MuiButton-startIcon MuiButton-iconSizeMedium css-1l6c7y9'])[4]")
    _inprogress_tab = "//button[normalize-space()='In Progress']"
    _enrolled_tab = "//button[normalize-space()='Enrolled']"
    _completed_tab = "//button[normalize-space()='Completed']"
    _menu_button = "//img[@src='/main/All Apps.svg']"  # 9 dots button
    _manage_tab_button = "//img[@src='/main/manage.svg']"
    _tenant_tab_button = "//img[@src='/main/tenantIcon.svg']"
    _users_tab_db = ("//*[@class='MuiTypography-root MuiTypography-body2 MuiListItemText-secondary css-5iszde' "
                     "and contains(text(),'Users')]")  # users tab on dashboard
    _License_db = ("//*[@class='MuiTypography-root MuiTypography-body2 MuiListItemText-secondary css-5iszde' "
                   "and contains(text(),'Licensing')]")  # users tab on dashboard
    _notification_tab = ("//*[@class='MuiTypography-root MuiTypography-body2 MuiListItemText-secondary css-5iszde' "
                         "and contains(text(),'Notification')]")
    _request_tab_db = ("//*[@class='MuiTypography-root MuiTypography-body2 MuiListItemText-secondary css-5iszde' and "
                       "contains(text(),'Requests')]")
    _Labs_button = "//*[@class='MuiTypography-root MuiTypography-subtitle2 css-17bzhog' and contains(text(),'Labs')]"
    _LXP_button = "//*[@class='MuiTypography-root MuiTypography-subtitle2 css-17bzhog' and contains(text(),'LXP')]"
    _Assessments_button = ("//*[@class='MuiTypography-root MuiTypography-subtitle2 css-17bzhog' and contains(text(),"
                           "'Assesments')]")
    _Recewt_button = ("//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-17bzhog' and normalize-space(text("
                      "))='Hiring']")
    _tenant_header = "//*[@class='MuiTypography-root MuiTypography-h3 css-upmft4']"  # For validation of tenant tab
    _chat_bot_close = "//em[@class='siqico-close']"
    _reports_tab_button = "//img[@src='/main/ico- reports.svg']"
    _reports_tab_tenant = "(//a[@class='MuiListItem-root MuiListItem-gutters css-1pklig1'])[2]"
    _audit_Logs_tab = "//img[@src='/main/audit.svg']"
    _reporting_tab = "(//p[@class='MuiTypography-root MuiTypography-body2 MuiListItemText-secondary css-5iszde'])[6]"
    _invoice_tab = "//img[@src='/main/ico-invoices.svg']"

    # def selectTenant(self,tenant):
    #   try:
    #    ele= self.getElement(self._select_tenant,"xpath")

    #   if ele is not None :
    #      self.waitForElement(self._select_tenant,"xpath",timeout=10,pollFrequency=0.5)
    #     ele.click()
    #    time.sleep(10)
    #   ele.sendkeys(Keys.DOWN)
    #  ele.sendkeys(Keys.ENTER)
    # else:
    #  self.log.info("Element not present with locator: " + self._select_tenant)
    # except:
    #   print("Element not found")

    def SelectTenant(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._select_tenant_dropdown, locator_type="xpath")
        self.element_click(self._select_tenant_dropdown_option, locator_type="xpath")

    def ClickonLabs(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.scroll_by_visible_element(self._trending_Labs, "xpath")
        self.element_click(self._trending_Labs, locator_type="xpath")

    def ClickonLxp(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._trending_lxp, locator_type="xpath")

    def ClickonAssessments(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._trending_Assessments, locator_type="xpath")

    def ClicktrendingAllApps(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.scroll_by_visible_element(self._user_trending_All_apps, "xpath")
        self.element_click(self._user_trending_All_apps, locator_type="xpath")

    def Clicktrendinglxp(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._user_trending_lxp, locator_type="xpath")

    def Clicktrendinglab(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._user_trending_labs, locator_type="xpath")

    def Clicktrendingassessment(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._user_trending_assessments, locator_type="xpath")

    def clickcontinuelearningallapps(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._continue_learning_All_apps, locator_type="xpath")

    def clickcontinuelearninglxp(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._continue_learning_lxp, locator_type="xpath")

    def clickcontinuelearninglab(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._continue_learning_labs, locator_type="xpath")

    def clickcontinuelearningassessment(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._continue_learning_assessments, locator_type="xpath")

    def inprogresslearning(self):
        self.element_click(self._inprogress_tab, locator_type="xpath")

    def enrolledlearning(self):
        self.element_click(self._enrolled_tab, locator_type="xpath")

    def completedlearning(self):
        self.element_click(self._completed_tab, locator_type="xpath")

    def selectprogress(self):
        self.inprogresslearning()
        time.sleep(5)
        self.enrolledlearning()
        time.sleep(5)
        self.completedlearning()

    def CheckDBdetail(self):
        self.SelectTenant()
        self.ClickonLabs()
        time.sleep(5)
        self.ClickonLxp()
        time.sleep(5)
        self.ClickonAssessments()

    def ChecktenantDBtrendingnow(self):
        self.ClickonLabs()
        time.sleep(5)
        self.ClickonLxp()
        time.sleep(5)
        self.ClickonAssessments()

    def Checkcontinuelearning(self):
        self.clickcontinuelearningallapps()
        self.selectprogress()
        self.clickcontinuelearningallapps()
        self.selectprogress()
        self.clickcontinuelearninglxp()
        self.selectprogress()
        self.clickcontinuelearninglxp()
        self.selectprogress()
        self.clickcontinuelearningallapps()
        self.selectprogress()

    def CheckenduserDBtrendingnow(self):
        self.ClicktrendingAllApps()
        time.sleep(5)
        self.Clicktrendinglxp()
        time.sleep(5)
        self.Clicktrendinglab()
        time.sleep(5)
        self.Clicktrendingassessment()

    def ClickonMenu(self):
        self.wait_till_element_invisibility("//div[@class='loading']","xpath",50)
        self.wait_for_element(self._menu_button, locator_type="xpath")
        self.element_click(self._menu_button, locator_type="xpath")

    def ClickonManage(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath",50)
        self.wait_for_element(self._manage_tab_button, locator_type="xpath")
        self.element_click(self._manage_tab_button, locator_type="xpath")

    def ClickonTenant(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.wait_for_element(self._tenant_tab_button, locator_type="xpath")
        self.element_click(self._tenant_tab_button, locator_type="xpath")

    def ClickOnUsersTab(self):
        self.element_click(self._users_tab_db, locator_type="xpath")

    def ClickOnRequestTab(self):
        self.element_click(self._request_tab_db, locator_type="xpath")

    def ClickOnNotificationTab(self):
        self.element_click_js(self._notification_tab, "xpath")

    def ClickOnLicensing(self):
        self.element_click_js(self._License_db, "xpath")

    def CloseChatBot(self):
        self.wait_for_element(self._chat_bot_close, "xpath")
        self.element_click_js(self._chat_bot_close, "xpath")

    def NavigateToTenantTab(self):
        self.CloseChatBot()
        self.ClickonManage()
        self.ClickonTenant()

    def NavigateToTenantTabAdmin(self):
        self.CloseChatBot()
        self.ClickonManage()
        self.ClickonTenant()

    def NavigateToUsersTab(self):
        self.ClickonManage()
        self.ClickOnUsersTab()

    def NavigateToRequestTab(self):
        self.ClickonManage()
        self.ClickOnRequestTab()

    def NavigateToLicensing(self):
        self.ClickonManage()
        self.ClickOnLicensing()

    def NavigateToNotificationTab(self):
        time.sleep(5)
        self.ClickonManage()
        time.sleep(5)
        self.ClickOnNotificationTab()

    def clickOnLabs(self):
        self.element_click_js(self._Labs_button, "xpath")

    def clickOnLXP(self):
        self.element_click_js(self._LXP_button, "xpath")

    def clickOnAssessments(self):
        self.element_click_js(self._Assessments_button, "xpath")

    def clickOnRecrewt(self):
        self.element_click_js(self._Recewt_button, "xpath")

    def navigateToLabs(self):
        self.ClickonMenu()
        self.clickOnLabs()

    def navigateToLXP(self):
        self.ClickonMenu()
        self.clickOnLXP()

    def navigateToAssessments(self):
        self.ClickonMenu()
        self.clickOnAssessments()

    def navigateToRecrewt(self):
        self.ClickonMenu()
        self.clickOnRecrewt()

    def VerifyTenantManage(self):
        self.verify_by_element_presence(locator=self._tenant_header, locator_type="xpath", result_msg="TenantListTest")

    def Verify_MML(self):
        self.verify_by_comparing_title_of_webpage(expected_title="MakeMyLabs", result_msg="RouteToMML")

    def Verify_Yaksha(self):
        self.verify_by_comparing_title_of_webpage(expected_title="Assessment Platform", result_msg="RouteToYaksha")

    def Verify_LXP(self):
        self.verify_by_comparing_title_of_webpage(expected_title="Techademy", result_msg="RouteToB2B")

    def Verify_Recrewt(self):
        self.verify_by_comparing_title_of_webpage(expected_title="ReCREWt", result_msg="RouteToHiring")

    def ClickonReports(self):
        self.wait_for_element(self._reports_tab_button, locator_type="xpath")
        self.element_click(self._reports_tab_button, locator_type="xpath")

    def ClickontenantReport(self):
        self.wait_for_element(self._reports_tab_tenant, locator_type="xpath")
        self.element_click(self._reports_tab_tenant, locator_type="xpath")

    def ClickonAuditLogs(self):
        self.wait_for_element(self._audit_Logs_tab, locator_type="xpath")
        self.element_click(self._audit_Logs_tab, locator_type="xpath")

    def clickonInvoice(self):
        time.sleep(5)
        self.wait_for_element(self._invoice_tab, locator_type="xpath")
        self.element_click(self._invoice_tab, locator_type="xpath")

    def ClickonReporting(self):
        self.wait_for_element(self._reporting_tab, locator_type="xpath")
        self.element_click(self._reporting_tab, locator_type="xpath")
