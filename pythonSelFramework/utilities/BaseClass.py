import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import logging
import inspect


@pytest.mark.usefixtures("setup")
class BaseClass:
    """
    BaseClass provides common utility methods for interacting with web elements and logging during tests.

    This class includes helper functions for verifying the presence of links, selecting dropdown options by visible text,
    and setting up logging functionality. It is intended to be inherited by other test classes to reuse these common methods.

    Attributes:
    driver: WebDriver instance, typically set by the test framework, to interact with the browser.
    """

    def verify_link_presence(self, text):
        """
        This method waits for the presence of a link with the given visible text on the page.
        :param text: String
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self, locator, text):
        """
        This method selects an option from a dropdown menu by the visible text.
        :param locator: WebElement
        :param text: String
        :return: None
        """
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        """
        This method configures and returns a logger instance for logging messages to a file (logfile.log).
        :return: Logger
        """
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # File handler object
        file_handler = logging.FileHandler("logfile.log")

        # Define the logging format
        formatter = logging.Formatter(
            "%(asctime)s: %(levelname)s: %(name)s: %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Set log level
        logger.setLevel(logging.DEBUG)
        return logger
