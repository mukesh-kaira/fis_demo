from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EbayPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    SEARCH_BOX = (By.XPATH, "//div/input[@type='text']")
    SEARCH_BTN = (By.XPATH,"//input[@type='submit']")
    FIRST_ITEM = (By.XPATH, "(//li[contains(@class, 's-item')])[3]/div/div[2]/a")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[@id='atcBtn_btn_1']")
    CART_COUNT = (By.XPATH, "//i[@id='gh-cart-n']")

    # Actions
    def navigate_to_ebay(self):
        """Navigate to eBay homepage."""
        self.driver.get("https://www.ebay.com")

    def search_for_item(self, item):
        """Search for a specific item."""
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        search_box.send_keys(item)

    def click_search(self):
        """Click Search Button"""
        search_btn = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN))
        search_btn.click()

    def click_first_item(self):
        """Click on the first item in the search results."""
        first_item = self.wait.until(EC.element_to_be_clickable(self.FIRST_ITEM))
        first_item.click()

    def switch_to_new_tab(self):
        """Switch to a newly opened browser tab by index."""
        try:
            # Get all open window handles
            all_tabs = self.driver.window_handles
            print(f"All tabs: {all_tabs}")

            # Switch to the second tab (index 1)
            if len(all_tabs) > 1:
                self.driver.switch_to.window(all_tabs[1])
            else:
                raise Exception("No new tab found to switch to.")
        except Exception as e:
            print(f"Error while switching tabs: {e}")


    def add_to_cart(self):
        """Click the 'Add to Cart' button."""
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()

    def get_cart_count(self):
        """Retrieve the count of items in the cart."""
        cart_count = self.wait.until(EC.presence_of_element_located(self.CART_COUNT))
        return int(cart_count.text)
