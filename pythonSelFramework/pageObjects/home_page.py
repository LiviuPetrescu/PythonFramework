from selenium.webdriver.common.by import By
from pageObjects.checkout_page import CheckOutPage


class HomePage:
    """
    HomePage class represents the home page of the application.

    This class contains locators for various elements on the home page and provides methods to interact with them.
    Allows interaction with form fields, selecting options, submitting forms, and navigating to the checkout page.
    """

    def __init__(self, driver):
        """
        Attributes:
        driver: WebDriver instance to interact with the web page.
        shop_button: Locator for the shop button to navigate to the shop page.
        name_input: Locator for the name input field in the form.
        email_input: Locator for the email input field in the form.
        example_check_box: Locator for the example checkbox input.
        gender_select_form: Locator for the gender selection dropdown.
        submit: Locator for the submit button to submit the form.
        alert_text: Locator for the success alert message element.
        """
        self.driver = driver

    shop_button = (By.CSS_SELECTOR, "a[href*='shop']")
    name_input = (By.CSS_SELECTOR, "[name='name']")
    email_input = (By.NAME, "email")
    example_check_box = (By.ID, "exampleCheck1")
    gender_select_form = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    alert_text = (By.CSS_SELECTOR, ".alert-success")

    def shop_items(self):
        """
        This method clicks the shop button and returns a CheckOutPage object for further interaction with the checkout
        page.
        """
        self.driver.find_element(*HomePage.shop_button).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    def get_name_input(self):
        """
        This method returns the name input field element.
        """
        return self.driver.find_element(*HomePage.name_input)

    def get_email_input(self):
        """
        This method returns the email input field element.
        """
        return self.driver.find_element(*HomePage.email_input)

    def get_example_check_box(self):
        """
        This method returns the example checkbox input element.
        """
        return self.driver.find_element(*HomePage.example_check_box)

    def get_gender_select_form(self):
        """
        This method returns the gender selection dropdown element.
        """
        return self.driver.find_element(*HomePage.gender_select_form)

    def submit_form(self):
        """
        This method returns the submit button element to submit the form.
        """
        return self.driver.find_element(*HomePage.submit)

    def get_alert_text(self):
        """
        This method returns the element containing the success alert message after form submission.
        """
        return self.driver.find_element(*HomePage.alert_text)
