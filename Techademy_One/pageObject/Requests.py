"""
This page includes locators and functions of Request page
"""

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage

class Requests(Basepage):
    """
    Page class for Requests page
    """
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _requests_header = "//h3[@class='MuiTypography-root MuiTypography-h3 css-kkhisd']"
    _req_id = "//h6[contains(text(),'RA-')]"
    _req_info = "//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv']"
    _pending_req = "//button[normalize-space()='Pending Requests']"
    _completed_req = "//button[normalize-space()='Completed Requests']"
    _pending_req_verify = "//button[normalize-space()='Pending Requests' and @aria-selected='true']"
    _completed_req_verify = "//button[normalize-space()='Completed Requests' and @aria-selected='true']"

    def click_on_req_id(self):
        """
        Click on Request ID element
        """
        self.element_click(self._req_id, "xpath")

    def click_on_pending(self):
        """
        Click on Pending Requests button
        """
        self.element_click(self._pending_req, "xpath")

    def click_on_completed(self):
        """
        Click on Completed Requests button
        """
        self.element_click(self._completed_req, "xpath")

    def verify_requests(self):
        """
        Verify the Requests header text
        """
        self.verify_by_comparing_text(self._requests_header, "xpath", "Manage Requests", "RequestPageTest")

    def verify_req_name(self):
        """
        Verify the presence of Request Information element
        """
        self.verify_by_element_presence(self._req_info, "xpath", "ReqInfoTEst")

    def verify_pending_tab(self):
        """
        Verify the presence of Pending Requests tab
        """
        self.verify_by_element_presence(self._pending_req_verify, "xpath", "PendingReq")

    def verify_completed_tab(self):
        """
        Verify the presence of Completed Requests tab
        """
        self.verify_by_element_presence(self._completed_req_verify, "xpath", "Completed")
