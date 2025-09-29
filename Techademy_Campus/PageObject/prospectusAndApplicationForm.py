from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl
import time
from Common_Packages.resources.ConfigPath import UploadFile
from Techademy_Campus.Configuration.readProperties import ReadConfig


class ProspectusAndApplicationForm(Basepage):
    log = cl.custom_logger()

    '''
         This Prospectus and Application form is for  creating a prospectus and application form in registrar role 

          author : Meghana Avinash Kadam 

    '''


    search_value = ReadConfig.get_prospectus_and_application_form('Prospectus And Application Form',
                                                                  'search_textbox')
    prospectus_fee_value = ReadConfig.get_prospectus_and_application_form('Prospectus And Application Form',
                                                                          'Prospectus_fee_textbox')
    application_form_title_value = ReadConfig.get_prospectus_and_application_form('Prospectus And Application Form',
                                                                                  'application_form_title')
    application_description_value = ReadConfig.get_prospectus_and_application_form('Prospectus And Application Form',

                                                                                   'application_description')
    textbox_value = ReadConfig.get_prospectus_and_application_form('Prospectus And Application Form', 'textbox')
    email_id_value = ReadConfig.get_prospectus_and_application_form('Prospectus And Application Form',
                                                                    'email_id_textbox')
    description_value = ReadConfig.get_prospectus_and_application_form('Prospectus And Application Form',
                                                                       'description_textbox')
    fee_value = ReadConfig.get_prospectus_and_application_form('Prospectus And Application Form', 'fee')
    expected_result_create = ReadConfig.get_expected_result('Expected Results', 'create_prospectus_form')
    path = UploadFile.file_upload_path('Pdf (1).pdf')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _manage_tab = "//button[text()='Manage']"
    _prospectus_and_application_tab = "//span[text()='Prospectus and Application form']"
    _search = "//input[@placeholder='Search...']"
    _add_new_button = "//button[text()='+ Add New']"
    _cluster = "//div[@name='ClusterId']"
    _cluster_name = "//li[text()='Engineering']"
    _department = "//div[@name='DepartmentId']"
    _department_name = "//li[text()='Marine Engineering']"
    _select_program = "//div[@name='course_id']"
    _select_program_name = "//li[text()='Test']"
    _prospectus_fee = "//input[@name='prospectus_fee']"
    _browse = "//label[text()='Browse']"
    _preview = "//button[text()='Preview']"
    _close_icon = ("//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium qa-close-icon "
                   "css-logsyf']")
    _save_and_next = "//button[text()='Save and Next']"
    _application_form_title = "//input[@name='formTitle']"
    _application_description = "//textarea[@name='formDescription']"
    _enter_details = "//input[@name='fields[0].heading']"
    _select_type = "//input[@name='fields[0].type']"
    _type_name = "//li[text()='Email']"
    _textbox = ("(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall "
                "css-1blbzq8'])[3]")
    _description_textbox = "//input[@name='feesSections[0].description']"
    _fee = "//input[@name='feesSections[0].fee']"
    _publish = "//button[text()='Publish']"
    _cancel = "//button[text()='Cancel']"
    _actual_result = "//div[text()='Course Prospectus form published.']"


    def click_on_manage(self):
        self.wait_for_element(self._manage_tab, locator_type="xpath")
        self.element_click(self._manage_tab, "xpath")

    def click_on_prospectus_and_application_form(self):
        self.wait_for_element(self._prospectus_and_application_tab, locator_type="xpath")
        self.element_click(self._prospectus_and_application_tab, "xpath")

    def enter_search(self, search_textbox):
        self.wait_for_element(self. _search, locator_type="xpath")
        self.element_click(self. _search, "xpath")
        self.send_keys(search_textbox, self._search, "xpath")

    def click_on_add_new_button(self):
        self.wait_for_element(self. _add_new_button, locator_type="xpath")
        self.element_click(self. _add_new_button, "xpath")

    def click_on_cluster(self):
        # self.waitForElement(self._cluster, locator_type="xpath")
        self.element_click_js(self._cluster, "xpath")
        self.wait_for_element(self._cluster_name, locator_type="xpath")
        self.element_click(self._cluster, "xpath")
        self.element_click_js(self._cluster_name, "xpath")


    def click_on_department(self):
        # self.waitForElement(self._department, locator_type="xpath")
        self.element_click_js(self._department, "xpath")
        self.wait_for_element(self._department_name, locator_type="xpath")
        self.element_click(self._department, "xpath")
        self.element_click_js(self._department_name, "xpath")

    def click_on_program(self):
        # self.waitForElement(self._select_program, locator_type="xpath")
        self.element_click_js(self._select_program, "xpath")
        self.wait_for_element(self._select_program_name, locator_type="xpath")
        self.element_click(self._select_program, "xpath")
        self.element_click_js(self. _select_program_name, "xpath")

    def enter_prospectus_fee(self, Prospectus_fee_textbox):
        # self.waitForElement(self._prospectus_fee, locator_type="xpath")
        self.element_click_js(self._prospectus_fee, "xpath")
        self.send_keys(Prospectus_fee_textbox, self._prospectus_fee, "xpath")

    def click_on_browse(self, path):
        self.element_click(self._browse, "xpath")
        time.sleep(1)
        self.upload_file(path, self._browse, locator_type="xpath")
        time.sleep(1)


    def click_on_preview(self):
        # self.waitForElement(self._preview, locator_type="xpath")
        self.element_click(self._preview, "xpath")

    def click_on_close_icon(self):
        self.wait_for_element(self._close_icon, locator_type="xpath")
        self.element_click(self._close_icon, "xpath")

    def click_on_save_and_next(self):
        # self.waitForElement(self. _save_and_next, locator_type="xpath")
        self.element_click_js(self. _save_and_next, "xpath")

    def enter_application_form_title(self, application_form_title):
        # self.waitForElement(self. _application_form_title, locator_type="xpath")
        self.element_click(self. _application_form_title, "xpath")
        self.send_keys(application_form_title, self._application_form_title, "xpath")


    def enter_application_form_description(self, application_description):
        # self.waitForElement(self. _application_description, locator_type="xpath")
        self.element_click(self._application_description, "xpath")
        self.send_keys(application_description, self._application_description, "xpath")

    def enter_text(self, textbox):
        # self.waitForElement(self. _enter_details, locator_type="xpath")
        self.element_click_js(self. _enter_details, "xpath")
        self.send_keys(textbox, self._enter_details, "xpath")

    def click_on_select_type(self):
        # self.waitForElement(self. _select_type, locator_type="xpath")
        self.element_click_js(self. _select_type, "xpath")
        self.element_click_js(self._type_name, "xpath")

    def enter_email_id(self, email_id_textbox):
        # self.waitForElement(self. _textbox, locator_type="xpath")
        self.element_click_js(self. _textbox, "xpath")
        self.send_keys(email_id_textbox, self._textbox, "xpath")

    def enter_description_textbox(self, description_textbox):
        self.wait_for_element(self._description_textbox, locator_type="xpath")
        self.element_click_js(self._description_textbox, "xpath")
        self.send_keys(description_textbox, self._description_textbox, "xpath")

    def enter_fee(self, fee):
        self.wait_for_element(self._fee, locator_type="xpath")
        self.element_click_js(self._fee, "xpath")
        self.send_keys(fee, self._fee, "xpath")

    def click_on_publish(self):
        self.wait_for_element(self. _publish, locator_type="xpath")
        self.element_click_js(self._publish, "xpath")

    def click_on_cancel(self):
        self.wait_for_element(self. _cancel, locator_type="xpath")
        self.element_click_js(self. _cancel, "xpath")

    def search(self):
        self.click_on_manage()
        self.click_on_prospectus_and_application_form()
        self.enter_search(self.search_value)


    def creation_prospectus_and_application_form(self):
        self.click_on_manage()
        self.click_on_prospectus_and_application_form()
        self.click_on_add_new_button()
        self.click_on_cluster()
        self.click_on_department()
        self.click_on_program()
        self.enter_prospectus_fee(self.prospectus_fee_value)
        self.click_on_browse(self.path)
        self.click_on_preview()
        time.sleep(1)
        self.click_on_close_icon()
        self.click_on_save_and_next()
        time.sleep(2)
        self.enter_application_form_title(self.application_form_title_value)
        self.enter_application_form_description(self.application_description_value)
        self.web_scroll("down")
        self.enter_text(self.textbox_value)
        self.click_on_select_type()
        self.enter_email_id(self.email_id_value)
        self.click_on_save_and_next()
        time.sleep(2)
        self.enter_description_textbox(self.description_value)
        self.enter_fee(self.fee_value)
        self.click_on_save_and_next()
        time.sleep(3)
        self.web_scroll("down")
        self.click_on_publish()
        self.verify_create_prospectus_and_application_form()
        time.sleep(2)
        # self.click_on_cancel()


    def verify_create_prospectus_and_application_form(self):
        self.verify_by_comparing_text(locator=self._actual_result, locator_type="xpath",
                                      expected_result=self.expected_result_create,
                                      result_msg="Prospectus Form Not Created")























