
import pytest

def run_tests():
    pytest.main(["--html=reports/report.html", "--self-contained-html"])

if __name__ == "__main__":
    run_tests()
