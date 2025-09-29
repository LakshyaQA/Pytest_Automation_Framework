# import time


from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Common_Packages.resources.ConfigPath import UploadFile

class Badge(Basepage):
    log = cl.custom_logger()

    '''
           This create a badge class is for creating a badge with adding new badge , creating badge from library,
         creating a badge for All programs, For Particular Program ,For Particular Subject ,For particular end date)
         in registrar role as well edit and delete the badge with validations and search functionality.
         
           Author : Meghana Avinash Kadam

       '''

    _badge_title_value = ReadConfig.get_badge('Badge Creation', 'badge_title')
    _description_value = ReadConfig.get_badge('Badge Creation', 'description_details')
    _add_point_value = ReadConfig.get_badge('Badge Creation', 'add_point')
    _expected_results = ReadConfig.get_expected_result('Expected Results', 'Badge_creation')
    _expected_result_update = ReadConfig.get_expected_result('Expected Results', 'badge_update')
    _expected_result_delete = ReadConfig.get_expected_result('Expected Results', 'badge_delete')
    _search_textbox_value = ReadConfig.get_badge('Badge Creation', 'search_badge_name')
    path = UploadFile.file_upload_path('Attendance Badge.jpg')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _manage_tab = "//button[text()='Manage']"
    _badge_creation_tab = "//span[text()='Badge-Creation']"
    _create_badge_button = "//button[text()='Create a Badge']"
    _badge_title = "//input[@name='title']"
    _description = "//textarea[@name='description']"
    _select_badge = "(//input[@name='iconType'])[1]"
    _select_badge_icon = "//button[text()='Select Badge Icon']"
    _select_badge_image = ("//img[@src='https://irisb2aqadatacontainer.blob.core.windows.net/usermanagementpycontainer"
                           "/trial/Academic Excellence Badge.jpg']")
    _select_button = "//button[text()='Select']"
    _add_new_badge = "(//input[@name='iconType'])[2]"
    _drag_and_drop = "//div[@class='dropzone']"
    _select_all_Program = "(//input[@name='badge_applicable_for'])[1]"
    _select_particular_program = "(//input[@name='badge_applicable_for'])[2]"
    _particular_subject = "(//input[@name='badge_applicable_for'])[3]"
    _select_program = "//input[@name='program_name']"
    _select_program_name = "//li[text()='BTech in Marine Engineering']"
    _select_subject = "//input[@name='subject_name']"
    _select_subject_name = "//li[text()='Basic Electrical and Electronics Engineering(ME1-02)']"
    _start_date = "//input[@placeholder='mm/dd/yyyy']"
    _enable_end_date = "//input[@name='end_date_required']"
    _end_date = "(//input[@placeholder='mm/dd/yyyy'])[2]"
    _select_criteria = "//input[@name='criteria_condition_details.criteria']"
    _select_criteria_name = "//li[text()='Attendance']"
    _select_criteria_condition = "//input[@name='criteria_condition_details.condition.field']"
    _select_criteria_value = "//li[text()='90-100%']"
    _add_point = "//input[@name='criteria_condition_details.points']"
    _create_button = "//button[text()='CREATE']"
    _cancel_button = "//button[text()='Cancel']"
    _actual_result = "//div[text()='Badge created succesfully']"
    _three_dot = "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1rtdwbw'])[2]"
    _search_textbox = "//input[@placeholder='Search...']"
    _edit = "//span[text()='Edit']"
    _edit_button = "//button[text()='EDIT']"
    _delete = "//span[text()='Delete']"
    _actual_delete_result = "//div[text()='Badge deleted succesfully']"
    _actual_update_result = "//div[text()='Badge updated succesfully']"






    def click_on_manage(self):
        self.wait_for_element(self._manage_tab, locator_type="xpath")
        self.element_click(self._manage_tab, "xpath")

    def click_on_badge_creation(self):
        self.wait_for_element(self._badge_creation_tab, locator_type="xpath")
        self.element_click_js(self._badge_creation_tab, "xpath")

    def click_on_create_badge_button(self):
        self.wait_for_element(self._create_badge_button, locator_type="xpath")
        self.element_click_js(self._create_badge_button, "xpath")

    def enter_badge_title(self, badge_title):
        self.element_click_js(self._badge_title, "xpath")
        self.send_keys(badge_title, self._badge_title, locator_type="xpath")

    def enter_badge_description(self, description):
        self.element_click_js(self._description, "xpath")
        self.send_keys(description, self._description, locator_type="xpath")

    def click_on_select_badge_icon_from_library(self):
        self.wait_for_element(self._select_badge, locator_type="xpath")
        self.element_click(self._select_badge, "xpath")
        self.wait_for_element(self._select_badge_icon, locator_type="xpath")
        self.element_click(self._select_badge_icon, "xpath")
        self.wait_for_element(self. _select_badge_image, locator_type="xpath")
        self.element_click(self. _select_badge_image, "xpath")
        self.wait_for_element(self._select_button, locator_type="xpath")
        self.element_click_js(self._select_button, "xpath")

    def click_on_add_new_badge_icon(self):
        self.wait_for_element(self._add_new_badge, locator_type="xpath")
        self.element_click(self._add_new_badge, "xpath")

    def click_on_drag_and_drop_file(self, path):
        self.wait_for_element(self. _drag_and_drop, locator_type="xpath")
        self.element_click(self. _drag_and_drop, "xpath")
        self.upload_file(path, self._drag_and_drop, locator_type="xpath")

    def click_on_particular_subject_radio(self):
        self.element_click(self. _particular_subject, "xpath")

    def click_on_all_program(self):
        self.element_click(self._select_all_Program, "xpath")

    def click_on_particular_program(self):
        self.element_click(self. _select_particular_program, "xpath")

    def click_on_program_dropdown(self):
        # self.waitForElement(self._select_program, locator_type="xpath")
        self.element_click_js(self._select_program, "xpath")
        self.wait_for_element(self. _select_program_name, locator_type="xpath")
        self.element_click_js(self. _select_program_name, "xpath")

    def click_on_subject_dropdown(self):
        # self.waitForElement(self._select_subject, locator_type="xpath")
        self.element_click_js(self._select_subject, "xpath")
        self.wait_for_element(self. _select_subject_name, locator_type="xpath")
        self.element_click_js(self. _select_subject_name, "xpath")

    def enter_start_date(self):
        self.wait_for_element(self._start_date, locator_type="xpath")
        self.element_click_js(self._start_date, locator_type="xpath")
        date = self.get_current_date(0)
        string_date = str(date)
        self.send_keys(string_date, self._start_date, "xpath")



    def enter_end_date(self):
        self.element_click_js(self._enable_end_date, "xpath")
        self.clear_input_field(self._end_date, "xpath")
        date = self.get_current_date(0+2)
        string_date = str(date)
        self.send_keys(string_date, self._end_date, locator_type="xpath")



    def click_on_select_criteria(self):
        # self.waitForElement(self._select_criteria, locator_type="xpath")
        self.element_click_js(self._select_criteria, "xpath")
        self.wait_for_element(self. _select_criteria_name, locator_type="xpath")
        self.element_click_js(self. _select_criteria_name, "xpath")


    def click_on_select_criteria_condition(self):
        # self.waitForElement(self._select_criteria_condition, locator_type="xpath")
        self.element_click_js(self._select_criteria_condition, "xpath")
        self.wait_for_element(self.  _select_criteria_value, locator_type="xpath")
        self.element_click_js(self.  _select_criteria_value, "xpath")

    def enter_add_point(self, add_point):
        self.wait_for_element(self._add_point, locator_type="xpath")
        self.element_click_js(self._add_point, "xpath")
        self.send_keys(add_point, self._add_point, locator_type="xpath")

    def click_on_create_button(self):
        self.wait_for_element(self._create_button, locator_type="xpath")
        self.element_click_js(self._create_button, "xpath")

    def click_on_cancel_button(self):
        self.wait_for_element(self._cancel_button, locator_type="xpath")
        self.element_click(self._cancel_button, "xpath")

    def click_on_three_dot(self):
        self.wait_for_element(self._three_dot, locator_type="xpath")
        self.element_click_js(self._three_dot, "xpath")

    def click_on_edit_icon(self):
        self.wait_for_element(self._edit, locator_type="xpath")
        self.element_click_js(self._edit, "xpath")

    def click_on_edit_button(self):
        self.wait_for_element(self._edit_button, locator_type="xpath")
        self.element_click(self._edit_button, "xpath")

    def click_on_radio_button_of_library(self):
        self.wait_for_element(self._select_badge, locator_type="xpath")
        self.element_click(self._select_badge, "xpath")

    def click_on_delete_button(self):
        self.wait_for_element(self._delete, locator_type="xpath")
        self.element_click(self._delete, "xpath")

    def enter_search_badge_name(self, search_badge_name):
        self.wait_for_element(self._search_textbox, locator_type="xpath")
        self.send_keys(search_badge_name, self._search_textbox, locator_type="xpath")



    # Creating a badge with Adding New badge icon with particular subject


    def creation_of_badge_with_adding_new_badge(self):
        self.click_on_manage()
        self.click_on_badge_creation()
        self.click_on_create_badge_button()
        self.enter_badge_title(self._badge_title_value)
        self.enter_badge_description(self._description_value)
        self.click_on_add_new_badge_icon()
        self.click_on_drag_and_drop_file(self.path)
        self.click_on_particular_subject_radio()
        self.click_on_program_dropdown()
        self.click_on_subject_dropdown()
        self.enter_start_date()
        self.web_scroll("down")
        self.click_on_select_criteria()
        self.click_on_select_criteria_condition()
        self.enter_add_point(self._add_point_value)
        self.click_on_create_button()
        self.verify_creation_of_badge()

        # self.click_on_cancel_button()


    # Creating badge with selecting badge icon from library for particular program


    def creating_badge_from_library(self):
        self.click_on_manage()
        self.click_on_badge_creation()
        self.click_on_create_badge_button()
        self.enter_badge_title(self._badge_title_value)
        self.enter_badge_description(self._description_value)
        self.click_on_select_badge_icon_from_library()
        self.click_on_particular_program()
        self.click_on_program_dropdown()
        # time.sleep(1)
        self.enter_start_date()
        self.web_scroll("down")
        self.click_on_select_criteria()
        self.click_on_select_criteria_condition()
        self.enter_add_point(self._add_point_value)
        self.click_on_create_button()
        self.verify_creation_of_badge()
        # time.sleep(1)

    # Creating badge with selecting badge icon from library for All Program with end date
    def creating_badge_for_all_programs(self):
        self.click_on_manage()
        self.click_on_badge_creation()
        self.click_on_create_badge_button()
        self.enter_badge_title(self._badge_title_value)
        self.enter_badge_description(self._description_value)
        self.click_on_select_badge_icon_from_library()
        self.click_on_all_program()
        # time.sleep(2)
        self.enter_start_date()
        # self.enter_end_date()
        self.web_scroll("down")
        self.click_on_select_criteria()
        self.click_on_select_criteria_condition()
        self.enter_add_point(self._add_point_value)
        self.click_on_create_button()
        self.verify_creation_of_badge()
        # time.sleep(1)

    def update_badge(self):
        self.click_on_three_dot()
        self.click_on_edit_icon()
        self.click_on_radio_button_of_library()
        self.click_on_all_program()
        self.click_on_edit_button()
        self.verify_update_badge()

    def delete_badge(self):
        # self.click_on_manage()
        # self.click_on_badge_creation()
        # self.enter_search_badge_name(self._search_textbox_value)
        self.click_on_three_dot()
        self.click_on_delete_button()
        self.verify_delete_badge()

    def search_badge(self):
        self.enter_search_badge_name(self._search_textbox_value)



    def verify_creation_of_badge(self):
        self.verify_by_comparing_text(locator=self. _actual_result, locator_type="xpath",
                                      expected_result=self._expected_results, result_msg="Already badge is exist")

    def verify_update_badge(self):
        self.verify_by_comparing_text(locator=self._actual_update_result, locator_type="xpath",
                                      expected_result=self._expected_result_update,
                                      result_msg="Badge Updation Unsuccessful")

    def verify_delete_badge(self):
        self.verify_by_comparing_text(locator=self._actual_delete_result, locator_type="xpath",
                                      expected_result=self._expected_result_delete, result_msg="Badge Not Deleted")
