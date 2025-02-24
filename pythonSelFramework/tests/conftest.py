import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

global driver

"""
Test Setup and Reporting Utilities for Selenium WebDriver Tests.

This file includes fixtures and hooks that facilitate test setup and enhance test reporting by embedding
screenshots into the HTML report whenever a test fails.
"""


@pytest.fixture(scope="class")
def setup(request):
    """
        This fixture initializes the Chrome WebDriver, sets an implicit wait, opens the target URL in the browser,
    and maximizes the browser window. The WebDriver instance is shared across the test class using the `request.cls.driver`
    assignment. After the test execution, the WebDriver is closed.

    Scope: Class-level (setup is executed once per class).
        :param request:
        :return: None
    Usage:
        The `setup` fixture is automatically used for tests when scoped at the class level. Screenshots will be
        automatically taken and added to the HTML report when a test fails or is skipped.
    """

    global driver

    # Chrome
    service_object = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_object)

    # Define Implicit wait
    driver.implicitly_wait(4)

    # Define driver
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed a screenshot in the HTML report whenever a test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ["call", "setup"]:
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("driver")  # ✅ Access the driver from test fixtures
            if driver:
                file_name = report.nodeid.replace("::", "_") + ".jpg"
                _capture_screenshot(driver, file_name)  # ✅ Pass driver and file_name
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(driver, name):
    """
    Captures a screenshot of the current browser state and saves it with the specified name.
    :param driver: WebDriver instance
    :param name: String (filename)
    :return: None
    """
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    """
    This method sets the title of the generated HTML report to "Automation Report".
    :param report:
    :return: None
    """
    report.title = "Automation Report"
