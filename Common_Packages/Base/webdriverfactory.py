from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser.lower()

    def get_web_driver_instance(self, app_url, PAGE_LOAD_TIMEOUT=5):

        if self.browser == "iexplorer":
            # Internet Explorer setup
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            # Firefox setup
            options = FirefoxOptions()
            # options.headless = True
            options.set_preference("browser.download.folderList", 2)  # Prompt for download location
            options.set_preference("browser.download.useDownloadDir", False)  # Prompt for download location

            try:
                driver = webdriver.Firefox(options=options)
            except Exception as e:
                raise RuntimeError(f"WebDriver failed to initialize: {e}")

        elif self.browser == "chrome":
            # Chrome setup
            options = ChromeOptions()
            options.add_argument("--incognito")
            options.add_argument("--window-size=1920,1080")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

            # options.headless = True
            try:
                driver = webdriver.Chrome(options=options)
            except Exception as e:
                raise RuntimeError(f"WebDriver failed to initialize: {e}")
        else:
            # Default to Firefox
            options = FirefoxOptions()
            # options.headless = True
            options.set_preference("browser.download.folderList", 2)  # Prompt for download location
            options.set_preference("browser.download.useDownloadDir", False)  # Prompt for download location
            try:
                driver = webdriver.Firefox(options=options)
            except Exception as e:
                raise RuntimeError(f"WebDriver failed to initialize: {e}")

        # Common setup
        driver.implicitly_wait(4)
        driver.maximize_window()
        driver.get(app_url)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        return driver
