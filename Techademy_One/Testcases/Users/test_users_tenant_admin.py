import unittest

import pytest

from Common_Packages.Utility.exceldatareader import Exceldatareader
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.UserGroups import UserGroup
from Techademy_One.pageObject.UserManagementPage import UserManagement


@pytest.mark.usefixtures("tech_one_setup")
class TestUserManagementAdmin:
    username = ReadConfig.get_username('tenant admin', 'tenantusername1')
    password = ReadConfig.get_password('tenant admin', 'tenantpassword1')
    # first_name = ReadConfig.get_first_name('User Management', 'first_name1')
    # last_name = ReadConfig.get_last_name('User Management', 'last_name1')
    # email = ReadConfig.get_email('User Management', 'email1')


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.um = UserManagement(self.driver)
        self.ug = UserGroup(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize(
        "tenant_name,tenant_display_name,tenant_org,tenant_domain,date,GST,address_1,address_2,zipcode,admin_first_name,admin_last_name,admin_email,contact,support_contact,support_email,login_text_desc,login_header,first_name,last_name,email,first_name1,last_name1,email1",
        Exceldatareader.get_Data_from_excel(sheetname="techademy_one"))
    @pytest.mark.order(27)
    def test_user_onboarding_by_tenantadmin(self,tenant_name,tenant_display_name,tenant_org,tenant_domain,date,GST,address_1,address_2,zipcode,admin_first_name,admin_last_name,admin_email,contact,support_contact,support_email,login_text_desc,login_header,first_name,last_name,email,first_name1,last_name1,email1):
        self.cl.info("************  Test Case Started : Tenant Admin : Create User  ***********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToUsersTab()
        self.um.CreateUser(first_name1, last_name1, email1)
        self.um.VerifyUserCreation()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(28)
    def test_usergrp_creation_by_tenantadmin(self):
        self.cl.info("************  Test Case Started : Tenant Admin : Create User Group  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToUsersTab()
        self.um.clickOnUserGroup()
        self.ug.create_usergroup_tenantadmin()
        self.ug.VerifyUserGrpCreation()
