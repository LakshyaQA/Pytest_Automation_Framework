import time

from Common_Packages.Base.basepage import Basepage
from ReCrewt.configuration.readProperties import ReadConfig
import Common_Packages.Utility.custom_logger as cl


class PostAJob(Basepage):
    log = cl.custom_logger()


    def __init__(self, driver):
       super().__init__(driver)
       self.driver = driver

    LOI_para = """Dear {Candidate Name},
    We are pleased to extend this Letter of Intent to offer you the position of [Position Title] at [Your Company Name]. After careful consideration of your qualifications, experience, and suitability for the role, we are confident that your skills and expertise will be valuable assets to our team.
    This Letter of Intent outlines the key terms and conditions of our offer:
    Position: You will be hired as a [Position Title], reporting to [Supervisor/Manager's Name].
    Start Date: Your anticipated start date will be [Date].
    Compensation: Your starting salary will be [Salary Amount] per [year/month/week], with [details of any additional benefits or perks, if applicable].
    Work Schedule: Your regular work hours will be [Hours] per [day/week], with [details of any flexibility or remote work options, if applicable].
    Probationary Period: You will be subject to a probationary period of [duration], during which time your performance will be evaluated.
    Employment Status: This offer of employment is contingent upon the successful completion of [any necessary background checks, drug tests, or other pre-employment requirements].
    Please note that this Letter of Intent is not intended to be a legally binding contract and is subject to the execution of a formal employment agreement, which will include more detailed terms and conditions of employment.
    We kindly request your acknowledgment and acceptance of this Letter of Intent by [insert deadline, if applicable]. If you have any questions or require further clarification regarding the terms outlined herein, please do not hesitate to contact us.
    We are excited about the possibility of you joining our team at [Your Company Name] and contributing to our continued success. Thank you for considering this opportunity, and we look forward to your positive response.
    Sincerely,
    {User Name}"""
    #Locators
    _heading_postajob = "//h3[contains(text(), 'Post')]"
    _job_title = "//input[@name = 'job_title']"
    _location = "//input[@name = 'location']"
    _description = "//textarea[@name = 'description']"
    _job_type_dropdown = "//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-17ajz8m']"
    _department = "//input[@name = 'department']"
    _no_of_position = "//input[@name = 'no_of_positions']"
    _min_experience = "//input[@name = 'min_experience']"
    _max_experience = "//input[@name = 'max_experience']"
    _education = "//input[@name = 'education_details']"
    _technical_skills = "(//input[@placeholder='Press Enter to add skill'])[1]"
    _nontechnical_skills = "(//input[@placeholder='Press Enter to add skill'])[2]"
    _min_compensation = "//input[@name = 'min_compensation']"
    _max_compensation = "//input[@name = 'max_compensation']"
    _other = "//textarea[@name='other']"
    _requestedby_dropdown = "//input[@role='combobox']"
    _end_date = ("//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary "
                 "MuiInputBase-formControl MuiInputBase-adornedEnd css-uc6xwg']")
    _save = "//button[contains(text(), 'Save & Continue')]"
    _work_from_office = "//li[contains(text(), 'Work from Office')]"
    _work_from_home = "//li[contains(text(), 'Work from Home')]"
    _hybrid = "//li[contains(text(), 'Hybrid')]"
    _calender = "(//*[name() = 'svg' and @class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[4]"
    _monthyear = "//div[@class='MuiPickersCalendarHeader-label css-1v994a0']"
    _licence_validate = "//div[@id='notistack-snackbar' and contains(text(), 'License validated !')]"
    _actual_result = "//div[@id='notistack-snackbar']"
    _detail_description = "//div[@class='ql-editor ql-blank']"
    _second_step = "(//span[@class='MuiStepLabel-iconContainer MuiStepLabel-alternativeLabel css-a5nipc'])[1]"
    _third_step = "(//span[@class='MuiStepLabel-iconContainer MuiStepLabel-alternativeLabel css-a5nipc'])[2]"
    _delete_step = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-ab19sr']//img[@src='/assets/ico-delete-f17da7b9.svg']"
    _no_step_added = "//h5[contains(text(), 'No Steps added yet')]"
    _add_step = "//button[contains(text(), 'Add Process Steps')]"
    _add_assessment = "//p[text() = 'Assessment']//parent::div//label"
    _add_ai_assessment = "//p[text() = 'AI Based Assessment']//parent::div//label"
    _add_gd = "//p[text() = 'Group Discussion']//parent::div//label"
    _add_LOI = "//p[text() = 'Letter of Intent']//parent::div//label"
    _add_interview = "//p[text() = 'Interview']//parent::div//label"
    _select = "//button[contains(text(), 'Select')]"
    _weightage = "(//div//input[@type = 'number'])"
    _continue = "//button[contains(text(), 'Continue')]"
    _forth_step = "(//span[@class='MuiStepLabel-iconContainer MuiStepLabel-alternativeLabel css-a5nipc'])[3]"
    _skills_toggle = "//span[@class='MuiButtonBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary PrivateSwitchBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary css-so683j']"
    _scroll_bar = "//span[@data-index='4']"
    _publish = "//button[contains(text(), 'Publish')]"
    _Job_publish_confirmation = "//div[contains(text(), 'Posted Job Successfully')]"
    _fifth_step = "(//span[@class='MuiStepLabel-iconContainer MuiStepLabel-alternativeLabel css-a5nipc'])[4]"
    _manual_desc = "//p[contains(text(), 'Manually Enter')]//parent::div//parent::div[@class='MuiStack-root css-mvrtzj']"
    _validation = "//div[@id='notistack-snackbar']"
    _sendApproval = "//button[contains(text() , 'Send for Approval')]"
    _sendApprovalRequest = "//button[contains(text(), 'Send Approval Request')]"
    _approval_ativated = "//div[contains(text(), 'Approval Activated']"
    _approval_sent_confirmation = "//h5[contains(text(), 'Your approval request sent successfully')]"
    _close = "//button[contains(text() , 'Close')]"
    _loader = "//div[@class='MuiBackdrop-root loader css-xuaqpw']"
    _configure_AIAssessment = "(//p[text() = 'AI Based Assessment']//parent::div//div//button)[1]"
    _configure_Assessment = "(//p[text() = 'Assessment']//parent::div//div//button)[1]"
    _ai_assessment_label = "(//input[@placeholder='Enter label..'])[2]"
    _ai_assessment_name = "//input[@name='assessment_name']"
    _ai_category_name = "(//div[@role='combobox'])[1]"
    _ai_skill_name = "(//div[@role='combobox'])[2]"
    _ai_sub_skill_name = "(//div[@role='combobox'])[3]"
    _ai_number_que = "//input[ @ name = 'number_of_questions']"
    _ai_save = "(//button[text() = 'Save'])[1]"
    _ai_category_type = "//li[@data-value='Testing']"
    _ai_skill_type = "//li[@data-value='Java']"
    _ai_sub_skill_type = "//li[@data-value='API']"
    _assessment_label = "(//input[@placeholder='Enter label..'])[3]"
    _category = "(// div[@ role='combobox'])[4]"
    _category_option = "//li[text() = 'Testing']"
    _assessment_select = "//button[text() = 'Select']"
    _assessment_attemptes = "//input[@name='attemptsAllowed']"
    _assessment_passing = "//input[@name='passingPercentage']"
    _assessment_duration = "//input[@name='assessmentDuration']"
    _assessment_save = "(//button[contains(text(), 'Save')])[3]"
    _configure_LOI = "(//p[text() = 'Letter of Intent']//parent::div//div//button)[1]"
    _LOI_email = "(//div[@class='ql-editor ql-blank'])[1]"
    _LOI_letter = "(//div[@class='ql-editor ql-blank'])[2]"
    _LOI_save = "(//button[contains(text(), 'Save')])[2]"
    _edit = "//button[contains(text(), 'Edit')]"
    _approval = "(//span[@class='MuiStepLabel-root MuiStepLabel-horizontal MuiStepLabel-alternativeLabel css-1abj2s5'])[6]"
    _publish_job_expected_result = "(//div[@id='notistack-snackbar'])[2]"















    def enter_job_title(self, job_title):
        self.wait_for_element(self._job_title, locator_type="xpath")
        self.send_keys(job_title, self._job_title, locator_type="xpath")

    def enter_location(self, location):
        self.wait_for_element(self._location, locator_type="xpath")
        self.send_keys(location, self._location, locator_type="xpath")

    def enter_description(self, description):
        self.wait_for_element(self._description, locator_type="xpath")
        self.send_keys(description, self._description, locator_type="xpath")

    def enter_job_type(self, job_type):
        self.wait_for_element(self._job_type_dropdown, locator_type="xpath")
        self.element_click(self._job_type_dropdown, locator_type="xpath")
        _jobtypeoption = "//li[contains(text(), '" + job_type + "')]"
        self.element_click(_jobtypeoption, locator_type="xpath")

    def enter_deparment(self, department):
        self.wait_for_element(self._department, locator_type="xpath")
        self.send_keys(department, self._department, locator_type="xpath")

    def enter_no_of_position(self, no_of_position):
        self.wait_for_element(self._no_of_position, locator_type="xpath")
        self.send_keys(no_of_position, self._no_of_position, locator_type="xpath")

    def enter_min_experiance(self, min_experience):
        self.wait_for_element(self._min_experience, locator_type="xpath")
        self.send_keys(min_experience, self._min_experience, locator_type="xpath")

    def enter_max_experiance(self, max_experience):
        self.wait_for_element(self._max_experience, locator_type="xpath")
        self.send_keys(max_experience, self._max_experience, locator_type="xpath")

    def enter_education(self, education):
        self.wait_for_element(self._education, locator_type="xpath")
        self.send_keys(education, self._education, locator_type="xpath")

    def enter_technical_skills(self, technical_skills):
        self.wait_for_element(self._technical_skills, locator_type="xpath")
        self.sendkeys_multi_value(technical_skills, self._technical_skills, locator_type="xpath")

    def enter_non_technical_skills(self, non_technical_skills):
        self.wait_for_element(self._nontechnical_skills, locator_type="xpath")
        self.sendkeys_multi_value(non_technical_skills, self._nontechnical_skills, locator_type="xpath")

    def enter_min_compensation(self, min_compensation):
        self.wait_for_element(self._min_compensation, locator_type="xpath")
        self.send_keys(min_compensation, self._min_compensation, locator_type="xpath")

    def enter_max_compensation(self, max_compesation):
        self.wait_for_element(self._max_compensation, locator_type="xpath")
        self.send_keys(max_compesation, self._max_compensation, locator_type="xpath")

    def enter_other(self, other):
        self.wait_for_element(self._other, locator_type="xpath")
        self.send_keys(other, self._other, locator_type="xpath")

    def enter_requested_by(self, requested_by):
        self.wait_for_element(self._requestedby_dropdown, locator_type="xpath")
        self.element_click(self._requestedby_dropdown, locator_type="xpath")
        _requestedbyoption = "//*[contains(text(), '" + requested_by + "')]"
        self.element_click(_requestedbyoption, locator_type="xpath")

    def enter_end_date(self, day, month, year):
        self.wait_for_element(self._end_date, locator_type="xpath")
        self.element_click(self._calender, locator_type="xpath")
        self.wait_for_element(self._monthyear, locator_type="xpath")
        self.element_click(self._monthyear, locator_type="xpath")
        _year = "//button[contains(text(), '" + year + "')]"
        self.wait_for_element(_year, locator_type="xpath")
        self.element_click(_year, locator_type="xpath")
        _day = "//button[contains(text(), '" + day + "')]"
        self.wait_for_element(_day, locator_type="xpath")
        self.element_click(_day, locator_type="xpath")

    def save_job(self):
        self.wait_for_element(self._save, locator_type="xpath")
        self.element_click(self._save, locator_type="xpath")

    def click_manualJD(self):
        self.wait_for_element(self._manual_desc, locator_type="xpath")
        self.element_click_js(self._manual_desc, locator_type="xpath")

    def edite_detail_description(self, detail_description):
        self.wait_for_element(self._detail_description, locator_type="xpath")
        self.send_keys(detail_description, self._detail_description, locator_type="xpath")
        self.save_job()
        self.wait_for_page_load()
        self.wait_for_element(self._actual_result, locator_type="xpath")
        return self.get_text(self._actual_result, locator_type="xpath")

    def setup_hiring_flow_delete_steps(self):
        condition = True

        while not (self.is_element_displayed(self._no_step_added, "xpath")):
            self.wait_for_element(self._delete_step, locator_type="xpath")
            self.element_click_js(self._delete_step, locator_type="xpath")
            self.wait_for_page_load()

            if (self.is_element_displayed(self._no_step_added, "xpath")):
                condition = False

        self.wait_for_element(self._no_step_added, "xpath")
        return self.get_text(self._no_step_added, "xpath")

    def click_add_steps(self):
        self.wait_for_element(self._add_step, locator_type="xpath")
        self.element_click(self._add_step, locator_type="xpath")
        self.wait_for_page_load()

    def click_assessment_checkbox(self):
        self.wait_for_element(self._add_assessment, locator_type="xpath")
        self.element_click_js(self._add_assessment, locator_type="xpath")
        self.wait_for_page_load()

    def click_ai_assessment_checkbox(self):
        self.wait_for_element(self._add_ai_assessment, locator_type="xpath")
        self.element_click_js(self._add_ai_assessment, locator_type="xpath")
        self.wait_for_page_load()

    def click_interview_checkbox(self):
        self.wait_for_element(self._add_interview, locator_type="xpath")
        self.element_click_js(self._add_interview, locator_type="xpath")
        self.wait_for_page_load()

    def click_gd_checkbox(self):
        self.wait_for_element(self._add_gd, locator_type="xpath")
        self.element_click_js(self._add_gd, locator_type="xpath")
        self.wait_for_page_load()

    def click_LOI_checkbox(self):
        self.wait_for_element(self._add_LOI, locator_type="xpath")
        self.element_click_js(self._add_LOI, locator_type="xpath")
        self.wait_for_page_load()

    def click_select(self):
        self.wait_for_element(self._select, locator_type="xpath")
        self.element_click_js(self._select, locator_type="xpath")
        self.wait_for_page_load()

    def enter_waightage(self):
        self.wait_for_element(self._weightage, "xpath")
        self.send_keys("25", self._weightage + "[2]", "xpath")
        self.wait_for_element(self._weightage, "xpath")
        self.send_keys("25", self._weightage + "[4]", "xpath")
        self.wait_for_element(self._weightage, "xpath")
        self.send_keys("25", self._weightage + "[6]", "xpath")
        self.wait_for_element(self._weightage, "xpath")
        self.send_keys("25", self._weightage + "[8]", "xpath")


    def enter_cutOff(self):
        self.wait_for_element(self._weightage, "xpath")
        self.send_keys("10", self._weightage + "[1]", "xpath")
        self.wait_for_element(self._weightage, "xpath")
        self.send_keys("10", self._weightage + "[3]", "xpath")
        self.wait_for_element(self._weightage, "xpath")
        self.send_keys("10", self._weightage + "[5]", "xpath")
        self.wait_for_element(self._weightage, "xpath")
        self.send_keys("10", self._weightage + "[7]", "xpath")

    def click_continue(self):
        self.wait_for_element(self._continue, locator_type="xpath")
        self.element_click_js(self._continue, locator_type="xpath")
        self.wait_for_page_load()

    def click_skill_toggle(self):
        self.wait_for_element(self._skills_toggle, locator_type="xpath")
        self.element_click_js(self._skills_toggle, locator_type="xpath")

    def click_scroll_bar(self):
        self.wait_for_element(self._scroll_bar, locator_type="xpath")
        self.element_click(self._scroll_bar, locator_type="xpath")

    def publish_job_post(self):
        self.wait_for_element(self._edit, locator_type="xpath")
        self.element_click_js(self._edit, locator_type="xpath")
        self.wait_for_page_load()
        self.wait_for_element(self._approval, locator_type="xpath")
        self.element_click_js(self._approval, locator_type="xpath")
        self.wait_for_page_load()
        self.wait_for_element(self._publish, locator_type="xpath")
        self.element_click_js(self._publish, locator_type="xpath")
        self.wait_for_page_load()
        self.wait_for_element(self._publish_job_expected_result, "xpath")
        return self.get_text(self._publish_job_expected_result, "xpath")

    def click_send_approval(self):
        self.wait_for_element(self._sendApproval, locator_type="xpath")
        self.element_click_js(self._sendApproval, locator_type="xpath")
        self.wait_for_page_load()

    def click_send_approval_request(self):
        self.wait_for_element(self._sendApprovalRequest, locator_type="xpath")
        self.element_click_js(self._sendApprovalRequest, locator_type="xpath")
        self.wait_for_page_load()

    def click_close(self):
        self.wait_for_element(self._close, locator_type="xpath")
        self.element_click_js(self._close, locator_type="xpath")
        self.wait_for_page_load()

    def set_AIassessment(self):
        self.wait_for_element(self._configure_AIAssessment, locator_type="xpath")
        self.element_click_js(self._configure_AIAssessment, locator_type="xpath")
        self.wait_for_element(self._ai_assessment_label, locator_type="xpath")
        self.send_keys("AI Assessment", self._ai_assessment_label, locator_type="xpath")
        self.wait_for_element(self._ai_assessment_name, locator_type="xpath")
        self.send_keys("AI Assessment", self._ai_assessment_name, locator_type="xpath")
        self.wait_for_element(self._ai_category_name, locator_type="xpath")
        self.element_click(self._ai_category_name, locator_type="xpath")
        self.wait_for_element(self._ai_category_type, locator_type="xpath")
        self.element_click(self._ai_category_type, locator_type="xpath")
        time.sleep(1)
        self.wait_for_element(self._ai_skill_name, locator_type="xpath")
        self.element_click(self._ai_skill_name, locator_type="xpath")
        self.wait_for_element(self._ai_skill_type, locator_type="xpath")
        self.element_click(self._ai_skill_type, locator_type="xpath")
        time.sleep(1)
        self.wait_for_element(self._ai_sub_skill_name, locator_type="xpath")
        self.element_click(self._ai_sub_skill_name, locator_type="xpath")
        self.wait_for_element(self._ai_sub_skill_type, locator_type="xpath")
        self.element_click(self._ai_sub_skill_type, locator_type="xpath")
        self.wait_for_element(self._ai_number_que, locator_type="xpath")
        self.send_keys("10", self._ai_number_que, locator_type="xpath")
        self.element_click(self._ai_save, "xpath")

    def set_assessment(self):
        self.wait_for_element(self._configure_Assessment, locator_type="xpath")
        self.element_click_js(self._configure_Assessment, locator_type="xpath")
        self.wait_for_element(self._assessment_label, locator_type="xpath")
        self.send_keys("Assessment", self._assessment_label, locator_type="xpath")
        self.wait_for_element(self._category, locator_type="xpath")
        self.element_click(self._category, locator_type="xpath")
        self.wait_for_element(self._category_option, locator_type="xpath")
        self.element_click(self._category_option, locator_type="xpath")
        self.wait_for_element(self._assessment_select, locator_type="xpath")
        self.element_click(self._assessment_select, locator_type="xpath")
        time.sleep(2)
        self.wait_for_element(self._assessment_attemptes, locator_type="xpath")
        self.send_keys("5", self._assessment_attemptes, locator_type="xpath")
        self.wait_for_element(self._assessment_passing, locator_type="xpath")
        self.send_keys("35", self._assessment_passing, locator_type="xpath")
        self.wait_for_element(self._assessment_duration, locator_type="xpath")
        self.send_keys("10", self._assessment_duration, locator_type="xpath")
        self.element_click(self._assessment_save, "xpath")

    def set_LOI(self):
        self.wait_for_element(self._configure_LOI, locator_type="xpath")
        self.element_click_js(self._configure_LOI, locator_type="xpath")
        self.wait_for_element(self._LOI_email, locator_type="xpath")
        self.send_keys(self.LOI_para, self._LOI_email, locator_type="xpath")
        self.wait_for_element(self._LOI_email, locator_type="xpath")
        self.send_keys(self.LOI_para, self._LOI_email, locator_type="xpath")
        self.element_click(self._LOI_save, "xpath")

    def post_a_job_send_approval(self, job_title, location, description, job_type, department, no_of_position, min_experience, max_experience, education, technical_skills,
                   non_technical_skills, min_compensation, max_compesation, other, requested_by, enddate, detail_description):
        self.wait_for_element(self._licence_validate, locator_type="xpath")
        self.wait_till_element_invisibility(self._licence_validate, locator_type="xpath")
        self.enter_job_title(job_title)
        self.enter_location(location)
        self.enter_job_type(job_type)
        self.enter_deparment(department)
        self.enter_no_of_position(no_of_position)
        self.enter_min_experiance(min_experience)
        self.enter_max_experiance(max_experience)
        self.enter_education(education)
        self.enter_technical_skills(technical_skills)
        self.enter_non_technical_skills(non_technical_skills)
        self.enter_min_compensation(min_compensation)
        self.enter_max_compensation(max_compesation)
        self.enter_other(other)
        self.enter_requested_by(requested_by)
        day, month, year =self.split_text(enddate, "/")
        self.enter_end_date(day, month, year)
        self.save_job()
        self.wait_for_page_load()
        self.wait_till_element_invisibility(self._validation, "xpath")
        self.click_manualJD()
        self.edite_detail_description(detail_description)
        self.wait_till_element_invisibility(self._validation, "xpath")
        self.click_add_steps()
        self.click_assessment_checkbox()
        self.click_ai_assessment_checkbox()
        self.click_interview_checkbox()
        self.click_gd_checkbox()
        self.click_LOI_checkbox()
        self.click_select()
        self.enter_waightage()
        self.enter_cutOff()
        self.set_AIassessment()
        self.set_assessment()
        self.set_LOI()
        self.click_continue()
        self.wait_till_element_invisibility(self._validation, "xpath")
        self.click_skill_toggle()
        self.click_scroll_bar()
        self.click_continue()
        self.wait_till_element_invisibility(self._validation, "xpath")
        self.click_send_approval()
        time.sleep(3)
        self.click_send_approval_request()
        self.wait_for_element(self._approval_sent_confirmation, "xpath")
        actual = self.get_text(self._approval_sent_confirmation, locator_type="xpath")
        self.click_close()
        return actual






















