import os
import time

from pytest_bdd import scenarios, given, when, then
from utils.file_parser import FileParser
from utils.browser_manager import BrowserManager
from utils.car_details_page import CarDetailsPage

scenarios("../features/car_verification.feature")
file_parser = None
browser_manager = BrowserManager()
car_details_page = None
reg_numbers = []


@given('User reads the input file "resources/input/car_input.txt"')
def read_input_file():
    global file_parser, reg_numbers

    input_file = "resources/input/car_input.txt"
    output_file = "resources/output/car_output.txt"

    file_parser = FileParser(input_file, output_file)
    reg_numbers = file_parser.get_registration_numbers()

    assert reg_numbers, "No registration numbers found in the input file!"


@when('User extracts vehicle registration numbers based on patterns')
def extract_registration_numbers():

    global reg_numbers
    assert reg_numbers, "Registration numbers should have been extracted in the given step!"


@then('User compares results of registration numbers from the website with the output file')
def compare_results():

    global car_details_page, reg_numbers

    driver = browser_manager.start_browser()
    assert driver is not None, "Failed to start the browser session!"

    car_details_page = CarDetailsPage(driver)

    missing_registrations = []
    mismatched_details = []

    for reg in reg_numbers:
        try:

            url = f"https://cartaxcheck.co.uk/car-history-check/vehicle-details/?vrm={reg}"
            car_details_page.open_url(url)
            time.sleep(5)
            car_details = car_details_page.get_car_details()  # Assuming this returns a dictionary
            assert car_details is not None, f"Failed to retrieve details for registration: {reg}"


            expected = file_parser.get_expected_results().get(reg)
            assert expected is not None, f"No expected details found for registration: {reg}"

            if car_details != expected:
                mismatched_details.append({
                    "reg": reg,
                    "expected": expected,
                    "actual": car_details
                })
        except Exception as e:
            print(f"Error processing registration {reg}: {e}")


    generate_report(missing_registrations, mismatched_details)
    assert not missing_registrations, f"Missing registrations detected: {missing_registrations}"
    assert not mismatched_details, f"Mismatched details detected: {mismatched_details}"
    browser_manager.close_browser(driver)


def generate_report(missing_registrations, mismatched_details):

    report_path = "resources/reports/car_check_report.txt"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    with open(report_path, "w") as report_file:
        report_file.write("Car Registration Verification Report\n")
        report_file.write("=" * 50 + "\n")

        if missing_registrations:
            report_file.write(f"Missing Registrations:\n")
            report_file.write(", ".join(missing_registrations) + "\n")

        if mismatched_details:
            report_file.write("\nMismatched Details:\n")
            for detail in mismatched_details:
                report_file.write(
                    f"Reg: {detail['reg']} - Expected: {detail['expected']} - Actual: {detail['actual']}\n"
                )

        report_file.write("=" * 50 + "\n")

    print(f"Report generated: {report_path}")
    assert os.path.exists(report_path), "Report file was not generated!"
