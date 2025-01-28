from selenium.webdriver.common.by import By


class ConfirmPage:
    """
    ConfirmPage class represents the confirmation page of the application.

    This class provides a method to interact with and retrieve information from the confirmation page,
    specifically to check if a success message is displayed after a successful checkout process.
    """

    def __init__(self, driver):
        """
        Attributes:
        driver: WebDriver instance to interact with the web page.
        success_text: Locator for the success message element on the confirmation page.
        """
        self.driver = driver

    success_text = (By.CLASS_NAME, "alert-success")

    def get_success_text(self):
        """
        This method returns a list of elements containing the success message on the confirmation page.
        """
        return self.driver.find_elements(*ConfirmPage.success_text)
