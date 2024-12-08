
# Car Check Test Automation

### Pre-requisites

1. **Python**: Version 3.10 or above.
2. **pip**: Python package manager.
3. **Google Chrome Browser**: Ensure Chrome is installed.
4. **Webdriver Manager**: Automatically manages ChromeDriver.
 
---

### Features

1. **Pytest BDD**: Allows for easily adding input and output files for testing.
2. **Selenium WebDriver**: Handles browser automation for accessing car details.
3. **HTML Reporting**: Generates comprehensive test reports in HTML format.
4. **Automatic WebDriver Management**: Automatically downloads and configures the correct version of ChromeDriver.
5. **Page Object Model (POM)**: Implements reusable and maintainable code structure.
6. **Custom REGEX**: Supports all UK vehicle registration formats.
7. **Error Handling**: Handles failures when vehicles are not found on [cartaxcheck.co.uk](https://cartaxcheck.co.uk) or in output files.

---

### Usage

1. **Clone or Download the Project**:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # MacOS/Linux
   .venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Tests**:
   Execute the following command to run tests and generate an HTML report:
   ```bash
   Pytest -- #to execute the test with out report 
   pytest --html=reports/test_report.html --self-contained-html
   ```

5. **View the Report**:
   Open the generated HTML report located at:
   ```plaintext
   file:///Users/swapna/PycharmProjects/Shiva_CarTest/reports/test_report.html?sort=result
   ```

---


---

### How the Report Looks

After executing the tests, the HTML report is generated and includes detailed logs and screenshots for failed tests.

Report 
 Generated html report: file:///Users/swapna/PycharmProjects/Shiva_CarTest/reports/test_report.html 

---
