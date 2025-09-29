import unittest

from Techademy_One.Testcases.Dashboard.test_dashboard import DashboardTests
from Techademy_One.Testcases.Dashboard.test_requests import RequestTests
from Techademy_One.Testcases.Dashboard.test_routing_to_app_admin import RoutingTestsAdmin
from Techademy_One.Testcases.Dashboard.test_routing_to_app_superadmin import RoutingTests
from Techademy_One.Testcases.Invoice_Generation.test_invoicegeneration import InvoiceTests
from Techademy_One.Testcases.Login.test_login import LoginTests
from Techademy_One.Testcases.Notifications.test_notification_creation import NotificationCreationTests
from Techademy_One.Testcases.Reports.test_report import ReportsTest
from Techademy_One.Testcases.Reports.test_report_settings import ReportSetting
from Techademy_One.Testcases.Tenant_Management.test_bill_configuration import BillConfigurationTests
from Techademy_One.Testcases.Tenant_Management.test_license_configuration import LicenseConfigurationTests
from Techademy_One.Testcases.Tenant_Management.test_self_sub import SelfSubscriptionTest
from Techademy_One.Testcases.Tenant_Management.test_teant_manage_tenant_admin import TenantManageAdminTests
from Techademy_One.Testcases.Tenant_Management.test_tenant_creation import TestTenantCreation
from Techademy_One.Testcases.Tenant_Management.test_tenant_manage import TenantManageTests
from Techademy_One.Testcases.Tenant_Management.test_tenant_report import ReportAdminTests
from Techademy_One.Testcases.Users.test_user_management import  TestUserManagement
from Techademy_One.Testcases.Users.test_users_tenant_admin import TestUserManagementAdmin

if __name__ == "__main__":
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None

    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(LoginTests))
    suite.addTests(loader.loadTestsFromTestCase(DashboardTests))
    suite.addTests(loader.loadTestsFromTestCase(TestTenantCreation))
    suite.addTests(loader.loadTestsFromTestCase(TenantManageTests))
    suite.addTests(loader.loadTestsFromTestCase(TestUserManagement))
    suite.addTests(loader.loadTestsFromTestCase(TenantManageAdminTests))
    suite.addTests(loader.loadTestsFromTestCase(TestUserManagementAdmin))
    suite.addTests(loader.loadTestsFromTestCase(RoutingTests))
    suite.addTests(loader.loadTestsFromTestCase(RoutingTestsAdmin))
    suite.addTests(loader.loadTestsFromTestCase(BillConfigurationTests))
    suite.addTests(loader.loadTestsFromTestCase(LicenseConfigurationTests))
    suite.addTests(loader.loadTestsFromTestCase(SelfSubscriptionTest))
    suite.addTests(loader.loadTestsFromTestCase(ReportsTest))
    suite.addTests(loader.loadTestsFromTestCase(ReportSetting))
    suite.addTests(loader.loadTestsFromTestCase(InvoiceTests))
    suite.addTests(loader.loadTestsFromTestCase(RequestTests))
    suite.addTests(loader.loadTestsFromTestCase(ReportAdminTests))
    suite.addTests(loader.loadTestsFromTestCase(NotificationCreationTests))





    runner = unittest.TextTestRunner()
    runner.run(suite)
