import time
import pytest
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Make_My_Labs.Configration.configpath import UploadFile
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testcreatetenant(Basetest):

    @pytest.fixture(autouse=True)
    def class_setup_in(self):
        self.lp.login(self.username, self.password)
        self.db.click_tenant_management()
        time.sleep(1)

    @pytest.mark.order(14)
    @pytest.mark.parametrize("create_tenant_data",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_Create_Tenant"))
    def test_tenant_creation(self, create_tenant_data):
        tenant_name, email_id, address1, address2, country_name, state_name, city_name, zip_code, service, account_manager, csm_user, machine_catalog_1, machine_catalog_2, machine_catalog_3, auth_configuration, tenant_url, auto_onboarding_status, pricing_profile, billing_cycle, end_date_of_agreement, one_time_on_boarding_fee_status, one_time_on_boarding_fee_value, currency, billing_visible_to_tenant_user_toggle, instance_size, cost_against_instance, no_of_hours, pay_per_use_status, budget_allocated, core_status, no_of_core, memory_status, memory_quantity, storage_status, storage_quantity, total_vm_count_status, total_vm_count, monthly_vm_quota_status, monthly_vm_quota, suspend_vm, quota_rest_for_user, concurrent_connections_status, concurrent_connections, no_of_max_users_status, no_of_max_users, max_vm_per_user_status, max_vm_per_user, max_vm_auto_approve_per_user_status, max_vm_auto_approve_per_user, vm_max_extension_count_status, vm_max_extension_count, extension_approval_status, include_deleted_v_ms_for_max_v_ms_count_status, base_pack_name, base_pack_days, base_pack_minutes, default_basepack_status, autodelete_status, extension_pack_name, extension_pack_days, extension_pack_minutes, work_space_check_box_status, vm_expiry_warning_notification_1_status, vm_expiry_warning_notification_1_days, vm_expiry_warning_notification_2_status, vm_expiry_warning_notification_2_days, vm_expiry_warning_notification_3_status, vm_expiry_warning_notification_3_days, vm_expiry_remaining_hours_notification_1_status, vm_expiry_remaining_hours_notification_1_hours, vm_expiry_remaining_hours_notification_2_status, vm_expiry_remaining_hours_notification_2_hours, vm_expiry_remaining_hours_notification_3_status, vm_expiry_remaining_hours_notification_3_hours, vm_unutilized_warning_notification_days_status, vm_unutilized_warning_notification_days_days, enter_vm_decomission_after_expiry_status, enter_vm_decomission_after_expiry_days, vm_decomission_warning_notification_status, vm_decomission_warning_notification_days, togglestatus = create_tenant_data
        self.cl.info(f"Data received from JSON File :{create_tenant_data}")
        self.cl.info(
            "************  Test Case Started : test_tenant_creation  **********")
        self.db.click_tenants()
        self.ct.click_create_tenant_button()
        self.ct.create_tenant(tenant_name, email_id, address1, address2, country_name, state_name, city_name, zip_code,
                              service, account_manager, csm_user, machine_catalog_1, machine_catalog_2,
                              machine_catalog_3,
                              auth_configuration,
                              tenant_url, auto_onboarding_status)
        assert self.ct.verify_tenant_created() == "Tenant Created Successfully !", self.cl.info(("Assertion Failed : "
                                                                                                 "Tenant not"
                                                                                                 "created"))
        self.ct.click_tenant_proceed()
        time.sleep(1)
        self.ct.fixed_cost_per_vm(pricing_profile, billing_cycle, end_date_of_agreement,
                                  one_time_on_boarding_fee_status, one_time_on_boarding_fee_value, currency,
                                  billing_visible_to_tenant_user_toggle, instance_size, cost_against_instance)

        assert self.ct.verify_pricing_profile_created() == "Pricing Profile Created Successfully", self.cl.info((
            "Assertion Failed : "
            "Pricing Profile "
            "not set"))
        time.sleep(1)
        self.ct.set_quota_page(core_status, no_of_core, memory_status, memory_quantity, storage_status,
                               storage_quantity, total_vm_count_status, total_vm_count, monthly_vm_quota_status,
                               monthly_vm_quota, suspend_vm, quota_rest_for_user,
                               concurrent_connections_status, concurrent_connections, no_of_max_users_status,
                               no_of_max_users, max_vm_per_user_status, max_vm_per_user,
                               max_vm_auto_approve_per_user_status, max_vm_auto_approve_per_user,
                               vm_max_extension_count_status, vm_max_extension_count, extension_approval_status,
                               include_deleted_v_ms_for_max_v_ms_count_status)

        assert self.ct.verity_set_quota() == "Set Quota created Successfully", self.cl.info("Assertion Failed : Quota "
                                                                                            "not set")
        time.sleep(1)
        self.ct.extention_and_expiry_page(base_pack_name, base_pack_days, base_pack_minutes, default_basepack_status,
                                          autodelete_status, extension_pack_name, extension_pack_days,
                                          extension_pack_minutes, work_space_check_box_status)
        assert self.ct.verify_extension_and_expiry() == "Extension & Expiry details created successfully.", self.cl.info(
            (
                "Assertion "
                "Failed : "
                "Extension & Expiry details not set"))
        self.cl.info("extension and expiry data set successfully")
        time.sleep(1)
        self.ct.notification_setting_page(vm_expiry_warning_notification_1_status,
                                          vm_expiry_warning_notification_1_days,
                                          vm_expiry_warning_notification_2_status,
                                          vm_expiry_warning_notification_2_days,
                                          vm_expiry_warning_notification_3_status,
                                          vm_expiry_warning_notification_3_days,
                                          vm_expiry_remaining_hours_notification_1_status,
                                          vm_expiry_remaining_hours_notification_1_hours,
                                          vm_expiry_remaining_hours_notification_2_status,
                                          vm_expiry_remaining_hours_notification_2_hours,
                                          vm_expiry_remaining_hours_notification_3_status,
                                          vm_expiry_remaining_hours_notification_3_hours,
                                          vm_unutilized_warning_notification_days_status,
                                          vm_unutilized_warning_notification_days_days,
                                          enter_vm_decomission_after_expiry_status,
                                          enter_vm_decomission_after_expiry_days,
                                          vm_decomission_warning_notification_status,
                                          vm_decomission_warning_notification_days, togglestatus)

        assert self.ct.verify_notification_setting() == "Notification Settings updated Successfully", self.cl.info(
            "Assertion Failed : Notification Settings not updated")
        self.cl.info("notification set successfully")
        time.sleep(1)
        self.ct.summary_page()
        self.cl.info(
            "************  Test Case Ended : test_tenant_creation  **********")

    @pytest.mark.order(19)
    @pytest.mark.parametrize("mml_guided_lab_login",
                             Jsondatareader.get_data_from_json(UploadFile.json_data_file("\\MML_Data_File.json"),
                                                               "MML_GuidedLab_Data"))
    def test_guided_lab_user_login(self, mml_guided_lab_login):
        tenant_name, email_id, password, lab_type, catalog_name = mml_guided_lab_login
        self.cl.info(f"Data received from JSON File :{mml_guided_lab_login}")
        self.cl.info(
            "************  Test Case Started : test_guided_lab_user_login  **********")
        self.db.click_tenants()
        self.ct.search_tenant(tenant_name)
        self.ct.click_searched_tenant(tenant_name)
        self.ct.copy_tenant_url()
        self.ct.logout_super_admin()
        self.ct.visit_tenant_url()
        self.ct.login(email_id, password)
        self.db.click_do_not_show_again()
        self.db.click_machine_catalog2()
        self.mc.select_private_lab_type(lab_type)
        self.mc.search_catalog(catalog_name)
        self.mc.click_enroll_button()
        self.mc.click_my_labs_button()
        self.labs.visit_guidedlab_vm()
        assert self.labs.verify_guidedlab_vm() == "Stop", self.cl.info("VM page not reached")
        self.cl.info(
            "************  Test Case Ended : test_guided_lab_user_login  **********")
