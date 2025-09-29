# import time
from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
from Common_Packages.resources.ConfigPath import UploadFile
from Techademy_Campus.Configuration.readProperties import ReadConfig


class BulkUploadStudent(Basepage):

    log = cl.custom_logger()

    """
         This Bulk Upload student class is to uploading a student in bulk in registrar role.
         
           author : Meghana Avinash Kadam
         
    """

    expected_results = ReadConfig.get_expected_result('Expected Results', 'bulk_upload_student')
    path = UploadFile.file_upload_path('student_Format (4).xlsx')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _manage_tab = "//button[text()='Manage']"
    _student_tab = "//span[text()='Student']"
    _onboard_student = "//button[normalize-space()='Onboard Student']"
    _bulk_upload = "//input[@value='bulkupload']"
    _download_sample_svc = "//button[text()='Download Sample CSV']"
    _drag_drop = "//div[@role='presentation']"
    _actual_result_element = "//div[text()='User uploaded successfully']"

    def click_on_manage(self):
        self.wait_for_element(self._manage_tab, locator_type="xpath")
        self.element_click(self._manage_tab, "xpath")

    def click_on_student(self):
        self.element_click(self._student_tab, "xpath")

    def click_onboard_student(self):
        self.element_click_js(self._onboard_student, "xpath")
        # self.waitForElement(self._onboard_student, locator_type="xpath")

    def navigate_to_onboard_student_button(self):
        self.click_on_manage()
        self.click_on_student()
        self.click_onboard_student()


    def click_on_bulk_upload(self):
        # self.waitForElement(self. _bulk_upload, locator_type="xpath")
        self.element_click_js(self. _bulk_upload, "xpath")

    def click_on_sample_template(self):
        self.wait_for_element(self. _download_sample_svc, locator_type="xpath")
        self.element_click(self. _download_sample_svc, "xpath")



    def click_on_drag_and_drop(self, path):
        self.element_click(self._drag_drop, "xpath")
        # time.sleep(3)
        self.upload_file(path, self._drag_drop, locator_type="xpath")
        # time.sleep(4)


    def bulk_upload_student(self):
        self.navigate_to_onboard_student_button()
        self.click_on_bulk_upload()
        self.click_on_drag_and_drop(self.path)


    def verify_bulk_upload_student(self):
        self.verify_by_comparing_text(locator=self._actual_result_element, locator_type="xpath",
                                      expected_result="expected_results", result_msg="User Not Uploaded")
