from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.custom_metaclass import Logmethodmeta


class Loginpage(Basepage, metaclass=Logmethodmeta):

    def __init__(self, driver):
        super().__init__(driver)

    login_button = "//button[@type='button' and @class='ant-btn ant-btn-primary qa-login-btn']"
    email_id_field = "//div[@class='placeholderContainer']//input[@type='email']"
    password_field = "//div[@class='placeholderContainer']//input[@name='passwd']"
    next_button = "//div[@class='inline-block button-item ext-button-item']//input[@type='submit']"
    signin_button = "//div[@class='inline-block button-item ext-button-item']//input[@type='submit']"
    welcome_text = "//div[@class='mml-title']//div"

    def click_login_button(self):
        self.element_click(self.login_button, locator_type="xpath")

    def enter_email(self, email):
        self.send_keys(email, self.email_id_field, locator_type="xpath")

    def click_next_button(self):
        self.element_click_js(self.next_button, locator_type="xpath")

    def enter_password(self, password):
        self.send_keys(password, self.password_field, locator_type="xpath")

    def click_signin_button(self):
        self.element_click_js(self.signin_button, locator_type="xpath")

    def login(self, email, password):
        self.wait_for_element(self.login_button, locator_type="xpath")
        self.click_login_button()
        self.wait_for_element(self.email_id_field, locator_type="xpath")
        self.enter_email(email)
        self.wait_for_element(self.next_button, locator_type="xpath")
        self.click_next_button()
        self.wait_for_element(self.password_field, locator_type="xpath")
        self.enter_password(password)
        self.wait_for_element(self.password_field, locator_type="xpath")
        self.click_signin_button()

    def get_welcome_text_login(self):
        return self.get_text(self.welcome_text, locator_type="xpath")
