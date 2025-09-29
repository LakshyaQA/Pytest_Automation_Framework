import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta


class ForgotPasswordPage(Basepage, metaclass=Logmethodmeta):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cl = cl.custom_logger()

    # Locators
    _reset_password_button = "//button[contains(text(),'Reset Password')]"
    _back_to_login_button = "//button[contains(text(),'Back To Login')]"

    def click_reset_password_button(self):
        self.element_click(self._reset_password_button, locator_type="xpath")

    def click_back_to_login_button(self):
        self.element_click(self._back_to_login_button, locator_type="xpath")

    def verify_forget_password_link_sent(self):
        return self.get_text("//div[contains(text(),'Password Reset link sent. Please check your Email')]",
                             locator_type="xpath")

    def verify_unregistered_email_alert(self):
        return self.get_text("//div[contains(text(),'User matching query does not exist.')]",
                             locator_type="xpath")

    def verify_login_page(self):
        return self.get_text("//h1[contains(text(),'Login')]", "xpath")
