import pytest

if __name__ == "__main__":
    exit_code = pytest.main(["-v", "--disable-warnings"])
    exit(exit_code)