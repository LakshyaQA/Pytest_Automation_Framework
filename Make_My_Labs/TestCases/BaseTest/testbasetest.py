import pytest

from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Common_Packages.Utility.custom_logger import custom_logger
from Make_My_Labs.Configration.readproperties import Readconfig
from Make_My_Labs.pageObjects.createtemplatepage import Createtemplatepage
from Make_My_Labs.pageObjects.dashboardpage import Dashboardpage
from Make_My_Labs.pageObjects.labspage import Labspage
from Make_My_Labs.pageObjects.loginpage import Loginpage
from Make_My_Labs.pageObjects.machinecatalogpage import Machinecatalogpage
from Make_My_Labs.pageObjects.resourceproviderpage import ResourceProvider
from Make_My_Labs.pageObjects.tenantcatalogpage import TenantCatalogPage
from Make_My_Labs.pageObjects.tenantpage import Createtenantpage
from Make_My_Labs.pageObjects.usermanagementpage import Usermanagementpage
from Make_My_Labs.pageObjects.workspacepage import Workspacepage


@pytest.mark.usefixtures("mml_setup")
class Basetest(metaclass=Logmethodmeta):
    """
    Base class for test cases, setting up common configurations.

    Attributes:
        username (str): The username retrieved from the configuration file.
        password (str): The password retrieved from the configuration file.
    """
    username = Readconfig.get_username("common info", "username")
    password = Readconfig.get_password("common info", "password")

    @pytest.fixture(autouse=True)
    def class_setup(self, mml_setup):
        self.driver = mml_setup
        self.cl = custom_logger()
        self.lp = Loginpage(self.driver)
        self.db = Dashboardpage(self.driver)
        self.rp = ResourceProvider(self.driver)
        self.tc = TenantCatalogPage(self.driver)
        self.mc = Machinecatalogpage(self.driver)
        self.ct = Createtenantpage(self.driver)
        self.ctemp = Createtemplatepage(self.driver)
        self.um = Usermanagementpage(self.driver)
        self.ws = Workspacepage(self.driver)
        self.labs = Labspage(self.driver)