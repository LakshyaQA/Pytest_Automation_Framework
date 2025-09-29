# import time

from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl

from Techademy_Campus.Configuration.readProperties import (ReadConfig)




class Student(Basepage):
    log = cl.custom_logger()

    """
        The Student Details class is for onboarding a student with mandatory fields in registrar role 
        and edit the student as well delete the student with validations and search student with name.

        Author : Meghana Avinash Kadam

    """


    first_name_value = ReadConfig.get_onboard_student_details('Onboard student', 'first_name')
    mobile_number_value = ReadConfig.get_onboard_student_details('Onboard student', 'mobile_number')
    email_value = ReadConfig.get_onboard_student_details('Onboard student', 'email')
    expected_results = ReadConfig.get_expected_result('Expected Results', 'Onboarded_student')
    date_of_birth_value = ReadConfig.get_onboard_student_details('Onboard student', 'date_of_birth')
    expected_edit_delete_result = ReadConfig.get_expected_result('Expected Results', 'update_delete_student')
    search_textbox_value = ReadConfig.get_onboard_student_details('Onboard student', 'search_student_name')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _manage_tab = "//button[text()='Manage']"
    _search_tab = "//input[@placeholder= 'Search']"
    _student_tab = "//span[text()='Student']"
    _onboard_student = "//button[normalize-space()='Onboard Student']"
    _first_name = "//*[@name ='first_name']"
    _mobile_number = "//input[@name='contact_no']"
    _email = "//input[@name='email']"
    _gender = "//input[@name='gender']"
    _select_gender = "//li[text()='Male']"
    _submit_button = "//button[text()='Submit']"
    _cancel_button = "//button[text()='Cancel']"
    _actual_result_element = "//div[text()='Student Onboarded Successfully.']"
    _three_dot = "(//div[@class='qa-student-elipses'])[1]"
    _delete_button = "//span[text()='Delete']"
    _conformation_delete = "//button[text()='Delete']"
    _edit_button = "//span[text()='Edit']"
    _date_of_birth = "//input [@placeholder='mm/dd/yyyy']"
    _update_button = "//button [text()='Update']"
    _actual_result_edit_delete = "//div [text()='The operation completed successfully']"


    def click_on_manage(self):
        self.wait_for_element(self._manage_tab, locator_type="xpath")
        self.element_click(self._manage_tab, "xpath")

    def click_on_student(self):
        self.wait_for_element(self._student_tab, locator_type="xpath")
        self.element_click(self._student_tab, "xpath")


    def click_onboard_student(self):
        self.element_click_js(self._onboard_student, "xpath")
        self.wait_for_element(self._onboard_student, locator_type="xpath")

    def navigate_to_onboard_student_button(self):
        self.click_onboard_student()

    def enter_first_name(self, first_name):
        self.element_click(self._first_name, "xpath")
        self.send_keys(first_name, self._first_name, locator_type="xpath")

    def enter_mobile_number(self, mobile_number):
        self.element_click(self._mobile_number, "xpath")
        self.send_keys(mobile_number, self._mobile_number, locator_type="xpath")

    def enter_email(self, email):
        self.element_click(self._email, "xpath")
        self.send_keys(email, self._email, locator_type="xpath")

    def enter_student_name(self, search_student_name):
        self.element_click(self._search_tab, "xpath")
        self.send_keys(search_student_name, self._search_tab, locator_type="xpath")

    def click_on_gender(self):
        # self.waitForElement(self._gender, locator_type="xpath")
        self.element_click_js(self._gender, "xpath")
        self.element_click(self._select_gender, "xpath")

    def click_on_submit(self):
        self.element_click_js(self._submit_button, "xpath")

    def click_on_cancel(self):
        self.element_click(self._cancel_button, "xpath")

    def click_on_three_dot_icon(self):
        self.element_click(self._three_dot, "xpath")

    def click_on_edit_icon(self):
        self.element_click(self._edit_button, "xpath")

    def click_on_update_button(self):
        self.element_click_js(self._update_button, "xpath")

    def click_on_delete_button(self):
        self.element_click(self._delete_button, "xpath")

    def click_on_delete_conformation(self):
        self.element_click(self._conformation_delete, "xpath")

    def enter_date_of_birth(self, date_of_birth):
        self.element_click_js(self._date_of_birth, "xpath")
        self.send_keys(date_of_birth, self._date_of_birth, locator_type="xpath")




    def enter_mandatory_details(self):
        self.enter_first_name(self.first_name_value)
        self.enter_mobile_number(self.mobile_number_value)
        self.enter_email(self.email_value)
        self.click_on_gender()
        self.web_scroll("down")
        self.click_on_submit()
        self.verify_on_boarded_student()
        # time.sleep(2)


    def edit_student_details(self):        # Date of Birth Will Edit
        self.click_on_three_dot_icon()
        self.click_on_edit_icon()
        self.enter_date_of_birth(self.date_of_birth_value)
        self.click_on_update_button()
        self.verify_edit_delete_student()


    def delete_student(self):
        self.click_on_three_dot_icon()
        self.click_on_delete_button()
        self.click_on_delete_conformation()
        self.verify_edit_delete_student()

    def search_student(self):
        self.enter_student_name(self.search_textbox_value)


    def verify_on_boarded_student(self):
        self.verify_by_comparing_text(locator=self._actual_result_element, locator_type="xpath", expected_result=self.
                                      expected_results, result_msg="Student onboarding unsuccessful")


    def verify_edit_delete_student(self):
        self.verify_by_comparing_text(locator=self._actual_result_edit_delete, locator_type="xpath",
                                      expected_result=self.expected_edit_delete_result, result_msg=
                                      "Student Not Updated/Deleted")
