import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class HomePage(Basepage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _manage_tab = "//img[@src='/assets/manage-279a41b4.svg']"
    _dashboard_tab = "//img[@src='/assets/dashboardLogo-c3fb869b.svg']"
    _Jobs_tab = "//img[@src='/assets/jobsLogo-c8f7062c.svg']"
    _emp_tab = "//img[@src='/assets/employeesLogo-96730d0e.svg']"
    _candidate_tab = "//img[@src='/assets/candidatesLogo-dfaa39a1.svg']"
    _reports_tab = "//img[@src='/assets/reportsLogo-355f706d.svg']"
    _numberOfApplication = "(//*[@class='MuiTypography-root MuiTypography-h2 css-8crv3w'])[1]"
    _candidateShortlisted = "(//*[@class='MuiTypography-root MuiTypography-h2 css-8crv3w'])[2]"
    _post_a_job = "//button[contains(text(), 'Post a Job')]"
    _profile = "//div[@class='MuiStack-root css-jj2ztu']"
    _logout = "//li[contains(text(), 'Logout')]"
    _login = "//h3[contains(text(), 'Login')]"
    _loader = "//div[@class='MuiBackdrop-root loader css-xuaqpw']"


    def click_on_manage(self):
        self.element_click(self._manage_tab, "xpath")

    def click_on_dashboard(self):
        self.element_click(self._dashboard_tab, "xpath")

    def click_on_jobs(self):
        self.wait_till_element_invisibility(self._loader, "xpath")
        self.wait_for_element(self._Jobs_tab, "xpath")
        self.element_click_js(self._Jobs_tab, "xpath")
        self.wait_for_page_load()

    def click_on_emp(self):
        self.element_click(self._emp_tab, "xpath")

    def click_on_candidate(self):
        self.wait_till_element_invisibility(self._loader, "xpath")
        self.wait_for_element(self._candidate_tab, "xpath")
        self.element_click_js(self._candidate_tab, "xpath")
        self.wait_for_page_load()

    def click_on_reports(self):
        self.element_click(self._reports_tab, "xpath")

    def click_on_profile(self):
        self.wait_for_element(self._profile, locator_type="xpath")
        self.element_click(self._profile, locator_type="xpath")

    def click_on_logout(self):
        self.wait_for_element(self._logout, locator_type="xpath")
        self.element_click(self._logout, locator_type="xpath")

    def logout(self):
        self.click_on_profile()
        self.click_on_logout()
        self.wait_for_element(self._login, locator_type="xapth")
