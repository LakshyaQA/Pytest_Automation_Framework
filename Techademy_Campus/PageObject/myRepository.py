# import time
from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
from Common_Packages.resources.ConfigPath import UploadFile
from Techademy_Campus.Configuration.readProperties import ReadConfig


class MyRepository(Basepage):
    log = cl.custom_logger()

    """
          This My Repository class is for Uploading a file in repository ,Search the file with name,Edit the file name, 
        
           Share the file ,Delete the file  for all roles (Registrar ,HOD ,Faculty, Student, HR )

            Author : Meghana Avinash Kadam

            """


    _search_name_value = ReadConfig.get_my_repository('My Repository', 'search_name')
    _file_name_value = ReadConfig.get_my_repository('My Repository', 'file_name')
    expected_upload_output = ReadConfig.get_expected_result('Expected Results', 'upload_file_repository')
    expected_edit_output = ReadConfig.get_expected_result('Expected Results', 'edit_file_repository')
    expected_share_output = ReadConfig.get_expected_result('Expected Results', 'share_file_repository')
    expected_share_delete = ReadConfig.get_expected_result('Expected Results', 'delete_file_repository')
    path = UploadFile.file_upload_path('sample.pdf')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _profile_tab = "//p[@class='designation-title']"
    _my_repository_tab = "//span[text()='My Repository']"
    _search_textbox = "//input[@placeholder='Search']"
    _show_My_files_only = "//input[@class='PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3']"
    _upload_button = "//button[text()='Upload']"
    _drag_and_drop = "//div[@class='dropzone']"
    _preview_textlink = "//button[text()='Preview']"
    _close_icon = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium qa-close-icon "
                   "css-logsyf'])[2]")
    _submit_button = "//button[text()='Submit']"
    _cancel_button = "//button[text()='Cancel']"
    _three_dots = "(//button[@aria-label='more'])[1]"
    _edit_icon = "//span[text()='Edit']"
    _file_name = "//textarea[@name='uploadedFileName']"
    _save_button = "//button[text()='SAVE']"
    _share_button = "//span[text()='Share']"
    _add_more_people = ("//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputTypeSearch "
                        "MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input "
                        "MuiAutocomplete-inputFocused css-1081rr0']")
    _select_people = "//li[@data-option-index='2']"
    _click_share = ("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained "
                    "MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium "
                    "MuiButton-colorSecondary MuiButton-root MuiButton-contained MuiButton-containedSecondary "
                    "MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorSecondary qa-submit-btn "
                    "css-zpl1rm']")
    _delete_button = "//span[text()='Delete']"
    _delete_conformation = "//button[text()='Delete']"
    _delete_actual_result = "//div[text()='File Deleted']"
    _share_actual_result = "//div[text()='File Shared']"
    _edit_actual_result = "//div[text()='File Renamed']"
    _upload_actual_result = "//div[text()='File uploaded']"
    _logout_tab = "//span[text()='Logout']"



    def click_on_profile(self):
        self.element_click_js(self._profile_tab, "xpath")


    def click_on_my_repository(self):
        # self.waitForElement(self._my_repository_tab, locator_type="xpath")
        self.element_click_js(self._my_repository_tab, "xpath")

    def enter_search_name(self, search_name):
        self.element_click(self. _search_textbox, "xpath")
        self.send_keys(search_name, self._search_textbox, locator_type="xpath")

    def click_on_show_my_files_only(self):
        # self.waitForElement(self. _show_My_files_only, locator_type="xpath")
        self.element_click_js(self. _show_My_files_only, "xpath")

    def click_on_upload_button(self):
        # self.waitForElement(self._upload_button, locator_type="xpath")
        self.element_click_js(self._upload_button, "xpath")

    def click_on_drag_and_drop(self, path):
        # self.waitForElement(self. _drag_and_drop, locator_type="xpath")
        self.element_click(self. _drag_and_drop, "xpath")
        self.upload_file(path, self._drag_and_drop, locator_type="xpath")

    def click_on_preview_textlink(self):
        # self.waitForElement(self. _preview_textlink, locator_type="xpath")
        self.element_click_js(self. _preview_textlink, "xpath")

    def click_on_close_icon(self):
        # self.waitForElement(self._close_icon, locator_type="xpath")
        self.element_click_js(self._close_icon, "xpath")

    def click_on_submit_button(self):
        # self.waitForElement(self. _submit_button, locator_type="xpath")
        self.element_click_js(self. _submit_button, "xpath")

    def click_on_cancel_button(self):
        self.wait_for_element(self._cancel_button, locator_type="xpath")
        self.element_click(self._cancel_button, "xpath")

    def click_on_three_dot_icon(self):
        # self.waitForElement(self. _three_dots, locator_type="xpath")
        self.element_click(self. _three_dots, "xpath")

    def click_on_edit_icon(self):
        # self.waitForElement(self.  _edit_icon, locator_type="xpath")
        self.element_click_js(self.  _edit_icon, "xpath")

    def enter_file_name(self, file_name):
        self.clear_input_field(self._file_name, "xpath")
        self.send_keys(file_name, self._file_name, locator_type="xpath")

    def click_on_save_button(self):
        # self.waitForElement(self.  _save_button, locator_type="xpath")
        self.element_click(self.   _save_button, "xpath")

    def click_on_share_button(self):
        # self.waitForElement(self. _share_button, locator_type="xpath")
        self.element_click(self.  _share_button, "xpath")

    def click_on_add_more_people(self):
        # self.waitForElement(self._add_more_people, locator_type="xpath")
        self.element_click(self._add_more_people, "xpath")

    def click_on_people_name(self):
        # self.waitForElement(self._select_people, locator_type="xpath")
        self.element_click(self._select_people, "xpath")
        self.element_click(self._click_share, "xpath")



    def click_on_logout(self):
        self.wait_for_element(self._logout_tab, locator_type="xpath")
        self.element_click(self._logout_tab, "xpath")


    def click_on_delete_button(self):
        self.wait_for_element(self. _delete_button, locator_type="xpath")
        self.element_click(self.  _delete_button, "xpath")
        self.element_click(self._delete_conformation, "xpath")

    def upload_file_in_my_repository(self):
        self.click_on_profile()
        self.click_on_my_repository()
        self.click_on_upload_button()
        self.click_on_drag_and_drop(self.path)
        self.click_on_preview_textlink()
        # time.sleep(1)
        self.click_on_close_icon()
        # time.sleep(2)
        self.click_on_submit_button()
        self.verify_upload_output()
        # time.sleep(1)
        # self.click_on_show_my_files_only()
        # self.click_on_cancel_button()
        # time.sleep(1)


    def search_name(self):
        # self.click_on_profile()
        # self.click_on_my_repository()
        self.enter_search_name(self._search_name_value)
        # time.sleep(1)

    def edit_file_name(self):
        # self.click_on_profile()
        # self.click_on_my_repository()
        self.click_on_three_dot_icon()
        self.click_on_edit_icon()
        self.enter_file_name(self._file_name_value)
        self.click_on_save_button()
        self.verify_edit_output()
        # time.sleep(1)


    def share_file(self):
        # self.click_on_profile()
        # self.click_on_my_repository()
        self.click_on_three_dot_icon()
        self.click_on_share_button()
        self.click_on_add_more_people()
        self.click_on_people_name()
        self.verify_share_output()
        # time.sleep(1)


    def delete_file(self):
        # self.click_on_profile()
        # self.click_on_my_repository()
        self.click_on_three_dot_icon()
        self.click_on_delete_button()
        self.verify_delete_output()
        self.click_on_profile()
        self.click_on_logout()
        # time.sleep(1)


    def verify_upload_output(self):
        self.verify_by_comparing_text(locator=self._upload_actual_result, locator_type="xpath", expected_result=self.
                                      expected_upload_output, result_msg="File Not Uploaded")

    def verify_edit_output(self):
        self.verify_by_comparing_text(locator=self._edit_actual_result, locator_type="xpath",
                                      expected_result=self.expected_edit_output, result_msg="File Not Edited")

    def verify_share_output(self):
        self.verify_by_comparing_text(locator=self._share_actual_result, locator_type="xpath", expected_result=self.
                                      expected_share_output, result_msg="File Not Shared")


    def verify_delete_output(self):
        self.verify_by_comparing_text(locator=self._delete_actual_result, locator_type="xpath", expected_result=self.
                                      expected_share_delete, result_msg="File Not Deleted")
