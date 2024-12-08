from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CarDetailsPage:
    def __init__(self, driver=None):
        if driver is None:
            raise ValueError("Driver is required")
        self.driver = driver

    def open_url(self, url):

        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        try:
            skip_link = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Skip, with limited data']"))
            )
            skip_link.click()
        except Exception:
            pass

    def get_car_details(self):

        try:
            if not self.vehicle_found():
                print("Vehicle details not found.")
                return None


            reg_no = self.driver.find_element(By.XPATH, "//dt[text()='Registration']/following-sibling::dd").text
            vehicle = self.driver.find_element(By.XPATH, "//dt[text()='Vehicle']/following-sibling::dd").text
            year = self.driver.find_element(By.XPATH, "//dt[text()='Year']/following-sibling::dd").text
            color = self.driver.find_element(By.XPATH, "//dt[text()='Colour']/following-sibling::dd").text


            make, model = vehicle.split(' ', 1) if ' ' in vehicle else (vehicle, '')

            return {
                "reg_no": reg_no,
                "make": make,
                "model": model,
                "year": year,
                "color": color
            }
        except Exception as e:
            print(f"Error fetching car details: {e}")
            return None
    def vehicle_found(self):

        try:

            self.driver.find_element(By.XPATH, "//dl[dt[text()='Registration']]")
            return True
        except Exception:
            return False
