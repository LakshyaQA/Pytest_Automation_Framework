import time
import unittest

import pytest

from Common_Packages.Utility.exceldatareader import Exceldatareader
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.CreateTenantPage import TenantDetails
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.TenantListPage import TenantList


@pytest.mark.usefixtures("tech_one_setup")
class TestTenantCreation:
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.tm = TenantList(self.driver)
        self.td = TenantDetails(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize(
        "tenant_name,tenant_display_name,tenant_org,tenant_domain,date,GST,address_1,address_2,zipcode,admin_first_name,admin_last_name,admin_email,contact,support_contact,support_email,login_text_desc,login_header,first_name,last_name,email,first_name1,last_name1,email1",
        Exceldatareader.get_Data_from_excel(sheetname="techademy_one"))
    @pytest.mark.order(7)
    def test_tenant_creation(self, tenant_name, tenant_display_name, tenant_org, tenant_domain,
                                                    date, GST, address_1, address_2, zipcode, admin_first_name,
                                                    admin_last_name, admin_email, contact, support_contact,
                                                    support_email, login_text_desc, login_header, first_name, last_name,
                                                    email, first_name1, last_name1, email1):
        self.cl.info("************  Test Case Started : Tenant Creation  ************")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.ClickonCreate()
        self.td.EnterBasicDetails(tenant_display_name, tenant_org, tenant_domain, date, GST, address_1,
                                  address_2, zipcode, admin_first_name, admin_last_name, admin_email, contact)
        self.td.CustomizationDetails(support_contact, support_email, login_text_desc, login_header)
        self.td.SelectPlan()
        self.td.VerifyTenantCreation()

    @pytest.mark.parametrize(
        "tenant_name,tenant_display_name,tenant_org,tenant_domain,date,GST,address_1,address_2,zipcode,admin_first_name,admin_last_name,admin_email,contact,support_contact,support_email,login_text_desc,login_header,first_name,last_name,email,first_name1,last_name1,email1",
        Exceldatareader.get_Data_from_excel(sheetname="techademy_one"))
    @pytest.mark.order(42)
    def test_tenant_creation_with_same_name(self, tenant_name, tenant_display_name, tenant_org, tenant_domain,
                                                    date, GST, address_1, address_2, zipcode, admin_first_name,
                                                    admin_last_name, admin_email, contact, support_contact,
                                                    support_email, login_text_desc, login_header, first_name, last_name,
                                                    email, first_name1, last_name1, email1):
        self.cl.info("************  Test Case Started : Tenant Creation  ************")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.ClickonCreate()
        self.td.EnterBasicDetails(tenant_display_name, tenant_org, tenant_domain, date, GST, address_1,
                                  address_2, zipcode, admin_first_name, admin_last_name, admin_email, contact)

        self.td.verifyTenantWithSameName()
