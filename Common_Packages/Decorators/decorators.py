import functools
import pytest
import os
from datetime import datetime
from Common_Packages.Utility.custom_logger import custom_logger

def log_method(func, class_name: str):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        logger = custom_logger()
        logger.info(f"Calling method '{func.__name__}' of class '{class_name}'")
        return func(self, *args, **kwargs)
    return wrapper

def screenshot_on_assertion_failure(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except AssertionError as e:
            driver = getattr(self, "driver", None)
            if driver:
                # Use existing screen_shot method if available
                sd = getattr(self, "sd", None)
                if sd and hasattr(sd, 'screen_shot'):
                    sd.screen_shot(f"assertion_failed_{func.__name__}")
                else:
                    # Fallback to direct screenshot
                    screenshots_dir = os.path.join(os.getcwd(), "Common_Packages", "screenshots")
                    os.makedirs(screenshots_dir, exist_ok=True)
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    file_path = os.path.join(screenshots_dir, f"{func.__name__}_{timestamp}.png")
                    driver.save_screenshot(file_path)
            raise
    return wrapper
