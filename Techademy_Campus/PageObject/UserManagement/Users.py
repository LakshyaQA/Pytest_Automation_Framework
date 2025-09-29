import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class Users(Basepage):
    log = cl.custom_logger()

    '''
        This class includes creating/searching of the Users in the HR role under User Management feature.

        author: Abhilash

        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating, searching a user

    manage_tab = "//button[@id='basic-button']"
    UserManagement_option = "//span[text()='User Management']"
    CreateUser_button = "//button[text()='Create a user']"
    salutation_dropdown = ("(//div[@class='MuiSelect-select MuiSelect-outlined "
                           "MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputMultiline "
                           "MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-7987uh'])[1]")
    salutation_option = "//li[text()='Mr']"
    firstname_field = "//input[@name='first_name']"
    lastname_field = "//input[@name='last_name']"
    MobileNo_field = "//input[@name='contact_no']"
    EmailID_field = "//input[@name='email']"
    gender_dropdown = ("(//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input "
                       "MuiInputBase-inputMultiline MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd "
                       "css-7987uh'])[2]")
    gender_option = "//li[text()='Male']"
    maritalstatus_dropdown = ("(//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input "
                              "MuiOutlinedInput-input MuiInputBase-inputMultiline MuiInputBase-inputSizeSmall "
                              "MuiInputBase-inputAdornedEnd css-7987uh'])[3]")
    maritalstatus_option = "//li[text()='Married']"
    birthdate_field = "//input[@type='tel']"
    UserRole_dropdown = ("(//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input "
                         "MuiInputBase-inputMultiline MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd "
                         "css-7987uh'])[4]")
    faculty_option = "//li[text()='Faculty']"
    hod_option = "//li[text()='Hod']"
    cluster_dropdown = "//div[@name='cluster']"
    department_dropdown = "//div[@name='department']"
    cluster_option = "//li[text()='Medical Science']"
    department_option = "//li[text()='General Medicine']"
    submit_button = "(//button[@type='submit'])[2]"
    usercreation_successmessage = "//div[contains(text(), 'Staff Onboarded Successfully.')]"
    UserSearch_bar = "//input[@id='search-bar']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnUserManagement(self):
        self.wait_for_element(self.UserManagement_option, locator_type="xpath")
        self.element_click_js(self.UserManagement_option, "xpath")

    def clickOnCreateUserButton(self):
        self.element_click_js(self.CreateUser_button, "xpath")

    def clickOnSalutationDropdown(self):
        self.wait_for_element(self.salutation_dropdown, "xpath")
        self.element_click(self.salutation_dropdown, "xpath")

    def clickOnFirstName_field(self):
        self.wait_for_element(self.firstname_field, "xpath")
        self.element_click_js(self.firstname_field, "xpath")

    def clickOnLastName_field(self):
        self.wait_for_element(self.lastname_field, "xpath")
        self.element_click_js(self.lastname_field, "xpath")

    def clickOnMobileNo_field(self):
        self.wait_for_element(self.MobileNo_field, "xpath")
        self.element_click_js(self.MobileNo_field, "xpath")

    def clickOnEmailID_field(self):
        self.wait_for_element(self.EmailID_field, "xpath")
        self.element_click_js(self.EmailID_field, "xpath")

    def clickOnClusterDropdown(self):
        self.element_click(self.cluster_dropdown, "xpath")
        self.element_click(self.cluster_option, "xpath")

    def clickOnDepartmentDropdown(self):
        self.element_click(self.department_dropdown, "xpath")
        self.element_click(self.department_option, "xpath")

    def selectSalutationOption(self):
        self.element_click(self.salutation_dropdown, "xpath")
        self.element_click(self.salutation_option, "xpath")

    def enterFirstName_field(self, f_name):
        self.send_keys(f_name, self.firstname_field, "xpath")

    def enterLastName_field(self, l_name):
        self.send_keys(l_name, self.lastname_field, "xpath")

    def enterMobileNo_field(self, phone):
        self.send_keys(phone, self.MobileNo_field, "xpath")

    def enterEmailID_field(self, email):
        self.send_keys(email, self.EmailID_field, "xpath")

    def selectGenderOption(self):
        self.element_click(self.gender_dropdown, "xpath")
        self.wait_for_element(self.gender_option, "xpath")
        self.element_click(self.gender_option, "xpath")

    def selectUserRole_option(self):
        self.element_click(self.UserRole_dropdown, "xpath")
        self.wait_for_element(self.hod_option, "xpath")
        self.element_click(self.hod_option, "xpath")

    def clickOnSubmitButton(self):
        self.element_click(self.submit_button, "xpath")

    def clickOnSearchbar(self):
        self.wait_for_element(self.UserSearch_bar, locator_type="xpath")
        self.element_click(self.UserSearch_bar, "xpath")

    def enterUserInSearchbar(self, search_user):
        self.send_keys(search_user, self.UserSearch_bar, "xpath")

    def clickOnUserManagementOption(self):
        self.clickOnManageTab()
        self.clickOnUserManagement()

    def create_user(self, f_name, l_name, phone, email):
        self.clickOnCreateUserButton()
        self.clickOnSalutationDropdown()
        self.selectSalutationOption()
        self.clickOnFirstName_field()
        self.enterFirstName_field(f_name)
        self.clickOnLastName_field()
        self.enterLastName_field(l_name)
        self.clickOnMobileNo_field()
        self.enterMobileNo_field(phone)
        self.clickOnEmailID_field()
        self.enterEmailID_field(email)
        self.selectGenderOption()
        self.selectUserRole_option()
        self.clickOnClusterDropdown()
        self.clickOnDepartmentDropdown()
        self.clickOnSubmitButton()

    def searchTheUser(self, search_user):
        self.clickOnSearchbar()
        self.enterUserInSearchbar(search_user)
