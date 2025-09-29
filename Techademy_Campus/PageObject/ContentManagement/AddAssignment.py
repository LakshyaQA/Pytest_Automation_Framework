import logging
import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class AddAssignment(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the adding assignment content for a chapter under a subject

        author: Abhilash

        '''

    path = UploadFile.file_upload_path('Assignment.jpg')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for adding the assignment

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    ChapterClick = "//p[text()='Electric Boiler']"
    AddContent = "//p[text()='Add Content']"
    Add_Assignment = "//span[text()='Add Assignment']"
    Assignment_Title = "//input[@name='assignment_title']"
    Assignment_Marks = "//input[@name='marks']"
    Assignment_Description = "//textarea[@name='description']"
    GettingEvaluated_Yes = "(//input[@name='is_getting_evaluated'])[1]"
    GettingEvaluated_No = "(//input[@name='is_getting_evaluated'])[2]"
    AssignmentType_Upload = "(//input[@name='assignment_type'])[1]"
    Browse_field = "//label[text()='Browse']"
    Next_button = "//button[text()='Next']"
    Submission_type = "(//input[@name='submission_assignment_type'])[1]"
    SubmissionType_dropdown = "//input[@name='submission_type']"
    OnlineFileSubmission = "//li[text()='Online File Submission']"
    FilesAllowed = "(//input[@name='files_allow_per_submission'])[1]"
    Hours = "//input[@name='hours']"
    Minutes = "//input[@name='minutes']"
    Allowable_FileExtensions = "//input[@name='allowable_file_extensions']"
    NoRestrictions = "//li[text()='No Restrictions']"
    Submissions = "(//input[@name='submissions'])[1]"
    EndDateTime = "(//input[@placeholder='mm/dd/yyyy hh:mm (a|p)m'])[1]"
    Conditions = "//input[@name='conditions[0].condition']"
    ReleaseOn = "//li[text()='Release on']"
    ReleaseOn_DateTime = "(//input[@placeholder='mm/dd/yyyy hh:mm (a|p)m'])[2]"
    Guidelines = "//input[@name='evaluation_guidelines']"
    Create_button = "//button[text()='Create']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnDepartment(self):
        self.wait_for_element(self.Department_option, locator_type="xpath")
        self.element_click_js(self.Department_option, "xpath")

    def clickOnViewDetails(self):
        self.wait_for_element(self.ViewDetails_button, locator_type="xpath")
        self.element_click_js(self.ViewDetails_button, "xpath")

    def clickOnChapter(self):
        self.wait_for_element(self.ChapterClick, locator_type="xpath")
        self.element_click_js(self.ChapterClick, "xpath")

    def clickOnAddContent(self):
        self.wait_for_element(self.AddContent, locator_type="xpath")
        self.element_click_js(self.AddContent, "xpath")

    def clickOnAddAssignment(self):
        self.wait_for_element(self.Add_Assignment, locator_type="xpath")
        self.element_click_js(self.Add_Assignment, "xpath")

    def clickEnterAssignmentTitle(self, assignment_title):
        self.wait_for_element(self.Assignment_Title, locator_type="xpath")
        self.element_click_js(self.Assignment_Title, "xpath")
        self.send_keys(assignment_title, self.Assignment_Title, "xpath")

    def clickEnterAssignmentMarksOutOf(self, assignment_marks):
        self.wait_for_element(self.Assignment_Marks, locator_type="xpath")
        self.element_click_js(self.Assignment_Marks, "xpath")
        self.clear_input_field(self.Assignment_Marks, "xpath")
        self.send_keys(assignment_marks, self.Assignment_Marks, "xpath")

    def clickEnterAssignmentDescription(self, assignment_description):
        self.wait_for_element(self.Assignment_Description, locator_type="xpath")
        self.element_click_js(self.Assignment_Description, "xpath")
        self.send_keys(assignment_description, self.Assignment_Description, "xpath")

    def clickOnGettingEvaluated(self):
        self.wait_till_element_invisibility(self.GettingEvaluated_Yes, locator_type="xpath")
        self.element_click_js(self.GettingEvaluated_Yes, "xpath")

    def clickOnAssignmentType(self):
        self.wait_till_element_invisibility(self.AssignmentType_Upload, locator_type="xpath")
        self.element_click_js(self.AssignmentType_Upload, "xpath")

    def uploadAssignmentFile(self, path):
        self.log.info("Uploading Assignment file")
        self.element_click(self.Browse_field, "xpath")
        self.upload_file(path, self.Browse_field, locator_type="xpath")

    def clickOnNextButton(self):
        self.wait_for_element(self.Next_button, locator_type="xpath")
        self.element_click_js(self.Next_button, "xpath")

    def clickOnAssignmentSubmissionType(self):
        self.wait_till_element_invisibility(self.Submission_type, locator_type="xpath")
        self.element_click_js(self.Submission_type, "xpath")

    def selectSubmissionType(self):
        self.wait_till_element_invisibility(self.SubmissionType_dropdown, "xpath")
        self.element_click_js(self.SubmissionType_dropdown, "xpath")
        self.wait_for_element(self.OnlineFileSubmission, "xpath")
        self.element_click_js(self.OnlineFileSubmission, "xpath")

    def clickOnFilesAllowed(self):
        self.wait_till_element_invisibility(self.FilesAllowed, locator_type="xpath")
        self.element_click_js(self.FilesAllowed, "xpath")

    def clickEnterAssignmentHours(self, assignment_hours):
        self.wait_for_element(self.Hours, locator_type="xpath")
        self.element_click_js(self.Hours, "xpath")
        self.send_keys(assignment_hours, self.Hours, "xpath")

    def clickEnterAssignmentMinutes(self, assignment_minutes):
        self.wait_for_element(self.Minutes, locator_type="xpath")
        self.element_click_js(self.Minutes, "xpath")
        self.send_keys(assignment_minutes, self.Minutes, "xpath")

    def selectAllowableFileExtensions(self):
        self.wait_till_element_invisibility(self.Allowable_FileExtensions, "xpath")
        self.element_click_js(self.Allowable_FileExtensions, "xpath")
        self.wait_for_element(self.NoRestrictions, "xpath")
        self.element_click_js(self.NoRestrictions, "xpath")

    def clickOnSubmissions(self):
        self.wait_till_element_invisibility(self.Submissions, locator_type="xpath")
        self.element_click_js(self.Submissions, "xpath")

    def clickEnterEndDateTime(self):
        self.clear_input_field(self.EndDateTime, "xpath")
        time.sleep(2)
        date_time = self.get_current_date_and_time(5)
        logging.info(type(date_time))
        string_date_time = str(date_time)
        logging.info(type(string_date_time))
        self.send_keys(string_date_time, self.EndDateTime, locator_type="xpath")

    def selectConditions(self):
        self.wait_till_element_invisibility(self.Conditions, "xpath")
        self.element_click_js(self.Conditions, "xpath")
        self.wait_for_element(self.ReleaseOn, "xpath")
        self.element_click_js(self.ReleaseOn, "xpath")

    def clickEnterGuidelines(self, guideline):
        self.wait_for_element(self.Guidelines, locator_type="xpath")
        self.element_click_js(self.Guidelines, "xpath")
        self.send_keys(guideline, self.Guidelines, "xpath")

    def clickOnCreateButton(self):
        self.wait_for_element(self.Create_button, locator_type="xpath")
        self.element_click_js(self.Create_button, "xpath")

    def addingTheUploadAssignment(self, assignment_title, assignment_marks, assignment_description, assignment_hours,
                                  assignment_minutes, guideline):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnChapter()
        self.clickOnAddContent()
        self.clickOnAddAssignment()
        self.clickEnterAssignmentTitle(assignment_title)
        self.clickEnterAssignmentMarksOutOf(assignment_marks)
        self.clickEnterAssignmentDescription(assignment_description)
        self.clickOnGettingEvaluated()
        self.clickOnAssignmentType()
        self.uploadAssignmentFile(self.path)
        self.clickOnNextButton()
        self.clickOnAssignmentSubmissionType()
        self.selectSubmissionType()
        self.clickOnFilesAllowed()
        self.clickEnterAssignmentHours(assignment_hours)
        self.clickEnterAssignmentMinutes(assignment_minutes)
        self.selectAllowableFileExtensions()
        self.clickOnSubmissions()
        time.sleep(1)
        self.clickEnterEndDateTime()
        self.selectConditions()
        time.sleep(1)
        self.clickEnterGuidelines(guideline)
        self.clickOnCreateButton()
        self.clickOnCreateButton()
