import unittest
import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.ContentManagement.AddAssignment import AddAssignment
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class AddAssignmentContent(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    assignment_title = ReadConfig.getUploadAssignmentTitle()
    assignment_marks = ReadConfig.getUploadAssignmentMarks()
    assignment_description = ReadConfig.getUploadAssignmentDescription()
    assignment_hours = ReadConfig.getUploadAssignmentHours()
    assignment_minutes = ReadConfig.getUploadAssignmentMinutes()
    guideline = ReadConfig.getUploadAssignmentGuideline()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.aa = AddAssignment(self.driver)

    @pytest.mark.run()
    def test_AddAssignment(self):
        self.cl.info("********** TestCase: HOD - AddAssignment **********")
        self.lp.login(self.username, self.password)
        self.aa.addingTheUploadAssignment(self.assignment_title, self.assignment_marks, self.assignment_description,
                                          self.assignment_hours, self.assignment_minutes, self.guideline)
