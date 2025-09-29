import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class CreateNotification(Basepage):
    log = cl.custom_logger()

    '''
            This class includes the creation of notification across the user roles available.

            author: Abhilash

            '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating the notification

    megaphone_symbol = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall "
                        "css-13mhdve'])[2]")
    notification_name = "//input[@name='name']"
    description_field = "//textarea[@name='description']"
    send_invites_field = "//input[@type='search']"
    option_selection = "//li[contains(text(), 'student@campusqa.in')]"
    DropFile_field = "//div[@class='dropzone']"
    create_button = "//button[text()='Create']"
    result_notification = "//div[text()='Notification created successfully']"

    def clickOnSymbol(self):
        self.wait_for_element(self.megaphone_symbol, locator_type="xpath")
        self.element_click(self.megaphone_symbol, "xpath")

    def clickOnNotificationName(self):
        self.element_click_js(self.notification_name, "xpath")

    def clickOnDescription(self):
        self.element_click_js(self.description_field, "xpath")

    def clickOnSendInvites(self):
        self.wait_for_element(self.send_invites_field, locator_type="xpath")
        self.element_click_js(self.send_invites_field, "xpath")

    def clickOnDropFile(self):
        self.element_click_js(self.DropFile_field, "xpath")

    def enterNotificationName(self, name):
        self.send_keys(name, self.notification_name, "xpath")

    def enterDescription(self, desc):
        self.send_keys(desc, self.description_field, "xpath")

    def selectOptionElement(self):
        self.element_click(self.send_invites_field, "xpath")
        self.element_click(self.option_selection, "xpath")

    def clickOnCreate(self):
        self.element_click_js(self.create_button, "xpath")

    def create_notification(self, name, desc):
        self.clickOnSymbol()
        self.clickOnNotificationName()
        self.enterNotificationName(name)
        self.clickOnDescription()
        self.enterDescription(desc)
        self.clickOnSendInvites()
        self.selectOptionElement()
        self.clickOnCreate()

    def create_notification_verification(self):
        self.wait_for_element(self.result_notification, "xpath")
        self.is_element_displayed(self.result_notification, "xpath")
