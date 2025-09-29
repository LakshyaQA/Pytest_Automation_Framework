from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl


class InterviewerPage(Basepage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _in_approval_job = "//span[contains(text(), 'In Approval')]"
    _view_details = ("//span[contains(text(), 'In Approval')]//parent::div//parent::div//parent::div//parent::div"
                     "//button[contains(text(), 'View Details')]")
    _approve_request = "(//button[contains(text(), 'Approve Request')])[1]"
    _new_frame = ("//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation24 "
                  "MuiDialog-paper MuiDialog-paperScrollPaper MuiDialog-paperWidthSm css-y4of9k']")
    _comment_field = "//textarea[@name='comment']"
    _approve_button = "(//button[contains(text(), 'Approve')])[2]"
    _success_message = "//h6[contains(text(), 'Your approval has been successfully recorded')]"
    _close_button = "//button[contains(text(), 'Close')]"

    def in_approval_job(self):
        self.wait_for_element(self._in_approval_job, locator_type="xpath")
        self.element_click_js(self._in_approval_job, locator_type="xpath")
        return self.get_text(self._in_approval_job, locator_type="xpath")

    def click_on_view_details(self):
        self.wait_for_element(self._view_details, locator_type="xpath")
        self.element_click_js(self._view_details, locator_type="xpath")

    def click_approve_request(self):
        self.wait_for_element(self._approve_request, locator_type="xpath")
        self.element_click_js(self._approve_request, locator_type="xpath")

    def enter_comment(self, comment):
        self.wait_for_element(self._comment_field, locator_type="xpath")
        self.send_keys(comment, self._comment_field, locator_type="xpath")

    def click_on_approve(self):
        self.wait_for_element(self._approve_button, locator_type="xpath")
        self.element_click_js(self._approve_button, locator_type="xpath")

    def click_on_close(self):
        self.wait_for_element(self._close_button, locator_type="xpath")
        self.element_click_js(self._close_button, locator_type="xpath")

    def job_approve(self, comment):
        self.click_on_view_details()
        self.click_approve_request()
        self.enter_comment(comment)
        self.click_on_approve()
        self.wait_for_element(self._success_message, locator_type="xpath")
        self.click_on_close()
        return self.get_text(self._success_message, locator_type="xpath")
