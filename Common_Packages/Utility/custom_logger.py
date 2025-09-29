import logging
import os
import inspect


def custom_logger(log_level=logging.INFO):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger("automation_logger")
    logger.setLevel(log_level)

    log_file = r"C:\Users\lakshya757\Desktop\QA-Automation-develop\Common_Packages\Logs\automation.log"
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not logger.handlers:
        # Add encoding='utf-8' to support Unicode characters
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional: Add console handler with UTF-8 encoding
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(formatter)
        # logger.addHandler(console_handler)

    return logger
