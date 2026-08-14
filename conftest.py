import pytest
import allure
from fixture.driver_factory import get_driver
from config.config import BASE_URL , execution_mode
@pytest.fixture(
    params=["chrome"] if execution_mode == "local"
    else ["chrome", "firefox", "edge"],
    scope="function"
)
def driver(request):

    driver = get_driver(request.param)


    yield driver

    driver.quit()