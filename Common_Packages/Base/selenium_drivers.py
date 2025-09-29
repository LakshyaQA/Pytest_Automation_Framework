import inspect
import random
import string
import time
import os
import logging
from datetime import datetime, timedelta
from typing import Optional, Tuple, Any, List

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webelement import WebElement

try:
    # pynput may not be available in CI/headless environments; only use as fallback
    from pynput.keyboard import Controller, Key

    PYNPUT_AVAILABLE = True
except Exception:
    PYNPUT_AVAILABLE = False

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
    ElementNotInteractableException,
    ElementNotSelectableException,
)

from Common_Packages.Utility.custom_logger import custom_logger


class SeleniumDriver:
    """Refactored SeleniumDriver utility class.

    Major improvements:
      - Fixed deprecated/incorrect exception usage
      - Safer file upload/download (prefers send_keys to <input type=file>)
      - Fixed frame switching and JS/send_keys usage bugs
      - Consolidated duplicate methods and added small optimizations
      - Improved logging and error handling
    """

    search_bar_xpath = (
        "//div[@class='MuiInputBase-root MuiOutlinedInput-root "
        "MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-adornedEnd css-nibknj']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.log = custom_logger() if callable(custom_logger) else logging.getLogger(__name__)
        self.invite_link: Optional[str] = None

    # ---------------------------- Screenshots & Allure ----------------------------
    def screen_shot(self, result_message: str) -> str:
        """
        Take a screenshot and save it in the fixed screenshots folder.
        Returns the full path to the screenshot file.
        """
        # Determine project root dynamically (two levels up from Common_Packages folder)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_directory = os.path.join(os.getcwd(), "Common_Packages", "screenshots")
        os.makedirs(screenshot_directory, exist_ok=True)

        # Unique filename using epoch milliseconds
        file_name = f"{result_message}.{round(time.time() * 1000)}.png"
        destination_file = os.path.join(screenshot_directory, file_name)

        try:
            self.driver.save_screenshot(destination_file)
            self.log.info(f"Screenshot saved successfully: {destination_file}")
            # Attach directly to Allure report
            self.attach_screenshot_to_allure(destination_file, name=result_message)
            return destination_file
        except Exception as e:
            self.log.exception(f"Failed to take screenshot: {e}")
            raise

    def attach_screenshot_to_allure(self, screenshot_path: str, name: str = "Screenshot") -> None:
        """
        Attach screenshot to Allure report.
        """
        try:
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name=name, attachment_type=AttachmentType.PNG)
                self.log.info(f"Attached screenshot to Allure: {name}")
        except Exception as e:
            self.log.exception(f"Failed to attach screenshot to Allure: {e}")
            raise

    # ---------------------------- Basic helpers ----------------------------
    def get_title(self) -> str:
        return self.driver.title

    def get_by_type(self, locator_type: str) -> Any:
        locator_type = (locator_type or "").lower()
        mapping = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "link": By.LINK_TEXT,
        }
        by = mapping.get(locator_type)
        if not by:
            self.log.info(f"Locator type '{locator_type}' not supported")
            return False
        return by

    def get_element(self, locator: str, locator_type: str = "id"):
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(f"Element found with locator: {locator} and locatorType: {locator_type}")
            return element
        except Exception as e:
            self.log.exception(e)
            raise

    def get_element_list(self, locator: str, locator_type: str = "id") -> List:
        try:
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.log.info(f"Element list found with locator: {locator} and locatorType: {locator_type}")
            return elements
        except Exception as e:
            self.log.exception(e)
            raise

    # ---------------------------- Actions ----------------------------
    def element_click(self, locator: str, locator_type: str = "id",
                      wait_for_clickable: bool = True, timeout: int = 5) -> None:
        try:
            if wait_for_clickable:
                element = self.wait_until_clickable(locator, locator_type, timeout)
                if not element:
                    raise TimeoutException(f"Element '{locator}' not clickable within {timeout}s")
            else:
                element = self.get_element(locator, locator_type)

            element.click()
            self.log.info(f"[OK] Clicked element: {locator} (type: {locator_type})")
        except ElementNotInteractableException:
            self.log.warning(f"Element not interactable, trying JS click: {locator}")
            self.element_click_js(locator, locator_type)
        except Exception as e:
            self.log.exception(f"Failed to click element '{locator}': {e}")
            raise

    def send_keys(self, data: str, locator: str = "", locator_type: str = "id",
                  element=None, clear_first: bool = True) -> None:
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            if not element:
                raise ValueError("No element provided for send_keys")

            if clear_first:
                element.clear()

            element.send_keys(data)
            self.log.info(f"[OK] Sent data to element: {locator} (type: {locator_type}) - Data: {data}")
        except Exception as e:
            self.log.exception(f"Failed to send keys to '{locator}': {e}")
            raise

    def get_text(self, locator: str = "", locator_type: str = "id", element=None, info: str = "") -> Optional[str]:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            text = element.text or element.get_attribute("innerText") or ""
            if text:
                self.log.info(f"Getting text on element :: {info}")
                text = text.strip()
            return text
        except Exception as e:
            self.log.exception(e)
            raise

    # ---------------------------- Presence/Visibility checks ----------------------------
    def is_element_present(self, locator: str = "", locator_type: str = "id", element=None) -> bool:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            exists = element is not None
            self.log.info(f"Element present: {exists} - locator: {locator} type: {locator_type}")
            return exists
        except Exception:
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator: str = "", locator_type: str = "id", element=None) -> bool:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            is_displayed = bool(element and element.is_displayed())
            self.log.info(f"Element is_displayed: {is_displayed} - locator: {locator}")
            return is_displayed
        except Exception as e:
            self.log.exception(e)
            return False

    def element_presence_check(self, locator: str, by_type: Any) -> bool:
        try:
            element_list = self.driver.find_elements(by_type, locator)
            present = len(element_list) > 0
            self.log.info(f"Element present: {present} - locator: {locator} by_type: {by_type}")
            return present
        except Exception as e:
            self.log.exception(e)
            raise

    # ---------------------------- Waits ----------------------------
    def wait_until_clickable(self, locator: str, locator_type: str = "id", timeout: int = 5,
                             poll_frequency: float = 0.2):
        try:

            by_type = self.get_by_type(locator_type)
            self.log.info(f"Waiting up to {timeout}s for element '{locator}' to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, WebDriverException,
                                                     ElementNotInteractableException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            return element
        except TimeoutException:
            self.log.warning(f"Element '{locator}' not clickable after {timeout} seconds.")
            return None
        except Exception as e:
            self.log.exception(f"Exception while waiting for element: {e}")
            return None

    def wait_until_visible(self, locator: str, locator_type: str = "id", timeout: int = 5,
                           poll_frequency: float = 0.2):
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info(f"Waiting up to {timeout}s for element '{locator}' to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[
                                     NoSuchElementException,
                                     WebDriverException,
                                     ElementNotInteractableException,
                                     ElementNotSelectableException
                                 ])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            return element
        except TimeoutException:
            self.log.warning(f"Element '{locator}' not visible after {timeout} seconds.")
            return None
        except Exception as e:
            self.log.exception(f"Exception while waiting for element: {e}")
            return None

    def wait_till_element_invisibility(self, locator: str, locator_type: str = "id", timeout: int = 10,
                                       poll_frequency: float = 0.2):
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info(f"Waiting up to {timeout}s for element '{locator}' to become invisible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotInteractableException,
                                                     ElementNotSelectableException])
            return wait.until(EC.invisibility_of_element_located((by_type, locator)))
        except Exception as e:
            self.log.exception(e)
            return False

    # ---------------------------- Scrolling ----------------------------
    def web_scroll(self, pixels: int = 1000, direction: str = "down") -> None:
        offset = pixels if direction == "down" else -pixels
        self.driver.execute_script(f"window.scrollBy(0, {offset});")

    def scroll_by_visible_element(self, locator: str, locator_type: str = "id") -> None:
        element = self.get_element(locator, locator_type)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_by_visible_element_by_webelement(self, element) -> None:
        # kept for backward compatibility
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # ---------------------------- File upload / download ----------------------------
    def upload_file(self, file_path: str, locator: str = "", locator_type: str = "id",
                    element: WebElement = None) -> None:
        """
        Upload file to an input[type=file] element if possible,
        otherwise fallback to keyboard automation for native dialogs.
        """
        try:
            if locator and not element:
                element = self.get_element(locator, locator_type)

            if not element:
                raise ValueError("No element provided for file upload")

            tag = element.get_attribute("tagName").lower()
            input_type = (element.get_attribute("type") or "").lower()

            if tag == "input" and input_type == "file":
                element.send_keys(file_path)
            else:
                if not PYNPUT_AVAILABLE:
                    raise EnvironmentError("pynput not available for native dialog interaction")
                element.click()
                time.sleep(1)
                keyboard = Controller()
                keyboard.type(file_path)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(1)

            self.log.info(f"File uploaded successfully: {file_path}")
        except Exception as e:
            self.log.exception(f"File upload failed: {file_path} - {e}")
            raise

    def download_file(self, path: str, locator: str = "", locator_type: str = "id", file_name: str = "",
                      element=None) -> None:
        """
        Trigger download and optionally wait for file to appear.
        Prefer configuring browser prefs for automatic downloads.
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                element.click()

            if file_name:
                file_path = os.path.join(path, file_name)
                timeout = 30
                elapsed = 0
                while elapsed < timeout:
                    if os.path.isfile(file_path):
                        self.log.info(f"Downloaded file found: {file_path}")
                        break
                    time.sleep(1)
                    elapsed += 1
                else:
                    self.log.warning(f"Download not found after {timeout}s: {file_path}")

            self.log.info(f"File download triggered at: {path}")
        except Exception as e:
            self.log.exception(f"Error during file download: {e}")
            raise

    # ---------------------------- Selection helpers ----------------------------
    def select_element_keyboard(self, option: str, locator: str = "", locator_type: str = "id", element=None) -> None:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            element.send_keys(option)
            element.send_keys(Keys.UP)
            element.send_keys(Keys.ENTER)
            self.log.info(f"Sent data on element with locator: {locator} locatorType: {locator_type}")
        except Exception as e:
            self.log.exception(e)
            raise

    def select_element(self, locator: str = "", option_locator: str = "", locator_type: str = "id",
                       element=None) -> None:
        try:
            if locator:
                dropdown_element = self.get_element(locator, locator_type)
                dropdown_element.click()
                self.wait_for_element(option_locator, locator_type)
                option_element = self.get_element(option_locator, locator_type)
                option_element.click()
                self.log.info(f"Selected option in dropdown: locator={locator}")
        except Exception as e:
            self.log.exception(e)
            raise

    def switch_to_frames(self, locator: str = "", locator_type: str = "id", element=None) -> None:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            self.driver.switch_to.frame(element)
            self.log.info(f"Switched to frame: locator={locator}")
        except Exception as e:
            self.log.exception(e)
            raise

    def element_click_js(self, locator: str = "", locator_type: str = "id", element=None) -> None:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            self.driver.execute_script("arguments[0].click();", element)
            self.log.info(f"Clicked on element (JS) with locator: {locator}")
        except Exception as e:
            self.log.exception(e)
            raise

    def switch_to_new_window(self) -> None:
        try:
            new_tab_handle = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_tab_handle)
            self.log.info("Switched to newest window/tab")
        except Exception as e:
            self.log.exception(e)
            raise

    def switch_to_old_window(self) -> None:
        try:
            old_tab_handle = self.driver.window_handles[0]
            self.driver.switch_to.window(old_tab_handle)
            self.log.info("Switched to first window/tab")
        except Exception as e:
            self.log.exception(e)
            raise

    def sendkeys_js(self, data: str, locator: str = "", locator_type: str = "id", element=None) -> None:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            self.driver.execute_script("arguments[0].value = arguments[1]", element, data)
            self.log.info(f"Set value (JS) on locator: {locator} data: {data}")
        except Exception as e:
            self.log.exception(e)
            raise

    def sendkeys_multi_value(self, data: str, locator: str = "", locator_type: str = "id", element=None) -> None:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            element.send_keys(data)
            element.send_keys(Keys.ENTER)
            self.log.info(f"Sent multi value on locator: {locator}")
        except Exception as e:
            self.log.exception(e)
            raise

    # ---------------------------- Small utilities ----------------------------
    @staticmethod
    def generate_random_name(name: str) -> str:
        random_name = ''.join(random.choices(string.ascii_lowercase, k=4))
        return f"{name}{random_name}"

    def select_dropdown_by_name(self, name: str, drop_down_xpath: str, list_xpath: str) -> None:
        try:
            dropdown = self.driver.find_element(By.XPATH, drop_down_xpath)
            self.driver.execute_script("arguments[0].click();", dropdown)
            time.sleep(0.3)
            dropdown.send_keys(name)
            time.sleep(0.3)
            drop_down_list = self.driver.find_elements(By.XPATH, list_xpath)
            for option in drop_down_list:
                option_text = option.text
                if option_text == name:
                    option.click()
                    self.log.info(f"Option '{name}' selected from the dropdown.")
                    break
            else:
                self.log.info(f"Option '{name}' not found in the dropdown.")
        except NoSuchElementException as e:
            self.log.exception(e)
            raise

    def get_current_date_and_time(self, hours_offset: int) -> str:
        later = datetime.now() + timedelta(hours=hours_offset)
        return later.strftime("%m/%d/%Y %I:%M %p")

    def get_current_date(self, days_count: int) -> str:
        return (datetime.now().date() + timedelta(days=days_count)).strftime("%m/%d/%Y")

    def get_current_ddmmyyyy(self, count: int) -> str:
        return (datetime.now().date() + timedelta(days=count)).strftime("%d/%m/%Y")

    def get_url(self) -> str:
        return self.driver.current_url

    def get_page_source(self) -> str:
        return self.driver.page_source

    def convert_text_to_int(self, text: str) -> int:
        self.log.info(f"Returning int value for text {text}")
        return int(text)

    def split_text(self, text: str, symbol: str) -> Tuple[str, str, str]:
        parts = text.split(symbol)
        part1 = parts[0] if len(parts) > 0 else ""
        part2 = parts[1] if len(parts) > 1 else ""
        part3 = parts[2] if len(parts) > 2 else ""
        return part1, part2, part3

    def wait_for_page_load(self, timeout: int = 20) -> None:
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            self.log.info("Page loaded successfully.")
        except Exception as e:
            self.log.exception(e)

    def get_caller_method_name(self) -> str:
        frame = inspect.currentframe().f_back
        return frame.f_code.co_name

    def clear_input_field(self, locator: str = "", locator_type: str = "id", element=None) -> None:
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.clear()
            self.log.info("Input field cleared successfully.")
        except Exception as e:
            self.log.exception(e)
            raise

    def element_click_by_webelement(self, element) -> None:
        try:
            element.click()
            self.log.info("Clicked on element")
        except Exception as e:
            self.log.exception("Failed to click on element")
            raise

    def refresh_page(self) -> None:
        self.driver.refresh()

    def copy_invite(self, locator: str = "", locator_type: str = "id") -> None:
        self.invite_link = self.get_text(locator, locator_type)
        self.log.info("Invite Link copied")

    def open_invite_link(self) -> None:
        if not self.invite_link:
            raise ValueError("Invite link not set. Call copy_invite first.")
        self.driver.get(self.invite_link)
        self.log.info(f"Going to {self.invite_link}")

    def visit_url(self, url: str) -> None:
        self.driver.get(url)
        self.log.info(f"Going to {url}")

    def mouse_hover_on_element(self, locator: str = "", locator_type: str = "id", hover_time: int = 0) -> None:
        hover_element = self.get_element(locator, locator_type)
        ActionChains(self.driver).move_to_element(hover_element).perform()
        time.sleep(int(hover_time))

    def is_radio_button_checked(self, locator: str = "", locator_type: str = "id") -> bool:
        try:
            self.wait_for_element(locator, locator_type)
            radio_button = self.get_element(locator, locator_type)
            return bool(radio_button and radio_button.is_selected())
        except Exception:
            return False

    # ---------------------------- Verification helpers ----------------------------
    def verify_by_comparing_text(self, locator: str, locator_type: str,
                                 expected_result: str, result_msg: str,
                                 timeout: int = 10, case_sensitive: bool = True) -> None:
        """
        Verify element text matches expected result.
        """
        try:
            element = self.wait_for_element(locator, locator_type, timeout)
            if not element:
                raise TimeoutException(f"Element '{locator}' not found within {timeout}s")

            actual_result = self.get_text(element=element)

            if not case_sensitive:
                actual_result = actual_result.lower()
                expected_result = expected_result.lower()

            assert actual_result == expected_result, (
                f"Text mismatch for '{result_msg}': "
                f"Expected='{expected_result}', Actual='{actual_result}'"
            )
            self.log.info(f"[PASS]Test passed: Text matches for '{result_msg}'")
        except AssertionError as e:
            self.log.error(f"[FAIL]] Test failed: {str(e)}")
            self.screen_shot(f"text_mismatch_{result_msg}")
            raise
        except Exception as e:
            self.log.exception(f"Exception during text verification: {e}")
            raise


def wait_for_element(self, locator: str, locator_type: str = "id", timeout: int = 10,
                     poll_frequency: float = 0.2):
    """
    Generic wait for element to be present in DOM.
    Used by multiple verification and interaction methods.
    """
    try:
        by_type = self.get_by_type(locator_type)
        self.log.info(f"Waiting up to {timeout}s for element '{locator}' to be present")
        wait = WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll_frequency,
            ignored_exceptions=[
                NoSuchElementException,
                WebDriverException,
                ElementNotInteractableException,
                ElementNotSelectableException
            ]
        )
        element = wait.until(EC.presence_of_element_located((by_type, locator)))
        return element
    except TimeoutException:
        self.log.warning(f"Element '{locator}' not found after {timeout} seconds.")
        return None
    except Exception as e:
        self.log.exception(f"Exception while waiting for element: {e}")
        return None

    def verify_by_element_presence(self, locator: str, locator_type: str,
                                   result_msg: str, timeout: int = 10) -> None:
        """
        Verify element is present within timeout period.
        Raises AssertionError if element not found.
        """
        try:
            self.log.info(
                f"Verifying presence of element '{locator}' with type '{locator_type}' for '{result_msg}'"
            )
            element = self.wait_for_element(locator, locator_type, timeout)
            assert element is not None, f"Element '{locator}' not found for '{result_msg}'"
            self.log.info(f"[PASS]Test passed: element '{locator}' present for '{result_msg}'")
        except AssertionError as e:
            self.log.error(f"[FAIL]] Test failed: {str(e)}")
            self.screen_shot(f"verification_failed_{result_msg}")
            raise
        except Exception as e:
            self.log.exception(f"Exception during verification of element '{locator}': {e}")
            raise
