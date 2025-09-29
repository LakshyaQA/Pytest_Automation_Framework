import time


import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class Candidates(Basepage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators of candidate tab

    _download_template = "//button[normalize-space()='Download Template']"
    _upload_list_button = "//button[normalize-space()='Upload Candidates List']"
    _browse_file = "//*[@class='MuiTypography-root MuiTypography-subtitle1 css-9kc8q5']"
    _cancel_upload = ("//*[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary "
                      "MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-root MuiButton-outlined "
                      "MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium qa-cancel-btn "
                      "css-d6gq8g']")
    _upload = ("//*[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary "
               "MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained "
               "MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium qa-submit-btn "
               "css-1qu76of']")
    _add_candidates = "//button[normalize-space()='Add Candidate']"
    _search_candidate = "//input[@placeholder='Search']"
    _delete_candidate = "//h6[contains(text(), 'Chetan')]//parent :: a//parent::div//parent::div//following-sibling::div[@data-field='action']//button"
    _actual_result = "(//div[@id = 'notistack-snackbar'])"
    _yes_delete = "//button[contains(text(), 'Yes, Delete')]"
    _add_bulk = "//button[contains(text(), 'Upload Candidates List')]"
    _add_bulk_file = "//label//input[@type='file']"
    _upload_bulk_file_button = "(//button[contains(text(), 'Upload')])[2]"
    _bulk_upload_actual_result = "//h5[contains(text(), 'Bulk Uploading Initiated...')]"
    _close_bulk_upload = "//button[contains(text(), 'Close')]"
    _bulk_candidate = "//h6[contains(text(), 'Test')]"
    _bulk_candidate_checkbox = " //h6[contains(text(), 'Test')]//parent::a//parent::div//parent::div//preceding-sibling::div//span//input"
    _delete_bulk = "//button[contains(text(), 'Delete')]"
    _loader = "//div[@class='MuiBackdrop-root loader css-xuaqpw']"



    def click_on_download_temp(self):
        self.element_click(self._download_template, "xpath")

    def click_on_upload_list(self):
        self.element_click(self._upload_list_button, "xpath")

    def upload_candidate_list(self, path):
        self.upload_file(path, self._browse_file, "xpath")

    def click_on_upload_button(self):
        self.element_click(self._upload, "xpath")

    def click_on_add_candidate(self):
        self.wait_for_element(self._add_candidates, "xpath")
        self.element_click_js(self._add_candidates, "xpath")
        self.wait_for_page_load()

    def search_candidate(self):
        self.element_click(self._search_candidate, "xpath")
        self.send_keys("Chetan", self._search_candidate, "xpath")

    def click_on_delete(self):
        self.wait_for_element(self._delete_candidate, "xpath")
        self.element_click_js(self._delete_candidate, "xpath")

    def click_on_yes_delete(self):
        self.wait_for_element(self._yes_delete, locator_type="xpath")
        self.element_click_js(self._yes_delete, locator_type="xpath")

    def click_on_add_bulk(self):
        self.wait_for_element(self._add_bulk, locator_type="xpath")
        self.element_click_js(self._add_bulk, locator_type="xpath")
        self.wait_for_page_load()

    def click_on_bulk_upload(self):
        self.wait_for_element(self._upload_bulk_file_button, locator_type="xpath")
        self.element_click_js(self._upload_bulk_file_button, locator_type="xpath")
        self.wait_for_page_load()

    def upload_bulk_file(self):
        self.wait_for_element(self._add_bulk_file, locator_type="xpath")
        self.send_keys(UploadFile.upload_zip(), self._add_bulk_file, locator_type="xpath")
        self.wait_for_page_load()

    def click_on_close_bulk_upload(self):
        self.wait_for_element(self._close_bulk_upload, locator_type="xpath")
        self.element_click_js(self._close_bulk_upload, locator_type="xpath")
        self.wait_for_page_load()

    def delete_candidate(self):
        self.click_on_delete()
        self.wait_for_page_load()
        self.click_on_yes_delete()
        self.wait_for_page_load()
        self.wait_for_element(self._actual_result, locator_type="xpath")
        return self.get_text(self._actual_result, locator_type="xpath")



    def add_bulk_upload(self):
        self.click_on_add_bulk()
        self.upload_bulk_file()
        self.click_on_bulk_upload()
        self.wait_for_page_load()
        self.wait_for_element(self._bulk_upload_actual_result, "xpath")
        text = self.get_text(self._bulk_upload_actual_result, "xpath")
        self.click_on_close_bulk_upload()
        return text

    def delete_multiple_candidate(self):
        condition = True
        result = ""
        try:
            while True:
                if not self.is_element_displayed(self._bulk_candidate, "xpath"):
                    break

                candidate = self.get_element_list(self._bulk_candidate_checkbox, "xpath")
                for element in candidate:
                    self.scroll_by_visible_element_by_webelement(element)
                    self.element_click_by_webelement(element)

                self.wait_for_element(self._delete_bulk, "xpath")
                self.element_click_js(self._delete_bulk, "xpath")
                self.wait_for_element(self._yes_delete, "xpath")
                self.element_click_js(self._yes_delete, "xpath")
                self.wait_for_element(self._actual_result + "[1]", "xpath")
                result = self.get_text(self._actual_result + "[1]", "xpath")
                self.wait_till_element_invisibility(self._actual_result, "xpath")

        except Exception as e:
            return result

