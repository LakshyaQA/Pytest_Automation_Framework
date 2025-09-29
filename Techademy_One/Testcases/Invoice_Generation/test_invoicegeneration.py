import unittest
import pytest
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.InvoiceGenerationPage import InvoiceGeneration


@pytest.mark.usefixtures("tech_one_setup")
class InvoiceTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.ig = InvoiceGeneration(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(41)
    def test_Invoice_Generation(self):
        self.cl.info("************  Test Case Started : Invoice_Generation Test  ************")
        self.lp.login(self.username, self.password)
        self.db.CloseChatBot()
        self.db.clickonInvoice()
        self.ig.verifygenerateinvoice()
