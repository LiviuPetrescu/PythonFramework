from selenium.webdriver.common.by import By
from pageObjects.confirm_page import ConfirmPage


class CheckOutPage:
    """
    CheckOutPage class represents the checkout page of the application.

    This class contains locators for various elements on the checkout page and provides methods to interact with them.
    Allows obtaining and interacting with payment page elements, such as card title, card footer, checkout button,
    delivery location, and terms and conditions.
    The methods also support navigation to the next page (ConfirmPage) after clicking the 'checkout' button.
    """

    def __init__(self, driver):
        """
        Attributes:
        driver: WebDriver instance to interact with the web page.
        card_title: Locator for the card title element.
        card_footer: Locator for the card footer element.
        check_out_button: Locator for the checkout button element.
        check_out: Locator for the final checkout button to confirm the purchase.
        delivery_location: Locator for the delivery location dropdown element.
        suggested_locations: Locator for suggested location dropdown options.
        select_location: Locator for selecting the "India" location.
        agree_terms_and_conditions: Locator for the terms and conditions checkbox element.
        purchase_button: Locator for the purchase button to finalize the purchase.
        """
        self.driver = driver

    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    check_out_button = (By.CSS_SELECTOR, "a[class*= 'btn-primary']")
    check_out = (By.XPATH, "//button[@class='btn btn-success']")
    delivery_location = (By.ID, "country")
    suggested_locations = (By.CSS_SELECTOR, ".suggestions")
    select_location = (By.LINK_TEXT, "India")
    agree_terms_and_conditions = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    purchase_button = (By.CSS_SELECTOR, '[type="submit"]')

    def get_card_title(self):
        """
        This method returns a list of card title elements on the checkout page.
        """
        return self.driver.find_elements(*CheckOutPage.card_title)

    def get_card_footer(self):
        """
        This method returns a list of card footer elements on the checkout page.
        """
        return self.driver.find_elements(*CheckOutPage.card_footer)

    def get_check_out_button(self):
        """
        This method returns the checkout button element on the checkout page.
        """
        return self.driver.find_element(*CheckOutPage.check_out_button)

    def get_check_out(self):
        """
        This method clicks the final checkout button and returns a ConfirmPage object.
        """
        self.driver.find_element(*CheckOutPage.check_out).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

    def get_delivery_location(self):
        """
        This method returns the delivery location dropdown element.
        """
        return self.driver.find_element(*CheckOutPage.delivery_location)

    def get_suggested_locations(self):
        """
        This method returns the suggested locations dropdown element.
        """
        return self.driver.find_element(*CheckOutPage.suggested_locations)

    def get_location(self):
        """
        This method returns the element for selecting a specific location.
        """
        return self.driver.find_element(*CheckOutPage.select_location)

    def get_terms_conditions(self):
        """
        This method returns the checkbox element for agreeing to terms and conditions.
        """
        return self.driver.find_element(*CheckOutPage.agree_terms_and_conditions)

    def get_purchase_button(self):
        """
        This method returns the purchase button element to finalize the checkout process.
        """
        return self.driver.find_element(*CheckOutPage.purchase_button)
