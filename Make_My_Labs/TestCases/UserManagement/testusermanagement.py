import time
import pytest
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Make_My_Labs.Configration.configpath import UploadFile
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testusermanagement(Basetest):

    @pytest.fixture(autouse=True)
    def class_setup_in(self):
        self.lp.login(self.username, self.password)
        self.db.click_tenant_management()
        time.sleep(1)

    @pytest.mark.order(15)
    @pytest.mark.parametrize("create_users",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_Create_Users"))
    def test_create_new_user(self, create_users):
        tenant_name, first_name, middle_name, last_name, email_id, mobile_num, role_name = create_users
        self.cl.info(f"Data received from JSON File :{create_users}")
        self.cl.info("************  Test Case Started : test_create_new_user  **********")
        self.db.click_user_management()
        self.um.create_new_user(tenant_name, first_name, middle_name, last_name, email_id, mobile_num, role_name)
        assert self.um.verify_new_user() == f"{first_name} {last_name} account has been created successfully!", \
            f"Failed to create {first_name} {last_name} account!"
        self.um.click_success_msg_box()
        self.cl.info("************  Test Case Ended : test_create_new_user  **********")
