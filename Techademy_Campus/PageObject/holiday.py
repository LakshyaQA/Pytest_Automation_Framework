from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl

import time
from Techademy_Campus.Configuration.readProperties import (ReadConfig)


class Holiday(Basepage):

    log = cl.custom_logger()

    '''
         This Holiday creation class is for  creating a holiday in registrar role 
         as well edit the  holiday and delete the holiday with validations.
         
          Author : Meghana Avinash Kadam 

    '''


    location_name_value = ReadConfig.get_holiday('Holiday Creation', 'location_name')
    description_value = ReadConfig.get_holiday('Holiday Creation', 'holiday_description')
    send_invite_value = ReadConfig.get_holiday('Holiday Creation', 'send_invite')
    expected_result_create = ReadConfig.get_expected_result('Expected Results', 'create_holiday')
    expected_result_update = ReadConfig.get_expected_result('Expected Results', 'update_holiday')
    expected_result_delete = ReadConfig.get_expected_result('Expected Results', 'delete_holiday')



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _calendar_tab = "//a[normalize-space()='']//*[name()='svg']"
    _holiday_tab = "//button[text()='HOLIDAYS']"
    _add_icon = ("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedSecondary "
                 "MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorSecondary MuiButton-root "
                 "MuiButton-outlined MuiButton-outlinedSecondary MuiButton-sizeMedium MuiButton-outlinedSizeMedium "
                 "MuiButton-colorSecondary css-e3y5vm']")
    # "(//span[@class='MuiTouchRipple-root css-w0pj6f'])[10]")
    _title_name = "//input[@name= 'title']"
    _date = "//input[@placeholder='mm/dd/yyyy']"
    # _set_date="//button[text()='25']"
    _location = "//input[@name='location']"
    _description = "//textarea[@name='description']"
    _send_invite = ("//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputTypeSearch "
                    "MuiInputBase-inputSizeSmall MuiAutocomplete-input MuiAutocomplete-inputFocused css-1g6d2zd']")
    # _select_invite = "//li[contains(text(),'Faculty group')]"
    _add_holiday_button = "//button[text()='Add Holiday']"
    _cancel_button = "//button[text()='Cancel']"
    _edit_button = "(//span[text()='Edit'])[1]"
    _save_button = "//button[text()='Save']"
    _delete_button = "(//span[text()='Delete'])[1]"
    _actual_delete_result = "//div[text()='Holiday deleted successfully']"
    _actual_edit_button = "//div[text()='Holiday Updated Successfully']"
    _actual_create_holiday = "//div[text()='Holiday Created']"



    def click_on_calendar_tab(self):
        self.wait_for_element(self._calendar_tab, locator_type="xpath")
        self.element_click(self._calendar_tab, "xpath")


    def navigate_to_calendar_tab(self):
        self.click_on_calendar_tab()

    def click_on_holiday_tab(self):
        self.wait_for_element(self. _holiday_tab, locator_type="xpath")
        self.element_click_js(self. _holiday_tab, "xpath")

    def click_on_add_icon(self):
        self.element_click_js(self. _add_icon, "xpath")

    def click_on_edit_icon(self):
        self.element_click_js(self. _edit_button, "xpath")

    def click_on_save_button(self):
        self.element_click_js(self._save_button, "xpath")

    def click_on_delete_button(self):
        self.element_click_js(self._delete_button, "xpath")




    def enter_title_name(self, name):
        self.element_click(self._title_name, "xpath")
        random_name = self.generate_random_name(name)
        self.send_keys(random_name, self._title_name, locator_type="xpath")

    def enter_date(self):
        self.clear_input_field(self._date, "xpath")
        date = self.get_current_date(0+2)
        string_date = str(date)
        self.send_keys(string_date, self._date, locator_type="xpath")
        time.sleep(2)


    def enter_location_name(self, location_name):
        self.element_click(self._location, "xpath")
        self.send_keys(location_name, self._location, locator_type="xpath")

    def enter_description(self, holiday_description):
        self.element_click(self._description, "xpath")
        self.send_keys(holiday_description, self._description, locator_type="xpath")

    def enter_send_invite(self, send_invite):
        self.element_click(self._send_invite, "xpath")
        self.send_keys(send_invite, self._send_invite, locator_type="xpath")



    def click_on_add_holiday_button(self):
        self.wait_for_element(self._add_holiday_button, locator_type="xpath")
        self.element_click(self._add_holiday_button, "xpath")

    def navigate_to_add_holiday_button(self):
        self.click_on_add_holiday_button()

    def click_on_cancel_button(self):
        self.wait_for_element(self._cancel_button, locator_type="xpath")
        self.element_click(self._cancel_button, "xpath")

    def navigate_to_cancel_button(self):
        self.click_on_cancel_button()

    def create_holiday(self, name):
        self.click_on_calendar_tab()
        self.click_on_holiday_tab()
        self.click_on_add_icon()
        self.enter_title_name(name)
        self.enter_date()
        self.enter_location_name(self.location_name_value)
        self.enter_description(self.description_value)
        time.sleep(1)
        self.enter_send_invite(self.send_invite_value)
        self.navigate_to_add_holiday_button()
        self.verify_create_holiday_result()


    def update_holiday(self, name):
        # self.click_on_calendar_tab()
        # self.click_on_holiday_tab()
        self.click_on_edit_icon()
        self.enter_title_name(name)
        # self.enter_date(self.set_date_value)
        # self.enter_location_name(self.location_name_value)
        # self.enter_description(self.description_value)
        self.click_on_save_button()
        self.verify_update_holiday_result()


    def delete_holiday(self):
        # self.click_on_calendar_tab()
        # self.click_on_holiday_tab()
        self.click_on_delete_button()
        self.verify_delete_holiday_result()


    def verify_create_holiday_result(self):
        self.verify_by_comparing_text(locator=self._actual_create_holiday, locator_type="xpath",
                                      expected_result=self.expected_result_create, result_msg=" Holiday Not Created ")

    def verify_update_holiday_result(self):
        self.verify_by_comparing_text(locator=self._actual_edit_button, locator_type="xpath",
                                      expected_result=self.expected_result_update, result_msg="Holiday Not Updated")

    def verify_delete_holiday_result(self):
        self.verify_by_comparing_text(locator=self._actual_delete_result, locator_type="xpath",
                                      expected_result=self.expected_result_delete, result_msg="Holiday Not Deleted")




