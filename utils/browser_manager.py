from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserManager:
    def __init__(self):
        self.driver = None

    def start_browser(self):

        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.maximize_window()
            return self.driver
        except Exception as e:
            print(f"Error starting the browser: {e}")
            return None

    def stop_browser(self):

        if self.driver:
            self.driver.quit()
        else:
            print("Browser not started.")




    def close_browser(self, driver):

        if driver:
            driver.quit()
