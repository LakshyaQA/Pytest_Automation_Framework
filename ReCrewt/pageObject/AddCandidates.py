import Common_Packages.Utility.custom_logger as cl

from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class AddCandidates(Basepage):
    log = cl.custom_logger()
    path = UploadFile.upload_pdf()


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _first_name = "//*[@name='first_name']"
    _last_name = "//*[@name='last_name']"
    _gender_dropdown = "(//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-feqhe6'])[3]"
    _date_of_birth = "(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1b6xge3'])[2]"
    _preferred_location = "(//input[@class='MuiInputBase-input MuiOutlinedInput-input css-39zpkw'])[3]"
    _email_id = "//*[@name='email_id']"
    _phone_no = "//*[@name='phone_number']"
    _tech_skills = "(//input[@class='MuiInputBase-input MuiOutlinedInput-input css-39zpkw'])[6]"
    _current_role = "//*[@name='job_role']"
    _year = "//*[@name='year']"
    _month = "//*[@name='month']"
    _upload_resume = "//input[@type ='file']"
    _upload_resume1 = "//h6[@class='MuiTypography-root MuiTypography-subtitle1 css-ffxjtb']"
    _submit_btn = "//button[normalize-space()='Submit']"
    _cancel_btn = "//button[normalize-space()='Cancel']"
    _actual_result = "//div[@id = 'notistack-snackbar']"
    _dob_clear = "//*[local-name() = 'svg' and @data-testid='ClearIcon']"
    _dob_icon = "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-pofinn'])[2]"
    _month_year = "//div[@class='MuiPickersCalendarHeader-label css-1v994a0']"

    def enter_firstname(self, f_name):
        self.element_click_js(self._first_name, "xpath")
        self.send_keys(f_name, self._first_name, "xpath")

    def enter_lastname(self, l_name):
        self.element_click_js(self._last_name, "xpath")
        self.send_keys(l_name, self._last_name, "xpath")

    def select_gender(self, gender):
        self.wait_for_element(self._gender_dropdown, "xpath")
        self.element_click(self._gender_dropdown, "xpath")
        options = "//ul//li[contains(text(), '" + gender +"')]"
        self.wait_for_element(options, "xpath")
        self.element_click_js(options, "xpath")

    def enter_dob(self, day, year):
        self.wait_for_element(self._dob_icon, "xpath")
        self.element_click_js(self._dob_icon, "xpath")
        self.wait_for_element(self._month_year, "xpath")
        self.element_click_js(self._month_year, "xpath")
        _dob_year = "//button[contains(text(), '" + year + "')]"
        _dob_day = "//button[contains(text(), '" + day + "')]"
        self.wait_for_element(_dob_year, "xpath")
        self.element_click_js(_dob_year, "xpath")
        self.wait_for_element(_dob_day, "xpath")
        self.element_click_js(_dob_day, "xpath")

    def select_location(self, locate):
        self.sendkeys_multi_value(locate, self._preferred_location, "xpath")

    def enter_emai(self, email_id):
        self.element_click_js(self._email_id, "xpath")
        self.send_keys(email_id, self._email_id, "xpath")

    def enter_phone_no(self, phone_no):
        self.element_click_js(self._phone_no, "xpath")
        self.send_keys(phone_no, self._phone_no, "xpath")

    def enter_skills(self, skills):
        self.sendkeys_multi_value(skills, self._tech_skills, "xpath")

    def enter_role(self, role):
        self.send_keys(role, self._current_role, "xpath")

    def enter_year(self, year):
        self.wait_for_element(self._year, "xpath")
        self.element_click_js(self._year, "xpath")
        self.send_keys(year, self._year, "xpath")

    def enter_month(self, month):
        self.wait_for_element(self._month, "xpath")
        self.element_click_js(self._month, "xpath")
        self.send_keys(month, self._month, "xpath")

    def upload_resume(self, path):
        self.wait_for_element(self._upload_resume, locator_type="xpath")
        self.send_keys(UploadFile.upload_pdf(), self._upload_resume, locator_type="xpath")


    def click_cancel(self):
        self.wait_for_element(self._cancel_btn, "xpath")
        self.element_click_js(self._cancel_btn, "xpath")

    def click_on_submit(self):
        self.wait_for_element(self._submit_btn, "xpath")
        self.element_click_js(self._submit_btn, "xpath")

    def add_candidate(self, first_name, last_name, gender, dob, location, email, mobile, skills, role, exp_year, exp_month):
        self.enter_firstname(first_name)
        self.enter_lastname(last_name)
        self.select_gender(gender)
        day, month, year = self.split_text(dob, "/")
        self.enter_dob(day, year)
        self.select_location(location)
        self.enter_emai(email)
        self.enter_phone_no(mobile)
        self.enter_skills(skills)
        self.enter_role(role)
        self.enter_year(exp_year)
        self.enter_month(exp_month)
        self.upload_resume(UploadFile.upload_pdf())
        self.click_on_submit()
        self.wait_for_page_load()
        self.wait_for_element(self._actual_result, locator_type="xpath")
        return self.get_text(self._actual_result, locator_type="xpath")

