import pytest
from pageObjects.home_page import HomePage
from test_data.home_page_data import HomePageData
from utilities.BaseClass import BaseClass



class TestHomePage(BaseClass):
    """
        TestHomePage class contains tests related to the form submission on the home page.

    This class inherits from `BaseClass` and tests the functionality of submitting a form with different sets of data
    on the home page. It uses a fixture to provide the data and verifies that the form submission is successful.
    """

    def test_form_submission(self, get_data):
        """
            This method tests the form submission process using the provided test data.
        It fills in the form fields (first name, email, gender), submits the form, and verifies if the success message
        is displayed.

        Steps:
        1. Navigate to the Home Page.
        2. Fill in the first name, email, and gender fields using data provided by the `get_data` fixture.
        3. Click the checkbox and submit the form.
        4. Verify that the success message containing "Success!" is displayed after form submission.

        Assertions:
            - Verifies that the success message is displayed after form submission, indicating the form was submitted correctly.
        """

        # Navigate to the Home Page
        home_page = HomePage(self.driver)

        #  Define the Logger
        log = self.get_logger()

        # Clear the input fields and insert test data
        home_page.get_name_input().clear()
        home_page.get_name_input().send_keys(get_data["firstname"])
        log.info(f"First name is: {get_data['firstname']}")
        home_page.get_email_input().clear()
        home_page.get_email_input().send_keys(get_data["email"])
        log.info(f"Email is: {get_data['email']}")

        #  Find and click on "Example" checkbox
        home_page.get_example_check_box().click()

        # Find and select gender
        self.select_option_by_text(
            home_page.get_gender_select_form(), get_data["gender"]
        )
        home_page.submit_form().click()

        #  Get the alert text
        alert_text = home_page.get_alert_text().text

        # Verifies that the success message is displayed after form submission, indicating the form was submitted correctly.
        assert "Success!" in alert_text

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def get_data(self, request):
        """
        This fixture provides different sets of test data for each test execution, using data from
        `HomePageData.test_HomePage_data`.
        Each test run uses a different data set to validate form submission functionality.
        """
        return request.param
