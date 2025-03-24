import pytest
from utils.driver_setup import init_driver

@pytest.fixture
def driver():
    driver = init_driver()
    yield driver
    driver.quit()


