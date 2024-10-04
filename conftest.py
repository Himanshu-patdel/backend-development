# importing third-party modules =========================================================
import pytest
import logging
import os 
# Pytest hook to add a command-line option for specifying the base URL
# while running the tests, or it will default to "http://0.0.0.0:8000/api"
def pytest_addoption(parser):
    parser.addoption(
        "--base-url", action="store", default="http://0.0.0.0:8000/api", help="Base URL for the API"
    )

# Fixture to return the base URL for the API
# once per test session and can be used across multiple tests
@pytest.fixture(scope="session")
def  BASE_URL(request):
    return request.config.getoption("--base-url")
 
log_file = os.path.join(os.path.dirname(__file__), 'test_log.log')

#  to running testing script hit this command on terminal 
# pytest test_novelty.py --base-url http://localhost:8000/api
 
logging.basicConfig(
    level=logging.INFO,  # Set log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Log to the file
        logging.StreamHandler()         # Log to the console
    ]
)
