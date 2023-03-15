import sys
from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_healthforce_hyperlink():
    # initialising chrome
    driver = webdriver.Chrome()
    # calling url required
    driver.get("http://localhost:6464/")
    assert "The greatest factorial calculator!" in driver.title
    driver.find_element(By.LINK_TEXT, 'Healthforce')
    # Quit the driver
    driver.quit()