import pytest
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Make_My_Labs.Configration.configpath import UploadFile
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testtenantcatalog(Basetest):
    @pytest.fixture(autouse=True)
    def class_setup_in(self):
        self.lp.login(self.username, self.password)
        self.db.click_tenant_catalog()

    @pytest.mark.order(18)
    @pytest.mark.parametrize("create_pooled_vm", Jsondatareader.get_data_from_json(
        UploadFile.json_data_file("\\MML_Data_File.json"), "Pooled_Tenant_Details"))
    def test_pooled_vm(self, create_pooled_vm):
        tenant_name, user_name, password = create_pooled_vm
        self.cl.info(f"Data received from JSON File :{create_pooled_vm}")
        self.cl.info(
            "************  Test Case Started : test_pooled_VM  **********")
        self.tc.download_csv_file(tenant_name)
        self.tc.login_pooled_vm()
        self.tc.login_end_user(user_name, password)
        self.cl.info("Login successful with credentials: " +
                     user_name + "," + password)
        assert self.tc.verify_pooled_vm_page() == "(Please Extend VM before session is over)*", self.cl.info("VM "
                                                                                                             "instance "
                                                                                                             "not "
                                                                                                             "created")
        self.driver.quit()
        self.cl.info(
            "************  Test Case Ended : test_pooled_VM  **********")
