from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
import time
from Common_Packages.resources.ConfigPath import UploadFile
from Techademy_Campus.Configuration.readProperties import ReadConfig



class PeerGroupInteraction(Basepage):
    log = cl.custom_logger()

    """
        This Peer Group Interaction class is for student role which  includes the functionality 
        of creating an interaction ,searching the interaction by title,searching interaction by date ,
        report to the interaction(report will be available only for received interaction),vote 
        and update the interaction,edit the created interaction and delete the interaction

        Author : Meghana Avinash Kadam

    """


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _title_value = ReadConfig.get_peer_group_interaction('Peer Group Interaction', 'interaction_title' )
    _description_value = ReadConfig.get_peer_group_interaction('Peer Group Interaction', 'interaction_description')
    _tool_option_value = ReadConfig.get_peer_group_interaction('Peer Group Interaction', 'tool_in_option')
    _second_tool_option_value = ReadConfig.get_peer_group_interaction('Peer Group Interaction', 'tool_in_option_second')
    _send_invites_value = ReadConfig.get_peer_group_interaction('Peer Group Interaction', 'interaction_send_invites')
    _search_by_title_value = ReadConfig.get_peer_group_interaction('Peer Group Interaction', 'search_by_title')
    _reply_textbox_value = ReadConfig.get_peer_group_interaction('Peer Group Interaction', 'enter_reply')
    _report_description_value = ReadConfig.get_peer_group_interaction('Peer Group Interaction', 'report_description')
    expected_result_create = ReadConfig.get_expected_result('Expected Results', 'create_interaction')
    expected_result_edit = ReadConfig.get_expected_result('Expected Results', 'edit_interaction')
    expected_result_report = ReadConfig.get_expected_result('Expected Results', 'report_interaction')
    expected_result_delete = ReadConfig.get_expected_result('Expected Results', 'delete_interaction')
    expected_result_comment = ReadConfig.get_expected_result('Expected Results', 'comment_interaction')
    path = UploadFile.file_upload_path('Pdf (1).pdf')

    #  x paths for tabs
    _my_learning = "//button[text()='My Learning']"
    _peer_group = "//span[text()='Peer Group']"
    _start_interaction = "//button[text()='Start Interaction']"
    _title = "//input[@name='title']"
    _description = "//textarea[@name='description']"
    _drag_and_drop_file = "//div[@class='dropzone']"
    _enable_poll = "//input[@name='createAPoll']"
    _tool_option = "//input[@name='poolingOptions.0.option_text']"
    _add_icon = "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1ouieb2'])[2]"
    _second_option = "//input[@name='poolingOptions.1.option_text']"
    _send_invites_to = ("//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputTypeSearch "
                        "MuiInputBase-inputSizeSmall MuiAutocomplete-input MuiAutocomplete-inputFocused css-1g6d2zd']")
    _select_send_invites = "//li[@id='free-solo-2-demo-option-3']"
    _toggle_button = "//input[@name='haveEndTime']"
    _start_date = "(//input[@placeholder='mm/dd/yyyy'])[2]"
    _end_date = "(//input[@placeholder='mm/dd/yyyy'])[3]"
    _hide_date = "//input[@name='hideAfterEndDate']"
    _submit_button = "//button[text()='Submit']"
    _cancel_button = "//button[text()='Cancel']"
    _search_by_title = "//input[@placeholder='Search By Title']"
    _selecting_date = "//input[@placeholder='mm/dd/yyyy']"
    _clear_filter = "//button[text()='Clear filter']"
    _upvote = "(//span[@class='MuiButton-icon MuiButton-startIcon MuiButton-iconSizeMedium css-6xugel'])[1]"
    _down_vote = "(//span[@class='MuiButton-icon MuiButton-startIcon MuiButton-iconSizeMedium css-6xugel'])[2]"
    _replies = "//li[text()=' Replies']"
    _reply_textbox = "//input[@name='comment']"
    _add_comment_button = "//button[text()='Add comment']"
    _three_dot = ("//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-colorSecondary "
                  "MuiIconButton-sizeMedium css-2kq788']")
    _report = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-4a5pjv']"
    _report_content = "//span[text()='Hate Speech']"
    _report_description = "//textarea[@name='description']"
    _report_submit = "//button[text()='Submit']"
    _report_cancel = "//button[text()='Cancel']"
    _interaction_radio_button = "(//input[@name='radio-buttons-polling-group'])[1]"
    _edit = "(//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-4a5pjv'])[1]"
    _edit_submit_button = "//button[text()='Submit']"
    _delete = "(//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-4a5pjv'])[2]"
    _delete_button = "//button[text()='Delete']"
    _actual_result_delete = "//div[text()='Discussion deleted']"
    _actual_result_edit = "//div[text()='Discussion updated']"
    _actual_result_report = "//div[text()='Reported to higher authority successfully.']"
    _actual_result_create = "//div[text()='Discussion created']"
    _actual_result_comment = "//div[text()='Comment added']"

    def click_on_my_learning(self):
        self.wait_for_element(self. _my_learning, locator_type="xpath")
        self.element_click_js(self. _my_learning, "xpath")

    def click_on_peer_group(self):
        self.wait_for_element(self._peer_group, locator_type="xpath")
        self.element_click_js(self._peer_group, "xpath")

    def click_on_start_interaction(self):
        self.wait_for_element(self. _start_interaction, locator_type="xpath")
        self.element_click_js(self. _start_interaction, "xpath")

    def enter_interaction_title(self,  interaction_title):
        self.element_click_js(self. _title, "xpath")
        self.send_keys(interaction_title, self._title, locator_type="xpath")

    def enter_description_name(self, interaction_description):
        self.element_click_js(self._description, "xpath")
        self.send_keys(interaction_description, self._description, locator_type="xpath")

    def enter_interaction_date(self, interaction_start_date):
        self.element_click_js(self._selecting_date, "xpath")
        self.clear_input_field(self._selecting_date, locator_type="xpath")
        self.send_keys(interaction_start_date, self._selecting_date, locator_type="xpath")

    def enter_start_date(self):
        self.element_click_js(self._start_date, "xpath")
        date = self.get_current_ddmmyyyy(0)
        string_date = str(date)
        self.send_keys(string_date, self._start_date, locator_type="xpath")

    def enter_end_date(self):
        self.element_click_js(self. _end_date, "xpath")
        date = self.get_current_ddmmyyyy(0)
        string_date = str(date)
        self.send_keys(string_date, self._end_date, locator_type="xpath")


    def click_on_drag_and_drop_file(self, path):
        self.element_click(self._drag_and_drop_file, "xpath")
        # time.sleep(3)
        self.upload_file(path, self._drag_and_drop_file, locator_type="xpath")
        # time.sleep(4)

    def click_on_enable_poll(self):
        # self.waitForElement(self. _enable_poll, locator_type="xpath")
        self.element_click(self. _enable_poll, "xpath")

    def enter_tool_option(self, tool_in_option):
        self.element_click_js(self. _tool_option, "xpath")
        self.send_keys(tool_in_option, self._tool_option, locator_type="xpath")

    def click_on_add_icon(self):
        # self.waitForElement(self._add_icon, locator_type="xpath")
        self.element_click_js(self._add_icon, "xpath")

    def enter_second_tool_option(self, tool_in_option_second):
        self.element_click_js(self.  _second_option, "xpath")
        self.send_keys(tool_in_option_second, self._second_option, locator_type="xpath")

    def enter_send_invites(self, interaction_send_invites):
        self.element_click_js(self. _send_invites_to, "xpath")
        self.send_keys(interaction_send_invites, self._send_invites_to, locator_type="xpath")

    def click_on_select_invites(self):
        # self.waitForElement(self._send_invites_to, locator_type="xpath")
        self.element_click(self._send_invites_to, "xpath")
        # self.waitForElement(self._select_send_invites, locator_type="xpath")
        self.element_click(self._select_send_invites, "xpath")

    def click_on_toggle_button(self):
        # self.waitForElement(self. _toggle_button, locator_type="xpath")
        self.element_click(self. _toggle_button, "xpath")

    def click_on_hide_date(self):
        # self.waitForElement(self._hide_date, locator_type="xpath")
        self.element_click(self._hide_date, "xpath")

    def click_on_submit_button(self):
        self.wait_for_element(self. _submit_button, locator_type="xpath")
        self.element_click(self. _submit_button, "xpath")


    def click_on_cancel_button(self):
        self.wait_for_element(self._cancel_button, locator_type="xpath")
        self.element_click(self._cancel_button, "xpath")

    def enter_search_by_title(self, search_by_title):
        self.element_click_js(self. _search_by_title, "xpath")
        self.send_keys(search_by_title, self._search_by_title, locator_type="xpath")

    def click_on_clear_filter(self):
        # self.waitForElement(self._clear_filter, locator_type="xpath")
        self.element_click_js(self._clear_filter, "xpath")

    def click_on_upvote(self):
        # self.waitForElement(self. _upvote, locator_type="xpath")
        self.element_click_js(self. _upvote, "xpath")

    def click_on_down_vote(self):
        self.wait_for_element(self._down_vote, locator_type="xpath")
        self.element_click_js(self._down_vote, "xpath")

    def click_on_interaction_radiobutton(self):
        # self.waitForElement(self._interaction_radio_button, locator_type="xpath")
        self.element_click_js(self._interaction_radio_button, "xpath")

    def click_on_edit(self):
        self.wait_for_element(self._edit, locator_type="xpath")
        self.element_click_js(self._edit, "xpath")

    def click_on_edit_submit(self):
        self.wait_for_element(self._edit_submit_button, locator_type="xpath")
        self.element_click_js(self._edit_submit_button, "xpath")

    def click_on_delete(self):
        self.wait_for_element(self._delete, locator_type="xpath")
        self.element_click(self._delete, "xpath")
        self.element_click(self. _delete_button, "xpath")


    def click_on_reply_icon(self):
        self.wait_for_element(self. _replies, locator_type="xpath")
        self.element_click_js(self. _replies, "xpath")

    def enter_reply(self, enter_reply):
        self.element_click_js(self._reply_textbox, "xpath")
        self.send_keys(enter_reply, self._reply_textbox, locator_type="xpath")

    def click_on_add_comment(self):
        self.wait_for_element(self._add_comment_button, locator_type="xpath")
        self.element_click_js(self._add_comment_button, "xpath")

    def click_on_three_dot_icon(self):
        self.wait_for_element(self._three_dot, locator_type="xpath")
        self.element_click_js(self._three_dot, "xpath")

    def click_on_report(self):
        self.wait_for_element(self. _report, locator_type="xpath")
        self.element_click_js(self. _report, "xpath")

    def click_on_report_content(self):
        self.wait_for_element(self. _report_content, locator_type="xpath")
        self.element_click_js(self. _report_content, "xpath")

    def enter_report_description(self, report_description):
        self.element_click_js(self._report_description, "xpath")
        self.send_keys(report_description, self._report_description, locator_type="xpath")

    def click_on_report_submit_button(self):
        self.wait_for_element(self._report_submit, locator_type="xpath")
        self.element_click(self._report_submit, "xpath")

    def click_on_report_cancel_button(self):
        self.wait_for_element(self. _report_cancel, locator_type="xpath")
        self.element_click(self._report_cancel, "xpath")

    def creating_interaction(self):
        self.click_on_my_learning()
        self.click_on_peer_group()
        self.click_on_start_interaction()
        self.enter_interaction_title(self. _title_value)
        self.enter_description_name(self._description_value)
        self.click_on_drag_and_drop_file(self.path)
        self.click_on_enable_poll()
        self.enter_tool_option(self._tool_option_value)
        self.web_scroll("down")
        self.click_on_add_icon()
        self.enter_second_tool_option(self._second_tool_option_value)
        self.enter_send_invites(self._send_invites_value)
        self.click_on_toggle_button()
        self.enter_start_date()
        self.enter_end_date()
        self.click_on_hide_date()
        self.click_on_submit_button()
        # self.click_on_cancel_button()


    def search_by_title(self):
        # self.click_on_my_learning()
        # self.click_on_peer_group()
        self.enter_search_by_title(self._search_by_title_value)

    def search_by_date(self):
        # self.click_on_my_learning()
        # self.click_on_peer_group()
        # self.enter_interaction_date()
        # time.sleep(2)
        self.click_on_clear_filter()

    def vote_and_reply(self):
        # self.click_on_my_learning()
        # self.click_on_peer_group()
        # time.sleep(2)
        self.click_on_interaction_radiobutton()
        # time.sleep(2)
        self.click_on_upvote()
        time.sleep(1)
        # self.click_on_down_vote()
        #  time.sleep(2)
        self.click_on_reply_icon()
        #  time.sleep(2)
        self.enter_reply(self._reply_textbox_value)
        time.sleep(1)
        self.click_on_add_comment()
        self.web_scroll("down")

    def report_interaction(self):
        # self.click_on_my_learning()
        # self.click_on_peer_group()
        # time.sleep(2)
        self.click_on_three_dot_icon()
        self.click_on_report()
        # time.sleep(2)
        self.click_on_report_content()
        # time.sleep(2)
        self.enter_report_description(self._report_description_value)
        # time.sleep(2)
        self.click_on_report_submit_button()
        # self.click_on_report_cancel_button()


    def edit_created_interaction(self):
        self.click_on_my_learning()
        self.click_on_peer_group()
        # time.sleep(2)
        self.click_on_three_dot_icon()
        self.click_on_edit()
        # time.sleep(2)
        self.click_on_select_invites()
        self.click_on_edit_submit()


    def delete_created_interaction(self):
        self.click_on_my_learning()
        self.click_on_peer_group()
        # time.sleep(2)
        self.click_on_three_dot_icon()
        self.click_on_delete()


    def verify_create_interaction(self):
        self.verify_by_comparing_text(locator=self._actual_result_create, locator_type="xpath", expected_result=self.
                                      expected_result_create, result_msg="Interaction Not Created")

    def verify_edit_interaction(self):
        self.verify_by_comparing_text(locator=self._actual_result_edit, locator_type="xpath", expected_result=self.
                                      expected_result_edit, result_msg="Interaction Not Updated")

    def verify_report_interaction(self):
        self.verify_by_comparing_text(locator=self._actual_result_report, locator_type="xpath", expected_result=self.
                                      expected_result_report, result_msg="Interaction Not Reported")

    def verify_delete_interaction(self):
        self.verify_by_comparing_text(locator=self._actual_result_delete, locator_type="xpath", expected_result=self.
                                      expected_result_delete, result_msg="Interaction Not Deleted")

    def verify_comment_interaction(self):
        self.verify_by_comparing_text(locator=self._actual_result_comment, locator_type="xpath", expected_result=self.
                                      expected_result_comment, result_msg="Interaction Not Commented")
























