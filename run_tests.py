import pytest

if __name__ == "__main__":
    exit_code = pytest.main(["-v", "--disable-warnings", "--html=report.html"])
    exit(exit_code)