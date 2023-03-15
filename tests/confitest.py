import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver


@pytest.fixture()
def getDriver(request):
    driver = None
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("http://localhost:6464/")
    request.cls.driver = driver
    yield driver
    # tear downDown
    time.sleep(2)
    driver.quit()


