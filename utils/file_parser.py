import re

class FileParser:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def get_registration_numbers(self):

        reg_numbers = []
        try:
            with open(self.input_file, "r") as file:
                text = file.read()

                reg_numbers = re.findall(r'\b[A-Z]{2}\d{2}[A-Z]{3}\b', text)
            print(f"Extracted registration numbers: {reg_numbers}")
        except Exception as e:
            print(f"Error reading input file: {e}")
        return reg_numbers

    def get_expected_results(self):

        return {
            "DN09HRM": {
                "reg_no": "DN09HRM",
                "make": "BMW",
                "model": "3 Series",
                "year": "2009",
                "color": "Black"
            },
            "BW57BOF": {
                "reg_no":"BW57BOF",
                "make": "Toyota",
                "model": "Yaris",
                "year": "2008",
                "color": "Red"
            },
            "KT17DLX": {
                "reg_no":"KT17DLX",
                "make": "Skoda",
                "model": "Superb",
                "year": "2017",
                "color": "White"
            },
            "SG18HTN": {
                "reg_no":"SG18HTN",
                "make": "Volkswagen",
                "model": "Golf Se Navigation Tsi Evo",
                "year": "2018",
                "color": "White"
            }

        }

    def save_car_details_to_file(self, reg_no, make, model, year, color):

        try:
            with open(self.output_file, "a") as file:
                file.write(f"{reg_no},{make},{model},{year},{color}\n")
        except Exception as e:
            print(f"Error saving car details to file: {e}")
