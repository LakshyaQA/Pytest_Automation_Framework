import unittest

import pytest

from Common_Packages.Utility.exceldatareader import Exceldatareader
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.TenantListPage import TenantList
from Techademy_One.pageObject.UserGroups import UserGroup
from Techademy_One.pageObject.UserManagementPage import UserManagement
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


@pytest.mark.usefixtures("tech_one_setup")
class TestUserManagement:
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')
    tenant_name = TenantDetails.tenant_name
    # first_name = ReadConfig.get_first_name('User Management', 'first_name')
    # last_name = ReadConfig.get_last_name('User Management', 'last_name')
    # email = ReadConfig.get_email('User Management', 'email')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.tm = TenantList(self.driver)
        self.um = UserManagement(self.driver)
        self.ug = UserGroup(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize(
        "tenant_name,tenant_display_name,tenant_org,tenant_domain,date,GST,address_1,address_2,zipcode,admin_first_name,admin_last_name,admin_email,contact,support_contact,support_email,login_text_desc,login_header,first_name,last_name,email,first_name1,last_name1,email1",
        Exceldatareader.get_Data_from_excel(sheetname="techademy_one"))
    @pytest.mark.order(17)
    def test_user_onboarding_by_superadmin(self,tenant_name,tenant_display_name,tenant_org,tenant_domain,date,GST,address_1,address_2,zipcode,admin_first_name,admin_last_name,admin_email,contact,support_contact,support_email,login_text_desc,login_header,first_name,last_name,email,first_name1,last_name1,email1):
        self.cl.info("************  Test Case Started : Super Admin : Create User  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToUsers(self.tenant_name)
        self.um.CreateUser(first_name, last_name, email)
        self.um.VerifyUserCreation()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize(
        "grp_name,dec",
        Exceldatareader.get_Data_from_excel(sheetname="techademy_one"))
    @pytest.mark.order(18)
    def test_usergrp_creation_by_superadmin(self,grp_name,desc):
        self.cl.info("************  Test Case Started : Super Admin : Create UserGroup  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToUsersTab()
        self.um.clickOnUserGroup()
        self.ug.CreateUserGroup(grp_name,desc)
        self.ug.VerifyUserGrpCreation()
