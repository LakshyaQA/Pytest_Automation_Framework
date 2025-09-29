import time
import pytest
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Make_My_Labs.Configration.configpath import UploadFile
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testresourceprovider(Basetest):

    @pytest.fixture(autouse=True)
    def class_setup_in(self):
        self.lp.login(self.username, self.password)
        self.db.click_resource_provider()

    @pytest.mark.order(7)
    @pytest.mark.parametrize("mml_resource_provider_data", Jsondatareader.get_data_from_json(
        UploadFile.json_data_file("\\MML_Data_File.json"), "MML_Resource_Provider"))
    def test_add_resource_provider(self, mml_resource_provider_data):
        (rp_connection_name, rp_server_url, rp_username, rp_password, rp_vm_provisioning_checkbox, vm_ware_data_center,
         vm_ware_cluster, datastore_cluster) = mml_resource_provider_data
        self.cl.info(f"Data received from JSON File :{mml_resource_provider_data}")
        self.cl.info("************  Test Case Started : test_add_resource_provider  **********")
        self.rp.click_add_resource_provider_button1()
        time.sleep(1)
        self.rp.send_resourceprovider_data(rp_connection_name, rp_server_url, rp_username, rp_password,
                                           rp_vm_provisioning_checkbox, vm_ware_data_center, vm_ware_cluster,
                                           datastore_cluster)
        time.sleep(1)
        assert self.rp.resource_provided_created_verify() == "Created", self.cl.info(("Assertion Failed : Created "
                                                                                      "didn't appear on"
                                                                                      "web page"))
        self.cl.info("test_add_resource_provider has passed")
        self.cl.info("************  Test Case Ended : test_add_resource_provider  **********")
