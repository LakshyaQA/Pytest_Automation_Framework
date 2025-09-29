import time

from Common_Packages.Base.basepage import Basepage
import Common_Packages.Utility.custom_logger as cl


class ReportPage(Basepage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _heading_reports = "//h5[contains(text(), 'Reports')]"
    _report_type_dropdown = ("//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input "
                             "MuiOutlinedInput-input css-ok94iy']")
    _select_candidates = "//li[@data-value='Candidates']"
    _select_employees = "//li[@data-value='Employees']"
    _select_job_posting = "//li[@data-value='Job Postings']"
    _date_from = ("//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd "
                  "MuiIconButton-sizeMedium css-pofinn'][1]")
    _month_year = "//div[@class='MuiPickersCalendarHeader-label css-1v994a0']"
    _select_date_from = "//button[contains(text(), '1')]"
    _date_to = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd "
                "MuiIconButton-sizeMedium css-pofinn'])[2]")
    _select_date_to = "//button[contains(text(), '31')]"
    _status_dropdown = "(//div[@role='combobox'])[2]"
    _generate_report_button = "//button[contains(text(), 'Generate Report')]"
    _column_heading = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1f53gjv']"
    _email_report_button = "//button[contains(text(), 'Email Report')]"
    _download_report_button = "//button[contains(text(), 'Download Report')]"
    _email_field = "//input[@type='email']"
    _send_button = "//button[@type='submit']"
    _confirmation_msg = "//div[contains(text(), 'Reports sent to your email successfully.')]"

    def report_type(self):
        self.wait_for_element(self._report_type_dropdown, locator_type="xpath")
        self.element_click(self._report_type_dropdown, locator_type="xpath")

    def select_candidate(self):
        self.wait_for_element(self._select_candidates, locator_type="xpath")
        self.element_click(self._select_candidates, locator_type="xpath")

    def select_employees(self):
        self.wait_for_element(self._select_employees, locator_type="xpath")
        self.element_click(self._select_employees, locator_type="xpath")

    def select_job_postings(self):
        self.wait_for_element(self._select_job_posting, locator_type="xpath")
        self.element_click(self._select_job_posting, locator_type="xpath")

    def select_date_from(self, fromday, fromyear):
        self.wait_for_element(self._date_from, locator_type="xpath")
        self.element_click_js(self._date_from, locator_type="xpath")
        self.wait_for_element(self._month_year, locator_type="xpath")
        self.element_click(self._month_year, locator_type="xpath")
        _year1 = "//button[contains(text(), '" + fromyear + "')]"
        _day1 = "//button[contains(text(), '" + fromday + "')]"
        self.wait_for_element(_year1, "xpath")
        self.element_click_js(_year1, "xpath")
        self.wait_for_element(_day1, "xpath")
        self.element_click_js(_day1, "xpath")

    def select_date_to(self, to_day, to_year):
        self.wait_for_element(self._date_to, locator_type="xpath")
        self.element_click_js(self._date_to, locator_type="xpath")
        self.wait_for_element(self._month_year, locator_type="xpath")
        self.element_click(self._month_year, locator_type="xpath")
        _year2 = "//button[contains(text(), '" + to_year + "')]"
        _day2 = "//button[contains(text(), '" + to_day + "')]"
        self.wait_for_element(_year2, "xpath")
        self.element_click_js(_year2, "xpath")
        self.wait_for_element(_day2, "xpath")
        self.element_click_js(_day2, "xpath")

    def select_status(self, option):
        self.wait_for_element(self._status_dropdown, locator_type="xpath")
        self.element_click(self._status_dropdown, locator_type="xpath")
        _status = "//li[contains(text(), '" + option + "')]"
        self.wait_for_element(_status, "xpath")
        self.element_click_js(_status, "xpath")

    def select_report_type(self, report_option):
        self.wait_for_element(self._report_type_dropdown, locator_type="xpath")
        self.element_click(self._report_type_dropdown, locator_type="xpath")
        _report = "//li[contains(text(), '" + report_option + "')]"
        self.wait_for_element(_report, locator_type="xpath")
        self.element_click_js(_report, locator_type="xpath")

    def generate_report_button(self):
        self.wait_for_element(self._generate_report_button, locator_type="xpath")
        self.element_click(self._generate_report_button, locator_type="xpath")

    def email_report(self):
        self.wait_for_element(self._email_report_button, locator_type="xpath")
        self.element_click(self._email_report_button, locator_type="xpath")

    def download_report(self, save):
        self.wait_for_element(self._download_report_button, locator_type="xpath")
        self.select_element_keyboard(save, self._download_report_button, locator_type="xpath")

    def enter_email(self, email1):
        self.wait_for_element(self._email_field, locator_type="xpath")
        self.element_click(self._email_field, locator_type="xpath")
        self.send_keys(email1, self._email_field, locator_type="xpath")

    def send(self):
        self.wait_for_element(self._send_button, locator_type="xpath")
        self.element_click(self._send_button, locator_type="xpath")

    def generate_report_candidate(self, email1):
        self.report_type()
        self.select_candidate()
        self.generate_report_button()
        self.email_report()
        self.sendkeys_multi_value(email1, self._email_field, locator_type="xpath")
        self.send()
        self.wait_for_element(self._confirmation_msg, locator_type="xpath")
        return self.get_text(self._confirmation_msg, locator_type="xpath")

    def generate_report_employees(self, email1):
        self.report_type()
        self.select_employees()
        self.generate_report_button()
        self.email_report()
        self.sendkeys_multi_value(email1, self._email_field, locator_type="xpath")
        self.send()
        self.wait_for_element(self._confirmation_msg, locator_type="xpath")
        return self.get_text(self._confirmation_msg, locator_type="xpath")

    def generate_report_job_postings(self, date_from, date_to, option, email_id):
        self.report_type()
        self.select_job_postings()
        day1, month1, year1 = self.split_text(date_from, "/")
        day2, month2, year2 = self.split_text(date_to, "/")
        self.select_date_from(day1, year1)
        time.sleep(2)
        self.select_date_to(day2, year2)
        self.select_status(option)
        self.generate_report_button()
        self.email_report()
        self.sendkeys_multi_value(email_id, self._email_field, locator_type="xpath")
        self.send()
        self.wait_for_element(self._confirmation_msg, locator_type="xpath")
        return self.get_text(self._confirmation_msg, locator_type="xpath")






