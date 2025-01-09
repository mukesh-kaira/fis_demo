import unittest
from ebay_ui.base.browser_setup import BrowserSetup
from ebay_ui.pages.ebay_page import EbayPage

class TestEbayCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup browser
        browser = BrowserSetup()
        cls.driver = browser.get_driver()
        cls.ebay_page = EbayPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # Close browser
        cls.driver.quit()

    def test_add_to_cart(self):
        # Test steps
        self.ebay_page.navigate_to_ebay()
        self.ebay_page.search_for_item("book")
        self.ebay_page.click_search()
        self.ebay_page.click_first_item()

        # Switch to the new tab
        self.ebay_page.switch_to_new_tab()
        self.ebay_page.add_to_cart()

        # Assertion
        cart_count = self.ebay_page.get_cart_count()
        self.assertEqual(cart_count,1,"Cart count did not match.")

if __name__ == "__main__":
    unittest.main()