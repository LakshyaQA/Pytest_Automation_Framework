from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl

from Techademy_Campus.Configuration.readProperties import (ReadConfig)



class Event(Basepage):
    log = cl.custom_logger()

    '''
         This Event creation class is for creating an event in registrar role.
         as well edit and delete the event with validations.
          
          Author : Meghana Avinash Kadam

    '''

    event_title_value = ReadConfig.get_event('Event Creation', 'event_title')
    description_value = ReadConfig.get_event('Event Creation', 'description_content')
    send_invites_value = ReadConfig.get_event('Event Creation', 'send_invites')
    expected_result_create = ReadConfig.get_expected_result('Expected Results', 'create_event')
    expected_result_update = ReadConfig.get_expected_result('Expected Results', 'update_event')
    expected_result_delete = ReadConfig.get_expected_result('Expected Results', 'delete_event')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _calendar_tab = "//a[normalize-space()='']//*[name()='svg']"
    _add_icon = ("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedSecondary "
                 "MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorSecondary MuiButton-root "
                 "MuiButton-outlined MuiButton-outlinedSecondary MuiButton-sizeMedium MuiButton-outlinedSizeMedium "
                 "MuiButton-colorSecondary css-e3y5vm']")
    _event_title = "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1blbzq8']"
    _calendar_icon = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd "
                      "MuiIconButton-sizeMedium css-jpqtc2'])[1]")
    _start_date = "(//input[@placeholder='mm/dd/yyyy'])[1]"
    _start_time = "(//input[@placeholder='hh:mm (a|p)m'])[1]"
    _end_date = "(//input[@type='tel'])[3]"
    _end_time = "(//input[@type='tel'])[4]"
    _description_content = "//textarea[@name='description']"
    _send_invites_to = ("//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputTypeSearch "
                        "MuiInputBase-inputSizeSmall MuiAutocomplete-input MuiAutocomplete-inputFocused css-1g6d2zd']")
    _add_event_button = "//button[text()='Add Event']"
    _cancel_button = "//button[text()='Cancel']"
    _event_name = "//span[text()='TechXplore']"
    _actual_result_create = "//div[text()='event created']"
    _three_dot = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1jka65r']"
    _edit_icon = "//div[text()=' Edit']"
    _save_button = "//button[text()='Save']"
    _actual_result_update = "//div[text()='Event Updated Successfully']"
    _delete_icon = "//div[text()=' Delete']"
    _delete_conformation = "//button[text()='Delete']"
    _actual_result_delete = "//div[text()='Event deleted successfully']"

    def click_on_calendar_tab(self):
        self.wait_for_element(self._calendar_tab, locator_type="xpath")
        self.element_click(self._calendar_tab, "xpath")

    def navigate_to_calendar_tab(self):
        self.click_on_calendar_tab()

    def click_on_add_icon(self):
        self.wait_for_element(self._add_icon, locator_type="xpath")
        self.element_click_js(self._add_icon, "xpath")

    def enter_event_title(self, event_title):
        self.element_click(self._event_title, "xpath")
        self.send_keys(event_title, self._event_title, locator_type="xpath")

    def enter_start_date(self, start_date):
        self.clear_input_field(self._start_date, "xpath")
        self.send_keys(start_date, self._start_date, "xpath")
        # time.sleep(3)

    def enter_start_time(self, start_time):
        self.clear_input_field(self._start_time, "xpath")
        self.send_keys(start_time, self._start_time, locator_type="xpath")
        # time.sleep(3)

    def enter_end_date(self, end_date):
        self.clear_input_field(self._end_date, "xpath")
        self.send_keys(end_date, self._end_date, locator_type="xpath")
        # time.sleep(2)

    def enter_end_time(self, end_time):
        self.clear_input_field(self._end_time, "xpath")
        self.send_keys(end_time, self._end_time, locator_type="xpath")
        # time.sleep(2)

    def enter_description(self, description_content):
        self.element_click(self._description_content, "xpath")
        self.send_keys(description_content, self._description_content, locator_type="xpath")

    def enter_send_invites(self, send_invites):
        self.element_click_js(self._send_invites_to, "xpath")
        self.sendkeys_js(send_invites, self._send_invites_to, locator_type="xpath")

    def click_on_add_event_button(self):
        self.wait_for_element(self._add_event_button, locator_type="xpath")
        self.element_click(self._add_event_button, "xpath")

    def click_on_three_dot_icon(self):
        self.wait_for_element(self._three_dot, locator_type="xpath")
        self.element_click(self._three_dot, "xpath")

    def click_on_edit_icon(self):
        self.wait_for_element(self._edit_icon, locator_type="xpath")
        self.element_click(self._edit_icon, "xpath")

    def click_on_save_button(self):
        self.wait_for_element(self._save_button, locator_type="xpath")
        self.element_click(self._save_button, "xpath")

    def click_on_delete_icon(self):
        self.wait_for_element(self._delete_icon, locator_type="xpath")
        self.element_click(self._delete_icon, "xpath")

    def click_on_delete_conformation(self):
        self.wait_for_element(self._delete_conformation, locator_type="xpath")
        self.element_click(self._delete_conformation, "xpath")

    def click_on_event_name(self):
        self.wait_for_element(self._event_name, locator_type="xpath")
        self.element_click(self._event_name, "xpath")


    def navigate_to_add_event_button(self):
        self.click_on_add_event_button()

    def click_on_cancel_button(self):
        self.wait_for_element(self._cancel_button, locator_type="xpath")
        self.element_click(self._cancel_button, "xpath")

    def navigate_to_cancel_button(self):
        self.click_on_cancel_button()

    def create_event(self):
        self.click_on_calendar_tab()
        self.click_on_add_icon()
        self.enter_event_title(self.event_title_value)
        self.enter_description(self.description_value)
        self.enter_send_invites(self.send_invites_value)
        self.click_on_add_event_button()
        self.verify_create_event()

        # time.sleep(3)

    def update_event(self):
        self.click_on_event_name()
        self.click_on_three_dot_icon()
        self.click_on_edit_icon()
        # self.enter_event_title(self.event_title_value)
        # self.enter_description(self.description_value)
        self.enter_send_invites(self.send_invites_value)
        self.click_on_save_button()
        self.verify_update_event()


    def delete_event(self):
        self.click_on_event_name()
        self.click_on_three_dot_icon()
        self.click_on_delete_icon()
        self.click_on_delete_conformation()
        self.verify_delete_event()


    def verify_create_event(self):
        self.verify_by_comparing_text(locator=self._actual_result_create, locator_type="xpath",
                                      expected_result=self.expected_result_create,
                                      result_msg="Event Creation Unsuccessful")


    def verify_update_event(self):
        self.verify_by_comparing_text(locator=self._actual_result_update, locator_type="xpath",
                                      expected_result=self.expected_result_update, result_msg="Event Not Updated")

    def verify_delete_event(self):
        self.verify_by_comparing_text(locator=self._actual_result_delete, locator_type="xpath",
                                      expected_result=self.expected_result_delete, result_msg="Event Not Deleted")
