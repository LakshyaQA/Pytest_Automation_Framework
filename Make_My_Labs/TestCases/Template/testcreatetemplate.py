import time
import pytest
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Make_My_Labs.Configration.configpath import UploadFile
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testcreatetemplate(Basetest):
    @pytest.fixture(autouse=True)
    def class_setup_in(self):
        self.lp.login(self.username, self.password)
        self.db.click_resource_provider()

    @pytest.mark.order(8)
    @pytest.mark.parametrize("mml_create_template_data",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_Create_Template"))
    def test_create_template_and_publish(self, mml_create_template_data):
        resource_provider_name, connection_name, type_of_template, add_category, platform_type, display_name, description, pooled_template_status, no_of_vm, lab_type, naming_prefix, admin_username, admin_password, enable_linked_clone_status, vt_enable_status, is_enable_for_provisioning_status, base_vm_folder_name, base_vm_name, base_vm_snapshots_name, instance_size, type_of_network, standard_type_of_network, template_name_search = mml_create_template_data
        self.cl.info(
            "************  Test Case Started : test_create_template and publish **********")
        self.ctemp.reach_template_page(
            resource_provider_name, connection_name, type_of_template)
        time.sleep(2)
        self.ctemp.creating_template_and_publish(add_category, platform_type, display_name, description,
                                                 pooled_template_status,
                                                 no_of_vm, lab_type, naming_prefix, admin_username, admin_password,
                                                 enable_linked_clone_status, vt_enable_status,
                                                 is_enable_for_provisioning_status,
                                                 base_vm_folder_name, base_vm_name, base_vm_snapshots_name,
                                                 instance_size,
                                                 type_of_network, standard_type_of_network, template_name_search)
        assert self.ctemp.verify_created_template() == "Template created successfully.", self.cl.info(
            ("Assertion Failed : Template "
             "not created"))
        assert self.ctemp.verify_created_published_template() == "Re-Publish", self.cl.info(
            ("Assertion Failed : Template not "
             "Published"))
        self.cl.info(
            "************  Test Case Ended : test_create_template and publish  **********")

    @pytest.mark.order(9)
    @pytest.mark.parametrize("mml_create_template_data_pooled",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_Create_Template_Pooled"))
    def test_create_pooled_template_and_publish(self, mml_create_template_data_pooled):
        resource_provider_name, connection_name, type_of_template, add_category, platform_type, display_name, description, pooled_template_status, no_of_vm, lab_type, naming_prefix, admin_username, admin_password, enable_linked_clone_status, vt_enable_status, is_enable_for_provisioning_status, base_vm_folder_name, base_vm_name, base_vm_snapshots_name, instance_size, type_of_network, standard_type_of_network, template_name_search = mml_create_template_data_pooled
        self.cl.info(
            "************  Test Case Started : test_create_pooled_template_and_publish **********")
        self.ctemp.reach_template_page(
            resource_provider_name, connection_name, type_of_template)
        time.sleep(2)
        self.ctemp.creating_pooled_template_and_publish(add_category, platform_type, display_name, description,
                                                        pooled_template_status,
                                                        no_of_vm, lab_type, naming_prefix, admin_username,
                                                        admin_password,
                                                        enable_linked_clone_status, vt_enable_status,
                                                        is_enable_for_provisioning_status,
                                                        base_vm_folder_name, base_vm_name, base_vm_snapshots_name,
                                                        instance_size,
                                                        type_of_network, standard_type_of_network, template_name_search)
        assert self.ctemp.verify_created_published_template() == "Re-Publish", self.cl.info(
            ("Assertion Failed : Template not "
             "Published"))
        self.cl.info(
            "************  Test Case Ended : test_create_pooled_template_and_publish  **********")

    @pytest.mark.order(10)
    @pytest.mark.parametrize("mml_create_template_data",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_Create_Template_Guided_Lab"))
    def test_create_guided_lab_non_pooled_template_and_publish(self, mml_create_template_data):
        resource_provider_name, connection_name, type_of_template, add_category, platform_type, display_name, description, pooled_template_status, no_of_vm, lab_type, naming_prefix, admin_username, admin_password, enable_linked_clone_status, vt_enable_status, is_enable_for_provisioning_status, base_vm_folder_name, base_vm_name, base_vm_snapshots_name, instance_size, type_of_network, standard_type_of_network, template_name_search = mml_create_template_data
        self.cl.info(f"Data received from JSON File :{mml_create_template_data}")
        self.cl.info(
            "************  Test Case Started : test_create_template and publish **********")
        self.ctemp.reach_template_page(
            resource_provider_name, connection_name, type_of_template)
        time.sleep(2)
        self.ctemp.creating_guided_lab_template_and_publish(add_category, platform_type, display_name, description,
                                                            pooled_template_status,
                                                            no_of_vm, lab_type, naming_prefix, admin_username,
                                                            admin_password,
                                                            enable_linked_clone_status, vt_enable_status,
                                                            is_enable_for_provisioning_status,
                                                            base_vm_folder_name, base_vm_name, base_vm_snapshots_name,
                                                            instance_size,
                                                            type_of_network, standard_type_of_network,
                                                            template_name_search)
        assert self.ctemp.verify_created_template() == "Template created successfully.", self.cl.info(
            ("Assertion Failed : Template "
             "not created"))
        assert self.ctemp.verify_created_published_template() == "Re-Publish", self.cl.info(
            ("Assertion Failed : Template not "
             "Published"))
        self.cl.info(
            "************  Test Case Ended : test_create_template and publish  **********")
