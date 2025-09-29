from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.Util import Util
from Common_Packages.Utility.custom_logger import custom_logger


class Basepage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()
        self.log = custom_logger()
