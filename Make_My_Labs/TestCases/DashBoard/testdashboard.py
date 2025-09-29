import time
import pytest
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testdashboard(Basetest):

    @pytest.fixture(autouse=True)
    def class_setup_in(self):
        self.lp.login(self.username, self.password)

    @pytest.mark.order(2)
    def test_click_dashboard(self):
        self.cl.info("************  Test Case Started : test_click_dashboard  **********")
        time.sleep(3)
        self.db.click_dashboard()
        self.cl.info("************  Test Case Ended : test_click_dashboard  **********")

    @pytest.mark.order(3)
    def test_click_resource_manager(self):
        self.cl.info("************  Test Case Started : test_click_resource_manager  **********")
        self.db.click_dashboard()
        self.cl.info("************  Test Case Ended : test_click_resource_manager  **********")

    @pytest.mark.order(4)
    def test_click_resource_provider(self):
        self.cl.info("************  Test Case Started : test_click_resource_provider  **********")
        self.db.click_resource_provider()
        self.cl.info("************  Test Case Ended : test_click_resource_provider  **********")

    @pytest.mark.order(5)
    def test_click_tenant_management(self):
        self.cl.info("************  Test Case Started : test_click_tenant_management  **********")
        self.db.click_tenant_management()
        self.cl.info("************  Test Case Ended : test_click_tenant_management  **********")

    @pytest.mark.order(6)
    def test_click_tenants(self):
        self.cl.info("************  Test Case Started : test_click_tenants  **********")
        self.db.click_tenants()
        self.cl.info("************  Test Case Ended : test_click_tenants  **********")
