import time
import pytest
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Make_My_Labs.Configration.configpath import UploadFile
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testworkspace(Basetest):

    @pytest.fixture(autouse=True)
    def class_setup_in(self):
        self.lp.login(self.username, self.password)
        self.db.click_workspace_manager()

    @pytest.mark.order(16)
    @pytest.mark.parametrize("create_work_space_data", Jsondatareader.get_data_from_json(
        UploadFile.json_data_file("\\MML_Data_File.json"), "MML_WorkSpace_AAD"))
    def test_create_workspace_aad(self, create_work_space_data):
        workspacename, tenant_name, labtype, scheduletype, all_day_checkbox, start_date_count, end_date_count, allday_start_date_and_time_count, allday_end_date_and_time_count, extra_schedule_checkbox, extra_schedule_start_date_and_time, extra_schedule_end_date_and_time, duration_no_of_days, duration_start_date_and_time_count, resource_template_name, instance_size, min_vm_count, max_vm_count, over_ride_cost_status, pricing_profile_name, over_ride_cost_per_hour_status, cost_per_hour, resource_usage_duration_per_user, vm_decommision_after_expiry, post_provision_login_status, post_provision_login, extend_duration_status, no_of_extensions, select_pack, threshhold_value, auth_name, auth_config, user_name, password, created_workspace_name = create_work_space_data
        self.cl.info(f"Data received from JSON File :{create_work_space_data}")
        self.cl.info(
            "************  Test Case Started : test_create_workspace_AAD **********")
        time.sleep(1)
        self.ws.create_workspace(workspacename, tenant_name, labtype, scheduletype, all_day_checkbox, start_date_count,
                                 end_date_count, allday_start_date_and_time_count, allday_end_date_and_time_count,
                                 extra_schedule_checkbox, extra_schedule_start_date_and_time,
                                 extra_schedule_end_date_and_time, duration_no_of_days,
                                 duration_start_date_and_time_count)
        time.sleep(1)
        self.ws.add_resource(resource_template_name, instance_size, min_vm_count, max_vm_count, over_ride_cost_status,
                             pricing_profile_name, over_ride_cost_per_hour_status, cost_per_hour,
                             resource_usage_duration_per_user, vm_decommision_after_expiry, post_provision_login_status,
                             post_provision_login, extend_duration_status, no_of_extensions, select_pack,
                             threshhold_value, auth_name, auth_config)
        time.sleep(1)
        self.ws.click_manual_registration(user_name)
        time.sleep(3)
        self.ws.search_and_publish_option(created_workspace_name)
        time.sleep(1)
        assert self.ws.verify_published_workspace_name() == "Published", self.cl.info(
            "Assertion Failed : WorkSpace not published")
        time.sleep(2)
        self.ws.get_invitation_link_and_visit_ws(created_workspace_name)
        time.sleep(3)
        self.ws.login_workspace_aad(user_name, password)
        self.ws.ws_connect()
        assert self.ws.verify_ws_vm_page() == "Stop", self.cl.info("Assertion Failed : VM instance screen didn't "
                                                                   "reached")
        self.cl.info(
            "************  Test Case Ended : test_create_workspace_AAD **********")

    @pytest.mark.order(17)
    @pytest.mark.parametrize("create_work_space_data", Jsondatareader.get_data_from_json(
        UploadFile.json_data_file("\\MML_Data_File.json"), "MML_WorkSpace_LocalUser"))
    def test_create_workspace_LocalUser(self, create_work_space_data):
        workspacename, tenant_name, labtype, scheduletype, all_day_checkbox, start_date_count, end_date_count, allday_start_date_and_time_count, allday_end_date_and_time_count, extra_schedule_checkbox, extra_schedule_start_date_and_time, extra_schedule_end_date_and_time, duration_no_of_days, duration_start_date_and_time_count, resource_template_name, instance_size, min_vm_count, max_vm_count, over_ride_cost_status, pricing_profile_name, over_ride_cost_per_hour_status, cost_per_hour, resource_usage_duration_per_user, vm_decommision_after_expiry, post_provision_login_status, post_provision_login, extend_duration_status, no_of_extensions, select_pack, threshhold_value, auth_name, auth_config, created_workspace_name, local_user_issuer_url, user_name, password = create_work_space_data
        self.cl.info(f"Data received from JSON File :{create_work_space_data}")
        self.cl.info("************  Test Case Started : test_create_workspace_LocalUser **********")
        time.sleep(1)
        self.ws.create_workspace(workspacename, tenant_name, labtype, scheduletype, all_day_checkbox, start_date_count,
                                 end_date_count, allday_start_date_and_time_count, allday_end_date_and_time_count,
                                 extra_schedule_checkbox, extra_schedule_start_date_and_time,
                                 extra_schedule_end_date_and_time, duration_no_of_days,
                                 duration_start_date_and_time_count)
        time.sleep(1)
        self.ws.add_resource(resource_template_name, instance_size, min_vm_count, max_vm_count, over_ride_cost_status,
                             pricing_profile_name, over_ride_cost_per_hour_status, cost_per_hour,
                             resource_usage_duration_per_user, vm_decommision_after_expiry, post_provision_login_status,
                             post_provision_login, extend_duration_status, no_of_extensions, select_pack,
                             threshhold_value, auth_name, auth_config)
        time.sleep(1)
        self.ws.auth_config_local_user_registration(local_user_issuer_url)
        time.sleep(3)
        self.ws.search_and_publish_option(created_workspace_name)
        time.sleep(1)
        assert self.ws.verify_published_workspace_name() == "Published", self.cl.info(
            "Assertion Failed : WorkSpace not published")
        time.sleep(2)
        self.ws.get_invitation_link_and_visit_ws(created_workspace_name)
        time.sleep(3)
        self.ws.login_workspace_local_user(user_name, password)
        self.ws.ws_connect()
        assert self.ws.verify_ws_vm_page() == "Stop", self.cl.info("Assertion Failed : VM instance screen didn't "
                                                                   "reached")
        self.cl.info(
            "************  Test Case Ended : test_create_workspace_LocalUser **********")
