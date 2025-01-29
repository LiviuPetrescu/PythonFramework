from pageObjects.home_page import HomePage
from test_data.checkout_page_data import CheckoutPageData
from test_data.home_shop_page_data import HomeShopPageData
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):
    """
        TestOne class contains the end-to-end test for the checkout process.

    This class inherits from `BaseClass` and tests the complete flow of selecting a product, proceeding to checkout,
    providing a delivery location, agreeing to terms, and completing a purchase on the website.
    """

    def test_e2e(self):
        """
                Test Steps:
        1. Navigate to the Home Page and click on the Shop button to go to the checkout page.
        2. Find all the products listed on the checkout page and select one specific product.
        3. Click the Checkout button to proceed to the checkout process.
        4. On the checkout page, enter a delivery location and wait for the location suggestions.
        5. Select one option from the location suggestions.
        6. Agree to the terms and conditions checkbox.
        7. Click the Purchase button to complete the purchase.
        8. On the confirmation page, verify that the success message is displayed to ensure the purchase was successful.

        Assertions:
            - Verifies that the success message is displayed on the checkout page.
        """

        # Define Home Page
        home_page = HomePage(self.driver)

        # Click on the Shop button
        check_out_page = home_page.shop_items()

        # Find all the products from the page
        product_title = check_out_page.get_card_title()
        i = -1

        # Search for a specific brand
        for title in product_title:
            i = i + 1
            card_text = title.text
            if card_text == HomeShopPageData.test_blackberry_data["product_brand"]:
                check_out_page.get_card_footer()[i].click()

        # Click on the 'Checkout' button
        check_out_page.get_check_out_button().click()

        # Go to Confirm page
        confirm_page = check_out_page.get_check_out()

        # Insert delivery location
        check_out_page.get_delivery_location().send_keys(CheckoutPageData.country_partial_data["partial_text"])

        # Wait for countries to appear with EXPLICIT wait
        self.verify_link_presence(CheckoutPageData.country_name["country_name"])

        # Get all the suggestions and click on India
        check_out_page.get_location().click()

        # Agree on terms and conditions
        check_out_page.get_terms_conditions().click()

        # Find and click on Purchase
        check_out_page.get_purchase_button().click()

        # Check if operation was successful
        success_text = confirm_page.get_success_text()
        search_text = ""
        for element in success_text:
            search_text = element.text

        # Verify that message "Success! Thank you!" is displayed on the Checkout page.
        assert CheckoutPageData.confirmation_text["confirmation_text"] in search_text