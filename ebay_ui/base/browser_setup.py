from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserSetup:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        # Use WebDriver Manager to download the correct ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        return self.driver