import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
config = configparser.RawConfigParser()
properties = configparser.RawConfigParser()
test = str(BASE_DIR)
config.read(test + "//configuration//configs.ini")


# config.read("C:/Users/GS-2155/PycharmProjects/pythonProject3/Configurations/logging.config")
# config.read("../Configurations/logging.config")"


class ReadConfig:

    @staticmethod
    def get_url(section, opt):
        url = config.get(section, opt)
        return url

    @staticmethod
    def get_username(section, opt):
        username = config.get(section, opt)
        return username

    @staticmethod
    def get_password(section, opt):
        password = config.get(section, opt)
        return password

    @staticmethod
    def get_emailid():
        email_id = properties.get('User Management', 'email_id')
        return email_id

    @staticmethod
    def get_mobile_number():
        mobile_number = properties.get('User Management', 'mobile_number')
        return mobile_number

    @staticmethod
    def get_auto_tenant_admin():
        username = config.get('Automation tenant admin', 'username')
        return username

    @staticmethod
    def get_auto_tenant_admin_pswd():
        password = config.get('Automation tenant admin', 'password')
        return password

    # Following methods are used for tenant creation
    @staticmethod
    def get_tenant_name():
        tenant_name = config.get('Tenant Creation', 'tenant_name')
        return tenant_name

    @staticmethod
    def get_tenant_display_name():
        tenant_display_name = config.get('Tenant Creation', 'tenant_display_name')
        return tenant_display_name

    @staticmethod
    def get_tenant_org():
        tenant_org = config.get('Tenant Creation', 'tenant_org')
        return tenant_org

    @staticmethod
    def get_domain():
        tenant_domain = config.get('Tenant Creation', 'tenant_domain')
        return tenant_domain

    @staticmethod
    def get_tenant_email():
        tenant_email = config.get('Tenant Creation', 'tenant_email')
        return tenant_email

    @staticmethod
    def get_tenant_url():
        tenant_url = config.get('Tenant Creation', 'tenant_url')
        return tenant_url

    @staticmethod
    def get_date():
        date = config.get('Tenant Creation', 'date')
        return date

    @staticmethod
    def get_GST():
        gst = config.get('Tenant Creation', 'gst')
        return gst

    @staticmethod
    def get_address_1():
        address_1 = config.get('Tenant Creation', 'address_1')
        return address_1

    @staticmethod
    def get_address_2():
        address_2 = config.get('Tenant Creation', 'address_2')
        return address_2

    @staticmethod
    def get_zip():
        zipcode = config.get('Tenant Creation', 'zipcode')
        return zipcode

    @staticmethod
    def get_admin_first_name():
        admin_first_name = config.get('Tenant Creation', 'admin_first_name')
        return admin_first_name

    @staticmethod
    def get_admin_last_name():
        admin_last_name = config.get('Tenant Creation', 'admin_last_name')
        return admin_last_name

    @staticmethod
    def get_admin_email():
        admin_email = config.get('Tenant Creation', 'admin_email')
        return admin_email

    @staticmethod
    def get_contact():
        contact = config.get('Tenant Creation', 'contact')
        return contact

    @staticmethod
    def get_issuerLink():
        issuer_link = config.get('Tenant Creation', 'issuer_link')
        return issuer_link

    @staticmethod
    def get_support_contact():
        support_contact = config.get('Tenant Creation', 'support_contact')
        return support_contact

    @staticmethod
    def get_support_email():
        support_email = config.get('Tenant Creation', 'support_email')
        return support_email

    @staticmethod
    def get_login_text_desc():
        login_text_desc = config.get('Tenant Creation', 'login_text_desc')
        return login_text_desc

    @staticmethod
    def get_login_header():
        login_header = config.get('Tenant Creation', 'login_header')
        return login_header

    @staticmethod
    def get_tenant():  # This will return tenant which we will use for testing
        tenant = config.get('Tenant details', 'tenant')
        return tenant

    @staticmethod
    def get_role_grp_name(section, opt):  # create role group for superadmin
        role_grp_name = config.get(section, opt)
        return role_grp_name

    @staticmethod
    def get_bu_name(section, opt):  # Create BU for superadmin
        bu_name = config.get(section, opt)
        return bu_name

    @staticmethod
    def get_bu_desc():
        bu_desc = config.get('Business Unit', 'bu_desc')
        return bu_desc

    @staticmethod
    def get_role_grp():
        role_grp = config.get('Business Unit', 'role_grp')
        return role_grp

    # Following methods will be used for user creation for superadmin flow
    @staticmethod
    def get_first_name(section, opt):
        first_name = config.get(section, opt)
        return first_name

    @staticmethod
    def get_last_name(section, opt):
        last_name = config.get(section, opt)
        return last_name

    @staticmethod
    def get_email(section, opt):
        email = config.get(section, opt)
        return email
    @staticmethod
    def get_grp_name(section,opt):
        grp_name = config.get(section,opt)
        return grp_name

    @staticmethod
    def get_grp_desc(section, opt):
        grp_name = config.get(section, opt)
        return grp_name

    # following methods are to get expected results of test cases
    @staticmethod
    def get_expected_result(section, opt):
        tenant_creation_result = config.get(section, opt)
        return tenant_creation_result

    @staticmethod
    def get_Report_name(section, opt):
        Report_name = config.get(section, opt)
        return Report_name

    @staticmethod
    def get_Start_date():
        Start_date = config.get('Report', 'start_date')
        return Start_date

    @staticmethod
    def get_End_date():
        end_date = config.get('Report', 'end_date')
        return end_date

    @staticmethod
    def get_Start_date1():
        Start_date1 = config.get('Report', 'start_date1')
        return Start_date1

    @staticmethod
    def get_End_date1():
        End_date1 = config.get('Report', 'end_date1')
        return End_date1


    @staticmethod
    def get_start_date():
        Start_date = config.get('Audit Logs', 'start_date')
        return Start_date

    @staticmethod
    def get_end_date():
        end_date = config.get('Audit Logs', 'end_date')
        return end_date

      # following methods are to Create Notification
    @staticmethod
    def get_notification_title(section, opt):
        notification_title = config.get(section, opt)
        return notification_title

    @staticmethod
    def get_description(section, opt):
        description = config.get(section, opt)
        return description
