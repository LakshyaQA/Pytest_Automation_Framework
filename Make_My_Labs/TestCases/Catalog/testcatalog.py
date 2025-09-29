import pytest
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Make_My_Labs.Configration.configpath import UploadFile
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testcatalog(Basetest):

    @pytest.fixture(autouse=True)
    def class_setup_in(self):
        self.lp.login(self.username, self.password)
        self.db.click_machine_catalog()

    @pytest.mark.order(11)
    @pytest.mark.parametrize("create_catalog_data",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_Create_Catalog"))
    def test_create_catalog(self, create_catalog_data):
        catalog_name, lab_type, template_name = create_catalog_data
        self.cl.info(f"Data received from JSON File :{create_catalog_data}")
        self.cl.info("************  Test Case Started : test_create_catalog  **********")
        self.mc.create_catalog(catalog_name, lab_type, template_name)
        self.mc.search_catalog(catalog_name)
        assert catalog_name in self.mc.machine_catalog_verify(
            catalog_name), f"Required text '{catalog_name}' not found in the page source."
        self.mc.publish_catalog(catalog_name)
        assert self.mc.publish_selected(catalog_name), "Publish button not selected."
        self.cl.info("************  Test Case Ended : test_create_catalog  **********")

    @pytest.mark.order(12)
    @pytest.mark.parametrize("create_catalog_data_pooled",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_Create_Catalog_Pooled"))
    def test_create_catalog_pooled(self, create_catalog_data_pooled):
        catalog_name, lab_type, template_name = create_catalog_data_pooled
        self.cl.info(f"Data received from JSON File :{create_catalog_data_pooled}")
        self.cl.info("************  Test Case Started : test_create_catalog  **********")
        self.mc.create_catalog_pooled(catalog_name, lab_type, template_name)
        self.mc.search_catalog(catalog_name)
        assert catalog_name in self.mc.machine_catalog_verify(
            catalog_name), f"Required text '{catalog_name}' not found in the page source."
        self.mc.publish_catalog(catalog_name)
        assert self.mc.publish_selected(catalog_name), "Publish button not selected."
        self.cl.info("************  Test Case Ended : test_create_catalog  **********")

    @pytest.mark.order(13)
    @pytest.mark.parametrize("create_catalog_data_guided",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_Create_Catalog_Guided"))
    def test_create_catalog_guided(self, create_catalog_data_guided):
        catalog_name, lab_type, template_name = create_catalog_data_guided
        self.cl.info(f"Data received from JSON File :{create_catalog_data_guided}")
        self.cl.info("************  Test Case Started : test_create_catalog_guided  **********")
        self.mc.create_catalog_guided(catalog_name, lab_type, template_name)
        self.mc.search_catalog(catalog_name)
        assert catalog_name in self.mc.machine_catalog_verify(
            catalog_name), f"Required text '{catalog_name}' not found in the page source."
        self.mc.publish_catalog(catalog_name)
        assert self.mc.publish_selected(catalog_name), "Publish button not selected."
        self.cl.info("************  Test Case Ended : test_create_catalog_guided  **********")
