import os
import time
import logging
from datetime import datetime
import pytest
import allure
import os
import sys

from Common_Packages.Base.read_application_url import ReadURL
from Common_Packages.Base.webdriverfactory import WebDriverFactory
from Common_Packages.Utility.custom_logger import custom_logger
from Make_My_Labs.pageObjects.dashboardpage import Dashboardpage
from ReCrewt.pageObject.HomePage import HomePage

# ------------------ DRIVER FIXTURES ------------------

@pytest.fixture(scope="function")
def tech_one_setup(request, browser):
    log = custom_logger()
    log.info("Running one-time setUp for Tech One")
    app_url = ReadURL.get_application_url("Techademy One info", "QA_URL")
    driver = WebDriverFactory(browser).get_web_driver_instance(app_url)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
    log.info("One-time tearDown complete for Tech One")

@pytest.fixture(scope="function")
def recrewt_setup(request, browser):
    log = custom_logger()
    log.info("Running one-time setUp for ReCREWt")
    app_url = ReadURL.get_application_url("ReCREWt info", "QA_URL")
    driver = WebDriverFactory(browser).get_web_driver_instance(app_url)
    if request.cls:
        request.cls.driver = driver
    yield driver
    try:
        HomePage(driver).logout()
    except Exception as e:
        log.error(f"Logout failed: {e}")
    driver.quit()
    log.info("One-time tearDown complete for ReCREWt")

@pytest.fixture(scope="function")
def tech_campus_setup(request, browser):
    log = custom_logger()
    log.info("Running one-time setUp for Tech Campus")
    app_url = ReadURL.get_application_url("Techademy Campus info", "QA_URL")
    driver = WebDriverFactory(browser).get_web_driver_instance(app_url)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
    log.info("One-time tearDown complete for Tech Campus")

@pytest.fixture(scope="function")
def Aeye_portal_setup(request, browser):
    log = custom_logger()
    log.info("Running one-time setUp for Aeye Portal")
    driver = WebDriverFactory(browser).get_web_driver_instance(ReadURL.get_application_url("Aeye portal info", "QA_URL"))
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
    log.info("Driver quit successfully")

@pytest.fixture(scope="function")
def mml_setup(request, browser):
    log = custom_logger()
    log.info("Running one-time setUp for Make My Labs")
    driver = WebDriverFactory(browser).get_web_driver_instance(ReadURL.get_application_url("Make My Labs info", "UAT_URL"))
    if request.cls:
        request.cls.driver = driver
    yield driver
    try:
        Dashboardpage(driver).logout()
    except Exception as e:
        log.error(f"Logout failed: {e}")
    driver.quit()
    log.info("One-time tearDown complete for Make My Labs")

# ------------------ CONFIG OPTIONS ------------------

# Force UTF-8 encoding for stdout/stderr on Windows
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser name: chrome/firefox")
    parser.addoption("--osType", help="Operating system type")
    parser.addoption("--runLocally", help="Set to 'yes' to run locally. Defaults to remote.")

@pytest.fixture(scope="session")
def browser(request):
    name = request.config.getoption("--browser") or "firefox"
    custom_logger().info(f"Using browser: {name}")
    return name

@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def run_locally(request):
    return request.config.getoption("--runLocally")

# ------------------ SCREENSHOT HOOK ------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(getattr(item, "instance", None), "driver", None)
        if driver:
            log = custom_logger()
            screenshots_dir = os.path.join(os.getcwd(), "Common_Packages", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = os.path.join(screenshots_dir, f"{item.name}_{timestamp}.png")
            try:
                driver.save_screenshot(file_path)
                log.info(f"Screenshot saved: {file_path}")
                allure.attach.file(file_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                log.error(f"Failed to capture screenshot: {e}")


#
# @pytest.fixture(autouse=True)
# def screenshot_on_failure(request):
#     """
#     Automatically takes a screenshot when a test fails,
#     before driver.quit() is called.
#     """
#     yield
#
#     rep_call = getattr(request.node, "rep_call", None)
#     if rep_call and rep_call.failed:
#         driver = request.node.funcargs.get("driver", None)
#         if driver:
#             screenshots_dir = os.path.join(os.getcwd(), "Common_Packages", "screenshots")
#             os.makedirs(screenshots_dir, exist_ok=True)
#
#             timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             test_name = request.node.name
#             file_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
#
#             try:
#                 driver.save_screenshot(file_path)
#                 logging.info(f"Screenshot saved: {file_path}")
#
#                 # Attach to Allure
#                 with open(file_path, "rb") as f:
#                     allure.attach(f.read(), name=test_name, attachment_type=allure.attachment_type.PNG)
#
#             except Exception as e:
#                 logging.error(f"Failed to take screenshot: {e}")
#         else:
#             logging.warning("Driver not available, screenshot skipped.")
