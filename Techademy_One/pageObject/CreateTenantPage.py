"""
    This page includes locators and functions on create tenant page

    """

import time

import allure

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Utility.exceldatareader import Exceldatareader
from Common_Packages.resources.ConfigPath import UploadFile
from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Techademy_One.configuration.read_properties import ReadConfig


class TenantDetails(Basepage):
    log = cl.custom_logger()
    # tenant_display_name_value = ReadConfig.get_tenant_display_name()
    # tenant_name1 = ReadConfig.get_tenant_name()
    # tenant_or_value = ReadConfig.get_tenant_org()
    # domain_value = ReadConfig.get_domain()
    # tenant_email_value = ReadConfig.get_tenant_email()
    # url_value = ReadConfig.get_tenant_url()
    # date_value = ReadConfig.get_date()
    # gst_value = ReadConfig.get_GST()
    # address_1_value = ReadConfig.get_address_1()
    # address_2_value = ReadConfig.get_address_2()
    # zipcode_value = ReadConfig.get_zip()
    # admin_first_name_value = ReadConfig.get_admin_first_name()
    # admin_last_name_value = ReadConfig.get_admin_last_name()
    # admin_email_value = ReadConfig.get_admin_email()
    # contact_value = ReadConfig.get_contact()
    # issuer_link_value = ReadConfig.get_issuerLink()
    path = UploadFile.file_upload_path('download.png')
    path_manual = UploadFile.file_upload_path('resume_dummy.pdf')
    # support_contact_value = ReadConfig.get_support_contact()
    # support_email_value = ReadConfig.get_support_email()
    # text_desc_value = ReadConfig.get_login_text_desc()
    # login_header_value = ReadConfig.get_login_header()
    tenant_name2 = SeleniumDriver.generate_random_name(Exceldatareader.read_column_from_excel("tenant_name"))
    tenant_name = tenant_name2


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators on page 1 - Details
    _tenant_name = "//*[@name='tenant_name']"
    _tenant_display_name = "//*[@name='display_name']"
    _tenant_organization = "//*[@name='tenant_organization']"
    _domain_name = "//*[@name='domain_name']"
    _tenant_email = "//*[@name='tenant_email']"
    _tenant_url = "//*[@name='tenant_url']"
    _activate_till_date = "//*[@name='active_till_date']"
    _gst_no = "//*[@name='gst_no']"
    _tenant_address_1 = "//*[@name='address.address_line_one']"
    _tenant_address_2 = "//*[@name='address.address_line_two']"
    _zip_code = "//*[@name='address.pincode']"
    _country_dropdown = "//*[@name='address.country' ]"
    _country_option = "//li[contains(@id,'option-100')]"
    _state_dropdown = "//*[@name='address.state' ]"
    _state_option = "//li[contains(@id,'option-20')]"
    _city_dropdown = "//*[@name='address.city' ]"
    _city_option = "//li[contains(@id,'option-424')]"
    _admin_first_name = "//*[@name='tenant_admin.0.first_name']"
    _admin_last_name = "//*[@name='tenant_admin.0.last_name']"
    _admin_email = "//*[@name='tenant_admin.0.email']"
    _admin_contact = "//*[@name='tenant_admin.0.contact_number']"
    _authenticate_type_dropdown = ("//*[@class = 'MuiSelect-select MuiSelect-outlined MuiInputBase-input "
                                   "MuiOutlinedInput-input css-pkbdyv']")
    _issuer_link = "//*[@name='auth_details.0.auth_config.issuer_url']"
    _CSM_dropdown = "//*[@name='csm_admins.0.csm_admin']"
    _CSM_option = "//li[contains(@id,'option-0')]"
    _account_manager_dropdown = "//*[@name='account_managers.0.account_manager']"
    _account_manager_option = "//li[contains(@id,'option-0')]"
    _save_btn = " //button[normalize-space()='Save and Next']"
    _back_btn = "//button[normalize-space()='Back']]"
    _authenticate_option = "//li[@data-value='0']"  # dropdown option

    # Locators on page 2 - Customize
    _upload_file = "//h6[contains(text(), 'Upload File')]/ancestor::div[contains(@class, 'MuiGrid-root') and contains(@class, 'css-2n3d0x')]//input"
    _upload_tenant_login_image = "//h6[contains(text(), 'Upload Tenant Login Image')]/ancestor::div[contains(@class, 'MuiGrid-root') and contains(@class, 'css-2n3d0x')]//input"
    _upload_user_manual = "//input[@type='file' and @accept='.pdf']"
    _login_text_header = "//*[@name='login_customization.login_header']"
    _login_text_desc = "//*[@name='login_customization.logon_text']"
    _support_phn_no = "//*[@name='support_information.support_no']"
    _support_email = "//*[@name='support_information.support_email']"
    _update_and_next = "//button[normalize-space()='Update and Next']"

    # Locators on page 3 - Plan
    _choose_enterprise = "//button[normalize-space()='Choose Enterprise Plan']"
    _choose_custom = "//button[normalize-space()='Choose Custom Plan']"
    _checkbox_click = "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"
    _confirmation_button = "//button[normalize-space()='Yes, Apply']"
    _update_tenant = "//button[normalize-space()='Update Tenant']"
    _unselect_lxp = "(//li[contains(@class, 'MuiListItem-root') and .//span[text()='LXP']]//input[@type='checkbox'])[2]"
    _tenant_with_same_name_msg = "//div[@id='notistack-snackbar' and contains(text(),'tenant_name: Tenant with given name already exists.')]"


    def enterTenantName(self, tenant_name):
        self.send_keys(tenant_name, self._tenant_name, locator_type="xpath")

    def enterTenantDisplayName(self, tenant_display_name):
        self.send_keys(tenant_display_name, self._tenant_display_name, locator_type="xpath")

    def enterTenantOrg(self, tenant_org):
        self.send_keys(tenant_org, self._tenant_organization, locator_type="xpath")

    def enterDomain(self, domain):
        self.send_keys(domain, self._domain_name, locator_type="xpath")

    def enterTenantEmail(self, t_email):
        self.send_keys(t_email, self._tenant_email, locator_type="xpath")

    def enterUrl(self, t_url):
        self.send_keys(t_url, self._tenant_url, locator_type="xpath")

    # Need to check if any other way to set the date
    def enterDate(self, ddmmyyyy):
        self.element_click(self._activate_till_date, locator_type="xpath")
        self.send_keys(ddmmyyyy, self._activate_till_date, locator_type="xpath")

    def enterGST(self, gstno):
        self.send_keys(gstno, self._gst_no, locator_type="xpath")

    def enterAddress1(self, address1):
        self.send_keys(address1, self._tenant_address_1, locator_type="xpath")

    def enterAddress2(self, address2):
        self.send_keys(address2, self._tenant_address_2, locator_type="xpath")

    def enterZip(self, zip_file):
        self.send_keys(zip_file, self._zip_code, locator_type="xpath")

    def selectCountry(self):
        self.select_element(self._country_dropdown, self._country_option, "xpath")

    def selectState(self):
        self.select_element(self._state_dropdown, self._state_option, locator_type="xpath")

    def selectCity(self):
        self.select_element(self._city_dropdown, self._city_option, locator_type="xpath")

    def enterAdminFirstname(self, f_name):
        self.send_keys(f_name, self._admin_first_name, locator_type="xpath")

    def enterAdminLastname(self, l_name):
        self.send_keys(l_name, self._admin_last_name, locator_type="xpath")

    def enterAdminEmail(self, a_email):
        self.send_keys(a_email, self._admin_email, locator_type="xpath")

    def enterContactNo(self, contact):
        self.send_keys(contact, self._admin_contact, locator_type="xpath")

    def selectAuthentication(self):
        self.select_element(self._authenticate_type_dropdown, self._authenticate_option, locator_type="xpath")

    def enterIssuerLink(self, issuer):
        self.send_keys(issuer, self._issuer_link, locator_type="xpath")

    def selectCSM(self):
        self.wait_till_element_invisibility("//div[@id='menu-auth_details.0.auth_type']","xpath")
        self.select_element(self._CSM_dropdown, self._CSM_option, locator_type="xpath")

    def selectAccManager(self):
        self.select_element(self._account_manager_dropdown, self._account_manager_option, locator_type="xpath")

    def clickOnSave(self):
        self.element_click_js(self._save_btn, locator_type="xpath")

    def clickOnBack(self):
        self.element_click(self._back_btn, locator_type="xpath")

    def EnterBasicDetails(self,tenant_display_name,tenant_org,tenant_domain,date,GST,address_1,address_2,zipcode,admin_first_name,admin_last_name,admin_email,contact):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.enterTenantName(self.tenant_name)
        self.enterTenantDisplayName(tenant_display_name)
        self.enterTenantOrg(tenant_org)
        self.enterDomain(tenant_domain)
        #self.enterTenantEmail(self.tenant_email_value)
        #self.enterUrl(self.url_value)
        self.enterDate(date)
        self.enterGST(GST)
        self.enterAddress1(address_1)
        self.enterAddress2(address_2)
        self.enterZip(zipcode)
        self.selectCountry()
        self.selectState()
        self.selectCity()
        self.web_scroll("down")
        self.enterAdminFirstname(admin_first_name)
        self.enterAdminLastname(admin_last_name)
        self.enterAdminEmail(admin_email)
        self.enterContactNo(contact)
        self.selectAuthentication()
        #self.enterIssuerLink(self.issuer_link_value)
        self.selectCSM()
        self.selectAccManager()
        self.web_scroll("up")
        self.clickOnSave()

    def enterLoginHeader(self, header):
        self.send_keys(header, self._login_text_header, locator_type="xpath")

    def enterTxtDesc(self, desc):
        self.send_keys(desc, self._login_text_desc, locator_type="xpath")

    def uploadTenantFile(self, path):
        self.log.info("Uploading file")
        self.wait_for_element(self._upload_file, "xpath")
        self.send_keys(path, self._upload_file, locator_type="xpath")


    def uploadTenantLogin(self, path):
        self.log.info("Uploading file")
        self.wait_for_element(self._upload_tenant_login_image, "xpath")
        self.send_keys(path, self._upload_tenant_login_image, locator_type="xpath")

    def uploadManual(self, path):
        self.log.info("Uploading file")
        self.wait_for_element(self._upload_user_manual, "xpath")
        self.send_keys(path, self._upload_user_manual, locator_type="xpath")

    def enterSupportContact(self, s_contact):
        self.send_keys(s_contact, self._support_phn_no, locator_type="xpath")

    def enterSupportEmail(self, s_email):
        self.send_keys(s_email, self._support_email, locator_type="xpath")

    # Choose plan page

    def clickEnterprisePlan(self):

        self.log.info("Waiting for 'Choose Enterprise Plan' button to be clickable...")
        self.wait_for_element(self._choose_enterprise, locator_type="xpath", timeout=20)
        self.log.info("'Choose Enterprise Plan' button found. Clicking...")
        self.element_click_js(self._choose_enterprise, locator_type="xpath")

    def clickCustomPlan(self):
        self.wait_for_element(self._choose_custom, "xpath")
        self.element_click(self._choose_custom, locator_type="xpath")

    def ClickOnConfirmation(self):
        self.element_click_js(self._confirmation_button, locator_type="xpath")

    def unselectLxp(self):
        self.element_click_js(self._unselect_lxp,"xpath")

    def clickUpdateAndNext(self):
        self.element_click_js(self._update_and_next, locator_type="xpath")

    def clickUpdateTenant(self):
        self.element_click_js(self._update_tenant, locator_type="xpath")

    def CustomizationDetails(self,support_contact,support_email,login_text_desc,login_header):
        time.sleep(1)
        self.enterLoginHeader(login_header)

        time.sleep(1)
        self.enterTxtDesc(login_text_desc)

        self.uploadTenantFile(self.path)

        self.uploadTenantLogin(self.path)
        self.uploadManual(self.path_manual)
        self.web_scroll("down")
        self.enterSupportEmail(support_email)
        self.enterSupportContact(support_contact)
        self.clickUpdateAndNext()


    def SelectPlan(self):
        self.clickCustomPlan()
        self.ClickOnConfirmation()
        self.unselectLxp()
        time.sleep(7)
        self.clickUpdateTenant()

    def VerifyTenantCreation(self):
        self.verify_by_comparing_text(locator="//h6[contains(text(),'"+self.tenant_name+"')]", locator_type="xpath",
                                      expected_result=self.tenant_name, result_msg="CreateTenant")


    def verifyTenantWithSameName(self):
        self.verify_by_element_presence(self._tenant_with_same_name_msg,"xpath","TenantWithSameName")